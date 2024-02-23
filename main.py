import mobile_device, edge_server, cloud_server

# Define the devices
mobile_device = mobile_device.MobileDevice(120, 30, 10, 0.4, 15)
edge_server_1 = edge_server.EdgeServer(500, 500, 100, 1000, 0.01, 0.001, 200, "1")
edge_server_2 = edge_server.EdgeServer(600, 800, 150, 1200, 0.015, 0.0015, 300, "2")
cloud_server_1 = cloud_server.CloudServer(800, 5000, 500, 2000, 0.0001, 0.00001, 500, "1")
cloud_server_2 = cloud_server.CloudServer(1000, 8000, 800, 3000, 0.00015, 0.000015, 800, "2")

# Store the devices in a list
devices = [edge_server_1, edge_server_2, cloud_server_1, cloud_server_2]

# Define the task parameters
data_size = 1000
required_computation_power = 200

# Loop over the tasks
for i in range(5):
    # Loop over the devices and execute the function on each device
    computation_time_on_devices = []
    for device in devices:
        energy_consumed = round(device.total_energy_consumed(data_size, required_computation_power), 4)
        # Add the energy consumed to the list of results
        computation_time_on_devices.append((device.__str__(), energy_consumed))

    # Sort the results by energy consumed in ascending order
    computation_time_on_devices.sort(key=lambda x: x[1])
    print(computation_time_on_devices)
    # Print the device with the lowest energy consumption
    print(f"The task_{i+1} will be computed on {computation_time_on_devices[0][0]} with energy consumed: {computation_time_on_devices[0][1]}")
