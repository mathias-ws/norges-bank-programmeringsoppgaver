from task_one import compare_ips_in_files
from task_two import find_last_scanned_ip, generate_ip_range

print("####################Task 1####################")
print(compare_ips_in_files(
    input("Please enter the folder where the csv file(s) and the txt file is located in: ")))

print("\n\n####################Task 2####################")
print("Creating the ip range 10.0.0.1-10.255.255.254.")
ip_range = generate_ip_range("10.0.0.1", "10.255.255.254")

print("Ip range created, starting to find the last ip to scan.")
print("The last ip to scan is: " + find_last_scanned_ip(ip_range))
