# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")


# import threading
# import time

# def io_task(name, sleep_time):
#     print(f"{name} started I/O for {sleep_time}s")
#     time.sleep(sleep_time)  # Giả lập I/O blocking
#     print(f"{name} finished I/O and continues work")

# # Main thread sẽ sleep 3s
# # Thread1 sẽ sleep 2s
# t1 = threading.Thread(target=io_task, args=("Thread1", 2), daemon=True)
# t1.start()

# print("Main Thread starting I/O for 3s...")
# time.sleep(3)
# print("Main Thread finished I/O!")

# t1.join()
# print("All done.")


# import logging
# import threading
# import time
# import concurrent.futures

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     # format = "%(asctime)s: %(message)s"
#     # logging.basicConfig(format=format, level=logging.INFO,
#     #                     datefmt="%H:%M:%S")

#     # threads = list()
#     # for index in range(3):
#     #     logging.info("Main    : create and start thread %d.", index)
#     #     x = threading.Thread(target=thread_function, args=(index,))
#     #     threads.append(x)
#     #     x.start()

#     # for index, thread in enumerate(threads):
#     #     logging.info("Main    : before joining thread %d.", index)
#     #     thread.join()
#     #     logging.info("Main    : thread %d done", index)
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))

# from concurrent.futures import ThreadPoolExecutor
# import time

# def task(name):
#     print(f"Starting {name}")
#     time.sleep(2)
#     print(f"Finished {name}")

# # Tạo pool tối đa 3 threads
# with ThreadPoolExecutor(max_workers=3) as executor:
#     # executor.map(task, range(10))
#     for i in range(10):
#         executor.submit(task, f"Task-{i}")

# from concurrent.futures import ThreadPoolExecutor
# import time

# def task(id):
#     print(f"Thread {id} start")
#     time.sleep(2)
#     print(f"Thread {id} done")

# print("Main start")

# with ThreadPoolExecutor(max_workers=3) as executor:
#     for i in range(5):
#         executor.submit(task, i)

# print("Main end")

import logging
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        # self.value += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)