# from typing import List
#
#
# def partition(numbers: List[int], low: int, high: int) -> int:
#     i = low - 1
#     pivot = numbers[high]
#     for j in range(low, high):
#         if numbers[j] <= pivot:
#             i += 1
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
#     return i+1
#
#
#
# def quick_sort(numbers: List[int]) -> List[int]:
#     def _quick_sort(numbers: List[int], low: int, high: int) -> None:
#         if low < high:
#             partition_index = partition(numbers, low, high)
#             _quick_sort(numbers, low, partition_index - 1)
#             _quick_sort(numbers, partition_index + 1, high)
#
#     _quick_sort(numbers, 0, len(numbers) - 1)
#     return numbers
#
#
# if __name__ == '__main__':
#
#
#     nums = [12, 4, 55, 33, 14, 4]
#     print(quick_sort(nums))



#
#
# from typing import List
#
#
# def merge_sort(numbers: List[int]) -> List[int]:
#     if len(numbers) <= 1:
#         return numbers
#
#     center = len(numbers) // 2
#     left = numbers[:center]
#     right = numbers[center:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     i = j = k = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             numbers[k] = left[i]
#             i += 1
#         else:
#             numbers[k] = right[j]
#
#             j += 1
#         k += 1
#     while i < len(left):
#         numbers[k] = left[i]
#         i += 1
#         k += 1
#
#
#     while j < len(right):
#         numbers[k] = right[j]
#         j += 1
#         k += 1
#
#
#     return numbers
#
# if __name__ == '__main__':
#     nums = [4,4,55,56,7]
#     print(merge_sort(nums))




#
# from typing import List, NewType
#
#
#
# IndexNum = NewType('indexnum', int)
#
#
# def linear_search(numbers: List[int], value: int) -> IndexNum:
#     for i in range(0, len(numbers)):
#         if numbers[i] == value:
#             return i
#
#     return -1


#
# def binary_search(numbers: List[int], value: int) -> IndexNum:
#     left, right = 0, len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid -1
#     return -1



# def binary_search(numbers: List[int], value: int) -> IndexNum:
    # left, right = 0, len(numbers) - 1
    # while left <= right:
    #     mid = (left + right) // 2
    #     if numbers[mid] == value:
    #         return mid
    #     elif numbers[mid] < value:
    #         left = mid + 1
    #     else:
    #         right = mid -1
    # return -1





# def binary_search(numbers: List[int], value: int) -> IndexNum:
#     def _binary_search(numbers: List[int], value: int,
#                       left: IndexNum, right: IndexNum) -> IndexNum:
#         if left > right:
#             return -1
#
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             return _binary_search(numbers, value, mid + 1, right)
#         else:
#             return _binary_search(numbers, value, left, mid-1)
#     return _binary_search(numbers, value, 0, len(numbers)-1)
#
#
#
# if __name__ == '__main__':
#     nums = [0, 1, 6,67,8,17,7]
#     print(binary_search(nums, 1))



#
# from typing import
#
#
#
#
# def find_max_circular_sequence_sum(numbers: List[int]) int:
#

#
# l = [1,1,1,1,23,2,9,4,59,4,5]
# print(set(l))
#
#
# # print([n for i, n in enumerate(l) if n not in l[:i]])



#
# # from itertools import permutations
# #
# # for r in permutations([1,2,3]):
# #     print(r)
#
#
#
# def all_perms(elements: List[int]) -> List[List[int]]:





