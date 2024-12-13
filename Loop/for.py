import time

my_time = int(input("Enter the timer in second: "))

for x in range(my_time, 0 ,-1):
    second = x % 60
    minutes = int(x /60)%60
    print(f"00:{minutes:02}:{second:02}")
    time.sleep(1)

print("Time up!!")