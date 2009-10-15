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
	</%def>


<head>
</head>
<body>
	<form action='parse_choices' method=post>
	<fieldset>
		<legend>Add Aliases<legend>
		<ul>
		%for item in c.unknown_aliases:
			<li>
				<label for="${item}">${item} refers to: </label>
				<select id="${item}" name="${item}">
						<option value=''>Ignore</option>
					%for category, members in c.categories.items():
						<optgroup label="${category.name}">
						%for member in members:
							<option value="${member.id}">${member.name}</option>
						%endfor
						</optgroup>
					%endfor
				</select>

			</li>
		%endfor
			<li>
				<input type="submit" value="submit" />
			</li> 
		</ul>
	</fieldset>
	</form>
</body>
</html>
