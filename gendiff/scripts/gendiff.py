#!/usr/bin/env python

from gendiff.cli import parse


def main():
    args = parse()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()