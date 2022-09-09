import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("--input-dir")
#parser.add_argument("--model", required="True")

args = parser.parse_args()

data = []

if args.input_dir is None:
    data = input().split()
else:
    f = open(args.input_dir)
    line = f.readline().split()