# # s = 'test'
# # print(''.join(reversed(s)))
#
#
# # print(s[::-1])
#
#
#
# # def is_palindrome(strings: str) -> bool:
# #     len_strings = len(strings)
# #     if not len_strings:
# #         return False
# #     if len_strings == 1:
# #         return True
# #     start, end = 0, len_strings - 1
# #     while start < end:
# #         if strings[start] != strings[end]:
# #             return False
# #         start += 1
# #         end -= 1
# #     return True
# #
# #
# # if __name__ == '__main__':
# #     print(is_palindrome('racecar'))
# #
# #
# #
# # for i in range(1, len(strings)-1):
# #     [yield s for s in find_palindome(string, i-1, i+1]
# #
# #     return
#
#
#
# # from typing import List
# #
# #
# #
# # def order_even_first_odd_last_v1(numbers: List[int]) -> None:
# #     even_list, odd_list = [],[]
# #     for num in numbers:
# #         if num % 2 == 0:
# #             even_list.append(num)
# #         else:
# #             odd_list.append(num)
# #     numbers[:] = even_list + odd_list
# #
# #
# #
# # def order_even_first_odd_last_v2(numbers: List[int]) -> None:
# #     i, j = 0, len(numbers) - 1
# #     while i < j:
# #         if numbers[i] % 2 == 0:
# #             i += 1
# #         else:
# #             numbers[i], numbers[j] = numbers[j], numbers[i]
# #
# #
# #             j -= 1
# #
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     l = [0, 3,4,5,7,5,6,8,6]
# #     # order_even_first_odd_last_v1(l)
# #     order_even_first_odd_last_v2(l)
# #     print(l)
#
#
#
#
# # from typing import List
# #
# # def order_change_by_indexex_v1(chars: List[str], indexes: List[int]) -> str:
# #     tmp = [None] * len(chars)
# #     for i, index in enumerate(indexes):
# #         tmp[index] = chars[i]
# #     return ''.join(tmp)
# #
# # def order_change_by_indexex_v2(chars: List[str], indexes: List[int]) -> str:
# #     i, len_indexes = 0, len(indexes)-1
# #     while i < len_indexes:
# #         while i != indexes[i]:
# #             index = indexes[i]
# #             chars[index], chars[i] = chars[i], chars[index]
# #             indexes[index], indexes[i] = indexes[i], indexes[index]
# #         i += 1
# #
# #     return ''.join(chars)
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     w = ['h', 'y', 'n', '@', 'f']
#     i = [3,1,2,1,4]
#     print(order_change_by_indexex_v1(w, i))




#
# from typing import List
# NUM_ALPHABET_MAPPING = {
#     0: '+',
#     1: '@',
#     2: 'ABC',
#     3: 'DEF',
#     4: 'GHI',
#     5: 'JKL',
#     6: 'MNO',
#     7: 'PQRS',
#     8: 'TUV',
#     9: 'WXYZ',
# }
#
#
# def phone_mnemonic_v1(phone_number: str) -> List[str]:
#     phone_number = [int(s) for s in phone_number.replace('-', '')]
#     candidate = []
#     tmp = [''] * len(phone_number)
#     def find_candidate_alphabet(digit: int=0) -> None:
#         if digit == len(phone_number):
#             candidate.append(''.join(tmp))
#         else:
#
#             for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
#                 tmp[digit] = char
#                 find_candidate_alphabet(digit+1)
#     find_candidate_alphabet()
#     return candidate
#
# if __name__ == '__main__':
#     for s in phone_mnemonic_v1('568-379-8466'):
#         if 'LOVEPYTOHN' in s:
#             print(s)



from typing import List
#
# def generate_primes_v1(numbers: int) -> list[int]:
#     primes = []
#     for x in range(2, numbers + 1):
#         for y in range(2, x):
#             if x % y == 0:
#                 break
#         else:
#             primes.append(x)
#     return primes
# def generate_primes_v2(numbers: int) -> list[int]:
#     primes = []
#     cache = {}
#     for x in range(2, numbers+1):
#         is_prime = cache.get(x)
#         if is_prime is False:
#             continue
#         primes.append(x)
#         cache[x] = True
#         for y in range(x*2, numbers+1, x):
#             cache[y] = False
#     return primes
#
#
# if __name__ == '__main__':
#
#     import time
#     start = time.time()
#
#     print(generate_primes_v1(500))
#
#     print(time.time() - start)
#     start = time.time()
#
#     print(generate_primes_v2(500))
#     print(time.time() - start)
# import math
#
#
# def is_prime_v1(num: int) -> bool:
#
#     if type(num) is not int:
#         return False
#
#
#     if num <= 1:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def is_prime_v2(num: int) -> bool:
#     if num <= 1:
#         return False
#
#     for i in range(3, math.floor(math.sqrt(num)+1), 2):
#         if num % i == 0:
#             return False
#
#
#
#
#     i = 2
#     while i*i <= num:
#         if num % i == 0:
#         return False
#     i += 1
#
#
#
#
#     return True
#
#
# def is_prime_v2(num: int) -> bool:
#     if num <= 1:
#         return False
#     if num == 2:
#         return False
#     if num % 2 == 0:
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     print(is_prime_v1(5))

#
# from typing import List, Tuple
#
# def taxi_cab_number(max_answer_num: int, match_answer_num: int=2) -> List[Tuple[int, List[Tuple[int, int]]]]:
# result = []
# got_answer_count = 0
# answer = 1




import gym
env = gym.make("CartPole-v1")
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)


