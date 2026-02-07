import time
import random
from typing import Iterator, Dict

def generate_sensor_stream(delay: float = 0.1) -> Iterator[Dict]:
    """Yields a continuous stream of mock sensor data."""
    device_ids = [f"sensor_{i:03d}" for i in range(1, 6)]
    
    while True:
        timestamp = time.time()
        device_id = random.choice(device_ids)
        temperature = random.uniform(20.0, 35.0)
        humidity = random.uniform(40.0, 60.0)
        
        # Inject occasional anomalies
        if random.random() < 0.05:
            temperature += 20.0 # Heat spike
            
        yield {
            "timestamp": timestamp,
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity
        }
        
        time.sleep(delay)
