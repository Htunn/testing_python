class TestFloat():

    def test_passing_a_float(self):
        result = util.str_to_int('1.99')
        assert result == 1