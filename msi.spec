# -*- mode: python -*-
a = Analysis(['msi.py'],
             pathex=['c:\\Users\\bmelton\\Google Drive\\mainwindow'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\msi', 'msi.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'msi'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'msi.app'))
