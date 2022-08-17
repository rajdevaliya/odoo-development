from odoo import models, fields, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_id = fields.Many2one('res.users', string='Confirm user')

    def _action_confirm(self):
        super(InheritSaleOrder, self)._action_confirm()
        self.confirmed_id = self.env.user
