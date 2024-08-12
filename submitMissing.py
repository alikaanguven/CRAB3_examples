"""
Use this if both `crab resubmit` and `crab recover` fail.
The remaining dataset should be already replicated on local storage (Vienna).
Then the missing lumi list is fed in the framework, so that CRAB gen find where those are found.
If you further restrict the processing site with whiteList, the jobs will be processed locally.
"""

import subprocess

datasets = {
#     'Run2017D_golden_pv2' : '/MET/Run2017D-09Aug2019_UL2017_rsb-v1/AOD',
    'Run2017E_golden_pv2' : '/MET/Run2017E-09Aug2019_UL2017_rsb-v1/AOD'
}

notFinishedLumisJSON = {
    # 'Run2017D_golden_pv2' : 'crab_projects/crab_20240808_163841/results/notPublishedLumis.json'
    'Run2017E_golden_pv2' : 'missingLumis_Run2017E.json'
}


for tag, name in datasets.items():

    crabConfig = """
import CRABClient
from CRABClient.UserUtilities import config 

config = config()

# config.General.requestName = '{}_recoveryTask_pv10'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/users/alikaan.gueven/Production/CMSSW_10_6_28/src/SoftDisplacedVertices/CustomMiniAOD/configuration/Data_UL17_CustomMiniAOD.py'
config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 1440
config.JobType.numCores = 2

config.Data.inputDataset = '{}'
config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.publication = True
config.Data.outputDatasetTag = '{}'
config.Data.partialDataset = True
config.Data.ignoreLocality = True
config.Data.lumiMask = '{}'

# config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist=["T2_AT_Vienna"]
# config.Site.blacklist=["T2_BR_SPRACE", "T2_IN_TIFR"]
config.Site.storageSite = "T2_AT_Vienna"

""".format(tag, name, tag, notFinishedLumisJSON[tag])
    with open("crabConfig_missing.py", "w") as f:
        f.write(crabConfig)
    
    print name
    subprocess.call(['crab', 'submit', '-c', 'crabConfig_missing.py'])

