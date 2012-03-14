import os.path

pianobar_key_bindings = {}

def pianobar_config_file():
  if "XDG_CONFIG_HOME" in os.environ:
    config_path = os.environ("XDG_CONFIG_HOME")
  else:
    config_path = os.path.expanduser("~/.config")
  return config_path + "/pianobar/config"

def pianobar_fifo_file():
  return os.path.dirname(pianobar_config_file()) + "/ctl";

def parse_pianobar_config():
  cfg = open(pianobar_config_file())
  lines = cfg.readlines()
  lines = map(str.rstrip, lines)

  config = {}

  for line in lines:
    line = line.split('=')
    config[line[0]] = line[1]

  pianobar_key_bindings["next_song"] = config.get('act_songnext', 'n')
  pianobar_key_bindings["pause_song"] = config.get('act_songpause', 'p')
  pianobar_key_bindings["quit_pianobar"] = config.get('act_quit', 'q')
