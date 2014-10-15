# -*- mode: python -*-
a = Analysis(['get_isolation_sources'],
             pathex=['/home/allis/Dropbox/Programming/Eclipse/GetIsolationSources'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='get_isolation_sources',
          debug=False,
          strip=None,
          upx=True,
          console=True )
