#!/usr/bin/env python3

import subprocess
import string
import re
from pwn import *


def count_instructions(args: list):
    callgrind = ['valgrind', '--tool=callgrind', '--callgrind-out-file=/dev/null']

    res = subprocess.run(callgrind + args, capture_output=True)
    inst_count = re.search('Collected : (\d+)', str(res.stderr, 'ascii')).group(1)
    
    return inst_count, res


if __name__ == '__main__':
    binary = './qualification.out'

    progress = log.progress('Cracking password')
    i = 0
    password = [''] * 8
    prev_inst_count = 0
    first = True
    done = False

    while not done:
        for c in '\x01' + string.printable:
            password[i] = c
            pw = ''.join(password)

            progress.status(pw)

            inst_count, res = count_instructions([binary, pw])
            out = str(res.stdout, 'ascii')

            if len(out) > 0 and 'flag' in out:
                log.success(f'Program output: {out}')
                log.success(f'Password = \'{pw}\'')
                done = True
                break

            if first:
                first = False
            elif inst_count < prev_inst_count:
                i += 1
                prev_inst_count = inst_count
                break

            prev_inst_count = inst_count

