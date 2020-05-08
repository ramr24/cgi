#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

# 1/0 # introducing an error to use debug (cgitb)

cgi.test()
