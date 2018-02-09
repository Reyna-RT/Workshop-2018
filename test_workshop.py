from workshop_assert import mean

def test_ints():
	num_list = [1,2,3,4,5]
	obs = mean(num_list)
	exp = 3
	assert obs == exp

def test_double():
	num_list = [1,2,3,4,5]
        obs = mean(num_list)
        exp = 3.
        assert obs == exp

def test_long():
	big = 10000000
	obs =mean(range(1,big))
	exp = big/2.
	assert obs == exp 
