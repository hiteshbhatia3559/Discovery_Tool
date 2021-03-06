import subprocess
# import multiprocessing
import nmap
import csv
import socket


def results(item):
    # x = item[0]
    y = item[1]
    got_ip = socket.gethostbyname(socket.gethostname()).split('.')
    status = subprocess.Popen('arp -a {}.{}.{}.{}'.format(got_ip[0],got_ip[1],got_ip[2], y), shell=True, stdout=subprocess.PIPE).stdout.read()
    print('Done for {}.{}.{}.{}'.format(got_ip[0],got_ip[1],got_ip[2], y))
    return status


def get_possibilities():
    array = range(0, 256)
    imp_array = []
    for y in array:
        imp_array.append((1, y))
    return imp_array


def write_data(name_of_file, net):
    temp = []
    for item in net:
        temp.append(len(list(item.keys())))
    index = temp.index(max(temp))

    keys = net[index].keys()
    with open(name_of_file, 'w+', newline='') as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(net)
        print("Done writing")


def get_results(net):
    nm = nmap.PortScanner()
    for item in net:
        try:
            print("Scanning port {}".format(item['ip']))
            nm.scan(item['ip'], '22-9000')
            ip = nm[item['ip']]

            item['details'] = dict()
            try:
                for key in list(ip['tcp'].keys()):
                    item['details'][key] = (ip['tcp'][key]['name'], ip['tcp'][key]['state'], ip['tcp'][key]['version'])
                # item['tcp'] = ip['tcp']
                print("Open ports found for {}".format(item['ip']))
            except:
                item['details'] = dict()
                print("No open ports for {}".format(item['ip']))
        except:
            # item['details'] = dict()
            print("Irrelevant IP found")
    return net


def clean_output(output):
    net = []
    for item in output:
        if 'No' not in str(item):
            temp = str(item)[-59:-20].split(" ")
            data = []
            for item in temp:
                if len(item) > 5:
                    data.append(item)
                    # print(item)
            net.append({"ip": data[0], "mac": data[1]})
    return net
