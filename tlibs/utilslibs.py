from tlibs.pdf_scrapper_api import sanitize_data as sd
from tlibs import merge as mrg
import os


def get_recovery_list(absolute_path):
    sd.Sanitize(absolute_path)
    recovery_list = []
    source = absolute_path
    
    xlsx_files = [file for file in os.listdir(source) if file.endswith('.xlsx') and not file.endswith('s.xlsx')]
    xlsx_files
    for xfile in xlsx_files:
        recovery_list.append(mrg.merge( source, xfile ))

    return recovery_list  