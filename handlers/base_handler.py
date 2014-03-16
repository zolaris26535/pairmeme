# -*- coding: utf-8 -*-
"""This file is the base class of request handler class.

This class provides template rendering services to derived classes. It uses the 
Jinja2 template engine from the webapp2_extras package. 

See http://webapp-improved.appspot.com/api/webapp2_extras/jinja2.html
for details.

"""
import webapp2

from webapp2_extras import jinja2

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        """Returns a cached instance of Jinja2 from the app registry.

        This function tries to get an instance of Jinja2 from the current app
        registry. If it is not registered, it will be instantiated and
        registered. Subsequent calls to this function will return the same
        instance.

        """
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, file_name, **context):
        """Renders a template and writes the result to the response object.

        :param file_name: 
            The template file name in the templates directory.
        :param context: 
            Keyword arguments used as variables in the rendered template. These 
            will override values set in the request context.

        """
        self.response.write(self.jinja2.render_template(file_name, **context))