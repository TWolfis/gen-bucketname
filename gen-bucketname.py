#!/usr/bin/python3
#gen-bucketname.py eases the process of conjuring up bucketnames for your objectstore 
#author Thomas Wolfis 

import argparse
import time 


def getTime():
    return time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("noun",type=str,help="noun to generate a unique bucket name from")

    args = parser.parse_args()

    print(args.noun + getTime())


