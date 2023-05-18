from odoo import models, fields, api


class DragAndDropItems(models.Model):
    _name = 'drag.drop.items'
    _description = 'drop your files in bulk'
    _rec_name = 'name'

    name = fields.Char('Name')
    file = fields.Binary("file", required=True)
    metadata = fields.Text("Metadata")
    audio = fields.Char(string='audio', compute="_compute_file_url")
    is_audio = fields.Boolean(string='is_audio')

    @api.depends('file')
    def _compute_file_url(self):
        for record in self:
            if record.file:
                record.audio = '/web/content/%s/%s/file/%s' % (
                    record._name, record.id, record.name)
                record.is_audio = record.audio.split('.')[-1] in ['mp3', 'ogg', 'wav']
            else:
                record.audio = ''

    def unlink(self):
        for rec in self:
            self.env['ir.attachment'].sudo().search(
                [('name', '=', rec.name), ('res_model', '=', 'drag.drop.items')]).unlink()
        return super(DragAndDropItems, self).unlink()
