#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file specifies the Google App Engine module configuration.

See https://developers.google.com/appengine/docs/python/tools/appengineconfig
for details.

"""
def webapp_add_wsgi_middleware(app):
    """This function enables the application's performance profiling at
    http://your_domain.com/_ah/stats.
    
    This function wraps the application with the Appstats middleware which
    records statics about each request handler.

    See 
    https://developers.google.com/appengine/docs/python/tools/appstats
    http://googleappengine.googlecode.com/svn/trunk/python/google/appengine/ext/appstats/sample_appengine_config.py
    for details.

    """
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app