# import threading
# import time
#
# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))
#
#
# def print_square1():
#     i = 0
#     while i < 5:
#         print(f'Запуск 2 потока № {i}', time.time_ns())
#         i+=1
# def print_square():
#     i = 0
#     while i < 5:
#         print(f'Запуск 1 потока № {i}', time.time_ns())
#         i+=1
# if __name__ == "__main__":
#     i = 0
#     # creating thread
#     t1 = threading.Thread(target=print_square)
#     t2 = threading.Thread(target=print_square1)
#     # print(f"first thread is starting: {time.time_ns()}")
#     t1.start()
#     # starting thread 2
#     # print(f"second thread is starting: {time.time_ns()}")
#     t2.start()
#
#
#
#     # # wait until thread 1 is completely executed
#     # t1.join()
#     # # wait until thread 2 is completely executed
#     # t2.join()
#
#     # both threads completely executed
#     print("Done!")

# from threading import Thread, Event
#
# ev = Event()
#
# def func():
#     ev.wait()
#     print("h", end = "", flush=True) #ДОЧЕРНИЙ ПОТОК
#     print("e", end = "", flush=True) #ДОЧЕРНИЙ ПОТОК
#     print("l", end = "", flush=True) #ДОЧЕРНИЙ ПОТОК
#     print("l", end = "", flush=True) #ДОЧЕРНИЙ ПОТОК
#     print("o", end = "", flush=True) #ДОЧЕРНИЙ ПОТОК
#
#
#
# th1 = Thread(target=func)
# th2 = Thread(target=func)
#
# ev.clear()
#
# th1.start()
# th2.start()
#
# ev.set()
#
# th1.join()
# th2.join()
#
# print(flush=True)