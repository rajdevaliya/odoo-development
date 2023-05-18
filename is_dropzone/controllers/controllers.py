# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64
import hashlib


class DragFiles(http.Controller):
    allowedTypes = [
        'text/plain',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/pdf',
        'application/rtf',
        'application/vnd.oasis.opendocument.text',
        'image/jpeg',
        'image/png',
        'image/gif',
        'image/bmp',
        'image/svg+xml',
        'audio/mpeg',
        'audio/wav',
        'audio/ogg',
        'audio/flac',
        'audio/aac',
        'video/mp4'
    ]

    @http.route('/web/upload-files', type='http', methods=['POST'])
    def upload_files(self, **kw):
        # import pdb
        # pdb.set_trace()
        files = request.httprequest.files.getlist('files')
        if files:
            if request.httprequest.method == 'POST':
                for file in files:
                    if file.content_type in self.allowedTypes:
                        file_hash = hashlib.sha1(file.read() or b'').hexdigest()
                        duplicate = request.env['ir.attachment'].sudo().search([('checksum', '=', file_hash)])
                        if not duplicate:
                            file_data = file.read()
                            file_name = file.filename
                            my_model = request.env['drag.drop.items'].sudo().create({
                                'file': base64.b64encode(file_data),
                                'name': file_name,
                                'metadata': [{'size': len(file_data), "type": file.content_type}]
                            })
                            # request.env['ir.attachment'].sudo().create({
                            #     'name': file_name,
                            #     'res_model': 'drag.drop.items',
                            #     'res_id': my_model.id,
                            #     'datas': my_model.file,
                            #     'store_fname': file_name,
                            #     'type': 'binary',
                            #     'mimetype': file.content_type
                            # })
        #
