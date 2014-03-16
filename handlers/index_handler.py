# -*- coding: utf-8 -*-
from base_handler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        context = {
            'title': 'Pairmeme'
        }
        self.render_template('index.html', **context)