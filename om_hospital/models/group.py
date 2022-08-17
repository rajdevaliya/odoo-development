# from odoo import models, fields, api
#
#
# class ResGroups(models.Model):
#     _inherit = 'res.groups'
#
#     def get_application_groups(self, domain):
#         group_id = self.env.ref('project.group_project_task_dependencies').id
#         return super(ResGroups, self).get_application_groups(domain + [('id', '!=', group_id)])
#
# #
# # class ResGroups(models.Model):
# #     _inheit = 'res.groups'
# #
# #     @api.model
# #     def get_application_groups(self, domain):
# #         group_id = self.env.ref['project.group_project_task_dependencies'].id
# #         return super(ResGroups, self).get_application_groups(domain + [{'id', '!=', 'group_id'}])
