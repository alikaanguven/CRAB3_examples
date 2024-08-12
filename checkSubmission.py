"""
A very simple script taking to JSONs and outputting the residual lumi sections.
It is merely a demonstraion of the '-' operator on LumiList objects.
"""


import json
from FWCore.PythonUtilities.LumiList import LumiList

first_missing_json = "crab_projects/crab_20240808_163902/results/notPublishedLumis.json"
second_to_process_json = "crab_projects/crab_20240811_100353/results/processedLumis.json"

firstMissing=LumiList(filename=first_missing_json)
secondToProcess=LumiList(filename=second_to_process_json)

print(firstMissing - secondToProcess)