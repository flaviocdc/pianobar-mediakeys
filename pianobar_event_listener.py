#!/usr/bin/env python2

import sys
import os
import dbus_client

if (len(sys.argv) <= 1):
  sys.exit(0)

event = sys.argv[1]
if event == 'userlogin':
  # have to fork here in order to unblock pianobar
  # since it waits for the event process to die before proceding
  pid = os.fork()
  if pid == 0:
    try:
      dbus_client.run()
    except KeyboardInterrupt:
      pass
