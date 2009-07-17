
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html14/loose.tdt">
<html>
<% self.seen_css = set() %>
<% self.seen_js = set() %>
    <head>
	${self.css()}
	${self.js()}
	</head>

	<%def name="css_links(path, media='')">
		%if path not in self.seen_css:
			<link rel="stylesheet" type="text/css" href="${path|h}" media="${media}" >
		% endif
		<%self.seen_css.add(path) %>
	</%def>
	<%def name="js_links(path)">
		%if path not in self.seen_js:
			<script type="text/javascript" src="${path|h}" ></script>
		% endif
		<%self.seen_js.add(path) %>
	</%def>

	<%def name="css()">
		${css_links('/css/rec.css', 'screen')}
	</%def>
	<%def name="js()">
		${js_links('/js/jquery-1.2.6.pack.js')}
		${js_links('/js/jquery.color.js')}
		${js_links('/js/buttons.js')}
	</%def>


    <body>
		<div id="container">
		<div id="majors_container">
			%for row in g.major_map:
				%for m in row:
				<% school = m['school'] %>
				<% major  = m['major'] %>
				<% css    = m['css'] %>
				%if major:
            	<span name="${school+'-'+major}" style="${css}" class="button major ${school}">
					<span class="button_label">
					${major.replace('_',' ')}
					</span>
					<span class="information" name="school">${school}</span>
				</span>
				%endif
				%endfor
			%endfor
			<span id="school"></span>
		</div>
		<div id="information">
			<h1>Epics Project Explorer</h1>
			<ul>
			<li>
			<span class="button selected"></span>
			<span class="inftext">Select any disciplines on the left that interest you.</span>
			</li>
			<li>
			<span class="button recomended"></span>
			<span calss="inftext">Select any interesting projects below for more information.</span>
			</li>
			</ul>
		
		
		</div>
		<div id="teams_container">
		%for team in g.teams:
           	<span name="${team}" class="button team">
				<span class="button_label"name="abbr">
					${team}
				</span>
				<span class="information" name="title">
					${team.name}
				</span>
				<span class="information" name="description">
					${team.info}
				</span>
				<a class="information" href="${team.link}"></a>
		</span>
		%endfor
		</div>
		<span id="description" class="popup"></span>
		</div>
	<input type="hidden" id="sid_hash" value="${c.sid_hash}">
    </body>
</html>
