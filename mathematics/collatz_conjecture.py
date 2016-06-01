def get_cycle_length(n):
    """ 
    takes an integer 0 < n < 10000
    returns the number of steps it
    will take to get to 1
    by performing n // 2 if n is even
    and n * 3 + 1 if n is odd
    """
    steps = 1
    while ( n != 1 ):
        if n % 2 == 0:
            n = n / 2
            steps = steps + 1
        else:
            n = n * 3 + 1
            steps = steps + 1

    return steps

def get_cycle_length_range(start, end):
    """ 
    takes 2 integers 0 < start, end < 10000
    finds the number for which it takes
    the maximum amount of steps to get to
    1 and returns the length of that cycle
    """
    largest = 0

    rangestart = end if start > end else start
    rangeend = end if start < end else start

    print ( "rangestart:", rangestart )
    print ( "rangeend:", rangeend )
    for i in range(rangestart, rangeend + 1):
        if get_cycle_length(i) > largest:
            largest = get_cycle_length(i)

    return largest

