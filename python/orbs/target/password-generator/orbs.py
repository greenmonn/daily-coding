#!/usr/bin/env python

import io
import os
import sys
import re
import copy
import time
import subprocess

import argparse


class ORBSlicer():
    def __init__(self):
        self.MAX_DEL_WINDOW_SIZE = 3
        self.target_code = None
        pass

    def _set_criteria(self):
        # TODO: set criteria (variable, input)
        # Question: How to select criteria variable? (manually?)
        self.input_set = []
        self.target_location = 172    # line number
        self.original_value = None

    def _read_source_file(self, filepath):
        # TODO: multiple files
        self.filepath = filepath
        self.temp_filepath = '{}temp_test.py'.format(self.filepath[:-3])
        self.criteria_filepath = os.path.join(
            os.path.dirname(self.filepath), 'criteria.txt')

        with open(filepath) as f:
            self.program_lines = f.readlines()
            self.program_lines_original = copy.deepcopy(
                self.program_lines)  # fixed

    def _write_code_to_file(self, filename=None):
        if filename == None:
            filename = self.temp_filepath

        code_str = ''.join(self.program_lines)

        with open(filename, 'w+') as f:
            f.write(code_str)

    def setup(self, filepath, arguments):
        self.program_lines = None
        self.program_lines_before = None    # for reverting of failing slice
        self.program_lines_original = None
        self.arguments = arguments

        self.filepath = None
        self.temp_filepath = None
        self.criteria_filepath = None

        self._read_source_file(filepath)
        self._set_criteria()

        # TODO: Print settings

    def _execute_program(self):
        argv = ['python', self.temp_filepath]
        argv.extend(self.arguments)

        # runpy.run_path(self.temp_filepath, run_name='__main__')
        # aexec(self.target_code, globals())
        try:
            output = subprocess.check_output(argv)
            output = output.decode('ascii')
            # print(output.decode('ascii'))
        except subprocess.CalledProcessError as e:
            print("command '{}' return with error (code {}): \
                {}".format(e.cmd, e.returncode, e.output))
            return False

        regex = re.compile(r'v_trajectory captured:\s[^\n]*##')
        matches = regex.findall(output)
        if len(matches) > 0:
            matched_elements = [m[23:-2] for m in matches]
            print(matched_elements)
            if self.original_value == None:
                self.original_value = matched_elements
                print('original value updated')
                return True

            else:
                for i, value in enumerate(matched_elements):
                    if self.original_value[i] != value:
                        return False

                return True

        return False

    def _compile_program(self):
        code_str = ''.join(self.program_lines)
        try:
            code = compile(code_str, 'orbs_target.py', 'exec')

        except SyntaxError as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            line_number = err.lineno
        else:
            self.target_code = code
            with open(self.temp_filepath, 'w') as f:
                f.write(code_str)

            return True

        print(("%s at line %d of source string: %s" %
               (error_class, line_number, detail)))

        return False

    def _check_criteria(self):
        # check target variable at target location is identical to the original
        if not os.path.isfile(self.criteria_filepath):
            return False

        has_same_value = False
        with open(self.criteria_filepath) as f:
            value = f.read()
            if value == self.original_value:
                has_same_value = True
                # What if type is different? compare in byte-level?

        if has_same_value:
            os.remove(self.criteria_filepath)
            return True

        return False

    def _delete_lines(self, start, end):
        # TODO: consider indentation level
        s = len(self.program_lines) - 1 - end
        e = len(self.program_lines) - 1 - start

        print('attempt to delete {} to {}'.format(s, e))
        assert s <= e
        assert s >= 0 and e >= 0

        del self.program_lines[s:e+1]

    def do_slicing(self):
        self.program_lines = copy.deepcopy(self.program_lines_original)
        deleted = False

        self._execute_program()

        print('Origianal Value for Criteria: ', self.original_value)

        while not deleted:  # until nothing can be deleted
            i = 0
            while i < len(self.program_lines):
                builds = False
                print('{}th iterations'.format(i))

                self.program_lines_before = copy.deepcopy(
                    self.program_lines)

                for j in range(0, self.MAX_DEL_WINDOW_SIZE):
                    self._delete_lines(
                        # TODO: why i becomes len(self.program_lines)
                        # when we attempt to delete 0 to 0? (behave like 0 to -1)
                        min(i, len(self.program_lines)-1), min(i+j, len(self.program_lines)-1))

                    builds = self._compile_program()
                    if builds:
                        # print('build success: window size {}'.format(j+1))
                        break

                if builds:
                    execute_success = self._execute_program()
                    if execute_success:
                        deleted = True
                        self._write_code_to_file(
                            '{}.success.{}_{}.py'.format(self.filepath[:-3], i, str(time.time())))
                    else:
                        self._write_code_to_file(
                            '{}.executefail.{}.py'.format(self.filepath[:-3], i))
                        self.program_lines = copy.deepcopy(
                            self.program_lines_before)
                        i += 1

                else:
                    self._write_code_to_file(
                        '{}.buildfail.{}.py'.format(self.filepath[:-3], i))

                    # print('restore: original program lines {}',
                    #   len(self.program_lines_before))
                    self.program_lines = copy.deepcopy(
                        self.program_lines_before)
                    i += 1


if __name__ == '__main__':
    argv = []

    if sys.argv[0] == 'python':
        argv = sys.argv[2:]
    else:
        argv = sys.argv[1:]

    print(argv)
    orbs = ORBSlicer()
    filepath = argv[0]
    arguments = argv[1:]
    # orbs._read_source_file(filepath, arguments_str)
    # orbs._delete_lines(10, 20)
    # orbs._compile_program()
    # result = orbs._execute_program()
    # print('result: ', result)
    # orbs._write_code_to_file()

    orbs.setup(filepath, arguments)
    orbs.do_slicing()
