#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
cgitb.enable(display=0, logdir="/path/to/logdir")
# Headers
print("Content-Type: text/html\n\n")
print()
print("""<html>
<head>
    <title>Título de la página</title>
</head>
<h3>Hola CGI!</h3>
</html>""")