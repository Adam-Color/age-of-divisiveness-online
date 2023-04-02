# https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "age-of-devisiveness-online",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)