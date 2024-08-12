"""
This submits queries with dasgoclient to get a list of files where the missing lumi sections are found.
I generally use thi script to later pass file list to Rucio to download them to the local storage (CLIP),
and then submit jobs to process data.
example Rucio code:
$ cat missingFilesRun2018D_part1.txt | xargs -I '{}' rucio attach user.aguven:/MET/Run2018D_missingFiles/USER#0000 'cms:{}'
"""

import subprocess
import json
import time

# dataset = "/MET/Run2018B-15Feb2022_UL2018-v1/AOD"
# dataset = "/MET/Run2017E-09Aug2019_UL2017_rsb-v1/AOD"
dataset = "/MET/Run2017D-09Aug2019_UL2017_rsb-v1/AOD"

missingFiles = []

notpublished_json = "crab_projects/crab_20240808_163841/results/notPublishedLumis.json"

with open(notpublished_json) as f:
    run_lumi = json.load(f)
    for run, lumiList in run_lumi.items():
        print "-" * 80
        print run
        for lumiRange in lumiList:
            # nlumis = lumiRange[1] - lumiRange[0]
            # print lumiRange[0]
            # print lumiRange[1]
            # print range(lumiRange[0], lumiRange[1] + 1)
            for lumi in range(lumiRange[0], lumiRange[1] + 1):
                print lumi
                # print '-query=\"file dataset={} run={} lumi={}\"'.format(dataset, run, lumi)
                # subprocess.call('dasgoclient -query=\"file dataset={} run={} lumi={}\"'.format(dataset, run, lumi),
                #                 shell=True)
                p = subprocess.Popen('dasgoclient -query=\"file dataset={} run={} lumi={}\"'.format(dataset, run, lumi),
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                p.wait()
                missingFile = p.stdout.read()
                if missingFile not in missingFiles:
                    missingFiles.append(missingFile)
                # print missingFiles
                # time.sleep(1)

with open("missingFiles.txt", "w") as mF:
    for missingFile in missingFiles:
        mF.write(missingFile)

