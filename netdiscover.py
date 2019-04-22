import multiprocessing
from lib import results,get_possibilities,get_results,write_data,clean_output

if __name__ == "__main__":
    # Get all IP possibilities
    imp_array = get_possibilities()

    # Run multiprocessed ARP scan
    pool = multiprocessing.Pool(6)
    output = pool.map(results, imp_array)

    # Cleaning output
    net = clean_output(output)

    # Print data here
    # print(net)
    net_results = get_results(net)

    # CSV output
    write_data('Results.csv', net_results)
