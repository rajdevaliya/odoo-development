from odoo import models, fields, api, _
import pytz
from datetime import datetime

class PoDateChangeLog(models.Model):
    _inherit = 'purchase.order'

    def write(self, value):
        print(">>>>>>>>>>>>>>>>>>> value", value)
        date_planned = value.get("date_planned")
        old_date = self.date_planned
        print(">>>>>>>>>>>>>> self.date_planned", self.date_planned)
        if date_planned is not None:
            if type(date_planned) != str:
                print(">>>>>>>>>>>>>>>>date_planned>>>>>", type(date_planned))
                print(">>>>>>>>>>>>>>>>date_planned>>>>>", date_planned)
                user_tz = pytz.timezone(self.env.user.tz or self.env.context.get('tz'))
                date_planned = pytz.utc.localize(date_planned).astimezone(user_tz).replace(tzinfo=None)
                old_date = pytz.utc.localize(old_date).astimezone(user_tz).replace(tzinfo=None)
            elif type(date_planned) == str:
                new = datetime.strptime(date_planned, "%Y-%m-%d %H:%M:%S")
                # old = datetime.strptime(old_date, "%Y-%m-%d %H:%M:%S")
                user_tz = pytz.timezone(self.env.user.tz or self.env.context.get('tz'))
                date_planned = pytz.utc.localize(new).astimezone(user_tz).replace(tzinfo=None)
                old_date = pytz.utc.localize(old_date).astimezone(user_tz).replace(tzinfo=None)

            self.message_post(body=_('Receipt date Updated :- %s <i class="fa fa-long-arrow-right"></i> %s', old_date, date_planned),
                              message_type='comment', subtype_xmlid="mail.mt_comment")
        return super(PoDateChangeLog, self).write(value)
