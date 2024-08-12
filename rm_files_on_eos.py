"""
Recursively deletes every subdirectory of a given directory on eos.cd
"""

import os
import subprocess

full  = "/eos/vbc/experiments/cms/store/user/aguven/MET/CRAB3_DATA"

for root, directories, files in os.walk(full):
    short =  '/' + '/'.join(root.split('/')[5:])
    for file in files:
        file_path = os.path.join(short, file)
        if os.path.isfile(os.path.join(root, file)):
            # print file_path
            subprocess.Popen(' '.join(['xrdfs', 'root://eos.grid.vbc.ac.at', 'rm', file_path]),
                             shell=True,stdin=None, stdout=None, stderr=None)

for root, directories, files in os.walk(full):
    short =  '/' + '/'.join(root.split('/')[5:])
    # print root
    # print short

    subprocess.Popen(' '.join(['xrdfs', 'root://eos.grid.vbc.ac.at', 'rmdir', short]),
                             shell=True,stdin=None, stdout=None, stderr=None)