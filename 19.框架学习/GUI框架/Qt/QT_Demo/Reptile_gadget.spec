# -*- mode: python -*-

block_cipher = None

added_files = [ ('images', 'images'),
                ('ico_rc.py', '.')
                ]

a = Analysis(['Reptile_gadget.py'],
             pathex=['D:\\21-DAY-Python\\19.Kuangjia\\GUI_Study\\Qt\\QT_Demo'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hujianli_Tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='D:\\phpstudy_pro\\hjl01.ico')
