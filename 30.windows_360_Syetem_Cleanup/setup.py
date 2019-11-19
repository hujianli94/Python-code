#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 17:18
# filename: dabao01.py

import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\18793\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\18793\Anaconda3\tcl\tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('findfat3.py', targetName='360_System cleanup_APP.exe', base=base)
]

include_files = [
    r'C:\Users\18793\Anaconda3\DLLs\tcl86t.dll',
    r'C:\Users\18793\Anaconda3\DLLs\tk86t.dll'
]

buildOptions = dict(
    packages=[], excludes=[],
    include_files=include_files,
)

setup(
    name='System cleanup1.0',
    version='1.0',
    description='System cleanup',
    options=dict(build_exe=buildOptions),
    executables=executables
)