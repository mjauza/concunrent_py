from multiprocessing import Pool

import time

work = (["David", 5], ["Dani", 2], ["Mia", 1], ["Masa", 3])

def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])

def mp_handler():
    p = Pool(2)
    p.map(work_log, work)
def seq_handler():
    for w in work:
        work_log(w)


if __name__ == '__main__':
    start_mp = time.time()
    mp_handler()
    end_mp = time.time()
    print(f"Multiprocess time: {end_mp - start_mp} s")

    start_sq = time.time()
    seq_handler()
    end_sq = time.time()
    print(f"Sequential time: {end_sq - start_sq} s")
