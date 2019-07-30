#!/usr/bin/env python3

import os
import sys
import argparse
import os.path

parser = argparse.ArgumentParser(description="Adds a prefix to all files in a given direcctory")
parser.add_argument("directory", help="Directory name")
parser.add_argument("--target", default="CTRL", help="Target of Assay; Default: CTRL")
args=parser.parse_args()

for file in os.listdir(args.directory):
    path=os.path.join(args.directory, file)
    newName=str(args.target+"."+file)
    os.rename(path, newName)
    newPath=os.path.join(os.getcwd(),newName)
    os.replace(newPath,os.path.join(args.directory, newName))
    

    

