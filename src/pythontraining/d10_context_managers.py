"""
Refactor the program below (use a "with" statement).
"""
import time


class Timer:

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        print(f"The run time was {end - self.start} second")


with Timer:
    def main():
        with open("excercise.txt", "w") as file:
            file.write("Explicit is better than implicit")


if __name__ == "__main__":
    main()
