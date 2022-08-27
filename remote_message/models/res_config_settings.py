# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    url = fields.Char(string='URL', config_parameter='remote_message.url')
    api_key = fields.Char(string='Api Key', config_parameter='remote_message.api_key')
    user_name = fields.Char(string='User Name', config_parameter='remote_message.user_name')
    sender_name = fields.Char(string='Sender Name', config_parameter='remote_message.sender_name')
    sms_type = fields.Char(string='Sms Type', config_parameter='remote_message.sms_type')
