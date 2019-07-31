#!/usr/bin/env python3

import os
import sys
import argparse
import os.path

#Arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Adds a prefix to all files in a given direcctory")
    parser.add_argument("directory", help="Directory name")
    parser.add_argument("--target", default="CTRL", help="Target of Assay; Default: CTRL")
    args=parser.parse_args()
    return args

#File for loop
def main():
    args = parse_arguments()
    for file in os.listdir(args.directory):
        path=os.path.join(args.directory, file) #Path = original directory + file
        newName=str(args.target+"."+file)
        os.replace(path,os.path.join(args.directory, newName))
 
if __name__ == '__main__':
    main()
    

    

    

