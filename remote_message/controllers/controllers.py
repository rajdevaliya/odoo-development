# -*- coding: utf-8 -*-
# from odoo import http


# class RemoteMessage(http.Controller):
#     @http.route('/remote_message/remote_message', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/remote_message/remote_message/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('remote_message.listing', {
#             'root': '/remote_message/remote_message',
#             'objects': http.request.env['remote_message.remote_message'].search([]),
#         })

#     @http.route('/remote_message/remote_message/objects/<model("remote_message.remote_message"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('remote_message.object', {
#             'object': obj
#         })
