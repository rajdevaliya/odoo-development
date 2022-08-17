from odoo import models, fields, api


class TagPatient(models.Model):
    _name = 'tag.patient'
    _description = 'civil hospital'
    _inherit = "mail.thread", "mail.activity.mixin"

    name = fields.Char(string='Name', tracking=True)
    active = fields.Boolean(string='Active', tracking=True, default=True, copy=False)
    # if you dont want to duplicate this field , put copy = False
    color = fields.Integer(string='color')
    date_of_birth = fields.Date(string='Date of Birth')
    color2 = fields.Char(string='color 2 ')
    appointment_ids = fields.Many2many('hospital.appointment', 'doctor_patient_rel', 'doctor_id_rec', 'appointment_id',
                                       string='Appointment')
    sequence = fields.Integer(string='Sequence')

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = f'{self.name} (copy)'
        default['sequence'] = 10
        return super(TagPatient, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name', 'unique(name)', 'Name must be unique'),
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be above zero')
    ]

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                return 0
