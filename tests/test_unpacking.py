import src.unpacking
from src.unpacking import Unpackers

class TestUnpacking:

    def test_first_last_others(self):
        a_list = [1, 2, 3, 4, 5]
        my_unpacker = Unpackers(a_list=a_list)
        values = my_unpacker.fist_last_others()
        assert type(values) == tuple
        assert values == (1, [2, 3, 4], 5)

