from scripts import interface, log_generator
import threading

if __name__ == '__main__':
    runner = False
    thread1 = threading.Thread(target=interface.runtime, args=())
    thread2 = threading.Thread(target=log_generator.port, args=(), daemon=True)
    thread1.start()
    thread2.start()
    thread1.join()

