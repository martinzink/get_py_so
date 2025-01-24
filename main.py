import sysconfig, os, glob

v = sysconfig.get_config_vars();
fpaths = [os.path.join(v[pv], v['LDLIBRARY']) for pv in ('LIBDIR', 'LIBPL')];
for fpath in fpaths:
    so_paths = glob.glob(f"{fpath}*")
    for so_path in so_paths:
        if os.path.exists(so_path):
            print(so_path)
            exit(0)
exit(1)