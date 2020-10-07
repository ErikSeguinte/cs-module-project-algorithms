'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    arr.sort()

    single = None
    test = arr[0]

    for n in arr[1:]:
        if test is not None:
            if test != n:
                single = test
                test = n
            else:
                test = None
        else:
            test = n

    if single is not None:
        return single
    else:
        return test



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")