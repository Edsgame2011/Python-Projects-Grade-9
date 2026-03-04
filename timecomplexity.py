import time

start_time = time.time()

for i in range(1000000000):
    pass

end_time = time.time()

elapsed_time = end_time - start_time

print(f"loop ran in {elapsed_time:.6f} seconds")