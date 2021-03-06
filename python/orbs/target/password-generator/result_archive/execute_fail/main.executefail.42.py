#!/usr/bin/env python3

# m4ngl3m3! v0.1.1
# Common password pattern generator using strings list
# Follow (Medium / Twitter): @localh0t

import argparse
import sys
import os

from Mangler import ManglingParameters
from Mangler import Mangler


def build_parser():
    """Add parser arguments and return an instance of ArgumentParser."""
    parser = argparse.ArgumentParser(description=("Common password pattern "
                              " (when in prefix-mode or dual-mode)"),
                        default=False)
    parser.add_argument("-mm", "--mutation-methods",
                        default='normal,'
                                'uppercase,'
                                'firstup,'
                                'replacevowels')
    return parser
def build_mangler_with_args(args):
    parameters = ManglingParameters()
    parameters.num_file = open(args.numbers_file, 'r').read().splitlines()
    parameters.sym_file = open(args.symbols_file, 'r').read().splitlines()
    if (args.custom_file):
        parameters.cus_file = open(args.custom_file, 'r').read().splitlines()
    parameters.mutation_mode = args.mutation_mode
    parameters.from_year = args.from_year
    parameters.to_year = args.to_year
    parameters.suffix_pos_swap = args.symbols_before_suffix
    return Mangler(mangling_parameters=parameters)
if __name__ == "__main__":
    args = build_parser().parse_args()
    mangler = build_mangler_with_args(args)
    mangler_functions = {
        "normal": mangler.normal_mangling,
        "uppercase": mangler.uppercase_mangling,
        "firstup": mangler.firstup_mangling,
        "replacevowels": mangler.replacevowels_mangling,
    }
    written_strings = 0
    with open(args.strings_file, 'r') as f:
        for line in f:
            mangled = []
            for method in args.mutation_methods.lower().split(","):
                try:
                    (name, output) = mangler_functions[method](line.strip())
                    mangled.extend(output)
                except KeyError:
                    print("[-] The method %s is not defined !" % method)
                print("[+] %s mutation method done on string: %s" %
                      (name, line.strip()))
            written_strings += len(mangled)
    print('##v_trajectory captured: {}##'.format(written_strings))
