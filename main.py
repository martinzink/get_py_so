import sysconfig, os, glob

v = sysconfig.get_config_vars();
fpaths = [os.path.join(v[pv], v['LDLIBRARY']) for pv in ('LIBDIR', 'LIBPL')]
print(fpaths)
for fpath in fpaths:
    so_paths = glob.glob(f"{fpath}*")
    for so_path in so_paths:
        print(so_path)
        if os.path.exists(so_path):
            print(f"FOUND IT {so_path}")