<html>
	<body>
		<% String name = request.getParameter("name");%>
		<p>Your name is: <%=name %></p>
        <p>${ssfn:escapeHtml(name)}</p>
	</body>
</html>
