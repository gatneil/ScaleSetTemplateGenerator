import argparse
import json
import sys

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
    print("TODO")
    sys.exit()
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
