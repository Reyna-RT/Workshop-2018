def mean(num_list):
	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError as detail:
		msg = "\nCannot compute the mean value of an empty list"
		raise ZeroDivisionError(detail.__str__()+msg)
	except TypeError as detail:
		msg = "\n Please pass a list of numbers"
		raise TypeError(detail.__str__() + msg)
