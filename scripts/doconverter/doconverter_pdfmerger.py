import os
import pyperclip
import sys
from plyer import notification
from PyPDF2 import PdfMerger
import ctypes

lexr_icon_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Icon\lexr_icon.ico")

def is_hidden(filepath):
    FILE_ATTRIBUTE_HIDDEN = 0x02
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)
        assert attrs != -1
        result = bool(attrs & FILE_ATTRIBUTE_HIDDEN)
    except (AttributeError, AssertionError):
        result = False
    return result

def combine_pdfs_in_folder(folder_path):
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf") and not is_hidden(os.path.join(folder_path, file))]
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    pdf_files.sort()
    merger = PdfMerger()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        merger.append(pdf_path)

    output_path = os.path.join(folder_path, "Combined.pdf")
    merger.write(output_path)
    merger.close()

    notification.notify(
        title="LEXR PDF Merger",
        message=f"PDFs combined into {output_path}",
        app_icon=lexr_icon_path,
        timeout=10
    )

def main():
    try:
        folder_path = pyperclip.paste().strip()
        if os.path.isdir(folder_path):
            combine_pdfs_in_folder(folder_path)
        else:
            print("Clipboard does not contain a valid directory path.")
    except Exception as e:
        print(f"Error: {str(e)}. Please contact the LEXR Tech team.")
        sys.exit(1)

if __name__ == "__main__":
    main()