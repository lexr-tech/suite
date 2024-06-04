#SingleInstance Force

^+P:: ; Ctrl+Shift+P
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\doconverter\doconverter_docx2pdf.py"
Return

^+D:: ; Ctrl+Shift+D
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\doconverter\doconverter_pdf2docx.py"
Return

^+M:: ; Ctrl+Shift+M
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\doconverter\doconverter_pdfmerger.py"
Return

^!E:: ; Ctrl+Alt+E
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\translator\translator_en.py"
Return

^!D:: ; Ctrl+Alt+D
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\translator\translator_de.py"
Return

^!F:: ; Ctrl+Alt+F
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\translator\translator_fr.py"
Return

^!I:: ; Ctrl+Alt+I
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\translator\translator_it.py"
Return

^!G:: ; Ctrl+Alt+G
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\translator\translator_el.py"
Return

^+A:: ; Ctrl+Shift+A
Run, pythonw "C:\Users\%USERNAME%\LEXR Tech\Scripts\article_finder\article_finder.py"
Return