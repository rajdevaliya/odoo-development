from odoo import models, fields, api


class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _inherit = "mail.thread", "mail.activity.mixin"
    _description = 'hospital'
    _rec_name = "operation"
    _order = "sequence"

    doctor_id = fields.Many2one('res.users', string='Odoo Oops',default=lambda self: self.env.user)
    operation = fields.Char(string='Appointment name')
    reference = fields.Reference(selection=[('hospital.patient', 'Patient'), ('hospital.appointment', 'Appointment')],
                                 string='Record')
    sequence = fields.Integer("Sequence", default=10)

    @api.model
    def name_create(self, name):
        return self.create({'operation': name}).name_get()[0]
