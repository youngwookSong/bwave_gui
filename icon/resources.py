import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
icon_close = os.path.join(root, 'close.png')
icon_maxi = os.path.join(root, 'maxi.png')
icon_mini = os.path.join(root, 'mini.png')

icon_search = os.path.join(root, 'search.png')
icon_reset = os.path.join(root, 'reset.png')
icon_delete = os.path.join(root, 'trash.png')

logo = os.path.join(root, 'bwave_logo_2.png')

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)