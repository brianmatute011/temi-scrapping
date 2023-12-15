from setuptools import setup, find_packages

setup(
    name='pdf_scrapper_api',
    version='1.5',
    author='Alphax',
    author_email='brianmatute011@gmail.com',
    description='Una app para extraer información de PDFs',
    url='https://github.com/brianmatute011/temi-scrapping',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'PyMuPDF>=1.18.14',
        'autocorrect>=1.0.0',
        'pdftables_api @ https://github.com/pdftables/python-pdftables-api/archive/master.tar.gz',
        'PyQt6>=6.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=3.0.0',
            'flake8>=3.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'pdf_scrapper=pdf_scrapper_api.scripts.main:main',
        ],
    },
    python_requires='>=3.6',
)