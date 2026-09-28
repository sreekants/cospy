#!/usr/bin/python
# Filename: test_Ticker.py
# Description: Test cases for the Ticker class (COS.024)

import unittest

from cos.core.time.Clock import Clock
from cos.core.time.Ticker import Ticker

class TickerTestCase(unittest.TestCase):
	def test_counts_simulated_seconds(self):
		clock	= Clock( 0.5 )
		ticker	= Ticker( 2.0, clock )

		fired	= []
		for _ in range(12):
			clock.advance()
			fired.append( ticker.signaled() )

		# 0.5 s per tick: every 4th tick is 2 simulated seconds
		self.assertEqual( [n+1 for n, f in enumerate(fired) if f], [4, 8, 12] )

	def test_does_not_fire_while_the_clock_stands_still(self):
		clock	= Clock()
		ticker	= Ticker( 1.0, clock )
		self.assertEqual( [ticker.signaled() for _ in range(5)], [False]*5 )

	def test_fires_on_the_pinned_tick_of_the_calling_thread(self):
		clock	= Clock()
		ticker	= Ticker( 3.0, clock )
		for _ in range(10):
			clock.advance()

		clock.pin( 2 )
		self.assertFalse( ticker.signaled() )
		clock.pin( 3 )
		self.assertTrue( ticker.signaled() )
		clock.unpin()

if __name__ == '__main__':
    unittest.main()
