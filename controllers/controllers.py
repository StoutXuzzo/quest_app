# -*- coding: utf-8 -*-
# from odoo import http


# class QuestApp(http.Controller):
#     @http.route('/quest_app/quest_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quest_app/quest_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quest_app.listing', {
#             'root': '/quest_app/quest_app',
#             'objects': http.request.env['quest_app.quest_app'].search([]),
#         })

#     @http.route('/quest_app/quest_app/objects/<model("quest_app.quest_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quest_app.object', {
#             'object': obj
#         })
