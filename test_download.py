from unittest import TestCase

from unittest import TestCase

from download import DMCAStorage

class TestBuildPath(TestCase):
    def test(self):
        self.assertEquals(DMCAStorage._build_path(103364), 
                          ('data/json/000/103', 'data/json/000/103/103364.json'))
