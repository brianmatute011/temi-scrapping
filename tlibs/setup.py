from setuptools import setup, find_packages

setup(
    name='pdf_scrapper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'matplotlib>=3.1.0',
        'pandas>=1.0.0',
        'PyMuPDF>=1.18.14', # Esta es la dependencia para fitz (PyMuPDF es el nombre del paquete que incluye fitz)
    ],
)