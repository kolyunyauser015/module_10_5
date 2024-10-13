import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]
"""
# Линейный вызов
start_l = datetime.datetime.now()
for name_file in filenames:
    read_info(name_file)
end_l = datetime.datetime.now()
result_linear = end_l - start_l
print(f'{result_linear} - (линейный)')
"""

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_mp = datetime.datetime.now()
        pool.map(read_info, filenames)
    end_mp = datetime.datetime.now()
    result_multiprocess = end_mp - start_mp
    print(f'{result_multiprocess} - (многопроцессный)')
