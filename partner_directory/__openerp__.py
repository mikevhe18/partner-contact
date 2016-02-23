# -*- coding: utf-8 -*-
# © 2016 Michael Viriyananda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agp

{
    'name': 'Partner Directory',
    'version': '8.0.1.0.0',
    'author': 'Michael Viriyananda,Odoo Community Association (OCA)',
    'category': 'Base',
    'website': 'http://github.com/mikevhe18',
    'depends': ['base'],
    'data': [
        'security/data_Groups.xml',
        'security/data_GroupsMenuAccess.xml',
        'view/view_ResPartner.xml',
        'window_action/waction_CorporatePartner.xml',
        'window_action/waction_IndividualPartner.xml',
        'window_action/waction_AllContacts.xml',
        'menu/menu_PartnersDirectory.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
