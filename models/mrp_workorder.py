# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _


class MrpWorkorder(models.Model):
    _name = 'mrp.workorder'
    _inherit = ['mrp.workorder','mail.thread', 'mail.activity.mixin']



