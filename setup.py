from setuptools import setup, find_packages

setup(
    name='pdf_scrapper_api',
    version='1.5',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'PyMuPDF>=1.18.14',
        'autocorrect>=1.0.0',
        'pdftables_api @ https://github.com/pdftables/python-pdftables-api/archive/master.tar.gz',
        'PyQt6>=6.0.0',
    ],
)