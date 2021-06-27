import cx_Freeze
import sys
import cryptography.fernet

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Decrypto.py", base=base, icon="iconde.ico"),cx_Freeze.Executable("Encrypto.py", base=base, icon="iconen.ico")]

cx_Freeze.setup(
    name = "Decrypto",
    options = {"build_exe": {"packages":["tkinter", "cryptography.fernet"], "include_files":["iconde.ico","iconde.png","iconen.ico","iconen.png"]}},
    version = "0.1",
    description = "Encrypt & Decrypt files",
    executables = executables
    )