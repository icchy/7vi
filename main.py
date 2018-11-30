#!/home/icchy/.pyenv/versions/3.7.1/bin/python
from mitmproxy.tools.main import mitmdump
from lib import get_path, get_ts

import sys
import os
import logging
import hashlib
import subprocess
import shutil

logger = logging.Logger(__name__)
logger.addHandler(logging.StreamHandler())

CACHEDIR_NAME = '.7vi'

curdir = os.path.abspath(os.path.curdir)
bindir = os.path.abspath(os.path.dirname(sys.argv[0]))
cachedir = os.path.join(curdir, CACHEDIR_NAME)
origdir = os.path.join(cachedir, 'original')
moddir = os.path.join(cachedir, 'modified')


def run():
    scriptpath = os.path.join(bindir, 'script.py')
    assert os.path.exists(scriptpath), 'script.py not found'
    sys.argv += ['-s', scriptpath]
    sys.exit(mitmdump())

def edit(url):
    origpath = get_path(url, origdir)
    modpath = get_path(url, moddir)
    editor = os.getenv('EDITOR', 'vim')

    cp_ts = None
    if not os.path.exists(modpath) and os.path.exists(origpath):
        modpath_dir = os.path.dirname(modpath)
        if not os.path.exists(modpath_dir):
            os.makedirs(modpath_dir)
        shutil.copyfile(origpath, modpath)
        cp_ts = get_ts(modpath)

    ret = subprocess.call([editor, modpath])

    # delete if no changes on copied file
    if cp_ts and cp_ts == get_ts(modpath):
        logger.info('no changes on {}'.format(modpath))
        os.remove(modpath)
    
def main():
    if not os.path.exists(cachedir):
        os.mkdir(cachedir)
    if not os.path.exists(origdir):
        os.mkdir(origdir)
    if not os.path.exists(moddir):
        os.mkdir(moddir)

    if len(sys.argv) == 1:
        run()
    if len(sys.argv) == 2:
        edit(sys.argv[1])

    assert len(sys.argv) <= 2, 'too many arguments'


if __name__ == '__main__':
    main()
