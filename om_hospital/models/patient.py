from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'civil hospital'
    _inherit = "mail.thread", "mail.activity.mixin"
    _order = 'id desc, name'
    # _log_access = False # by this crate uid, write uid, create date, write date will not be created

    name = fields.Char(string='Name', tracking=True)
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age', compute='compute_age', inverse='_inverse_compute_age', search='_search_age',
                         tracking=True, store=True)
    # age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    # gender1 = fields.Many2one('hospital.patient.gender', string='Gender')

    ref = fields.Char(string='Reference id')
    active = fields.Boolean(string='Active', tracking=True, default=True)
    appointment_count = fields.Integer(string='Appointment_count', compute='_compute_appointment_count')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='a ids')
    parent = fields.Char('Parent')
    marital_status = fields.Selection([('maried', 'Maried'), ('single', 'Single')])
    partner_name = fields.Char(string='Partner Name')
    is_birthday = fields.Boolean(string='is birthday', compute='_birthday_alert')
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    website = fields.Char("Website")

    # this function will give alert if there is a birthday of any
    @api.depends('dob')
    def _birthday_alert(self):
        for rec in self:
            is_birthday = False
            if rec.dob:
                today = date.today()
                if today.day == rec.dob.day and today.month == rec.dob.month:
                    is_birthday = True
            rec.is_birthday = is_birthday

    def test_object(self):
        pass  # this function if of appointment view.xml

    @api.depends('dob')
    def compute_age(self):
        for rec in self:
            today = fields.Date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0

    # rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id), ('state', '=', 'draft')])

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        appointment_group = self.env['hospital.appointment'].read_group(domain=[('state', '=', 'draft')],
                                                                        fields=['patient_id'],
                                                                        groupby=['patient_id'])
        print(",,,,,,,,,,,,,,,,,,,,,,,,", appointment_group)

        for appointment in appointment_group:
            patient_id = appointment.get('patient_id')[0]
            patient_rec = self.browse(patient_id)

            patient_rec.appointment_count = appointment['patient_id_count']
            self = self - patient_rec
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", self)
        self.appointment_count = 0

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.dob = today - relativedelta.relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        print('-------------------------------', value)
        dob = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = dob.replace(day=31, month=12)
        end_of_year = dob.replace(day=1, month=1)
        return [('dob', '>=', start_of_year), ('dob', '<=', end_of_year)]

    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(('This contain appointment so you cant delete'))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        # if not self.ref:  # it will compulsory change the ref
        if not self.ref and not vals.get('ref'):  # if value is already available then will not change
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
            return super(HospitalPatient, self).write(vals)

    def name_get(self):
        # patient_list = []
        # for record in self:
        #     name = str(record.ref) + str(record.name)
        #     patient_list.append((record.id, name))
        # return patient_list
        return [(record.id, "%s %s" % (record.ref, record.name)) for record in self]

# class HospitalPatientGender(models.Model):
#     _name = 'hospital.patient.gender'
#     _description = 'Gender'
#
#     name = fields.Char(default='name')
