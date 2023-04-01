# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerHierachyChart(http.Controller):
#     @http.route('/customer_hierachy_chart/customer_hierachy_chart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_hierachy_chart/customer_hierachy_chart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_hierachy_chart.listing', {
#             'root': '/customer_hierachy_chart/customer_hierachy_chart',
#             'objects': http.request.env['customer_hierachy_chart.customer_hierachy_chart'].search([]),
#         })

#     @http.route('/customer_hierachy_chart/customer_hierachy_chart/objects/<model("customer_hierachy_chart.customer_hierachy_chart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_hierachy_chart.object', {
#             'object': obj
#         })
