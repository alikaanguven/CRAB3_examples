"""
Add your first partially succesfull submission project directory to lumistoProcess.
Then add all your partially succesfull submissions to processedLumis as a list.
This script will attempt to list the residual lumi sections that are not processed.
If `{}`is seen in the output, this means all the lumi sections are succesfully produced.

"""

import json
from FWCore.PythonUtilities.LumiList import LumiList
# >>> pwd
# /users/alikaan.gueven/Production/CMSSW_10_6_28/src/SoftDisplacedVertices/CustomMiniAOD/testK/2017_production

# GOLDEN_JSON = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'

lumistoProcess = {
    'Run2017B_golden_pv2' : 'crab_20240808_163726',
    'Run2017C_golden_pv2' : 'crab_20240808_163755',
    'Run2017D_golden_pv2' : 'crab_20240808_163841',
    'Run2017E_golden_pv2' : 'crab_20240808_163902',
    'Run2017F_golden_pv2' : 'crab_20240808_163820'
}


processedLumis = {
    'Run2017B_golden_pv2' : ['crab_20240808_163726', 'crab_20240810_101821'],
    'Run2017C_golden_pv2' : ['crab_20240808_163755'],
    'Run2017D_golden_pv2' : ['crab_20240808_163841', 'crab_20240812_113046'],
    'Run2017E_golden_pv2' : ['crab_20240808_163902', 'crab_20240811_100353', 'crab_20240812_142114'],
    'Run2017F_golden_pv2' : ['crab_20240808_163820']
}


for tag, proj_dirs in processedLumis.items():
    to_process = LumiList(filename="crab_projects/{}/results/lumisToProcess.json".format(lumistoProcess[tag]))
    residue = to_process
    for proj_dir in proj_dirs:
        processed = LumiList(filename="crab_projects/{}/results/processedLumis.json".format(proj_dir))
        residue = residue - processed
    print(tag)
    print(residue)
    print '-'*80