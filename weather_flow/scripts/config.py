"""
Configuration settings for the WeatherFlow application.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_openweather_api_key")
WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY", "your_weatherapi_key")

# API URLs
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHERAPI_URL = "https://api.weatherapi.com/v1/current.json"

# List of cities to monitor
CITIES = [
    "London", "New York", "Tokyo", "Sydney", "Paris", 
    "Berlin", "Moscow", "Beijing", "Rio de Janeiro", "Cairo"
]

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC_RAW = "weather-raw"
KAFKA_TOPIC_PROCESSED = "weather-processed"

# Spark Configuration
SPARK_MASTER = os.getenv("SPARK_MASTER", "local[*]")

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
MONGODB_DB = "weatherflow"
MONGODB_COLLECTION_RAW = "weather_raw"
MONGODB_COLLECTION_PROCESSED = "weather_processed"

# Data paths
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, "processed")

# Ensure data directories exist
os.makedirs(RAW_DATA_PATH, exist_ok=True)
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

# Dashboard Configuration
DASHBOARD_PORT = int(os.getenv("DASHBOARD_PORT", "8050"))
