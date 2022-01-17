# carapace
Le squelette des projets PyQt5.

Commmande
===

Requirements
~~~~~~~~~~~~

Windows
~~~~~~~

You need a working windows environment to build Commmande windows packageL

    python-3.10.1-amd64.msi  (add C:\Python310;C:\Python310\Scripts; to PATH)

    reboot
 
    nsis-3.08-setup.exe

    pip install -r requirements.pip 

Once setup, create windows executable:
    cd path\carapace
    ``pyinstaller --onefile --windowed main.py``

Once windows binary is complete, create installer with:
    ``"C:\Program Files\NSIS\makensis.exe" installer.nsi``
    
