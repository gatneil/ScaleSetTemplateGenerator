import argparse
import json

parser = argparse.ArgumentParser(description="Generate VMSS Quickstart Templates.")
parser.add_argument('--osType', help='semver package version', required=True, choices=['Windows', 'Linux', 'Both'])
args = parser.parse_args()

print(args.osType)
