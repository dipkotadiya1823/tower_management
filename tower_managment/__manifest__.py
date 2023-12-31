{
    'name': 'Tower Management',
    'author': 'Entrivis Tech Pvt Ltd',
    'website': 'www.entrivistech.com',
    'version': '1.0',
    'depends': ['base','sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/tower_manage.xml',
        'data/tower.manage.csv',
        'wizard/report_print_view.xml',
        'wizard/order_report.xml',
        'report/report_action.xml',
        'report/sales_report_action.xml',
        'wizard/tips_info_view.xml',
        'views/tower_view.xml',
        'views/res_partner_view.xml',
        'views/res_partner_base_view.xml',
        'views/emanities.xml',
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
