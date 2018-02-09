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

def test_complex():
	num_list = [2+3j,3+4j,-32-2j]
	obs = mean(num_list)
	exp = NotImplemented
	assert obs == exp

def test_zero():
	num_list = [0,2,4,6]
	obs = mean(num_list)
	exp = 3
	assert obs == exp
