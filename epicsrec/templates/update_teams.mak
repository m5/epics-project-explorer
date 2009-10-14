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
			<table>
			<form action='scrape_teams' method=post>
			<fieldset class="admin">
				<legend>Scrape Team Information</legend>
				<ul>
					<li>
						<label for="from">From:</label>
						<input width="80em" type="text" id="from" name="from" value=${c.default_scrape_url} />
					</li>
					<li>
						<input type="submit" value="submit" />
					</li> 
				</ul>
			</fieldset>
			</form>
				
			<form action='parse_majors' method=post>
			<fieldset class="admin">
				<legend>Parse Majors</legend>
				<ul>
					<li>
						<label for="majors">Formatted majors list:</label>
						<textarea rows=10 id="majors" name="majors">${c.formatted_majors}</textarea>
					</li>
					<li>
						<input type="submit" value="submit" />
					</li> 
				</ul>
			</fieldset>
			</form>

			<form action='parse_choices' method=post>
			<fieldset class="admin">
				<legend>Parse Choices</legend>
				<ul>
					<li>
					<label for="majors">Space delimited choice data: </label>
						<textarea rows=20 cols=80 id="choices" name="choices"></textarea>
					</li>
					<li>
						<input type="submit" value="submit" />
					</li> 
				</ul>
			</fieldset>
			</form>

		</div>
	<input type="hidden" id="sid_hash" value="${c.sid_hash}">
    </body>
</html>
