#!/usr/bin/python

import subprocess

res = subprocess.check_output(["lsmod"])
for line in res.splitlines():
    print(line.decode("utf_8"))
