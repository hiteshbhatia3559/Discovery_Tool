import subprocess
import multiprocessing
import nmap
import csv


def results(item):
    x = item[0]
    y = item[1]
    status = subprocess.Popen('arp -a 192.168.{}.{}'.format(x, y), shell=True, stdout=subprocess.PIPE).stdout.read()
    print('Done for 192.168.{}.{}'.format(x, y))
    return status


def get_possibilities():
    array = range(0, 256)
    imp_array = []
    for y in array:
        imp_array.append((1, y))
    return imp_array


def write_data(name_of_file, data):
    net = data
    with open(name_of_file, 'w+', newline='') as outfile:
        for key in list(net[1].keys()):
            if key == list(net[1].keys())[-1]:
                outfile.write(key)
                outfile.write('\n')
            else:
                outfile.write(key)
                outfile.write(',')
        for item in net:
            items = list(item.values())
            outfile.write(items[0] + ',' + items[1] + '\n')


if __name__ == "__main__":
    # Get all IP possibilities
    imp_array = get_possibilities()

    # Run multiprocessed ARP scan
    pool = multiprocessing.Pool(6)
    output = pool.map(results, imp_array)

    # Result will be in below list
    net = []

    # Cleaning output
    for item in output:
        if 'No' not in str(item):
            temp = str(item)[-59:-20].split(" ")
            data = []
            for item in temp:
                if len(item) > 5:
                    data.append(item)
                    # print(item)
            net.append({"ip": data[0], "mac": data[1]})

    # Print data here
    # print(net)
    nm = nmap.PortScanner()
    for item in net:
        try:
            print("Scanning port {}".format(item['ip']))
            nm.scan(item['ip'], '22-9000')
            ip = nm[item['ip']]

            try:
                for key in list(ip['tcp'].keys()):
                    item[key] = (ip['tcp'][key]['name'], ip['tcp'][key]['state'], ip['tcp'][key]['version'])
                # item['tcp'] = ip['tcp']
                print("Open ports found for {}".format(item['ip']))
            except:
                print("No open ports for {}".format(item['ip']))
        except:
            print("Irrelevant IP found")
    print(net)

    # CSV output
    # write_data('Results.csv',net)
