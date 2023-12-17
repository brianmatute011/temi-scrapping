import os
import fitz  # PyMuPDF
import pdftables_api

class user_pdftables:
    def __init__(self, api_key):
        self.client = pdftables_api.Client(api_key)

    def remain(self):
        try:
            remaining_pages = self.client
            return remaining_pages.remaining( )
        except Exception as e:
            print(f"Error getting number of pages remaining: {e}")
            return None
    
    def count_page_document(input_file: str):
        try:
            if not input_file.lower().endswith('.pdf'):
                raise Exception(f"Ignoring '{input_file}': not a PDF file.")
            
            pdf_document = fitz.open(input_file)
            page_count = pdf_document.page_count
            pdf_document.close()
            return page_count

        except Exception as e:
            print(f"Error count document pages: {e}")
            return None
        
    def extract_pages(self, input_file: str, output_directory=None, **kwargs):
        try:
            if output_directory is None:
                output_directory = os.path.dirname(input_file)

            pdf_document = fitz.open(input_file)
            file_name = os.path.splitext(os.path.basename(input_file))[0]

            for page_number in range(pdf_document.page_count):
                new_document = fitz.open()
                new_document.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)

                output_path = f"{output_directory}/{file_name}_page_{page_number + 1}.pdf"
                new_document.save(output_path)
                new_document.close()

            pdf_document.close()
            print(f"Page extraction completed: {output_directory}")
            return True
        
        except Exception as e:
            print(f"Error extracting pages: {e}")
            return False
        
    def convert_pages_to_excel(self, input_file: str, output_directory=None, **kwargs):
        try:
            if output_directory is None:
                output_directory = os.path.dirname(input_file)

            for root, _, files in os.walk(input_file):
                for file in files:
                    # Check if is PDF file
                    if not file.lower().endswith('.pdf'):
                        print(f"Ignoring '{file}': not a PDF file.")
                        continue

                    file_path = os.path.join(root, file)
                    pdf_document = fitz.open(file_path)

                    # Check if the PDF has more than one page
                    if pdf_document.page_count > 1:
                        print(f"Ignoring '{file}': has more than one page.")
                        pdf_document.close()
                        continue

                    try:

                        # Convert to Excel only if you have one page
                        print(f"Converting '{file}' to Excel.")
                        excel_output = file.replace('.pdf', '.xlsx')
                        output_path = os.path.join(output_directory, excel_output)

                        # Check if the output file already exists, and remove it
                        if not os.path.exists(output_path):
                            self.client.xlsx(file_path, output_path)   
                        
                    except Exception as e:
                        print(f"Error converting '{file}' to Excel: {e}")

                    finally:
                        pdf_document.close()    
                                                  

            print("Conversions completed.")
            return True

        except Exception as e:
            print(f"Error processing files: {e}")
            return False     