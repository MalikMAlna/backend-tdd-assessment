#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Worked with Ybrayym and watched demo by madarp"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-u', "--upper",
        action="store_true",
        help="Takes text input and returns text in uppercase")
    parser.add_argument(
        '-l', "--lower",
        action="store_true",
        help="Takes text input and returns text in lowercase")
    parser.add_argument(
        '-t', "--title",
        action="store_true",
        help="Takes text input and returns text in titlecase")
    parser.add_argument(
        'text',
        help="Text to be manipulated")
    return parser


def main(raw_args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(raw_args)
    result = args.text
    if args.upper:
        result = result.upper()
    if args.lower:
        result = result.lower()
    if args.title:
        result = result.title()
    return result


if __name__ == '__main__':
    print(main(sys.argv[1:]))
