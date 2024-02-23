class CloudServer:
    computation_capacity = 0
    storage_capacity = 0
    communication_capacity = 0
    battery_capacity = 0
    computation_energy_rate = 0
    transmission_energy_rate = 0
    battery_threshold = 0
    name = ""

    def __init__(self, compuation_capacity, storage_capacity, communication_capacity, battery_capacity, computation_energy_rate, transmission_energy_rate, battery_threshold, name):
        self.computation_capacity = compuation_capacity
        self.storage_capacity = storage_capacity
        self.communication_capacity = communication_capacity
        self.battery_capacity = battery_capacity
        self.computation_energy_rate = computation_energy_rate
        self.transmission_energy_rate = transmission_energy_rate
        self.battery_threshold = battery_threshold
        self.name = name

    def total_energy_consumed(self, data_size, required_computation_power):
        if data_size > self.storage_capacity or required_computation_power > self.computation_capacity:
            return 0
        computation_time = data_size / self.computation_capacity
        computation_time = round(computation_time, 4)
        computation_energy_consumed = computation_time * self.computation_energy_rate
        transmission_energy_consumed = data_size * self.transmission_energy_rate
        total_energy_consumed = computation_energy_consumed + transmission_energy_consumed
        if self.battery_capacity - total_energy_consumed >= self.battery_threshold:
            return total_energy_consumed
        return 0
    
    def __str__(self):
        return "Cloud Server " + self.name
    