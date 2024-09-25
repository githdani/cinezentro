# -*- coding: utf-8 -*-
# from odoo import http


# class Cinezentro(http.Controller):
#     @http.route('/cinezentro/cinezentro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cinezentro/cinezentro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cinezentro.listing', {
#             'root': '/cinezentro/cinezentro',
#             'objects': http.request.env['cinezentro.cinezentro'].search([]),
#         })

#     @http.route('/cinezentro/cinezentro/objects/<model("cinezentro.cinezentro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cinezentro.object', {
#             'object': obj
#         })
