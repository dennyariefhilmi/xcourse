# -*- coding: utf-8 -*-
# from odoo import http


# class Xperpus(http.Controller):
#     @http.route('/xcourse/xcourse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xcourse/xcourse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xcourse.listing', {
#             'root': '/xcourse/xcourse',
#             'objects': http.request.env['xcourse.xcourse'].search([]),
#         })

#     @http.route('/xcourse/xcourse/objects/<model("xcourse.xcourse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xcourse.object', {
#             'object': obj
#         })
