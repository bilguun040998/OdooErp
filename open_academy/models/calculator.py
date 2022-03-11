# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models,fields


class Calculator(models.Model):
    _name = 'calculator.calculator'

    numbers = fields.Char(string='Number', required=True)
