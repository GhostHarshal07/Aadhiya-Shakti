<%@ page import="java.sql.*" %>
<%
int id = Integer.parseInt(request.getParameter("id"));
String name = request.getParameter("name");
String email = request.getParameter("email");
int age = Integer.parseInt(request.getParameter("age"));

Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
PreparedStatement ps = con.prepareStatement("UPDATE student SET name=?, email=?, age=? WHERE id=?");
ps.setString(1, name);
ps.setString(2, email);
ps.setInt(3, age);
ps.setInt(4, id);
ps.executeUpdate();
ps.close();
con.close();

response.sendRedirect("index.jsp");
%>
