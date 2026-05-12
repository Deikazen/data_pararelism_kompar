import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(square, data)
    
    pool.close()
    pool.join()
    
    print(results)