

def traffic_light(currentSignal, isEmergencyVehicleApproaching):
    if(isEmergencyVehicleApproaching):
        return "IMMEDIATE GREEN"
    
    signal = currentSignal.upper()

    match signal:
        case "RED":
            return "STOP"
        case "YELLOW":
            return "PREPARE TO STOP"
        case "GREEN":
            return "GO"
        case _:
            return "INVALID SIGNAL"
