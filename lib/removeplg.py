#!/usr/bin/env python

import sys
import os
import re
import xml.etree.ElementTree as ET

class RemovePlg:
  def __init__(self, path):
    self.path = path
    self.xml  = self.parse_plg()
    self.files = self.__collect_file_paths()
    self.remove_files()

  def parse_plg(self):
    if not os.path.exists(self.path):
      sys.exit('{0} not found'.format(self.path))

    return ET.parse(self.path)

  def remove_files(self):
    for file in self.files:
      self.__remove_file(file)

  def prompt_for_removal(self, file):
    name = os.path.basename(file)
    return raw_input("Are you sure you want to remove {0}? Other packages may depend on it. [yN]".format(name))

  def remove_package(self, file):
    name = os.path.basename(file)
    os.system("removepkg {0}".format(name))

  def __remove_file(self, file):
    if not os.path.exists(file): return

    print "Removing {0}".format(file)

    if self.__is_package(file):
      answer = self.prompt_for_removal(file)
      if answer == 'y':
        os.remove(file)
        self.remove_package(file)
      else:
        print "Skipping {0}".format(file)
    else:
      os.remove(file)

  def __collect_file_paths(self):
    return [node.attrib['Name'] for node in self.xml.iter('FILE')]

  def __is_package(self, file):
    return re.search('\.t\wz$', file)
