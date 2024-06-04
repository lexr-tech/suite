import pyperclip
import webbrowser
import re
import os

law_code_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\scripts\article_finder\law_code.txt")
jurisdiction_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\scripts\article_finder\jurisdiction.txt")
language_path = os.path.expandvars(r"C:\Users\%USERNAME%\LEXR Tech\scripts\article_finder\language.txt")

def get_jurisdiction():
    try:
        if os.path.exists(jurisdiction_path):
            with open(jurisdiction_path, 'r') as file:
                jurisdiction = file.read().strip()
                return jurisdiction
    except Exception as e:
        print(f"Error reading jurisdiction: {e}")
    return None

def get_language():
    try:
        if os.path.exists(language_path):
            with open(language_path, 'r') as file:
                language = file.read().strip()
                return language
    except Exception as e:
        print(f"Error reading language: {e}")   
    return None     

def get_last_law_code():
    try:
        if os.path.exists(law_code_path):
            with open(law_code_path, 'r') as file:
                return file.read().strip()
    except Exception as e:
        print(f"Error reading law code: {e}")
    return None

def set_last_law_code(law_code):
    try:
        os.makedirs(os.path.dirname(law_code_path), exist_ok=True)
        with open(law_code_path, 'w') as file:
            file.write(law_code)
    except Exception as e:
        print(f"Error writing law code: {e}")

def build_url(law_code, language, article_number, article_suffix, jurisdiction):
    ### SWITZERLAND ###
    # Federal Constitution
    if law_code in ["fc", "bv", "cst"]:
        return f"https://www.fedlex.admin.ch/eli/cc/1999/404/{language}#art_{article_number}{article_suffix}"
    # Code of Obligations
    elif law_code in ["co", "or"]:
        return f"https://www.fedlex.admin.ch/eli/cc/27/317_321_377/{language}#art_{article_number}{article_suffix}"
    # Civil Code
    elif law_code in ["cc", "zgb"]:
        return f"https://www.fedlex.admin.ch/eli/cc/24/233_245_233/{language}#art_{article_number}{article_suffix}"
    # Criminal Code
    elif law_code in ["scc", "stgb", "cp"]:
        if law_code != "stgb":
            return f"https://www.fedlex.admin.ch/eli/cc/54/757_781_799/{language}#art_{article_number}{article_suffix}"
        else:
            if jurisdiction == "ch":
                return f"https://www.fedlex.admin.ch/eli/cc/54/757_781_799/{language}#art_{article_number}{article_suffix}"
            elif jurisdiction == "de":
                return f"https://www.gesetze-im-internet.de/stgb/__{article_number}{article_suffix}.html"
    # Data Protection
    elif law_code in ["fadp", "dsg", "lpd"]:
        return f"https://www.fedlex.admin.ch/eli/cc/2022/491/{language}#art_{article_number}{article_suffix}"
    # Copyright
    elif law_code in ["copa", "urg", "lda"]:
        return f"https://www.fedlex.admin.ch/eli/cc/1993/1798_1798_1798/{language}#art_{article_number}{article_suffix}"
    ### GERMANY ###
    # Basic Law
    elif law_code in ["gg"]:
        return f"https://www.gesetze-im-internet.de/gg/art_{article_number}{article_suffix}.html"
    # Civil Code
    elif law_code in ["bgb"]:
        return f"https://www.gesetze-im-internet.de/bgb/__{article_number}{article_suffix}.html"
    # Data Protection
    elif law_code in ["bdsg"]:
        return f"https://www.gesetze-im-internet.de/bdsg_2018/__{article_number}{article_suffix}.html"
    # Copyright
    elif law_code in ["urhg"]:
        return f"https://www.gesetze-im-internet.de/urhg/__{article_number}{article_suffix}.html"                     

def find_article():
    jurisdiction = get_jurisdiction()
    language = get_language()
    
    print(f"Jurisdiction: {jurisdiction}")
    print(f"Language: {language}")
    
    if not jurisdiction or not language:
        print("Jurisdiction or language not found.")
        return
    
    clipboard_content = pyperclip.paste().strip()
    print(f"Original clipboard content: {clipboard_content}")

    # Clean up clipboard content
    clipboard_content = re.sub(r'\bal\.\s*\d+', '', clipboard_content, flags=re.IGNORECASE)
    clipboard_content = re.sub(r'\bAbs\.?\s*\d+', '', clipboard_content, flags=re.IGNORECASE)
    clipboard_content = re.sub(r'\bpara\.\s*\d+', '', clipboard_content, flags=re.IGNORECASE)
    print(f"Cleaned clipboard content: {clipboard_content}")
    
    # Check if input is law code only
    law_code_only_match = re.fullmatch(r'[A-Z]+', clipboard_content, re.IGNORECASE) 
    # Check if input is article
    article_match = re.search(r'\b(?:Art(?:icle)?\.?\s*)?(\d+)([a-z])?(?:.*?\b([A-Z]{2,})\b)?.*', clipboard_content, re.IGNORECASE)

    if law_code_only_match:
        law_code = law_code_only_match.group().lower()
        set_last_law_code(law_code) # store law code
        print(f"Law code only: {law_code}")

    elif article_match:
        # Article number
        article_number = article_match.group(1)
        # Article suffix if present
        if article_match.group(2):
            if jurisdiction == "ch":
                article_suffix = f"_{article_match.group(2)}"
            else:  # jurisdiction == "de"
                article_suffix = f"{article_match.group(2)}"
        else:
            article_suffix = ""
        # Law code
        if article_match.group(3): # if present
            law_code = article_match.group(3).lower()
            set_last_law_code(law_code) # store law code
        else: # else last used code
            law_code = get_last_law_code()
        
        print(f"Article number: {article_number}")
        print(f"Article suffix: {article_suffix}")
        print(f"Law code: {law_code}")

        url = build_url(law_code, language, article_number, article_suffix, jurisdiction)
        if url:
            # Open in default browser
            webbrowser.open(url)
            print(f"URL: {url}")
        else:
            print("Failed to build URL.")
    else:
        print("No valid article number or law code found in clipboard.")

if __name__ == "__main__":
    find_article()