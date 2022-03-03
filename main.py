from task_two import find_last_scanned_ip, generate_ip_range

print("Creating the ip range.")
ip_range = generate_ip_range("10.0.0.1", "10.255.255.254")

print("Ip range created, starting to find the last ip to scan.")
print("The last ip to scan is: " + find_last_scanned_ip(ip_range))
