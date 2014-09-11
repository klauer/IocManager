#!/usr/bin/env python
import sys
import utils
import time

if __name__ == '__main__':
  cfg  = sys.argv[1]
  host = sys.argv[2]
  result = utils.readConfig(cfg)
  if result == None:
      print "Cannot read configuration for %s!" % cfg
      sys.exit(-1)
  (mtime, config, hosts) = result
  for l in config:
      if l['host'] == host and l['disable'] == False:
          utils.startProc(cfg, l)
          try:
              time.sleep(l['delay'])
          except:
              pass
