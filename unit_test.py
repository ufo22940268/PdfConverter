#coding:utf-8
import unittest
import file_parser

class StringTestCase(unittest.TestCase):
    def testRemoveDuplicate(self):
        self.assertEqual(u"很好", file_parser.removeDup(u"很好很好"));
        self.assertEqual(u"很好很好aaa", file_parser.removeDup(u"很好很好aaa"));
        self.assertEqual(u"asdfijiasdjfiaf", file_parser.removeDup(u"asdfijiasdjfiaf"));
        self.assertEqual(u"asdf", file_parser.removeDup(u"asdfasdfasdf"));

if __name__ == '__main__':
    unittest.main()

