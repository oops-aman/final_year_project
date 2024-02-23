class MobileDevice:
    computation_capacity = 0
    battery_capacity = 0
    communication_capacity = 0
    computation_energy_rate = 0
    battery_threshold = 0

    def __init__(self, computation_capacity, battery_capacity, communication_capcity, computation_energy_rate, battery_threshold):
        self.computation_capacity = computation_capacity
        self.battery_capacity = battery_capacity
        self.communication_capacity = communication_capcity
        self.computation_energy_rate = computation_energy_rate
        self.battery_threshold = battery_threshold

    def total_energy_consumed(self, data_size, required_computation_power):
        if required_computation_power > self.computation_capacity:
            return 0
        computation_time = data_size / self.computation_capacity
        computation_time = round(computation_time, 4)
        computation_energy_consumed = computation_time * self.computation_energy_rate
        if self.battery_capacity - computation_energy_consumed >= self.battery_threshold:
            return computation_energy_consumed
        return 0
