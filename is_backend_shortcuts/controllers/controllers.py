# -*- coding: utf-8 -*-

import werkzeug

from odoo import http, _
from odoo.http import request


class AccessBackendShortcut(http.Controller):

    @http.route(['/is/<string:name>',
                 '/is/<string:name>/<string:view_type>'],
                methods=['GET'], type='http', auth='user')
    def backend_shortcut(self, name=None, view_type=None, **kw):
        rec = request.env['backend.shortcut'].search([('name', '=', name)])
        act_window_id = rec.act_window_id
        print("+++++++++++++++++++++++act window id", act_window_id)
        result = '/web?'
        if rec.debug_mode:
            result += 'debug=' + rec.debug_mode + '#'
        else:
            result += '#'
        if rec:
            access_checker = self.acceess_checker(act_window_id)
            print(">>>>>>>> access_checker", access_checker)
            if access_checker:
                if name:
                    result += f'view_type={view_type or rec.view_type}&model={act_window_id.res_model}&action={act_window_id.id}'
            else:
                raise werkzeug.exceptions.NotFound('You are not Authorized to Access this Page !')
        return request.redirect(result)

    def acceess_checker(self, act_window_id):
        action = ''
        if act_window_id:
            action = 'ir.actions.act_window,' + str(act_window_id.id)
            print("+++++++++++++++++++++++++++++++++++++ action", action)
        menus = request.env['ir.ui.menu'].search([('action', '!=', ''), ('action', '=', action)])
        has_access = False
        for menu in menus:
            if menu.action.xml_id == act_window_id.xml_id:
                group_ids = menu.groups_id.ids
                has_access = self._is_has_group(group_ids)
                return has_access
        return has_access

    def _is_has_group(self, gids):
        uid = request.env.uid
        result = False
        if not gids:
            return True
        else:
            query = '''SELECT 1 FROM res_groups_users_rel WHERE uid=%s AND gid IN %s'''
            request.env.cr.execute(query, [uid, tuple(gids)])
            result = request.env.cr.fetchone()
            result = result and result[0]
        return bool(result)
