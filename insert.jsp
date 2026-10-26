<%@ page import="java.sql.*" %>
<%
String name = request.getParameter("name");
String email = request.getParameter("email");
int age = Integer.parseInt(request.getParameter("age"));

Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
PreparedStatement ps = con.prepareStatement("INSERT INTO student(name, email, age) VALUES(?, ?, ?)");
ps.setString(1, name);
ps.setString(2, email);
ps.setInt(3, age);
ps.executeUpdate();
ps.close();
con.close();

response.sendRedirect("index.jsp");
%>
