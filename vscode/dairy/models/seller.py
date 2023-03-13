from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# from odoo import datetime
from datetime import datetime


class DairySeller(models.Model):
    _name = 'dairy.seller'
    _description = 'Dairy Seller'
    _rec_name = 'seller_id'

    seller_id = fields.Char(string='Seller Name', required=True)
    seller_last_name = fields.Char(string='Seller Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    mobile = fields.Char(string="Mobile", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Choose Gender", required=True)
    adrs = fields.Char(string="Address", required=True)
    country_id = fields.Many2one('res.country', required=True)
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=?', country_id)]", required=False)

    milkType = fields.Selection([('cow', 'Cow'), ('buffalo', 'Buffalo'), ('goat', 'Goat')], string="Choose Milk Type")
    liters = fields.Float(string="Enter The Liters")
    date = fields.Datetime(string="Creation Date")
    price = fields.Integer(string="Enter Price")
    active = fields.Boolean(string="Active", default=True)
    total = fields.Float(string="Total", compute="_total")

    @api.depends('liters', 'price')
    def _total(self):
        for rec in self:
            rec.total = rec.liters * rec.price

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Email already Exits')
    ]
