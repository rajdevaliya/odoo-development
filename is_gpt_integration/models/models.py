# -*- coding: utf-8 -*-

import openai

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Channel(models.Model):
    _inherit = 'mail.channel'

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        chatgpt_channel_id = self.env.ref('is_gpt_integration.channel_chatgpt')
        user_chatgpt = self.env.ref("is_gpt_integration.user_chatgpt")
        partner_chatgpt = self.env.ref("is_gpt_integration.partner_chatgpt")
        author_id = msg_vals.get('author_id')
        chatgpt_name = str(partner_chatgpt.name or '') + ', '
        prompt = msg_vals.get('body')
        print(["chatgpt_channel_id", chatgpt_channel_id],
              ["user_chatgpt", user_chatgpt],
              ["partner_chatgpt", partner_chatgpt],
              ["author_id", author_id],
              ["prompt", prompt]
              )
        if not prompt:
            return rdata
        openai.api_key = self.env['ir.config_parameter'].sudo().get_param('is_gpt_integration.openai')
        Partner = self.env['res.partner']
        partner_name = ''
        if author_id:
            partner_id = Partner.browse(author_id)
            if partner_id:
                partner_name = partner_id.name
        if author_id != partner_chatgpt.id and chatgpt_name in msg_vals.get('record_name', '') or 'ChatGPT,' in msg_vals.get('record_name', '') and self.channel_type == 'chat':
            try:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    tempeterature=0.6,
                    max_tokens=3000,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    user = partner_name,
                )
                res = response['choices'][0]['text']
                self.with_user(user_chatgpt).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment')
            except Exception as e:
                raise UserError(_(e))

        elif author_id != partner_chatgpt.id and msg_vals.get('model', '') == 'mail.channel' and msg_vals.get('res_id', 0) == chatgpt_channel_id.id:
            try:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.6,
                    max_tokens=3000,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    user = partner_name,
                )
                res = response['choices'][0]['text']
                chatgpt_channel_id.with_user(user_chatgpt).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment')
            except Exception as e:
                raise UserError(_(e))

        return rdata



# import openai
# from odoo import api, fields, models, _
# from odoo.exceptions import UserError
#
#
# class Channel(models.Model):
#     _inherit = 'mail.channel'
#
#     def _notify_thread(self, message, msg_vals=False, **kwargs):
#         res = super(Channel, self)._notify_thread(message, msg_vals=False, **kwargs)
#         order = self.env['sale.order'].sudo().search([('name', '=', 'S00007')])
#         print("<>>>>>>>>>>>>>>>>>>>>>>>>>>>> order ",  order.name)
#         channel_gpt = self.env.ref('is_gpt_integration.channel_chatgpt')
#         partner_chatgpt = self.env.ref('is_gpt_integration.partner_chatgpt')
#         user_chatgpt = self.env.ref("is_gpt_integration.user_chatgpt")
#         prompt = msg_vals.get('body')
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> kwags", msg_vals)
#         author_id = msg_vals.get('author_id')
#         if author_id != partner_chatgpt.id:
#             response = self.gpt_response(prompt)
#             self.with_user(user_chatgpt).message_post(
#                 body=_(response),
#                 message_type='comment',
#                 subtype_xmlid='mail.mt_comment'
#             )
#         return res
#
#     def gpt_response(self, prompt):
#
#
#         # Set your API key
#         openai.api_key = self.env['ir.config_parameter'].sudo().get_param('is_gpt_integration.openai')
#         # openai.api_key = "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"
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0.6,
#             max_tokens=3000,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#             user="Chat GPT",
#         )
#         res = response['choices'][0]['text']
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> res", res)
#         return res
