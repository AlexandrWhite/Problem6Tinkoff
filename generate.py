import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--model", required=True)
parser.add_argument("--length", required=True)
parser.add_argument("--prefix", default="")
