from scapy.all import rdpcap
import pyshark

# Load the pcap file
pcap_file_path = 'wireless_connection.pcap'

# Open the capture file
capture = pyshark.FileCapture(pcap_file_path)

# Initialize variables
total_packets = 0
total_bytes = 0
time_start = None
time_end = None

# Process packets to extract information
for packet in capture:
    # Get the packet size and timestamp
    packet_size = int(packet.length)
    packet_time = float(packet.sniff_timestamp)
    
    # Track total packets and bytes
    total_packets += 1
    total_bytes += packet_size
    
    # Track the time range (capture start and end time)
    if time_start is None:
        time_start = packet_time
    time_end = packet_time

# Calculate total capture time in seconds
capture_duration = time_end - time_start if time_end and time_start else 0

# Calculate other metrics
average_packet_size = total_bytes / total_packets if total_packets else 0
average_pps = total_packets / capture_duration if capture_duration > 0 else 0
average_bytes_per_second = total_bytes / capture_duration if capture_duration > 0 else 0

# Convert total bytes to MiB
total_bytes_mib = total_bytes / (1024 * 1024)

# Summary data
summary_data = {
    "Time of capture (min)": capture_duration / 60,
    "Packets": total_packets,
    "Bytes (MiB)": total_bytes_mib,
    "Average packet size (B)": average_packet_size,
    "Average packets per second (pps)": average_pps,
    "Average bytes per second (B/s)": average_bytes_per_second
}

print(
    f'''
      Time of capture (min): {summary_data["Time of capture (min)"]}
      Packets: {summary_data['Packets']}
      Bytes (MiB): {summary_data["Bytes (MiB)"]}
      Average packets per second (pps): {summary_data['Average packets per second (pps)']}
      Average packet size (B): {summary_data['Average packet size (B)']}
      Average bytes per second (B/s): {summary_data['Average bytes per second (B/s)']}
    '''
    )

# Given values
traffic_mbits = 2.804359436035156
time_seconds = 8.218785
bandwidth_mbps = 100

# Calculate relative network load
relative_load = traffic_mbits / (time_seconds * bandwidth_mbps)
print(f'Relative load: {relative_load}')