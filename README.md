# DIA Stock Price Tracker

A stock market data collection and visualization project developed as part of Citi's Technology Software Development Simulation.

The project uses Java to retrieve DIA ETF price data through the Twelve Data API, records timestamps for each observation, and stores observations in a queue. A separate Python script processes the collected data and visualizes price movements over time.

## Project Overview

This project explores how programming can be applied to financial data collection and analysis. It combines Java-based API integration with Python-based data processing and visualization.

## Features

- **Real-Time Data Collection:** Retrieves DIA price data using the Twelve Data API.
- **Timestamp Tracking:** Records the time associated with each price observation.
- **Queue-Based Storage:** Stores collected observations in a Java queue.
- **Automated Polling:** Requests new price observations every 15 seconds.
- **Data Processing:** Uses Python to extract timestamps and prices from Java output.
- **Data Visualization:** Generates a graph showing DIA prices over time.

## Technologies Used

- **Java** — API integration, data collection, timestamps, and queue management.
- **Python** — Data processing and visualization.
- **Twelve Data API** — Financial market data.
- **Pandas** — Data organization and processing.
- **Matplotlib** — Price visualization.
- **Google Colab** — Python development and execution.
- **GitHub** — Version control and project documentation.

## Repository Structure

```text
citi-stock-price-tracker/
│
├── App.java
├── dia_price_graph.py
└── README.md
