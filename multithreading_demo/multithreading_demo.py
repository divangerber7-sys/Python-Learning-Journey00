# Multithreading Example in Python
# --------------------------------
# Multithreading lets us perform multiple tasks concurrently.
# Useful for I/O bound tasks like reading files, fetching data, etc.

import threading
import time

# Sequential chores (one after another)
def sequential_chores():
    def walk_dog():
        time.sleep(6)
        print("Walking Dog")

    def take_out_trash():
        time.sleep(3)
        print("You take out the trash")

    def get_mail():
        time.sleep(5)
        print("Getting Mail")

    print("\nRunning chores sequentially...")
    walk_dog()
    take_out_trash()
    get_mail()
    print("All chores are complete (sequential).\n")


# Multithreaded chores (concurrent execution)
def threaded_chores():
    def walk_dog(first, last):
        time.sleep(6)
        print(f"You have finished walking {first} {last}")

    def take_out_trash():
        time.sleep(3)
        print("You take out the trash")

    def get_mail():
        time.sleep(5)
        print("Getting Mail")

    print("\nRunning chores with multithreading...")

    chore1 = threading.Thread(target=walk_dog, args=("Flynn", "Siff"))
    chore2 = threading.Thread(target=take_out_trash)
    chore3 = threading.Thread(target=get_mail)

    # Start all threads
    chore1.start()
    chore2.start()
    chore3.start()

    # Wait for all threads to finish
    chore1.join()
    chore2.join()
    chore3.join()

    print("All chores are complete (multithreading).\n")


if __name__ == "__main__":
    sequential_chores()
    threaded_chores()
