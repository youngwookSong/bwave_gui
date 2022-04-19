import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
icon_close = os.path.join(root, 'close.png')
icon_maxi = os.path.join(root, 'maxi.png')
icon_mini = os.path.join(root, 'mini.png')

logo = os.path.join(root, 'bwave_logo_2.png')

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)