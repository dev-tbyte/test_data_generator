# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['dist/main.py'],
    pathex=[],
    binaries=[],
    datas=[('dist/pyarmor_runtime_000000', 'pyarmor_runtime_000000')],
    hiddenimports=['fastapi', 'uvicorn', 'faker', 'pydantic'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='test-data-generator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
