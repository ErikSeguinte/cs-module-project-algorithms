from functools import lru_cache
'''
Input: an integer
Returns: an integer
'''


@lru_cache()
def eating_cookies(n = 500, *args):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1



    else:
        number = eating_cookies(n - 3) + eating_cookies(n-2) + eating_cookies(n-1)

    return number




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    # num_cookies = 5
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    from timeit import timeit
    print(timeit(eating_cookies))
    
    
