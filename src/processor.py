from collections import defaultdict
from typing import List, Dict

class WindowProcessor:
    def __init__(self, window_size_seconds: int):
        self.window_size = window_size_seconds
        self.current_window_start = None
        self.buffer = defaultdict(list)

    def process_event(self, event: Dict):
        """Ingests an event and potentially triggers a window emission."""
        timestamp = event["timestamp"]
        
        # Initialize window start if needed
        if self.current_window_start is None:
            self.current_window_start = timestamp//self.window_size * self.window_size

        # Check if event belongs to next window (Watermark = arrived time here for simplicity)
        # Assuming in-order arrival for this basic sim
        event_window_start = timestamp // self.window_size * self.window_size
        
        if event_window_start > self.current_window_start:
            self.emit_window()
            self.current_window_start = event_window_start
            self.buffer.clear()
        
        # Add to buffer
        self.buffer[event["device_id"]].append(event)

    def emit_window(self):
        """aggregates and prints metrics for the finished window."""
        print(f"\n--- Window Closed: {self.current_window_start} ---")
        for device_id, events in self.buffer.items():
            temps = [e["temperature"] for e in events]
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            count = len(temps)
            
            status = "NORMAL"
            if max_temp > 50.0:
                status = "CRITICAL HIGH TEMP"
            
            print(f"Device: {device_id} | Count: {count} | Avg Temp: {avg_temp:.2f}C | Max: {max_temp:.2f}C | Status: {status}")
