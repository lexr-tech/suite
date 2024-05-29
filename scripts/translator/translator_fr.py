import os
import deepl
import pyperclip
from plyer import notification

def extract_deepl_key_from_file(key_path):
    deepl_key_prefix = "deepl_key ="
    try:
        with open(key_path, "r") as file:
            for line in file:
                if line.strip().startswith(deepl_key_prefix):
                    deepl_key = line.strip().split("=")[1].strip().strip('"').strip("'")
                    return deepl_key
        print("deepl_key variable not found in the file.")
    except FileNotFoundError:
        print(f"File not found: {key_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

key_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Keys\keys.txt")
lexr_icon_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\Icon\lexr_icon.ico")
deepl_key = extract_deepl_key_from_file(key_path)

translator = deepl.Translator(deepl_key)
text_to_translate = pyperclip.paste()
translated_text = translator.translate_text(text_to_translate, target_lang="FR", formality="prefer_less")
pyperclip.copy(translated_text.text)
notification.notify(
    title="LEXR Translator",
    message=f'{translated_text}',
    app_icon=lexr_icon_path,
    timeout=10
)