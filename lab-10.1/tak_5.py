import time
nums = [i for i in range(1,1000000)]
squares = []
start_time = time.time()
squares = [n**2 for n in nums]
print(len(squares))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")