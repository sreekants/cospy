#!/usr/bin/python
# Filename: test_Clock.py
# Description: Test cases for the Clock class (COS.024)

import datetime, threading, unittest

from cos.core.time.Clock import Clock

UTC		= datetime.timezone.utc
PLUS3	= datetime.timezone( datetime.timedelta(hours=3) )

class ClockTestCase(unittest.TestCase):
	def test_time_is_epoch_plus_ticks_times_step(self):
		clock	= Clock( 2.0, datetime.datetime(2026, 6, 1, 20, 0, 0, tzinfo=UTC) )
		for _ in range(30):
			clock.advance()

		self.assertEqual( clock.tick, 30 )
		self.assertEqual( clock.tickcount, 30 )
		self.assertEqual( clock.seconds, 60.0 )
		self.assertEqual( clock.utc, datetime.datetime(2026, 6, 1, 20, 1, 0, tzinfo=UTC) )

	def test_utc_carries_a_timezone_and_local_keeps_the_epoch_offset(self):
		clock	= Clock( 1.0, '2026-06-01T21:00:00+03:00' )

		self.assertEqual( clock.utc.tzinfo, UTC )
		self.assertEqual( clock.utc.hour, 18 )
		self.assertEqual( clock.local.utcoffset(), datetime.timedelta(hours=3) )
		self.assertEqual( clock.local.hour, 21 )

	def test_host_time_does_not_move_the_clock(self):
		clock	= Clock()
		before	= clock.utc
		self.assertEqual( clock.utc, before )
		self.assertEqual( clock.seconds, 0.0 )

	def test_a_pin_holds_for_its_own_thread_only(self):
		clock	= Clock()
		for _ in range(5):
			clock.advance()
		clock.pin( 2 )
		clock.advance()

		seen	= []
		other	= threading.Thread( target=lambda: seen.append(clock.tick) )
		other.start()
		other.join()

		self.assertEqual( clock.tick, 2 )
		self.assertEqual( clock.live, 6 )
		self.assertEqual( seen, [6] )

		clock.unpin()
		self.assertEqual( clock.tick, 6 )

	def test_an_epoch_without_a_timezone_is_refused(self):
		with self.assertRaises( ValueError ):
			Clock( 1.0, datetime.datetime(2026, 1, 1) )

	def test_a_tick_length_must_be_positive(self):
		with self.assertRaises( ValueError ):
			Clock( 0.0 )

if __name__ == '__main__':
    unittest.main()
