import unittest
from envcheck.core import parse,issues
class Tests(unittest.TestCase):
 def test_entries(self): self.assertEqual(parse('A=1\n# x\nB=2')[1].key,'B')
 def test_issues(self): self.assertEqual(issues(parse('A=\nA=2')),['empty:A','duplicate:A'])
if __name__=='__main__': unittest.main()
