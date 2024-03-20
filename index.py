print('content-type:text/html\r\n\r\n')
import cgi
t = cgi.FieldStorage()
a = t.getvalue('email')
b = t.getvalue('password')
print(a)
print(b)
print("location:insert.html?msg=done")