from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'civil hospital'
    _inherit = "mail.thread", "mail.activity.mixin"
    _rec_name = 'patient_id'

    '''odoo will take name as default rec name
    but here we have many2one and dont have
    name so we have to defined rec name'''

    patient_id = fields.Many2one('hospital.patient', string='Patient',
                                 ondelete='restrict')  # ondelete = 'cascade' will delete from both side
    appointment_count = fields.Integer(related='patient_id.appointment_count')
    operations = fields.Many2one('hospital.operation', string='Odoo oops')
    age = fields.Integer(string='age', store=True)
    date_of_birth = fields.Date(string='Date of birth')
    # gender = fields.Selection(related='patient_id.gender', readonly=False, store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    ref = fields.Char(string='Reference id', tracking=True)
    active = fields.Boolean(string='Active', tracking=True, default=True)
    appointment_time = fields.Datetime(string='Appointment Time', tracking=True, default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', tracking=True, default=fields.Date.context_today)
    valid_till = fields.Float('valid Date')
    father = fields.Char(string='Father')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'High'),
        ('2', 'Very High'),
        ('3', 'Critical')
    ], string='Priority')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string='Status', default='draft')
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide Sales Price')
    image = fields.Image(string='image')
    tag_ids = fields.Many2many('tag.patient', 'doctor_patient_rel', 'appointment_id', 'doctor_id_rec', string='Doctor')
    progress = fields.Integer(string="Progress", compute='_compute_progress')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')

    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = 25
            elif rec.state == 'in_consultation':
                progress = 50
            elif rec.state == 'done':
                progress = 100
            else:
                progress = 0

            rec.progress = progress

    def action_view_appointment(self):
        print(f'--------------,{self.id}')
        print(f'--------------,{self}')
        return {
            'name': 'Appointment',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'context': {'default_patient_id': self.id},
            'domain': [('patient_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.age = self.patient_id.age
        self.ref = self.patient_id.ref
        self.gender = self.patient_id.gender
        self.date_of_birth = self.patient_id.dob

    def test_object(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.odoo.com'

        }

    def unlink(self):
        if self.state == 'done':
            raise ValidationError(('you can not delete done record'))
        return super(HospitalAppointment, self).unlink()

    def action_in_consultation(self):
        for rec in self:
            if rec.state in 'draft':
                rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'you clicked',
                    'type': 'rainbow_man'
                }
            }

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
        # action = self.env.ref('om_hospital.action_cancel_appointment_wizard').read()[0]
        # return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def whatsapp_share(self):
        if not self.patient_id.phone:
            raise ValidationError(("This not a valid number"))
        message = f"HI *{self.patient_id.name}* your appointment is confirmed with reference no. {self.ref} , Thank you"
        whatsapp_url = f'https://api.whatsapp.com/send?phone={self.patient_id.phone}&text={message}'
        self.message_post(body=message)

        return {
            'type': "ir.actions.act_url",
            'target': 'new',
            'url': whatsapp_url
        }

    def test_notification(self):
        msg = 'Button clicked successful'
        action = self.env.ref('om_hospital.action_hospital_patient')
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'danger',
                'title': 'Press on link to go to patient menu',
                'message': '%s',
                'sticky': True,
                'links': [{
                    'label': self.patient_id.name,
                    'url': f'#action={action.id}&id={self.id}&model=hospital.patient'
                }],
                'next': {
                    'type': 'ir.actions.act_window',
                    'res_model': 'hospital.patient',
                    'res_id': self.patient_id.id,
                    'views': [(False, 'form')]
                }
            }
        }

    # @api.model
    def create(self, vals):
        res = super(HospitalAppointment, self).create(vals)
        no = 0
        for line in res.pharmacy_line_ids:
            no += 1
            line.serial = no
        print('--------------------res', res)
        return res

    def write(self, vals):
        res = super(HospitalAppointment, self).write(vals)
        no = 0
        for line in self.pharmacy_line_ids:
            no += 1
            line.serial = no
        return res
    #
    # def compute_sr_no(self):
    #     no = 0
    #     for line in self.pharmacy_line_ids:
    #         no += 1
    #         line.serial = no


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'appointment pharmacy lines'
    product_id = fields.Many2one('product.product', string='Product')
    price = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Qty', default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    currency_id = fields.Many2one('res.currency', related='appointment_id.currency_id')
    price_subtotal = fields.Monetary(string="Subtotal", compute='_compute_subtotal', currency_field='currency_id')
    serial = fields.Integer(string='Sr No', readonly=True, compute='_compute_serial')

    # if there is fileld name currency_id , no need to put currency_field

    @api.depends('price', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price * rec.qty
    @api.depends('serial')
    def _compute_serial(self):
        n = 0
        for rec in self:
            n +=1
            rec.serial = n
