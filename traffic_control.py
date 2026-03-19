def calculate_signal_time(vehicle_count):

    if vehicle_count <= 5:
        return 10

    elif vehicle_count <= 15:
        return 20

    elif vehicle_count <= 30:
        return 40

    else:
        return 60