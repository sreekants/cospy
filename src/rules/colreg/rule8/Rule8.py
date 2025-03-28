#!/usr/bin/python
# Filename: Rule8.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
'''
Action to avoid Collision
(A amended paragraph (a) shall enter into force on 29 November 2003, as
amended by Resolution A.919(22))
(a) Any action to avoid collision shall be taken in accordance with the Rules of this Part and shall, if
the circumstances of the case admit, be positive, made in ample time and with due regard to the
observance of good seamanship.
(b) Any alteration of course and/or speed to avoid collision, shall, if the circumstances of the case
admit, be large enough to be readily apparent to another vessel observing visually or by radar; a
succession of small alterations of course and/or speed should be avoided.
(c) If there is sufficient sea room, alteration of course alone may be the most effective action to avoid
a close-quarters situation pcosided that it is made in good time, is substantial and does not result in
another close-quarters situation.
(d) Action taken to avoid collision with another vessel shall be such as to result in passing at a safe
distance. The effectiveness of the action shall be carefully checked until the other vessel is finally
past and clear.
(e) If necessary to avoid collision or allow more to assess the situation, a vessel shall slacken her
speed or take all way off by stopping or reversing her means of propulsion.
(f)
(i) A vessel which, by any of these Rules, is required not to impede the passage or safe
passage of another vessel shall, when required by the circumstances of the case, take
early action to allow sufficient sea room for the safe passage of the other vessel.
(ii) A vessel required not to impede the passage or safe passage of another vessel is not
relieved of this obligation if approaching the other vessel so as to involve risk of collision
and shall, when taking action, have full regard to the action which may be required by
the Rules of this part.
(iii) A vessel the passage of which is not to be impeded remains fully obliged to comply with
the rules of this part when the two vessels are approaching one another so as to involve
risk of collision.
'''


class Rule8(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule8()


