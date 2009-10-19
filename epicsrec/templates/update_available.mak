
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
                ${js_links('/js/update_available.js')}
	</%def>


    <body>
		<div id="container">
                <input type="submit" value="update" class="update"/>
		%for school in c.schools:
                        <fieldset><legend>${school.name}</legend>
                        %for major in school.members:
			<div id="teams_container">
				<span> ${major.name} </span>
				%for team in c.teams:
				<% selected = "selected" if major in team.available_choices else "" %>
					<span id="${str(major.id) + ',' + str(team.id)}" class="button team ${selected}">
						<span class="button_label"name="${c.abbr}">
							${team.name}
						</span>
						<span class="information" name="title">
							${team.long_name}
						</span>
						<span class="information" name="description">
							${team.description}
						</span>
						<a class="information" href="${team.link}"></a>
					</span>
				%endfor
			</div>
                        %endfor
                        </fieldset>
		%endfor
		</div>
                <input type="submit" value="update" class="update"/>
		</div>
	<input type="hidden" id="sid_hash" value="${c.sid_hash}">
    </body>
</html>
