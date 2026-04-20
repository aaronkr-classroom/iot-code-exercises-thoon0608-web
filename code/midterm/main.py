# main.py
from lib.sensor_module import RoomSensor

def main():
    sensor1 = RoomSensor("Kitchen", 31, 72, 180)
    sensor2 = RoomSensor("Bedroom", 24, 50, 250)
    sensor3 = RoomSensor("Balcony", 18, 35, 450)

    
    sensor_list = [sensor1, sensor2, sensor3]

    status_counts = {
        "Comfortable": 0,
        "Normal": 0,
        "Warning": 0
    }

    for sensor in sensor_list:
        sensor.show_info()
        
        comfort = sensor.comfort_level()
        light = sensor.light_status()
        
        print(f"Comfort Level: {comfort}")
        print(f"Light Status: {light}")
        
        status_counts[comfort] += 1

    # Part 5: 총 개수 출력 (최종 집계)
    print("Comfortable:", status_counts["Comfortable"])
    print("Normal:", status_counts["Normal"])
    print("Warning:", status_counts["Warning"])

if __name__ == "__main__":
    main()