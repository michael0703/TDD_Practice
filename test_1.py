import pytest
import math

def boilEgg(eggCount):
	#### one pot boils 8 eggs at most at the same time
	needBoil = math.ceil(eggCount / 8)
	return needBoil * 5

class TestBoil:

	def test_boilOneEgg(self):

		assert 5 == boilEgg(1)