from setuptools import setup, find_packages

setup(
    name='pdf_scrapper_api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'PyPDF2>=1.0.0',
        'shutil',
        'git+https://github.com/pdftables/python-pdftables-api.git',
        'PyMuPDF>=1.18.14', # Esta es la dependencia para fitz (PyMuPDF es el nombre del paquete que incluye fitz)
    ],
)