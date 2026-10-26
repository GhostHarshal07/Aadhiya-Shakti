<%@ page import="java.sql.*" contentType="text/html;charset=UTF-8" %>
<%
int id = Integer.parseInt(request.getParameter("id"));
Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
PreparedStatement ps = con.prepareStatement("SELECT * FROM student WHERE id=?");
ps.setInt(1, id);
ResultSet rs = ps.executeQuery();
String name = "", email = "";
int age = 0;
if (rs.next()) {
    name = rs.getString("name");
    email = rs.getString("email");
    age = rs.getInt("age");
}
rs.close();
ps.close();
con.close();
%>
<!DOCTYPE html>
<html>
<head>
<title>Edit Student</title>
<style>
body { font-family: Arial; margin: 30px; }
input { padding: 5px; margin: 4px 0; }
</style>
</head>
<body>
<h2>Edit Student</h2>
<form action="update.jsp" method="post">
<input type="hidden" name="id" value="<%= id %>">
Name: <input type="text" name="name" value="<%= name %>" required><br>
Email: <input type="email" name="email" value="<%= email %>" required><br>
Age: <input type="number" name="age" value="<%= age %>" required><br>
<input type="submit" value="Update">
<a href="index.jsp">Cancel</a>
</form>
</body>
</html>
