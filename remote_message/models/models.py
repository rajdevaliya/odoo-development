from odoo import models, fields, api
import requests
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


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
    message_id = fields.Char(string='Message_id', tracking=True)

    def action_send(self):
        print("---------------------first", self)
        # if not self.partner_id or not self.body:
        #     raise ValidationError(('Please Provide Details'))
        # if self.state == 'pending':
        print("-----------------second")
        # self.write({'state': 'sent'})
        print("-----------------------------------------------code is running", self.state)
        url = self.env['ir.config_parameter'].get_param('remote_message.url')

        querystring = {
            'apikey': self.env['ir.config_parameter'].get_param('remote_message.api_key'),
            'username': self.env['ir.config_parameter'].get_param('remote_message.user_name'),
            'sendername': self.env['ir.config_parameter'].get_param('remote_message.sender_name'),
            'smstype': self.env['ir.config_parameter'].get_param('remote_message.sms_type'),
            "message": self.body,
            "numbers": self.number}

        headers = {
            'cache-control': "no-cache"
        }
        # try:
        response = requests.request("GET", url,
                                    headers=headers,
                                    params=querystring)
        res = response.json()
        print("-------------------response-", res)
        if res and res[0] and res[0].get('responseCode') == 'INVALID_KEY':
            raise UserError(('check your API key'))
        elif res and res[0] and res[0].get('responseCode') == 'INVALID_USER':
            raise UserError(('Please check your user id'))
        elif res and res[0] and res[0].get('responseCode') == 'Sender Name Invalid':
            raise UserError(('Please check your sender name'))
        elif res and res[0] and res[0].get('responseCode') == 'Invalid Service':
            raise UserError(('Please check your service url'))
        elif res and res[0] and res[0].get('responseCode') == 'Message SuccessFully Submitted':
            print('You succefully submitted')
        else:
            raise UserError(('Something went wrong ! '))
        if res and res[0] and res[0].get('responseCode') == 'Message SuccessFully Submitted':
            self.message_id = res and res[1] and res[1].get('msgid')



    # except:
    #     raise ValidationError(("Please check your internet"))

    @api.model
    def create(self, vals):
        vals['serial'] = self.env['ir.sequence'].next_by_code('remote.message')
        return super(RemoteSms, self).create(vals)

    def write(self, vals):
        if not self.serial:  # it will compulsory change the seq.
            vals['serial'] = self.env['ir.sequence'].next_by_code('remote.message')
        return super(RemoteSms, self).write(vals)


# res.config.parameter
# Draft, SUBMITED, DELIVRD, REJECTED
# INVALID_KEY
# INVALID_USER
#
# Sender Name Invalid
#
# Invalid Service
#
# Message SuccessFully Submitted

# state
# json error handle and display
# crone bnavano background ma message send kare if not submitted
# balance cheking mate wizard menu
# if submmited succesfully store msg id
