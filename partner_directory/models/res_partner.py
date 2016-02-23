# -*- coding: utf-8 -*-
# © 2016 Michael Viriyananda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agp

from openerp import models, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    @api.multi
    def button_set_customer(self):
        for partner in self:
            self._flag_partner(
                change_customer=True,
                customer=True,
                change_supplier=False,
                supplier=False
            )

        return True

    @api.multi
    def button_set_supplier(self):
        for partner in self:
            self._flag_partner(
                change_customer=False,
                customer=False,
                change_supplier=True,
                supplier=True
            )

        return True

    @api.multi
    def button_unset_customer(self):
        for partner in self:
            self._flag_partner(
                change_customer=True,
                customer=False,
                change_supplier=False,
                supplier=False
            )

        return True

    @api.multi
    def button_unset_supplier(self):
        for partner in self:
            self._flag_partner(
                change_customer=False,
                customer=True,
                change_supplier=True,
                supplier=False
            )

        return True

    @api.multi
    def _flag_partner(
        self,
        change_customer=False,
        customer=True,
        change_supplier=False,
        supplier=False
    ):

        partner_ids = [self.id]
        
        lst_partner = self.browse(partner_ids)

        partner_dict = {}
        if change_customer:
            partner_dict['customer'] = customer
        if change_supplier:
            partner_dict['supplier'] = supplier
        lst_partner.write(partner_dict)

        return True

res_partner()
