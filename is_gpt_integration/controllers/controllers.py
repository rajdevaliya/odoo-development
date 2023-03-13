# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ChatGptIntegraation(http.Controller):
    @http.route('/chatgpt', website=True, auth='public')
    def chatgpt_form(self, **kw):
        return request.render("is_gpt_integration.chatgpt")


