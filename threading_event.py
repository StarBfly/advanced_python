# Homework 3: Event

import threading


def odd_numbers_generator():
    for odd in range(1, 101, 2):
        yield odd


def even_numbers_generator():
    for even in range(2, 101, 2):
        yield even


class CountingThread(threading.Thread):
    def __init__(self, num_type, set_event, clear_event):
        threading.Thread.__init__(self)
        self.num_type = num_type
        self.set_event = set_event
        self.clear_event = clear_event

    def run(self):
        if self.num_type == "odd":
            for i in odd_numbers_generator():
                print("Odd thread number: {}".format(i))
                self.set_event.set()
                self.clear_event.clear()
                self.clear_event.wait()
            self.set_event.set()
        else:
            for i in even_numbers_generator():
                print("Even thread number: {}".format(i))
                self.set_event.set()
                self.clear_event.clear()
                self.clear_event.wait()
            self.set_event.set()


event_1 = threading.Event()
event_2 = threading.Event()

odd_thread = CountingThread(num_type="odd",
                            set_event=event_1,
                            clear_event=event_2)

even_thread = CountingThread(num_type="even",
                             set_event=event_2,
                             clear_event=event_1)


odd_thread.start()
even_thread.start()

odd_thread.join()
even_thread.join()
