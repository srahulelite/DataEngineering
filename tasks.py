# 1. Log Analyzer
# Objective: Parse server logs (or custom logs) to extract insights.
# Concepts Covered: File handling, string manipulation, data filtering, dictionaries.
# Tasks:
# Create a function that reads and parses a sample log file.
# Extract and count occurrences of each status code (e.g., 200, 404).
# Identify top IP addresses by request frequency.
# Difficulty: Easy

# 2. Sales Data Summarizer
# Objective: Process a CSV file of sales records and summarize key metrics.
# Concepts Covered: File handling, csv module, dictionaries, data aggregation.
# Tasks:
# Load a CSV file with fields like Date, Product, Price, Quantity.
# Summarize the data, e.g., calculate total sales for each product.
# Find the most profitable product and the day with the highest sales.
# Difficulty: Easy to Medium

# 3. Mini ETL Pipeline Simulation
# Objective: Simulate a simplified ETL (Extract, Transform, Load) process.
# Concepts Covered: Data transformation, JSON, list comprehensions, error handling.
# Tasks:
# Read JSON files representing user data (name, age, purchase history).
# Filter users based on certain criteria (e.g., age).
# Transform and store the data in a different format, such as a cleaned-up JSON or CSV.
# Difficulty: Medium

# 4. Weather Data Analysis (API)
# Objective: Pull and analyze weather data using a public API.
# Concepts Covered: APIs, JSON parsing, dictionaries, list comprehensions.
# Tasks:
# Fetch weather data for a city (use a free API like OpenWeatherMap).
# Parse the data to calculate temperature averages, high/low, and other insights.
# Optionally, create a command-line interface to let the user pick cities and date ranges.
# Difficulty: Medium

# 5. Data Aggregator for Survey Responses
# Objective: Process and analyze survey data to extract insights.
# Concepts Covered: Dictionaries, lists, conditionals, data aggregation.
# Tasks:
# Given a list of dictionaries representing responses, extract counts for each answer.
# Calculate metrics like average age or most common response.
# Display results in a clean format or export to a CSV.
# Difficulty: Medium to Hard
# Let me know if one of these resonates with you, or if you’d like a few adjustments. We’ll take it step-by-step, reinforcing your Python skills as we go.


#HINTS
# 3. Mini ETL Pipeline Simulation
# Data Source: Use synthetic JSON data representing users. You can:
# Create JSON files manually, or use Mockaroo to generate JSON with fields like name, age, purchase_history.
# Generate sample JSON data in Python:
# python
# Copy code
# import json
# sample_data = [{"name": "Alice", "age": 30, "purchase_history": ["item1", "item2"]}]
# with open("sample_data.json", "w") as f:
#     json.dump(sample_data, f)

# 4. Weather Data Analysis (API)
# Data Source: Use the OpenWeatherMap API, which offers free access with a sign-up.
# Register to get an API key, then use Python’s requests module to pull data.
# Example Endpoint: http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
# Alternative: If you can’t access an API, create a small sample JSON file with similar data fields (temperature, humidity, wind_speed) for offline testing.

# 5. Data Aggregator for Survey Responses
# Data Source: Create a JSON or CSV file with survey responses. Fields might include name, age, gender, response1, response2, etc.
# Sample JSON:
# json
# Copy code
# [
#   {"name": "Alice", "age": 29, "gender": "F", "response1": "Yes", "response2": "No"},
#   {"name": "Bob", "age": 35, "gender": "M", "response1": "No", "response2": "Yes"}
# ]
# Or, Mockaroo: Generate custom survey responses in CSV or JSON format.