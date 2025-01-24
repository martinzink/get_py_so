import sysconfig
import os
import glob

v = sysconfig.get_config_vars()
so_name = v['LDLIBRARY']
libdir = v['LIBDIR']
libpl = v['LIBPL']
libdir_so = os.path.join(libdir, so_name)
libpl_so = os.path.join(libpl, so_name)

print(libdir_so)
print(os.path.exists(libdir_so))
print(libpl_so)
print(os.path.exists(libpl_so))

print("OLD")
print(min(glob.glob(os.path.join(v['LIBDIR'], f"libpython{sysconfig.get_config_var('VERSION')}.so*")), key=len, default=''))