#!/usr/bin/env python3

import os
import sys
import argparse
import os.path

#1st argument is the directories name in a sting
parser = argparse.ArgumentParser(description="Adds a prefix to all files in a given direcctory")
parser.add_argument("directory", help="Directory name")
#2nd argumant is the prefix 
parser.add_argument("--target", default="CTRL", help="Target of Assay; Default: CTRL")
args=parser.parse_args()
#loops through each file in the directory
for file in os.listdir(args.directory):
    #renames each file with prefix then orignial filename
    filePath=os.path.join(args.directory, file)
    os.rename(filePath, args.target+"."+file)
    