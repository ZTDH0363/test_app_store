{
    "name": "Website Sale Mandatory Information",
    "version": "17.0.1.0.0",
    "summary": """Define mandatory information to be provided by customers when buying a product in webshop""",
    "author": "2BIT AG",
    "website": "https://2bit.ch/",
    "category": "Website",
    "license": "OPL-1",
    "installable": False,
    "auto_install": False,
    "application": False,
    "price": 89,
    "currency": "EUR",
    "depends": [
        "website_sale",
    ],
    "data": [
        "views/assets.xml",
        "views/mandatory_information_views.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/templates.xml",
        "security/ir.model.access.csv",
    ],
    "demo": ["demo/demo_mandatory_information.xml",],
    "css": [],
    "images": [
        "static/description/img/module-banner.png",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
}
