import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('lib'))

from plg import Plg

class TestPlg(unittest.TestCase):
  def setUp(self):
    self.fixture = Plg('tests/support/dropbox_overbyrn.plg')

  def test_returns_not_found(self):
    with self.assertRaises(SystemExit) as cm:
      Plg('plugin.plg')
      self.assertEqual(cm.exception, "plugin.plg not found")

  def test_xml(self):
    self.assertEqual(self.fixture.xml.getroot().tag, 'PLUGIN')

  def test_files(self):
    files = ['/tmp/plugin-prepare', '/boot/config/plugins/dropbox/dropbox.png', '/boot/config/plugins/images/device_status.png', '/boot/config/plugins/images/new_config.png', '/boot/config/plugins/images/information.png', '/boot/packages/python-2.6.6-i486-1.txz', '/boot/config/plugins/dropbox/dropbox.py', '/tmp/plugin-cleanup', '/boot/config/plugins/dropbox/dropbox.cfg', '/tmp/plugin-chkcfg', '/etc/rc.d/rc.dropbox', '/usr/local/emhttp/plugins/dropbox/dropbox.png', '/usr/local/emhttp/plugins/dropbox/device_status.png', '/usr/local/emhttp/plugins/dropbox/new_config.png', '/usr/local/emhttp/plugins/dropbox/information.png', '/usr/local/emhttp/plugins/dropbox/dropbox.php', '/usr/local/emhttp/plugins/dropbox/event/disks_mounted', '/usr/local/emhttp/plugins/dropbox/event/unmounting_disks', '/tmp/plugin-install', '/usr/local/emhttp/plugins/dropbox/dropbox.page', '/var/log/plugins/dropbox', '/tmp/plugin-development']
    self.assertEqual(self.fixture.files, files)

if __name__ == '__main__':
    unittest.main()
