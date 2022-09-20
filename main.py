import filecmp
import os
import subprocess
import time

dir_path = '/home/frigobar123/CLionProjects/APIProject-2022/'
test_path = '/home/frigobar123/CLionProjects/APIProject-2022/test_suite/'

first_time = True
result_matrix = []
choosen_range = 100
subprocess.call(["gcc", "-Wall", "-Werror", "-O2", "-g3", dir_path + "main.c"])

# -------------------- SUBMIT TO TESTS --------------------------

for test_pack in range(choosen_range):
    elapsed_time = []
    for filename in os.listdir(test_path):
        split_tup = os.path.splitext(filename)
        if split_tup[1] == '.txt':
            st = time.time()
            subprocess.call("./a.out < " + test_path + filename + " > " + dir_path + "output.txt", shell=True)
            et = time.time()
            elapsed_time.append(et - st)
            if first_time:
                flag = filecmp.cmp(dir_path + "output.txt", test_path + "results/" + filename)
                if not flag:
                    print("!!! Output not correct for Test N°" + filename)
    if first_time:
        first_time = False
    result_matrix.append(elapsed_time)

# -------------------- CALCULATE AVERAGE VALUES --------------------

counter = 0
average_values = []
for filename in os.listdir(test_path):
    split_tup = os.path.splitext(filename)
    if split_tup[1] == '.txt':
        sum1 = 0
        for value in range(choosen_range):
            sum1 = sum1 + result_matrix[value][counter]
        average_values.append(round((sum1 / choosen_range), 3))
        counter = counter + 1

counter = 0
for avg_value in average_values:
    print("Test " + str(counter) + ": " + str(avg_value) + "s")
    counter = counter + 1
