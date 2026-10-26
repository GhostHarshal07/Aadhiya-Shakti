<%@ page import="java.sql.*" contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<title>Student CRUD</title>
<style>
body { font-family: Arial; margin: 30px; }
table { border-collapse: collapse; width: 70%; }
th, td { border: 1px solid #999; padding: 8px; text-align: left; }
th { background: #eee; }
input { padding: 5px; margin: 4px 0; }
</style>
</head>
<body>
<h2>Add Student</h2>
<form action="insert.jsp" method="post">
Name: <input type="text" name="name" required><br>
Email: <input type="email" name="email" required><br>
Age: <input type="number" name="age" required><br>
<input type="submit" value="Add">
</form>

<h2>Student List</h2>
<table>
<tr><th>ID</th><th>Name</th><th>Email</th><th>Age</th><th>Action</th></tr>
<%
Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
Statement st = con.createStatement();
ResultSet rs = st.executeQuery("SELECT * FROM student");
while (rs.next()) {
%>
<tr>
<td><%= rs.getInt("id") %></td>
<td><%= rs.getString("name") %></td>
<td><%= rs.getString("email") %></td>
<td><%= rs.getInt("age") %></td>
<td>
<a href="edit.jsp?id=<%= rs.getInt("id") %>">Edit</a> |
<a href="delete.jsp?id=<%= rs.getInt("id") %>" onclick="return confirm('Delete this record?')">Delete</a>
</td>
</tr>
<%
}
rs.close();
st.close();
con.close();
%>
</table>
</body>
</html>
