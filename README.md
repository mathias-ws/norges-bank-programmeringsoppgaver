# norges-bank-programmeringsoppgaver
Project with answers to programming tasks given by Norges Bank as 
part of the job interview process.

# How to run
To run this project you can clone this project, enter the folder
and run `python3 main.py` from the terminal. This will run both tasks.
For task one the program will ask you to specify a folder 
(view the Task 1 section to learn about its limits). 
For the task two to run the package dataclasses must be installed. 
All results are printed to the terminal.

# Task 1
The task 1 takes a path of a folder that contains at least one csv file
and a txt file. Furthermore, it opens the txt file and compares it lines
with the lines in the csv file(s). When it gets a match, it returns 
the csv file name and the line of where the function got a match.

## Some limitations
* For now the functions only verifies that the specified folder 
contains at least a txt file and a csv. It does however not check
if the folder exists and if the contents of the folder is empty.
If the folder does not have any elements, the program will crash.

# Task 2
The task 2 takes in an ip range and returns the ip address of the last
ip to be scanned. The algorithm determines which ip address to be
scanned last in accordance with the task specification.

## Some limitations
* The start and end ip addresses must be valid.

* The algorithm for generating the ip range is slow and takes up a lot of
ram. To mitigate some of those problems the ipaddress package could
have been used. However, it does only take in a subnet (that could
have been 10.0.0.1/8 in this case) but to make the script more
modular and applicable in other settings this was decided against.
* The algorithm for determining the last ip address is slow when the 
specified ip range is used (might be because it contains 16 million ips).
The algorithm could have skipped every even number because it will never
end on an ip ending with an even number. The assumption that every ip
should be visited and trigger a scan has been made.
