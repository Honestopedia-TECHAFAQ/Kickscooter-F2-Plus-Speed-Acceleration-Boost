import bluetooth

def discover_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    return nearby_devices

def connect_to_device(device_address):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((device_address, 1)) 
        return sock
    except Exception as e:
        print(f"Failed to connect to device: {e}")
        return None

def send_data(sock, data):
    try:
        sock.send(data)
    except Exception as e:
        print(f"Failed to send data: {e}")

def receive_data(sock, buffer_size=1024):
    try:
        data = sock.recv(buffer_size)
        return data
    except Exception as e:
        print(f"Failed to receive data: {e}")
        return None

def disconnect(sock):
    try:
        sock.close()
    except Exception as e:
        print(f"Failed to disconnect: {e}")

def main():
    nearby_devices = discover_devices()
    if nearby_devices:
        for addr, name in nearby_devices:
            if "Ninebot" in name:  
                device_address = addr
                break
        else:
            print("No Ninebot Kickscooter F2 Plus found.")
            return

        sock = connect_to_device(device_address)
        if sock:
            send_data(sock, "Hello")
            received_data = receive_data(sock)
            if received_data:
                pass
            disconnect(sock)
    else:
        print("No Bluetooth devices found.")

if __name__ == "__main__":
    main()
