"""
The usual CRAB submission code.
"""

import subprocess

datasets = {
    'wjetstolnuht0100_2017':  '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht0200_2017':  '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht0400_2017':  '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht0600_2017':  '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht0800_2017':  '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht1200_2017':  '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'wjetstolnuht2500_2017':  '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht0100_2017': '/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht0200_2017': '/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht0400_2017': '/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht0600_2017': '/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht0800_2017': '/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht1200_2017': '/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
    'zjetstonunuht2500_2017': '/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM',
}


for tag, name in datasets.items():
    crabConfig = """
import CRABClient
from CRABClient.UserUtilities import config 

config = config()
## If left unset CRAB will create one with the timestamp
## e.g. crab_20240229_214555
## config.General.requestName = 'my_unique_request_name'
## workArea will be the folder name
## e.g. the information about your submission will be 
##      written to this directory:
##      crab_projects/crab_20240229_214555
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/users/alikaan.gueven/Production/CMSSW_10_6_28/src/SoftDisplacedVertices/CustomMiniAOD/configuration/MC_UL17_CustomMiniAOD.py'
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2

config.Data.inputDataset = '{}'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic' # FileBased/LumiBased/...
config.Data.publication = True
## It is better to name your output dataset uniquely
## for instance naming them with version numbers
## This way when the dataset is published on DAS,
## it will only list the files from correct submission.
### When you CRAB saves the outputs it firsts creates the top directories with the first part of the inputDataset name.
### e.g. WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8
### Next it creates a subdirectory with the name that you specify.
### e.g. CustomMiniAOD_pv2
### Finally It creates a subsubdirectory where the name is the date and time of the submission
### e.g.
### The final output looks like this:
### /store/user/aguven/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/
### ├── CustomMiniAOD_pv1
### │   └── 240806_065234
### │       └── 0000
### │           ├── output_10.root
config.Data.outputDatasetTag = 'CustomMiniAOD_pv1'

## partialDataset will not issue TAPERECALL
## it will simply get the available block of data on any DISK
## only complete blocks are considered.
# config.Data.partialDataset = True

## If ignoreLocality = True
## it will run the data at any available site regardless of
## the location. whitelist,blacklist will be respected.
## config.Data.ignoreLocality = True

config.Site.blacklist=["T2_BR_SPRACE"]

config.Site.storageSite = "T2_AT_Vienna"
""".format(name)
    
    with open('{}_crabConfig.py'.format(tag), "w") as f:
        f.write(crabConfig)
        
    print name
    subprocess.call(['crab', 'submit', '-c', '{}_crabConfig.py'.format(tag)])