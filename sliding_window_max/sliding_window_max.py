from collections import deque
from heapq import heappush, heappushpop
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

class sliding_window_queue:

    def __init__(self, k):
        self.ls = None
        self.k = k
        self.max_list = []

    def add(self, n):
        self.ls.append(n)

        if len(self.ls) > self.k:
            old_number = self.ls.popleft()

        if len(self.ls) == self.k:
            self.max_list.append(max(self.ls))
#
# def sliding_window_max(nums, k):
#
#     window = sliding_window(k)
#
#     for n in nums:
#         window.add(n)
#
#     return window.max_list


def sliding_window_max(arr, k):
    q = deque()
    max_list = []
    for i in range(len(arr)):

        # If nothing in the queue, add index to queue
        if len(q) == 0:
            q.append(i)
        else:

            # if front index falls outside of the window, evict it
            front_index = q[0]
            if front_index <= i - k:
                q.popleft()
                front_index = q[0]

            # pop values from back of queue that are less then current value
            current_value = arr[i]
            rear_value = arr[q[-1]]

            while current_value > rear_value:
                q.pop()
                if len(q) == 0:
                    break
                rear_value = arr[q[-1]]

            # Add to Queue only when current less than back of queue OR queue is empty
            q.append(i)

            # Front of Queue is maximum value
            if i >= k - 1:
                max_list.append(arr[q[0]])

    return max_list







if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
