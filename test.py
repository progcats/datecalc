# -*- coding: utf-8 -*-
import unittest 
from datetime_calculator import Datecalc
 
class AddTest(unittest.TestCase):
	def test_positive_add(self):
		self.assertEqual(calc.mo12('ww'), 'ww, ddd, 2009-12-12')

	def test_pos_add(self):
		self.assertEqual(calc.mo12('Lisa'), 'Lisa, Zyuzina, 2000-04-24')

if __name__=='__main__':
	calc = Datecalc()
	unittest.main()