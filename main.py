import sysconfig, os, glob

v = sysconfig.get_config_vars();

so_paths = glob.glob(f"{v['LIBDIR']}/**/***{v['LDLIBRARY']}*")
print(so_paths)
for so_path in so_paths:
    print(so_path)
    if os.path.exists(so_path):
        print(f"FOUND IT {so_path}")