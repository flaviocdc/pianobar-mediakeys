#!/usr/bin/env python
import gobject
import dbus
import dbus.service
import dbus.mainloop.glib

from config_parser import *

APP_ID="pianobar-mediakeys"

def write_pianobar_cmd(cmd):
    fifo = open(pianobar_fifo_file(), 'a')
    fifo.write(cmd)
    fifo.close()

def on_mediakey(app, action):
  if app == APP_ID:
    if action == 'Play' or action == 'Pause':
      write_pianobar_cmd(pianobar_key_bindings['pause_song'])      
    elif action == 'Next':
      write_pianobar_cmd(pianobar_key_bindings['next_song'])      
    elif action == 'Stop':
      write_pianobar_cmd(pianobar_key_bindings['quit_pianobar'])      

parse_pianobar_config()

# set up the glib main loop.
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.Bus(dbus.Bus.TYPE_SESSION)

bus_object = bus.get_object('org.gnome.SettingsDaemon', '/org/gnome/SettingsDaemon/MediaKeys')

# this is what gives us the multi media keys.
dbus_interface='org.gnome.SettingsDaemon.MediaKeys'
bus_object.GrabMediaPlayerKeys(APP_ID, 0, dbus_interface=dbus_interface)

# connect_to_signal registers our callback function.
bus_object.connect_to_signal('MediaPlayerKeyPressed', on_mediakey)

# and we start the main loop.
mainloop = gobject.MainLoop()
mainloop.run()
