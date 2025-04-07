# -*- coding: utf-8 -*-
{
    'name': "My Module",
    'version': '18.0.1.0.0',
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'my_module/static/src/**/*',
        ],
    }

}