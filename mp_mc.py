import numpy as np
from multiprocessing import Pool
import time
def generate_sum_rn(_):
    np.random.seed(0)
    z = np.random.normal(size = 100_000)
    return z.sum()

def mp_algo(n):
    p = Pool()
    p.map(generate_sum_rn , range(n))

def seq_algo(n):
    for i in range(n):
        generate_sum_rn(i)

if __name__ == "__main__":
    n = 2**11
    sq_start = time.time()
    seq_algo(n)
    sq_end = time.time()
    print(f"Seq algo: {sq_end - sq_start} s")

    mp_start = time.time()
    mp_algo(n)
    mp_end = time.time()
    print(f"Mp algo: {mp_end - mp_start} s")