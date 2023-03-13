import pytz
from odoo.addons.purchase.controllers import portal
from odoo import http
from odoo.http import request
from datetime import datetime, time
from pytz import timezone, UTC

class WebsitePurchaseorderDateChange(portal.CustomerPortal):

    @http.route()
    def portal_my_purchase_order_update_dates(self, order_id=None, access_token=None, **kw):
        """
        This function will take date from website purchase order
        and change the date in backend order
        :param order_id:
        :param access_token:
        :param kw:
        :return:
        """
        res = super(WebsitePurchaseorderDateChange, self).portal_my_purchase_order_update_dates(order_id=None,
                                                                                                access_token=None)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> date", kw.get("my_datetimepicker"))
        date = kw.get("my_datetimepicker")
        datetime_object = datetime.strptime(date, "%m/%d/%Y %I:%M %p") #.utcnow()#.astimezone(timezone(request.env.context.get('tz')))
        # tz = pytz.timezone(request.env.context.get('tz'))
        # new = pytz.utc.localize(datetime_object).astimezone(tz)
        new = timezone(request.env.user.tz or request.env.context.get('tz') or 'UTC').localize(datetime_object).astimezone(UTC).replace(tzinfo=None)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> new", new)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> datetime object", datetime_object)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> datetime", new.tzinfo)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> datetime", request.env.user.tz)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> datetime", request.env.context.get("tz"))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> type", type(datetime_object))
        # converted_datetime_to_string = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        # converted =datetime.strptime(converted_datetime_to_string, '%Y-%m-%d %H:%M:%S')
        # print(">>>>>>>>>>>>>>>>>>>> order id", type(order_id))
        search_order = request.env['purchase.order'].sudo().search([("id", "=", order_id)])
        if search_order and datetime_object:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>> inside if statement")
            search_order.write({"date_planned": new})
            return request.redirect(f"/my/purchase/{order_id}?access_token={access_token}")
        return res
