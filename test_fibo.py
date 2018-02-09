from fibo_mod import fib

def test_fib0():
	obs = fib(0)
	exp = 0
	assert obs == exp
# Create a function to test fib(1)
def test_fib1():
	obs = fib(1)
	exp = 1
	assert obs == exp

#Function to test "standard" behaviour
def test_stand():
	obs = fib(5)
	exp = 5
	assert obs == exp

def test_negative():
	obs = fib(-4)
	exp = NotImplemented
	assert obs == exp
