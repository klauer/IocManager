#!/usr/bin/env python
import sys
import utils

if __name__ == '__main__':
  hutch  = sys.argv[1]
  sys.exit(utils.applyConfig(hutch))
