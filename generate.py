import argparse
import json
import sys

from collections import OrderedDict

def getListEntryIndex(k, v, l):
    i = 0
    for elem in l:
        if (elem[k] == v):
            return i
        
        i = i+1

    return None


parser = argparse.ArgumentParser(description="Generate VMSS Quickstart Templates.")
parser.add_argument("--osType", required=True, choices=["Windows", "Linux", "Both"], type=str)
parser.add_argument("--outFilePath", required=False, type=str, default="out/out.json")
parser.add_argument("--debug", required=False, type=bool, choices=[True, False], default=False)
parser.add_argument("--vnetType", required=False, choices=["New", "Existing"], type=str, default="New")
args = parser.parse_args()

with open("templates/linuxScaleSet.json", "r") as linuxScaleSetFile:
    res = json.loads(linuxScaleSetFile.read(), object_pairs_hook=OrderedDict)

with open("templates/vnet.json", "r") as vnetFile:
    vnetDict = json.loads(vnetFile.read(), object_pairs_hook=OrderedDict)


# customize OS Type
if args.osType == "Windows":
    with open("templates/windowsImageReference.json", "r") as windowsImageReferenceFile:
        windowsImageReference = json.loads(windowsImageReferenceFile.read())

    vmssResourceIndex = getListEntryIndex("type", "Microsoft.Compute/virtualMachineScaleSets", res["resources"])
    res["resources"][vmssResourceIndex]["properties"]["virtualMachineProfile"]["storageProfile"]["imageReference"] = windowsImageReference

elif args.osType == "Linux":
    ""
elif args.osType == "Both":
    print("TODO")
    sys.exit()
else:
    print("Invalid osType. Not generating template.")
    sys.exit()


# customize new or existing VNET
if args.vnetType == "New":
    res["variables"]["vnetName"] = "vnet"
    res["variables"]["subnetName"] = "subnet"
    res["variables"]["vnetID"] = "[resourceId('Microsoft.Network/virtualNetworks',variables('vnetName'))]"
    res["variables"]["subnetRef"] = "[concat(variables('vnetID'),'/subnets/',variables('subnetName'))]"
    
    vmssResourceIndex = getListEntryIndex("type", "Microsoft.Compute/virtualMachineScaleSets", res["resources"])
    res["resources"][vmssResourceIndex]["properties"]["virtualMachineProfile"]["networkProfile"]["networkInterfaceConfigurations"][0]["properties"]["ipConfigurations"][0]["properties"]["subnet"]["id"] = "[variables('subnetRef')]"
    res["resources"][vmssResourceIndex]["dependsOn"].append("[concat('Microsoft.Network/virtualNetworks/', variables('vnetName'))]")

    res["resources"].append(vnetDict["resource"])
    

    
elif args.vnetType == "Existing":
    res["parameters"]["existingSubnetResourceId"] = vnetDict["existingSubnetParameterBlock"]
    
    vmssResourceIndex = getListEntryIndex("type", "Microsoft.Compute/virtualMachineScaleSets", res["resources"])
    res["resources"][vmssResourceIndex]["properties"]["virtualMachineProfile"]["networkProfile"]["networkInterfaceConfigurations"][0]["properties"]["ipConfigurations"][0]["properties"]["subnet"]["id"] = "[parameters('existingSubnetResourceId')]"
    
else:
    print("Invalid value for vnetType. Not generating template.")
    sys.exit()


# print out result or write it to file
if args.debug:
    print(args.outFilePath)
    print(res)
else:
    with open(args.outFilePath, "w") as outFile:
        outFile.write(json.dumps(res))




