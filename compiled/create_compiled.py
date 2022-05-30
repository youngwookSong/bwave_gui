import os
import shutil
import py_compile

import resources #밖 resource
import com_resources #complide resource

control = "personal_data"

main_res = os.path.join(resources.root, control)
save_res = os.path.join(com_resources.root, control)

file_name = "resources.py"
file_name_save = file_name.split(".")[0] + ".cpython-310.py"
pyc_file = file_name_save.replace('.py', '.pyc')
print(pyc_file)

file = os.path.join(main_res, "{}".format(file_name))
py_compile.compile(file, os.path.join(save_res, pyc_file))