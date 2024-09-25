# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = 'res.partner'

    boletos_ids = fields.One2many('cinezentro.boletos', 'cliente_id', string='Boletos')
    opiniones_ids = fields.One2many('cinezentro.opinion', 'cliente_id', string='Opiniones')