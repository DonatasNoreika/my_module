# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'My Module',
    'version' : '1.1',
    'summary': 'Cia mano programa',
    'sequence': 15,
    'author': "Donatas Noreika",
    'description': """
    """,
    'category': 'Accounting/Accounting',
    'website': 'programosverslui.lt',
    'depends' : ['base'],
    'data': [
        # 'views/account_menuitem.xml',
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'qweb': [
        # "static/src/xml/account_payment.xml",
        # 'static/src/xml/account_resequence.xml',
        # "static/src/xml/account_report_backend.xml",
        # "static/src/xml/bills_tree_upload_views.xml",
        # 'static/src/xml/account_journal_activity.xml',
        # 'static/src/xml/grouped_view_widget.xml',
        # 'static/src/xml/tax_group.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
