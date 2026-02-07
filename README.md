# Data Analytics Realtime Processing Unit

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Streaming](https://img.shields.io/badge/Architecture-Streaming-orange.svg)](https://en.wikipedia.org/wiki/Stream_processing)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade real-time stream processing engine** simulating modern data engineering architectures. This repository implements a high-throughput data ingestion pipeline with tumbling window aggregation, simulating systems like Apache Flink or Spark Streaming.

## 🚀 Features

- **Stream Source Simulation**: Generates high-velocity mock data streams (e.g., IoT sensor readings).
- **Windowed Aggregation**: Implements Tumbling Windows for time-based data summarization (Avg, Max, Count).
- **Low Latency Processing**: Efficient in-memory buffer management for real-time analytics.
- **Event Time Processing**: Handles out-of-order events (basic implementation) via watermark timestamps.

## 📁 Project Structure

```
data-analytics-realtime-processing-unit/
├── src/
│   ├── stream_source.py  # Data Generator
│   ├── processor.py      # Windowing Logic
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/data-analytics-realtime-processing-unit.git

# Install
pip install -r requirements.txt

# Run Stream Processor
python src/main.py --window-size 5
```

## 📄 License

MIT License
