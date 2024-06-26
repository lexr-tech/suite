# LEXR Productivity Suite

A collection of tools developed by LEXR Tech to improve daily workflow with documents on Windows 10/11. It is inspired by the simplicity of GNU/Linux scripts and works best with [AutoHotKey](https://www.autohotkey.com/).

Currently, the following tools are available:
* **Translator:** Instantly translate text to English, German, and French with a shortcut.
* **Doconverter:** Convert all DOCX files in a folder to PDF (and vice versa) with a shortcut.

## Installing the suite

The process to install the suite takes about 20 minutes so make sure you have some spare time.

 1. Download and install Python from [Microsoft Store](https://apps.microsoft.com/detail/9nrwmjp3717k). If you can't find the button to install it, it's likely already installed.
 2. Download and install winget from [Microsoft Store](https://apps.microsoft.com/detail/9nblggh4nns1?). If you can't find the button to install it, it's likely already installed.
 3. Download and install AutoHotKey from [here](https://www.autohotkey.com/download/ahk-install.exe).
     1. Select Express Installation.
     2. After installation finishes, click Exit.
 4. Download the installer script from [here](https://github.com/lexr-tech/suite/releases). The latest release has an
    `installer.py` file under its "Assets" section.
     1. Run the installer script with Right Click > Open with > Python.
     2. Press `y` or simply `Enter` to all prompts.
     3. If you encounter any errors, contact the LEXR Tech team.
 5. Once setup is complete, save the DeepL key with the following steps:
     1. Go to `C:\Users\%USERNAME%\LEXR Tech`.
     2. Create a folder with the name "Keys".
     3. Inside that folder, create a .txt file with the name "keys".
     4. Inside the .txt file enter only this line: `deepl_key = <your_key>`.
     5. Save the file with `Ctrl+S`.
 6. Head to `C:\Users\%USERNAME%\LEXR Tech\Shortcuts` and run the `lexr_shortcuts.ahk` file. Nothing will show up, it will run in the background. It will also run on startup next time you restart your computer.
 7. You are now ready to use the LEXR Productivity Suite!

### Notifications

The Suite tools work best with notifications enabled. If you have your notifications disabled (Do not disturb), it is strongly recommended to whitelist the Suite notifications following these steps:

 1. Open Windows Settings.
 2. Navigate to System > Notifications > Set Priority Notifications.
 3. Click Add apps.
 4. Add all entries that mention "Python".
 5. Run one of the tools using the instructions below.

## Using the suite

### Translator

 1. Copy any text with `Ctrl+C`. All languages are supported.
 2. Press `Ctrl+Alt+E` for English, `Ctrl+Alt+F` for French and `Ctrl+Alt+D` for German (Deutsch).
 3. A notification should inform that the text was successfully translated and copied to clipboard. The process of contacting the DeepL servers takes about 2 seconds.
 4. Paste your translated text with `Ctrl+V`.

### Doconverter

 1. Go to a folder that contains multiple DOCX files.
 2. Copy the directory address from the top bar to clipboard.
 3. Press `Ctrl+Shift+P`.
 4. A notification should inform you that conversion started (unless you have disabled your notifications).
 5. All PDFs are saved in a "Converted PDFs" folder in the same directory.

 For PDF to DOCX, do the same with `Ctrl+Shift+D`.

## Updating the suite

 1. Go to `C:\Users\%USERNAME%\LEXR Tech\Admin`.
 2. Run `updater.py` with Right Click > Open with > Python.
 3. If a new version is available, simply press `Enter` to all prompts in the installer script that popped up.

## Licenses

For the license of the LEXR Productivity Suite, see [LICENSE](LICENSE).

| Dependency     | License       |
|----------------|---------------|
| [packaging](https://github.com/pypa/packaging) | BSD-2-Clause OR Apache-2.0 |
| [pyperclip](https://github.com/asweigart/pyperclip) | BSD-3-Clause |
| [plyer](https://github.com/kivy/plyer) | MIT |
| [comtypes](https://github.com/enthought/comtypes) | MIT |
| [deepl](https://github.com/DeepLcom/deepl-python) | MIT |
| [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | AGPL-3.0 |
| [pdf2docx](https://github.com/ArtifexSoftware/pdf2docx) | AGPL-3.0 |