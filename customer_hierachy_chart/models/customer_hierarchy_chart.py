from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    parent_id = fields.Many2one('res.partner')
    is_company = fields.Boolean('Is a Company')

    def toggle_sale_order(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> self", self)
        return {
            'name': 'Sale Orders',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'views': [[False, 'list'],
                      [False, 'form']],

            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }

    def toggle_children(self):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", self.id)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", self.parent_id.child_ids)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", self.mapped("child_ids").ids)
        return {
            'name': 'Partners',
            'res_model': 'res.partner',
            'view_mode': 'kanban,list,form',
            'views': [[self.env.ref('customer_hierachy_chart.res_partner_tree_view').id, 'list'],
                      [self.env.ref('base.view_partner_form').id, 'form'],
                      [self.env.ref('base.res_partner_kanban_view').id, 'kanban']],

            'domain': [('id', 'in', self.child_ids.ids)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }
        # for record in self:
        #     record.child_ids =  not record.child_ids
