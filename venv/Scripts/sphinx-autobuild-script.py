#!D:\Users\BG349759\PycharmProjects\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sphinx-autobuild==0.7.1','console_scripts','sphinx-autobuild'
__requires__ = 'sphinx-autobuild==0.7.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sphinx-autobuild==0.7.1', 'console_scripts', 'sphinx-autobuild')()
    )
