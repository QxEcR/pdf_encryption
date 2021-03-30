from setuptools import setup
setup(
    name='pdf-encrypt',
    version='0.1.0',
    packages=['maincli'],
    install_requires=[
        'PyPDF2'
    ],
    entry_points={
        'console_scripts': [
            'pdf_pass = maincli.__main__:main',
        ]
    }
)
