# from typing import List
#
#
# def bubble_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers - 1 - i):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
#     return numbers
#
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(bubble_sort(nums))

#
#
# import queue
#
#
# from multiprocessing.managers import BaseManager
#
#
#
# queue = queue.Queue()
#
# class QueueManager(BaseManager):
#     pass
#
#
# QueueManager.register(
#     'get_queue', callable=lambda: queue)
#
# manager = QueueManager(
#     address=('127.0.0.1', 50000),
#     authkey=b'abracadabara')
# server = manager.get_server()
# server.serve_forever()

#
# import concurrent.futures
# import logging
# import time
#
#
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')
#
#
# def worker(x, y):
#     logging.debug('start')
#     time.sleep(4)
#     r = x * y
#     logging.debug(r)
#     logging.debug('end')
#     return r
#
#
# def main():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
#         f1 = ex.submit(worker, 2, 5)
#         f2 = ex.submit(worker, 2, 5)
#         logging.debug(f1.result())
#         logging.debug(f2.result())
#         args = [[2], [5]]
#
#         r = ex.map(worker, *args)
#         logging.debug(r)
#         logging.debug([i for i in r])
#
#
#
#
# if __name__ == '__main__':
#     main()
#
#



from Crypto.Cipher import AES

