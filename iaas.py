#!/usr/bin/python2
import  cgi
import  cgitb
cgitb.enable()
import  commands
print  "Content-type:text/html"
print   ""

web_data=cgi.FieldStorage()
#  extracting  os name from html file 
name=web_data.getvalue('os')
ram=web_data.getvalue('or')
cpu=web_data.getvalue('oc')
hdd=web_data.getvalue('oh')


print  commands.getoutput("sudo virt-install --name "+name+" --ram "+str(ram)+" --vcpus "+str(cpu)+" --disk path='/var/lib/libvirt/images/rhel7.1-2.qcow2' --import ")
