#!/usr/bin/env python

"""
Draw names at random.
"""

import os
import sys
import random
import datetime
import argparse

from pymsbayes.utils import argparse_utils

participation_dir = '../.participation'

participation_path = os.path.join(participation_dir, 'participation.log')

_program_info = {
    'name': os.path.basename(__file__),
    'author': 'Jamie Oaks',
    'version': 'Version 0.1.0',
    'description': __doc__,
    'copyright': 'Copyright (C) 2014 Jamie Oaks',
    'license': 'GNU GPL version 3 or later',}

def get_random_line(file_path):
    with open(file_path, 'rU') as file_stream:
        current_line = next(file_stream)
        for i, line in enumerate(file_stream):
            if random.randrange(i + 2):
                continue
            current_line = line
    return current_line

def main():
    section_options = ['a', 'b']
    description = '{name} {version}'.format(**_program_info)
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument('--version',
            action='version',
            version='%(prog)s ' + _program_info['version'],
            help='report version and exit')
    parser.add_argument('-s', '--section',
            type = str,
            choices=section_options,
            help = ('The class section.'))
    parser.add_argument('-n', '--number',
            type = int,
            default = 1,
            help = ('The number of names to draw.'))
    args = parser.parse_args()

    name_path = '../class-lists/names.txt'
    if args.section:
        '../class-lists/{0}-names.txt'.format(args.section)

    if args.number < 2:
        name = get_random_line(name_path).strip()

        sys.stdout.write('\n{0}\n\n'.format(name))
        response = raw_input('(y)es/(n)o/(c)ancel: ')
        r = response.strip()[0].lower()
        participated = 0
        if r == 'y':
            participated = 1
        elif r == 'n':
            participated = 0
        else:
            sys.exit(0)
        

        if not os.path.isdir(participation_dir):
            os.mkdir(participation_dir)

        if not os.path.isfile(participation_path):
            with open(participation_path, 'w') as out:
                out.write('name\tsection\tparticipated\ttime\n')

        with open(participation_path, 'a') as out:
            out.write('{0}\t{1}\t{2}\t{3}\n'.format(name, args.section,
                    participated, str(datetime.datetime.now())))
        sys.exit(0)

    for i in range(args.number):
        name = get_random_line(name_path).strip()
        sys.stdout.write('{0}\n'.format(name))

if __name__ == '__main__':
    main()

