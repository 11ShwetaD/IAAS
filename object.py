#!/usr/bin/python2
import cgi
import cgitb
import commands ,os
print "content-type:text/html "
print ""
web=cgi.FieldStorage()
drive_name=web.getvalue('dn')
drive_size=web.getvalue('ds')

print(commands.getoutput('sudo ifconfig'))
'''
commands.getoutput('lvcreate --name '+drive_name+'-v'+drive_size+'m --thin cld/pool1 ')
#formatting the partition 
commands.getoutput('mkfs.xfs /dev/cld/' +drive_name)
#mount storage on server side
commands.getoutput('mkdir /var/www/html/mnt/' +drive_name)
#now mounting
commands.getoutput('mount /dev/cld/ '+drive_name ' /var/www/html/mnt/ ' +drive_name )

'''
