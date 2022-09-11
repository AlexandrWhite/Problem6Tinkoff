import argparse
import sys
import pickle
import re
import os
import random as rnd

parser = argparse.ArgumentParser()

parser.add_argument("--input-dir")
# parser.add_argument("--model", required="True")

args = parser.parse_args()

# data_source = sys.stdin if args.input_dir is None else os.listdir(args.input_dir)
model = {}


def create_ngram(data, n):
    for line in data.readlines():
        if not line.isspace():
            line = line.lower()
            line = re.sub(r'[^(\w|\s)]', '', line)
            line = re.sub(r'\d|\(|\)|', '', line)
            tokens = line.split()
            for i in range(0, len(tokens) - n + 1):
                yield ' '.join(tokens[i:i + n]), tokens[i + n] if i + n < len(tokens) else 'ENDWORD'


def train_model(data):
    for ngram, next_word in create_ngram(data, 2):
        if ngram not in model.keys():
            model[ngram] = {next_word: 1}
        else:
            if next_word not in model[ngram].keys():
                model[ngram][next_word] = 1
            else:
                model[ngram][next_word] += 1


def save_model():
    with open(args.model, 'wb') as f:
        pickle.dump(model, f)


def generate():
    start = rnd.choice(list(model.items()))
    print(start)


if args.input_dir is None:
    train_model(sys.stdin)
else:
    for file in os.listdir(args.input_dir):
        with open(args.input_dir + '\\' + file, 'r') as f:
            train_model(f)

# save_model()
generate()

for key, value in model.items():
    print(key, value)
