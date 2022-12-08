#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import subprocess

f = open("Dockerfile", "w")
f.write('FROM python:3.7.3\n\nADD Hello_Docker_World.py .\n\nRUN pip3 install flask\n\nCMD ["python","./Hello_Docker_World.py"]')
f.close()
subprocess.call(["docker", "build", "-t", "hello_world", "."])
subprocess.call(["docker", "run", "hello_world"])
