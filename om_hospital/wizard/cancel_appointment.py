from odoo import models, fields, api, _
from datetime import date
from dateutil import relativedelta

from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'cancel_appointment_wizard'
    _inherit = "mail.thread", "mail.activity.mixin"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['cancel_date'] = date.today()
        res['reason'] = 'no reason'
        res['appointment_id'] = self.env.context.get('active_id')
        print("---------active_id", self.env.context.get('active_id'))
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment',
                                     domain=[('state', '=', 'draft')])
    ref1 = fields.Char(related='appointment_id.ref', string='Ref id')
    cancel_date = fields.Date(string='Date')
    reason = fields.Char(string='Reason')

    def action_cancel(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_day')
        allowed_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
        if allowed_date <= date.today():
            raise ValidationError(("you can not cancel appointment on same day"))
        self.appointment_id.state = 'cancel'
        query = f"""select id,name from hospital_patient where id={self.appointment_id.id}"""
        self.env.cr.execute(query)
        patient =self.env.cr.dictfetchall()
        print("----------------->>>>>>sql query", patient)
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cancel.appointment.wizard',
            'res_id': self.id,
            'target': 'new'
        }
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload'
        # } # this is for popup onlu
