import socket
import time

min_rtt = 0
max_rtt = 0
sum_rtt = 0
success = 0

# Set up the server address and port
server_address = ('localhost', 12000)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout of 1 second for receiving packets
client_socket.settimeout(1)

# Send 10 pings to the server
for sequence_number in range(10):
    
    # Get the current time
    start_time = time.time()

    # Send the ping message to the server
    message = f'Ping {sequence_number+1} {time.time()}'.encode()
    client_socket.sendto(message, server_address)

    try:
        # Wait for a reply from the server
        data, server = client_socket.recvfrom(1024)

        # Calculate the round-trip time
        end_time = time.time()
        rtt = end_time - start_time

        # Print the reply message and round-trip time
        print(f'Reply from {server}: {data.decode()} (RTT={rtt:.6f}s)')
        
         # get minimum RTT
        if sequence_number == 0:
            min_rtt = rtt
        else:
            if rtt < min_rtt:
                min_rtt = rtt
        
        # get maximum RTT
        if sequence_number == 0:
            max_rtt = rtt
        else:
            if rtt > max_rtt:
                max_rtt = rtt
                
        # get average RTT
        if sequence_number == 0:
            sum_rtt = rtt
        else:
            sum_rtt += rtt
            
        success += 1

    except socket.timeout:
        # If no reply is received within 1 second, consider the packet lost
        print(f'Request timed out')
        
   
    
avg_rtt = sum_rtt / 10
        
# calculate the packet loss rate
packet_loss_rate = (10 - success) / 10 * 100

# Print the packet loss rate
print(f'Packet loss rate: {packet_loss_rate}%')

# Print the minimum RTT
print(f'Minimum RTT: {min_rtt:.6f}s')

# Print the maximum RTT
print(f'Maximum RTT: {max_rtt:.6f}s')

# Print the average RTT
print(f'Average RTT: {avg_rtt:.6f}s')

# Close the socket
client_socket.close()