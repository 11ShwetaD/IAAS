#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()
import mysql.connector as mysql

print "Content-type:text/html"
print ""



web_data=cgi.FieldStorage()

email=web_data.getvalue('email')
password=web_data.getvalue('password')
cpassword=web_data.getvalue('cpassword')
username=web_data.getvalue('usern')

connection=mysql.connect(user="root",password="abhi8384",database="test",host="localhost")
if connection.is_connected():
	print "Database is connected"
	print email
	print password
	print cpassword
	print username

	cur=connection.cursor()
	cur.execute("insert into register (Email_address,password,confirm_password,username) Values (%s,%s,%s,%s)",(email,password,cpassword,username))
	connection.commit()
	
else:
	print "Something went wrong"
