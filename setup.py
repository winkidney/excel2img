from distutils.core import setup
setup(
        name = 'excel2img',
        packages = ['excel2img'],
        version = '0.2',
        description = 'Save ranges from Excel documents as images',
        long_description=open('README.rst').read(),
        author = 'Alexey Gadyukov',
        author_email = 'glexey@gmail.com',
        url = 'https://github.com/glexey/excel2img',
        keywords = ['excel', 'range', 'image', 'CopyAsPicture'],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: Win32 (MS Windows)',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: Microsoft :: Windows',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Documentation',
            'Topic :: Multimedia :: Graphics :: Graphics Conversion',
            'Topic :: Office/Business :: Office Suites',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            ],
        )
