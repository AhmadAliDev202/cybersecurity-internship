# Basic Network Sniffer

## Overview
This project is a simple network sniffer built using Python and Scapy.  
It captures live network packets and extracts:

- Source IP
- Destination IP
- Protocol (TCP/UDP/ICMP)
- Source and Destination Ports

Logs are saved to `sniffer_log.txt`.

---

## Tools Used
- Python 3
- Scapy
- Npcap (Windows)

---

## How to Run

1. **Install dependencies**  
   Open terminal in VS Code or CMD and run:

   ```bash
   python -m pip install -r requirements.txt
````

2. **Run as Administrator**
   Open terminal as admin and run:

   ```bash
   python sniffer.py
   ```

3. **Generate network traffic**
   Open browser, ping a site, or do any internet activity.

4. **Stop the sniffer**
   The sniffer runs continuously until you stop it. Press:

   ```
   Ctrl + C
   ```

   in the terminal to stop the program.

---
