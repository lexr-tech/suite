import os
import shutil
import tempfile
import pyperclip
import sys
from plyer import notification
from pdf2docx import Converter

lexr_icon_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Icon\lexr_icon.ico")

def pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

def convert_files_in_folder(folder_path):
    docx_folder = os.path.join(folder_path, "Converted DOCXs")
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
    if not pdf_files:
        return
    notification.notify(
        title="LEXR Doconverter",
        message='Conversion in process...',
        app_icon=lexr_icon_path,
        timeout=10
    )           
    if not os.path.exists(docx_folder):
        os.makedirs(docx_folder)
    for file in pdf_files:
        full_path = os.path.join(folder_path, file)
        docx_path = os.path.join(docx_folder, os.path.splitext(file)[0] + '.docx')
        pdf_to_docx(full_path, docx_path)
        notification.notify(
            title="LEXR Doconverter",
            message=f'{file} converted to DOCX.',
            app_icon=lexr_icon_path,
            timeout=10
        )            

def main():
    try:
        folder_path = pyperclip.paste().strip()
        if os.path.isdir(folder_path):
            convert_files_in_folder(folder_path)
        else:
            print("Clipboard does not contain a valid directory path.")
    except Exception as e:
        print(f"Error: {str(e)}. Please contact the LEXR Tech team.")
        sys.exit(1)

if __name__ == "__main__":
    main()