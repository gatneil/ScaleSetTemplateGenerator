import argparse
import json
import sys

def getListEntryIndex(k, v, l):
    i = 0
    for elem in l:
        if (elem[k] == v):
            return i
        
        i = i+1

    return None


parser = argparse.ArgumentParser(description="Generate VMSS Quickstart Templates.")
parser.add_argument("--osType", required=True, choices=["Windows", "Linux", "Both"], type=str)
parser.add_argument("--outFilePath", required=False, type=str)
parser.add_argument("--debug", required=False, type=bool)
args = parser.parse_args()

outFilePath = "out/out.json"
if args.outFilePath:
    outFilePath = args.outFilePath

with open("templates/linuxScaleSet.json", "r") as linuxScaleSetFile:
    res = json.loads(linuxScaleSetFile.read())

if args.osType == "Windows":
    with open("templates/windowsImageReference.json", "r") as windowsImageReferenceFile:
        windowsImageReference = json.loads(windowsImageReferenceFile.read())

    vmssResourceIndex = getListEntryIndex("type", "Microsoft.Compute/virtualMachineScaleSets", res["resources"])
    res["resources"][vmssResourceIndex]["properties"]["virtualMachineProfile"]["imageReference"] = windowsImageReference

elif args.osType == "Linux":
    ""
elif args.osType == "Both":
    print("TODO")
    sys.exit()
else:
    print("Invalid osType. Not generating template.")
    sys.exit()

if args.debug:
    print(res)
else:
    with open(outFilePath, "w") as outFile:
        outFile.write(json.dumps(res))




