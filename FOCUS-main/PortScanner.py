import time, threading
from functions import port_scanner, OpenPorts, pushbullet_noti

print('Port scanner is Running...')
# Formatting Whitelist Ports
with open(r'C:\Users\aryam\the real things\Python-Proj\SDC\FOCUS-main\FOCUS-main\Whitelisted_Ports.txt', 'r') as WhitelistedPortsFile:
    WhitelistedPortsList = [int(port.strip()) for port in WhitelistedPortsFile.readlines()]

# Port scanning via multi-thread distribution
start = time.time()  # Function Start Time
for port in range(1, 65536):
    if port in WhitelistedPortsList:
        print(f"Port {port} - Authorized in Whitelist")
        continue

    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()

end = time.time()  # Function End Time

#Message formatting
message = ''
for port in OpenPorts:
    message = message + str(port) + '\n'

if len(OpenPorts) == 0:
    print('No other open port detected.')
else:
    #Port closer
    # print('Attempting to close ports...')
    # pushbullet_noti('Open Ports Detected and Terminated:\n', message)
    print("")
    print("")
    print("Scan Complete!")
    print(f"Time taken for scan: {end - start} Seconds")
    print('Hit enter to continue...')
    input()