import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('lib'))

from removeplg import RemovePlg

class TestRemovePlg(unittest.TestCase):
  def test_returns_not_found(self):
    with self.assertRaises(SystemExit) as cm:
      RemovePlg('plugin.plg')
      self.assertEqual(cm.exception, "plugin.plg not found")


if __name__ == '__main__':
    unittest.main()
