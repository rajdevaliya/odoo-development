from odoo import models, fields, api
import requests
from odoo.exceptions import ValidationError


class RemoteSms(models.Model):
    _name = "remote.message"
    _inherit = "mail.thread", "mail.activity.mixin"
    _order = "serial desc"
    _rec_name = 'serial'

    partner_id = fields.Many2one('res.partner', 'Recipient')
    number = fields.Char(string='Mobile', size=10)
    body = fields.Text("Message")
    serial = fields.Char("Sequence", readonly=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('sent', 'Sent')
    ], string='Status', default='pending')

    def action_send(self):
        print("---------------------first", self)
        # if not self.partner_id or not self.body:
        #     raise ValidationError(('Please Provide Details'))
        if self.state == 'pending':
            print("-----------------second")
            self.write({'state': 'sent'})
            print("-----------------------------------------------code is running", self.state)
        url = "http://otp.rajavirsolutions.com/sendSMS"

        querystring = {
            'apikey': '36adfbc5-5ad0-40ab-825c-4a5f4afdca15',
            'username': 'sjamod9',
            'sendername': 'INTSOL',
            'smstype': 'TRANS',
            "message": self.body,
            "numbers": self.number}

        headers = {
            'cache-control': "no-cache"
        }
        res = requests.request("GET", url,
                               headers=headers,
                               params=querystring)
        print("-------------------response-", res.json())
        return res

    @api.model
    def create(self, vals):
        vals['serial'] = self.env['ir.sequence'].next_by_code('remote.message')
        return super(RemoteSms, self).create(vals)

    def write(self, vals):
        if not self.serial:  # it will compulsory change the seq.
            vals['serial'] = self.env['ir.sequence'].next_by_code('remote.message')
        return super(RemoteSms, self).write(vals)

# res.config.parameter