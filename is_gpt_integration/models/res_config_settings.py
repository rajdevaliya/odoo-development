# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    openai_api = fields.Char(string='Chat Gpt api key', config_parameter='is_gpt_integration.openai')
