#!/usr/bin/env python3

import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())
