import cx_Freeze
import sys
import cryptography.fernet

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Encrypto.py", base=base, icon="iconen.ico")]

cx_Freeze.setup(
    name = "Encrypto",
    options = {"build_exe": {"packages":["tkinter", "cryptography.fernet"], "include_files":["iconen.ico","iconen.png"]}},
    version = "0.1",
    description = "Encrypt files",
    executables = executables
    )