# Arch Technology — Cybersecurity Internship Projects

> Two hands-on Python projects built to explore core cybersecurity concepts: packet analysis and keystroke monitoring both in controlled, educational environments.

---

## Table of Contents

- [About](#about)
- [Projects](#projects)
  - [Task 1: Network Sniffer](#task-1--network-sniffer)
  - [Task 2: Keylogger](#task-2--keylogger)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Ethical & Legal Notice](#ethical--legal-notice)

---

## About

This repository is part of the **Arch Technology Cybersecurity Internship** program. The projects here are designed to give you a ground-level feel for how network traffic flows and how input events are captured like the kind of fundamentals that sit underneath a lot of real-world security tooling.

Both tasks are strictly for **educational use** in isolated, controlled environments.

---

## Projects

### Task 1: Network Sniffer

**Location:** `task1-network-sniffer/`  
**Core Library:** [Scapy](https://scapy.net/)

Captures live network packets and logs the details that matter most for basic traffic analysis:

| Field | Description |
|---|---|
| Source IP | Where the packet came from |
| Destination IP | Where it's headed |
| Protocol | TCP, UDP, ICMP, etc. |
| Ports | Source and destination port numbers |

It's a great way to see, in real time, just how much is happening on a network even when you're not actively doing anything.

---

### Task 2: Keylogger

**Location:** `task2-keylogger/`  
**Core Library:** [pynput](https://pynput.readthedocs.io/)

Simulates a keylogger in a sandboxed environment. Every keystroke is captured and written to a log file along with a timestamp — which is exactly the kind of artifact you'd look for during a forensic investigation or endpoint audit.

Running this in your own controlled environment helps you understand *why* keyloggers are such a persistent threat, and *what* their output actually looks like.

---

## Prerequisites

Make sure you have the following before you run anything:

- Python 3.7+
- `pip` (comes with Python)
- Administrator / root privileges (required for the network sniffer)

---

## Getting Started

### Task 1: Network Sniffer

```bash
# 1. Move into the project folder
cd task1-network-sniffer

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Run as administrator
#    Windows: open your terminal as Admin, then —
python sniffer.py

#    macOS / Linux —
sudo python sniffer.py
```

Once it's running, just do something on your network like to open a browser tab, ping a host, anything. You'll see packets rolling in.

When you're done, hit `Ctrl + C` to stop the sniffer gracefully.

---

### Task 2: Keylogger

```bash
# 1. Move into the project folder
cd task2-keylogger

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Run the script
python keylogger.py
```

Keystrokes will be logged with timestamps to a local file. Review the output log to see what was captured.

---

## Ethical & Legal Notice

These tools are built **solely for learning** within environments you own and control.

Running a network sniffer or keylogger on systems, networks, or devices without **explicit permission** is illegal in most jurisdictions and a serious ethical violation such as regardless of intent.

Use these responsibly. The goal is to understand how attackers think, not to become one.

---

*Built as part of the Arch Technology Cybersecurity Internship.*
