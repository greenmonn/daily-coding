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
                                                  "generator using strings "
                                                  "list"),
                                     formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)
    parser.add_argument("mutation_mode",
                        metavar="MUTATION_MODE",
                        type=str,
                        help=("Mutation mode to perform: "
                              "(prefix-mode | suffix-mode | dual-mode)"),
                        choices=['prefix-mode', 'suffix-mode', 'dual-mode'])

    parser.add_argument("strings_file",
                        metavar="STRINGS_FILE",
                        type=str,
                        help="File with strings to mutate")
    parser.add_argument("output_file",
                        metavar="OUTPUT_FILE",
                        type=str,
                        help="Where to write the mutated strings")

    parser.add_argument("-fy", "--from-year",
                        metavar="FROM_YEAR",
                        type=int,
                        help="Year where our iteration starts",
                        default=2015)
    parser.add_argument("-ty", "--to-year",
                        metavar="TO_YEAR",
                        type=int,
                        help="Year where our iteration ends",
                        default=2020)
    parser.add_argument('-sy', "--short-year",
                        help=("Also add shorter year form when iterating"),
                        default=False)
    parser.add_argument("-nf", "--numbers-file",
                        default='./target/password-generator/files/numbers/numbers_set2.txt')
    parser.add_argument("-sf", "--symbols-file",
                        default='./target/password-generator/files/symbols/symbols_set2.txt')
    parser.add_argument("-cf", "--custom-file",
                        help="Custom words/dates/initials/etc file")
    parser.add_argument('-sbs', "--symbols-before-suffix",
                        help=("Insert symbols also before years/numbers/"
                              "custom (when in suffix-mode or dual-mode)"),
                        action='store_true',
                        default=False)
    parser.add_argument('-sap', "--symbols-after-prefix",
                        help=("Insert symbols also after years/numbers/custom"
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
