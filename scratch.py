import subprocess
import multiprocessing

def results(item):
    x = item[0]
    y = item[1]
    status = subprocess.Popen('arp -a 192.168.{}.{}'.format(x,y),shell=True, stdout=subprocess.PIPE).stdout.read()
    # print('Done for 192.168.{}.{}'.format(x,y))
    return status

def get_possibilities():
    array = range(0, 256)
    imp_array = []
    for x in array:
        imp_array.append((1, x))
    return imp_array


if __name__ == "__main__":
    imp_array = get_possibilities()
    pool = multiprocessing.Pool(6)
    output = pool.map(results,imp_array)
    results = []
    for item in output:
        if 'No' not in str(item):
            print(str(item)[-59:-20].split(" "))