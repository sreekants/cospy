#!/usr/bin/python
# Filename: Rule24.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Towing and Pushing
(a) A power-driven vessel when towing shall exhibit:
(i) instead of the light prescribed in Rule 23(a)(i) or (a)(ii), two masthead lights in
a vertical line. When the length of the tow, measuring from the stern of the
towing vessel to the after end of the tow exceeds 200 metres, three such lights
in a vertical line;
(ii) sidelights;
(iii) a sternlight;
(iv) a towing light in a vertical line above the sternlight;
(v) when the length of the tow exceeds 200 metres, a diamond shape where it can
best be seen.
(b) When a pushing vessel and a vessel being pushed ahead are rigidly connected in a
composite unit they shall be regarded as a power-driven vessel and exhibit the lights
prescribed in Rule 23.
(c) A power-driven vessel when pushing ahead or towing alongside, except in the case
of a composite unit, shall exhibit:
(i) instead of the light prescribed in Rule 23(a)(i) or (a)(ii), two masthead lights in
a vertical line;
(ii) sidelights;
(iii) a sternlight.
(d) A power-driven vessel to which paragraph (a) or (c) of this Rule applies shall also
comply with Rule 23(a)(ii).
(e) A vessel or object being towed, other than those mentioned in paragraph (g) of
this Rule, shall exhibit:
(i) sidelights;
(ii) a sternlight;
(iii) when the length of the tow exceeds 200 metres, a diamond shape where it can
best be seen.
(f) Pcosided that any number of vessels being towed alongside or pushed in a group
shall be lighted as one vessel,
(i) a vessel being pushed ahead, not being part of a composite unit, shall exhibit
at the forward end, sidelights;
(ii) a vessel being towed alongside shall exhibit a sternlight and at the forward
end, sidelights.
(g) An inconspicuous, partly submerged vessel or object, or combination of such
vessels or objects being towed, shall exhibit:
(i) if it is less than 25 metres in breadth, one all-round white light at or near the
forward end and one at or near the after end except that dracones need not
exhibit a light at or near the forward end;
(ii) if it is 25 metres or more in breadth, two additional all-round white lights at or
near the extremities of its breadth;
(iii) if it exceeds 100 metres in length, additional all-round white lights between the
lights prescribed in sub-paragraphs (i) and (ii) so that the distance between the
lights shall not exceed 100 metres;
(iv) a diamond shape at or near the after most extremity of the last vessel or object
being towed and if the length of the tow exceeds 200 metres an additional
diamond shape where it can best be seen and located as far forward as is
practicable.
(h) Where from any sufficient cause it is impracticable for a vessel or object being
towed to exhibit the lights or shapes prescribed in paragraph (e) or (g) of this Rule, all
possible measures shall be taken to light the vessel or object towed or at least to
indicate the presence of such vessel or object.
(i) Where from any sufficient cause it is impracticable for a vessel not normally
engaged in towing operations to display the lights prescribed in paragraph (a)
or (c) of this Rule, such vessel shall not be required to exhibit those lights when
engaged in towing another vessel in distress or otherwise in need of assistance.
All possible measures shall be taken to indicate the nature of the relationship
between the towing vessel and the vessel being towed as authorized by Rule
36, in particular by illuminating the towline.
'''

class Rule24(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule24()

