<%@ page import="java.sql.*" %>
<%
int id = Integer.parseInt(request.getParameter("id"));

Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
PreparedStatement ps = con.prepareStatement("DELETE FROM student WHERE id=?");
ps.setInt(1, id);
ps.executeUpdate();
ps.close();
con.close();

response.sendRedirect("index.jsp");
%>
