
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
			<dl id="schools" class="accordian">
			%for school, majors in g.majors.items():
				<a href='#'><dt>${school.replace('_',' ')}</dt></a>
				<dd style="height: ${3+50*((4+len(majors)) // 5)}px;">			
					%for major in majors:
						<span name="${school+'-'+major}" class="button major ${school}">
							<span class="button_label">${major}</span>
							<span class="information">${school}</span>
						</span>
					%endfor
				</dd>
			%endfor
			</ul>
		</div>
		<div id="information">
			<h1>Epics Project Explorer</h1>
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
		<div id="tutorial">Choose your school...</div>
		</div>
	<input type="hidden" id="sid_hash" value="${c.sid_hash}">
    </body>
</html>
