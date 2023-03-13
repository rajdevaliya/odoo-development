# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BackendShortcuts(models.Model):
    _name = 'backend.shortcut'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Backend Shortcuts'

    name = fields.Char(string='Name', required=True)
    act_window_id = fields.Many2one('ir.actions.act_window', string='Action', required=True,
                                    domain=[('view_mode', '!=', 'form')])
    view_type = fields.Selection([
        ('tree', 'Tree'),
        ('kanban', 'Kanban'),
        ('calender', 'Calender'),
        ('activity', 'Activity'),
        ('pivot', 'Pivot'),
        ('graph', 'Graph'),
    ], default='tree', string='View Type')
    debug_mode = fields.Selection([
        ('0', 'False'),
        ('1', 'Debug'),
        ('assets', 'Assets Debugging'),
    ], default='0', string='Debugging Mode')

    url = fields.Char(string='URL', compute='_compute_url', store=True)

    @api.depends('name')
    def _compute_url(self):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        base_url += f'/is/{self.name}'
        self.url = base_url
