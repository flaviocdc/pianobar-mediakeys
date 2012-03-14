#!/usr/bin/env python

from sys import argv
from sys import exit
import dbus_client

if (len(argv) <= 1):
  exit(0)

event = argv[1]
if event == 'userlogin':
  dbus_client.run();  
