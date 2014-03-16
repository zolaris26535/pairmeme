#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is the entry point to the application and defines the URL routing.

This application is based on the Google App Engine's webapp2 framework. See
http://webapp-improved.appspot.com for details.

"""
import os
import webapp2

from webapp2_extras.routes import RedirectRoute

routes = [
    RedirectRoute(r'/',
                  handler='handlers.index_handler.IndexHandler', 
                  name='index', 
                  strict_slash=True)
]

# In the development environment, SERVER_SOFTWARE variable returns
# "Development/X.Y", where "X.Y" is the version of the Google App Engine
# run-time.
#
# See https://webapp-improved.appspot.com/guide/app.html#debug-flag 
# for details.
debug = os.environ['SERVER_SOFTWARE'].startswith('Dev')

app = webapp2.WSGIApplication(routes=routes, debug=debug)