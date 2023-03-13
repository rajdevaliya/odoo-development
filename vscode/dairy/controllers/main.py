from odoo import http
from odoo.http import request

# Creating a Seller Controller
class DairySeller(http.Controller):
    # Seller Controller

    @http.route('/dairy/create_seller/', website=True, auth='public')
    def dairy_seller(self, **post):
        # return 'Hello Sellers'
        # countries = request.env['res.country'].sudo().search([])
        country_id = request.env['res.country'].sudo().search([])
        country_states = request.env['res.country.state'].sudo().search([])
        values = {'countries': country_id, 'country_states': country_states}

        if post:
            em = post.get('email')
            emails = request.env['dairy.seller'].search([('email', '=', em)])
            if emails:
                return request.render("dairy.seller_duplicate_email_template")

            else:
                seller = request.env['dairy.seller'].sudo().create({
                    'seller_id': post.get("seller_id"),
                    'seller_last_name': post.get('seller_last_name'),
                    'email': post.get('email'),
                    'mobile': post.get('mobile'),
                    'gender': post.get('gender'),
                    'adrs': post.get('adrs'),
                    "state_id": post.get("state_id"),
                    "country_id": post.get("country_id")
                })
                vals = {
                    'seller': seller,
                }
                return request.render("dairy.seller_thanks_template", vals)

        return request.render("dairy.create_seller", values)


    # Country States
    @http.route(['/dairy/country_infos/<model("res.country"):country>'], type='json', auth="public", methods=['POST'],
                website=True)
    def country_infos(self, country, **kw):
        print("country_id=================", country.name)
        states = dict(
            states=[(st.id, st.name, st.code) for st in country.state_ids],
        )
        print("states =============== >>>>>", states)
        return states
