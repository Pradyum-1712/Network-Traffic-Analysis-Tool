# Network Traffic Analysis Tool

A Python-based tool to capture, analyze, and classify network traffic in real-time. This project is aimed at monitoring network activity and helping detect potential threats or unusual traffic patterns.

## Features
- **Real-time Traffic Capture**: Capture live network traffic packets.
- **Traffic Classification**: Classify traffic by source IP, destination IP, protocols, and ports.
- **Traffic Visualization**: Generate visual reports for traffic analysis.
- **Alert System**: Detect anomalies and alert users about suspicious activity.
- **Logs Export**: Export traffic logs in CSV or JSON format for further analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Network-Traffic-Analysis-Tool.git
   ```
   
2. Install the dependencies:
 ```bash
pip3 install -r requirements.txt
```
3.Run the tool:
```bash
sudo python3 Network_analysis.py
```
## Usage

The tool captures and displays real-time traffic. Modify the interface in the script to choose a specific network interface.

## Future Enhancements

Packet filtering for specific protocols and ports.
Machine learning integration to predict or classify suspicious traffic.
