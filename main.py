import sysconfig, os, glob

v = sysconfig.get_config_vars();
possible_dirs_between = ['', 'x86_64-linux-gnu', 'aarch64-linux-gnu']
fpaths = [os.path.join(v['LIBDIR'], pdir, v['LDLIBRARY']) for pdir in possible_dirs_between]
print(fpaths)
for fpath in fpaths:
    so_paths = glob.glob(f"{fpath}*")
    print(so_paths)
    for so_path in so_paths:
        print(so_path)
        if os.path.exists(so_path):
            print(f"FOUND IT {so_path}")