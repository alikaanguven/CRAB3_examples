
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

config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17RECO-106X_mc2017_realistic_v6-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.splitting = 'LumiBased' # FileBased/LumiBased/...
# config.Data.unitsPerJob = 30
config.Data.publication = True
## It is better to name your output dataset uniquely
## for instance naming them with version numbers
## This way when the dataset is published on DAS,
## it will only list the files from correct submission.
config.Data.outputDatasetTag = 'RunIISummer20UL17CustomMiniAODpv2-106X_mc2017_realistic_v9'

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
