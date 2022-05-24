import os
import shutil
import py_compile

import resources #밖 resource
import com_resources #complide resource

main_res = resources.root
save_res = com_resources.root

file_name = "style.py"
file_name_save = file_name.split(".")[0] + ".cpython-310.py"
pyc_file = file_name_save.replace('.py', '.pyc')
print(pyc_file)

file = os.path.join(main_res, "{}".format(file_name))
py_compile.compile(file, os.path.join(save_res, pyc_file))