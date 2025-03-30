# FOCUS

## Introduction  

Port security is a critical aspect of cybersecurity, focusing on monitoring and controlling network traffic to enhance system efficiency and security. This project aims to develop a port security and process control system that tracks input and output traffic, prevents unauthorized background tasks, and incorporates face recognition-based protection for managing trusted processes.  

Primarily designed for enterprise servers, this project provides robust port security and process control mechanisms. The current implementation serves as a working prototype, developed and tested on a laptop, showcasing its potential for larger-scale applications.  



For the entire project overview, please visit: [Project Overview on Prezi](https://prezi.com/view/H9Voap45IgFbxAH62ifW/)

---

## Project Overview  

### The `FOCUS-Main` Folder  

The `FOCUS-Main` folder contains all the code necessary for the project. It houses the scripts and modules that power the port security and process control system.  

### Folder Structure for Photos  

The `photo` folder is organized into two subfolders:  

1. **auth**  
  - Contains a clear photo of the authorized person.  
  - Used for face recognition to verify access to the whitelist.  

2. **unauth**  
  - Stores images of individuals attempting unauthorized access to the whitelist.  
  - These images are captured and sent to the server admin via email for security purposes.  

---

## Current Features  

### `main.py`  

The `main.py` file serves as the core of the system, offering the following functionalities:  

1. **Port Closer**  
  - Monitors all active ports and compares them against the whitelist.  
  - Automatically closes any ports not listed in the whitelist.  

2. **Whitelist Management**  
  - Enables users to access and manage the whitelist.  
  - Secured with face recognition to ensure only authorized users can make changes.  
  - Sends photos of unauthorized users to the admin via email.  

3. **GitHub Repository**  
  - Provides a link to the project's GitHub repository for code access and collaboration.  

---

## Additional Functionalities  

1. **Port Scanner**  
  - Scans active ports on the system.  
  - Identifies authorized and unauthorized open ports.  

2. **Port Closer and Opener**  
  - Allows the server admin to manually open or close ports.  
  - Demonstrates functionality and tests automated port management.  

3. **Whitelist with Face Recognition Protection**  
  - Maintains a whitelist of trusted processes running through authorized ports.  
  - Uses facial recognition to grant or deny execution permissions.  
  - Prevents unauthorized modifications to the whitelist.  
  - Sends email alerts to the admin if unauthorized access is detected.  

---

## Usage Instructions  

### Real-World Scenario  

1. The server admin identifies the ports to be authorized.  
2. Run the `main.py` file and select "2. Whitelist".  
3. The server admin is verified via face recognition, and the `Whitelisted_Ports.txt` file is opened.  
4. The admin enters the authorized ports and closes the file.  
5. Run the `main.py` file again and select "1. Port Master".  
6. All ports except those listed in `Whitelisted_Ports.txt` are closed.  
7. The system runs continuously in the background, closing any unauthorized open ports.  

### Testing Scenario for Mini Hackathon  

1. Install all required modules listed in `Requirements.txt`.  
2. Upload a clear photo of the authorized person to the `auth` folder. This photo will be used for face recognition during whitelist management.  
3. Run `PortScanner.py` to identify all currently active ports. Add these ports to `Whitelisted_Ports.txt` to avoid network errors during testing. 
4. **Note on Whitelist Management**  
  - Currently, the `Whitelisted_Ports.txt` file can be directly accessed and edited.  
  - In future updates, this file will be encrypted and made inaccessible for direct edits.  
  - Once encrypted, use `Whitelist.py` to manage the whitelist securely.  
5. Run `PortOpener.py` to open a random port (e.g., a port not currently in use). This simulates an unauthorized port opened by a potential threat. Keep this process running.  
6. Run `main.py` and select "1. Port Master". The system will detect and close any unauthorized ports, including the port opened in step 4.  

