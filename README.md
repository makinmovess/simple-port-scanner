# simple-port-scanner
easy and interactive port scanner written in python.
# Lightweight TCP Port Scanner

A lightweight, fast, and interactive TCP port scanner written in Python. This tool was developed for educational purposes and network diagnostics, providing a practical demonstration of TCP/IP protocol interactions and socket programming.

It serves as a minimalistic utility for quick availability checks of standard services on authorized servers or network appliances.

## Features
* **Interactive Execution:** Prompts the user for the target IP address or hostname.
* **Optimized Timeout:** Utilizes a 1-second socket timeout for rapid scanning of closed or filtered ports.
* **Robust Error Handling:** Includes graceful exits for keyboard interrupts (`Ctrl+C`) and handles hostname resolution failures without crashing.
* **Real-time Console Output:** Implements `sys.stdout` for clean, in-place terminal updates during the scanning process.

## Prerequisites
* Python 3.x
* Built-in libraries: `socket`, `sys`, `time`

## Disclaimer
"This tool was created strictly for educational purposes and for testing your own network infrastructure (e.g., a homelab environment). Never scan networks, devices, or servers without explicit authorization from the owner. The author assumes no responsibility or liability for any illegal or malicious use of this script."

## Usage

**Option 1: Running via Python interpreter**
1. Clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Execute the script via terminal:
   ```bash
   python port_scanner.py

