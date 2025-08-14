import time


def timeTracker(function):

    def tracker():
        start = time.perf_counter()
        function()
        end = time.perf_counter()
        print(f"Execution Time: {end-start:0.9f} seconds")

    return tracker


@timeTracker
def infoTech():
    print("Through this function it gets the time of execution")


infoTech()
