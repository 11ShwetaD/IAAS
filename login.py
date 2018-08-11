#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()
import mysql.connector as mysql

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

password=web_data.getvalue('password')
username=web_data.getvalue('username')

connection=mysql.connect(user="root",password="abhi8384",database="test",host="localhost")
	
cur=connection.cursor()
cur.execute("select username,password from register where username=%s and password=%s",(username,password))
fetch=cur.fetchall()
if len(fetch)>0:
	print "please Wait..."
	print "<meta http-equiv='refresh' content='2; http://127.0.0.1/service.html'>"

elif len(fetch)==0:
	print "Enter correct Username And Password"

else:
	print "Something went wrong"
