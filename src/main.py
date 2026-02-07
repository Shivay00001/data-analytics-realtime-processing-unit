import argparse
from src.stream_source import generate_sensor_stream
from src.processor import WindowProcessor

def main():
    parser = argparse.ArgumentParser(description="Real-time Stream Processing Unit")
    parser.add_argument("--window-size", type=int, default=5, help="Tumbling window size in seconds")
    parser.add_argument("--speed", type=float, default=0.1, help="Simulation delay between events")
    
    args = parser.parse_args()
    
    print(f"Starting Stream Processor (Window Size: {args.window_size}s)...")
    
    processor = WindowProcessor(args.window_size)
    stream = generate_sensor_stream(delay=args.speed)
    
    try:
        for event in stream:
            # print(f"Received: {event}") # Verbose
            processor.process_event(event)
    except KeyboardInterrupt:
        print("\nStream stopped.")

if __name__ == "__main__":
    main()
