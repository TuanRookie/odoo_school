{
    'name': "School Management",
    'version': '1.0',
    'depends': [],
    'author': "The Odoo Show",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/school_information.xml',
        'views/class_infor.xml',
        'views/student_infor.xml',
        'views/subject_infor.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}