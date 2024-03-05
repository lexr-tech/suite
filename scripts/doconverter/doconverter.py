import ctypes
import os
import subprocess
import comtypes.client
import shutil
import tempfile
import pyperclip
import sys
from plyer import notification

# Unused; only use if somehow Word processes are locked
# def kill_word_processes():
#    try:
#        subprocess.call(['taskkill', '/F', '/IM', 'WINWORD.EXE'])
#    except Exception as e:
#        print(f"Failed to kill Word processes: {e}")

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

def docx_to_pdf(docx_path, pdf_path):
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    temp_dir = tempfile.gettempdir()
    base_name = os.path.basename(docx_path)
    temp_docx_path = os.path.join(temp_dir, f"temp_{base_name}")
    shutil.copyfile(docx_path, temp_docx_path)
    try:
        doc = word.Documents.Open(temp_docx_path)
        if doc.Comments.Count > 0:
            doc.DeleteAllComments()
        doc.SaveAs(pdf_path, FileFormat=17)
    finally:
        if doc:
            doc.Close(False)
        if os.path.exists(temp_docx_path):
            os.remove(temp_docx_path)
    word.Quit()

def convert_files_in_folder(folder_path):
    pdf_folder = os.path.join(folder_path, "Converted PDFs")
    docx_files = [file for file in os.listdir(folder_path) if file.endswith(".docx")]
    if not docx_files:
        return
    notification.notify(
        title="LEXR Doconverter",
        message='Conversion in process...',
        app_icon=lexr_icon_path,
        timeout=10
    )           
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith(".docx") and not is_hidden(full_path):
            docx_path = full_path
            pdf_path = os.path.join(pdf_folder, os.path.splitext(file)[0] + '.pdf')
            docx_to_pdf(docx_path, pdf_path)
            notification.notify(
                title="LEXR Doconverter",
                message=f'{file} converted to PDF.',
                app_icon=lexr_icon_path,
                timeout=10
            )            

def main():
    try:
        # kill_word_processes()
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