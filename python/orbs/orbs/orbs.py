#!/usr/bin/env python

import io
import os
import sys
import re
import copy
import time
import subprocess

import argparse


class Path():
    def __init__(self, target_file_path):
        working_directory, file_name = os.path.split(target_file_path)

        self.working_directory = working_directory

        self.temp_file_name = '{}_temp_test.py'.format(file_name[:-3])
        self.criteria_file_name = 'criteria.txt'

        self.result_path = "slices{}/".format(str(time.time()))

    def get_temp_file_path(self):
        return os.path.join(self.working_directory, self.temp_file_name)

    def get_criteria_filepath(self):
        return os.path.join(self.working_directory, self.criteria_file_name)

    def get_result_path(self):
        return os.path.join(self.working_directory, self.result_path)


class ORBSlicer():
    def __init__(self):
        self.MAX_DEL_WINDOW_SIZE = 3
        self.use_pytest = False

        """
        Criteria
        """
        self.target_location = -1    # line number
        self.original_value = None

        """
        Code Object
        """
        self.target_code = None
        self.program_lines = None
        self.program_lines_before = None    # for reverting of failing slice
        self.program_lines_original = None
        self.arguments = None

        """
        File Path
        """
        self.filepath = None
        self.temp_filepath = None
        self.criteria_filepath = None

    def set_pytest(self):
        self.use_pytest = True

    def setup(self, filepath, arguments):
        self.path = Path(filepath)
        self.filepath = filepath
        self.temp_filepath = self.path.get_temp_file_path()
        self.criteria_filepath = self.path.get_criteria_filepath()

        if len(filepath) > 0 and filepath[-8:] == '_test.py':
            self.set_pytest()

        program_lines = self._read_source_file(filepath)

        for i, arg in enumerate(arguments):
            if arg.find('./') >= 0:
                arguments[i] = arg.replace(
                    './', self.path.working_directory + '/')

        for i, l in enumerate(program_lines):
            if l.find('./') >= 0:
                program_lines[i] = l.replace(
                    './', self.path.working_directory + '/')

        self.arguments = arguments
        self.program_lines = program_lines
        self.program_lines_original = copy.deepcopy(
            self.program_lines)  # fixed

    def _read_source_file(self, filepath):
        # TODO: multiple files
        with open(filepath) as f:
            program_lines = f.readlines()

            return program_lines

    def _write_code_to_file(self, filepath=None):
        if filepath == None:
            filepath = self.temp_filepath

        try:
            os.makedirs(os.path.dirname(filepath))
        except FileExistsError:
            pass

        code_str = ''.join(self.program_lines)

        with open(filepath, 'w+') as f:
            f.write(code_str)

    def _execute_program(self):
        os.environ['PATH'] = ':'.join(
            [os.getenv('PATH'), self.path.working_directory])
        argv = ['python', self.temp_filepath]
        if self.use_pytest:
            argv = ['pytest', '-s', self.temp_filepath]
        argv.extend(self.arguments)

        try:
            output = subprocess.check_output(argv)
            output = output.decode('ascii')

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

            elif len(self.original_value) == len(matched_elements):
                for i, value in enumerate(self.original_value):
                    if value != matched_elements[i]:
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
                # What if type is mismatched? compare in byte-level?

        if has_same_value:
            os.remove(self.criteria_filepath)
            return True

        return False

    def _delete_lines(self, start, end):
        # TODO: consider indentation level
        s = len(self.program_lines) - 1 - end
        e = len(self.program_lines) - 1 - start

        print('* * * attempt to delete {} to {}'.format(s, e))
        assert s <= e
        assert s >= 0 and e >= 0

        del self.program_lines[s:e+1]

    def do_slicing(self):
        self.program_lines = copy.deepcopy(self.program_lines_original)
        deleted = False

        self._compile_program()
        self._execute_program()

        print('* Original Value for Criteria: ', self.original_value)

        while not deleted:  # until nothing can be deleted
            i = 0
            success_count = 0
            buildfail_count = 0
            execfail_count = 0

            while i < len(self.program_lines):
                builds = False
                print('* * {}th iterations'.format(i))

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
                            os.path.join(self.path.get_result_path(), 'success/success_{}_{}.py'.format(
                                i, success_count)))
                        success_count += 1

                    else:
                        self._write_code_to_file(
                            os.path.join(self.path.get_result_path(), 'execfail/execfail_{}_{}.py'.format(
                                i, execfail_count)))
                        execfail_count += 1

                        self.program_lines = copy.deepcopy(
                            self.program_lines_before)

                        i += 1
                        success_count = 0
                        buildfail_count = 0
                        execfail_count = 0

                else:
                    self._write_code_to_file(
                        os.path.join(self.path.get_result_path(), 'buildfail/buildfail_{}_{}.py'.format(
                            i, buildfail_count)))
                    buildfail_count += 1

                    self.program_lines = copy.deepcopy(
                        self.program_lines_before)

                    i += 1
                    success_count = 0
                    buildfail_count = 0
                    execfail_count = 0
