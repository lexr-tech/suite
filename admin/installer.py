import subprocess
import sys
import os
import shutil
import tempfile

def print_boxed_message(messages, padding=2):
    max_length = max(len(message) for message in messages) + (padding * 2)
    horizontal_border = "+" + "-" * (max_length + 2) + "+"

    print(horizontal_border)
    for message in messages:
        # Calculate total padding needed for the message to be centered
        total_padding = max_length - len(message)
        # Calculate padding for the left side; right side padding will be the remainder
        left_padding = total_padding // 2 + padding
        right_padding = total_padding - left_padding + padding + 2  # Adjust for the border

        formatted_message = "|" + " " * left_padding + message + " " * right_padding + "|"

        # Adjust if the total length is off due to rounding
        if len(formatted_message) > max_length + 4:
            formatted_message = formatted_message[:max_length + 3] + "|"
        elif len(formatted_message) < max_length + 4:
            formatted_message += " " * (max_length + 4 - len(formatted_message)) + "|"

        print(formatted_message)
    print(horizontal_border)

def setup_lexr_suite():
    temp_dir = tempfile.mkdtemp()
    repo_url = "https://github.com/lexr-tech/suite.git"
    try:
        subprocess.check_call(['git', 'clone', repo_url, temp_dir])
    except subprocess.CalledProcessError as e:
        input(f"Failed to clone repository: {e}")
        return

    def copy_contents(src_dir, dest_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)

    # admin
    shortcuts_src = os.path.join(temp_dir, "admin")
    shortcuts_dest = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Admin")
    copy_contents(shortcuts_src, shortcuts_dest)       

    # icon
    icon_src = os.path.join(temp_dir, "icon")
    icon_dest = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Icon")
    copy_contents(icon_src, icon_dest)

    # scripts
    scripts_src = os.path.join(temp_dir, "scripts")
    scripts_dest = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Scripts")
    copy_contents(scripts_src, scripts_dest)    

    # shortcuts
    shortcuts_src = os.path.join(temp_dir, "shortcuts")
    shortcuts_dest = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Shortcuts")
    copy_contents(shortcuts_src, shortcuts_dest)

def is_installed(tool):
    try:
        subprocess.run(['where', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_tool(tool, install_command):
    print(f"{tool} is not installed. Would you like to install it? (Y/n)")
    user_input = input().lower()
    if user_input == '' or user_input == 'y':
        subprocess.run(install_command, shell=True)
    else:
        input(f"You chose not to install {tool}. Exiting.")

def install_python_module(module):
    print(f"{module} is not installed. Would you like to install it? (Y/n)")
    user_input = input().lower()
    if user_input == '' or user_input == 'y':
        subprocess.run(['pip', 'install', '--user', module], shell=True)
    else:
        input(f"You chose not to install {module}. Exiting.")

def create_startup_shortcut(script_path, shortcut_name):
    import win32com.client
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut_path = os.path.join(startup_folder, shortcut_name + '.lnk')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = script_path
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.IconLocation = script_path
    shortcut.save()

def setup_article_finder():
    article_finder_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\scripts\article_finder")
    
    if not os.path.exists(article_finder_path):
        os.makedirs(article_finder_path)
        
        jurisdiction = None
        while jurisdiction not in {"1", "2"}:
            print("Please select your preferred jurisdiction:\n1. Switzerland\n2. Germany")
            jurisdiction = input()
            if jurisdiction not in {"1", "2"}:
                print("Invalid selection. Please enter 1 for Switzerland or 2 for Germany.")
        
        if jurisdiction == "1":
            with open(os.path.join(article_finder_path, "jurisdiction.txt"), "w") as file:
                file.write("ch")
                
            language = None
            while language not in {"1", "2", "3", "4"}:
                print("Please select your preferred language:\n1. English\n2. German\n3. French\n4. Italian")
                language = input()
                if language not in {"1", "2", "3", "4"}:
                    print("Invalid selection. Please enter a number between 1 and 4.")
            
            lang_code = {"1": "en", "2": "de", "3": "fr", "4": "it"}[language]
            with open(os.path.join(article_finder_path, "language.txt"), "w") as file:
                file.write(lang_code)
        
        elif jurisdiction == "2":
            with open(os.path.join(article_finder_path, "jurisdiction.txt"), "w") as file:
                file.write("de")
            print("Article finder for Germany currently only supports German.")
        
        print("Article finder was setup successfully.")

def main():
    try:
        messages = [
            "Welcome! This is LEXR's installer script for the LEXR Productivity Suite.",
        ]        
        print_boxed_message(messages)

        user_input = input("Would you like to proceed? (Y/n): ").lower()
        if user_input != 'y' and user_input != '':
            input("Exiting the script. If you have questions, please contact the LEXR Tech team.")

        if not is_installed('git'):
            install_tool('Git.Git', 'winget install Git.Git')         

        try:
            from packaging import version
        except ImportError:
            install_python_module('packaging')

        try:
            import comtypes
        except ImportError:
            install_python_module('comtypes')

        try:
            import pyperclip
        except ImportError:
            install_python_module('pyperclip')

        try:
            import deepl
        except ImportError:
            install_python_module('deepl')

        try:
            import plyer
        except ImportError:
            install_python_module('plyer')

        try:
            import pdf2docx
        except ImportError:
            install_python_module('pdf2docx')            

        setup_lexr_suite()
        setup_article_finder()
        create_startup_shortcut(os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\shortcuts\lexr_shortcuts.ahk"), "lexr_shortcuts")
        input("LEXR Suite setup completed successfully. You can now exit this script.")

    except Exception as e:
        input(f"Error: {str(e)}. Please contact the LEXR Tech team.")

if __name__ == "__main__":
    main()