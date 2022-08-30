# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conta_move(models.Model):
    
    _inherit = 'account.move'

    conta_ids = fields.Integer(index="True")

class asiento(models.Model):
    _inherit = 'account.move.line'

    asiente = fields.Many2one('account.move')
    asiento = fields.Char(compute='index')

    def index(self):
        for record in self:
            record.asiento = record.move_id.id