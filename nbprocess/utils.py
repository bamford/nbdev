# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/16_utils.ipynb.

# %% auto 0
__all__ = ['BASE_QUARTO_URL', 'install_quarto', 'install', 'docs', 'preview', 'deploy', 'pypi', 'conda', 'release', 'prepare',
           'chelp']

# %% ../nbs/16_utils.ipynb 2
import sys
from pkg_resources import iter_entry_points as ep
from os import system
from fastcore.script import run
from .read import get_config
from .test import nbprocess_test
from .clean import nbprocess_clean
from .doclinks import nbprocess_export
from .cli import nbprocess_quarto, nbprocess_sidebar, nbprocess_ghp_deploy, nbprocess_bump_version

BASE_QUARTO_URL='https://www.quarto.org/download/latest/'

def _dir(): return get_config().path("lib_path").parent
def _c(f, *args, **kwargs): return f.__wrapped__(*args, **kwargs)

# %% ../nbs/16_utils.ipynb 4
def _install_linux():
    run(f'wget -nv {BASE_QUARTO_URL}quarto-linux-amd64.deb')
    system('sudo dpkg -i *64.deb && rm *64.deb')
    
def _install_mac():
    run(f'wget -nv {BASE_QUARTO_URL}quarto-macos.pkg')
    run('open quarto-macos.pkg')

def install_quarto():
    "Installs latest quarto on mac or linux.  Prints instructions for Windows."
    print('...installing Quarto')
    "Install quarto for mac and linux platforms."
    if 'darwin' in sys.platform: _install_mac()
    elif 'linux' in sys.platform: _install_linux()
    else: print('Please visit https://quarto.org/docs/get-started/ to install quarto')
    
def install():
    "Install quarto and the current library."
    install_quarto()
    run(f'pip install -e "{_dir()}[dev]"')
    

# %% ../nbs/16_utils.ipynb 6
def docs():
    "Generate the docs."
    install()
    _c(nbprocess_quarto)

# %% ../nbs/16_utils.ipynb 8
def preview():
    "Start a local docs webserver."
    install()
    _c(nbprocess_sidebar)
    _c(nbprocess_quarto, preview=True)

# %% ../nbs/16_utils.ipynb 10
def deploy():
    "Deploy docs to GitHub Pages."
    docs()
    _c(nbprocess_ghp_deploy)

# %% ../nbs/16_utils.ipynb 12
def _dist(): run(f'cd {_dir()}  && rm -rf dist && python setup.py sdist bdist_wheel')
    
def pypi(ver_bump=True):
    "Create and upload python package to pypi."
    _dist()
    run(f'twine upload --repository pypi {_dir()}/dist/*')
    if ver_bump: _c(nbprocess_bump_version)
    
def conda(ver_bump=True): 
    "Create and upload a conda package."
    run(f'fastrelease_conda_package {_dir()}')
    if ver_bump: _c(nbprocess_bump_version)
    
def release():
    "Release both conda and pypi packages."
    pypi(ver_bump=False)
    conda(ver_bump=False)
    _c(nbprocess_bump_version)

# %% ../nbs/16_utils.ipynb 14
def prepare():
    "Export notebooks to python modules, test code and clean notebooks."
    _c(nbprocess_export)
    _c(nbprocess_test)
    _c(nbprocess_clean)

# %% ../nbs/16_utils.ipynb 16
def _cs(pkg_nm): return [e for e in ep('console_scripts') if e.module_name.startswith(pkg_nm)]

# %% ../nbs/16_utils.ipynb 17
class _CL:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def chelp():
    "Show help for all console scripts"
    for e in _cs('nbprocess'): 
        nm = _CL.BOLD+_CL.BLUE+e.name+_CL.ENDC
        doc = e.load().__doc__
        spc = ' ' * (40 - len(nm))
        print(f'{nm}     {spc}{doc}')
