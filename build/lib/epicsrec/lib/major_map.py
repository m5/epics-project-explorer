def Snake(width=5):
    xmax = width-1
    x = 0
    y = 0
    d = {'x':1,'y':0}
    yield x,y
    while 1:
        path = {'1,0,%d' % xmax: {'x':0, 'y':1},
                '-1,0,0'       : {'x':0, 'y':1},
                '0,1,%d' % xmax: {'x':-1,'y':0},
                '0,1,0'        : {'x':1, 'y':0},
                }
        curr = '%d,%d,%d' % (d['x'], d['y'], x)
        if curr  in path.keys():
            d = path[curr]
        x += d['x']
        y += d['y']
        yield x,y

def generate_map(majors,width=5):
    snake = Snake(width)
    map = []
    row = [{'major':'','school':'','css':''} for i in range(width)]
    for school in majors.keys():
        for major in majors[school]:
            icol,irow = snake.next()
            if irow > len(map):
                map.append(row)
                row = [{'major':'','school':'','css':''} for i in range(width)]

            row[icol] = {'major':major,'school':school,'css':''}
    map.append(row)
    return draw_borders(map)

def draw_borders(map):
    around = {'top':   (0,-1),
              'left':  (-1,0),
              'bottom':  (0,1),
              'right': (1,0)}

    css = lambda s: "padding-%s:0px;border-%s-width:1px" % (s,s)

    for irow in range(len(map)):
        for icol in range(len(map[irow])):
            borders = []
            for pos in around.keys():
                nrow,ncol = irow+around[pos][1], icol+around[pos][0]

                rowin = 0 <= nrow < len(map)
                colin = 0 <= ncol < len(map[irow])
                inrange = rowin and colin
                if not inrange:
                    borders.append(pos)
                else:                    
                    nschool = map[nrow][ncol]['school']
                    if nschool != map[irow][icol]['school']:
                        borders.append(pos)

            for pos in borders:
                if map[irow][icol]['css']:
                    map[irow][icol]['css'] += ';'
                map[irow][icol]['css'] += css(pos)
    return map
