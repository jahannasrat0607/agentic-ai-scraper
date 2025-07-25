# Amazon Product Scraper

**agentic-ai-scraper** is a modular and efficient Amazon product scraper built with Python and Streamlit.  
It allows users to search Amazon by keyword and region, and view product data like titles, prices, ratings, and more through an interactive web interface.

## Features

- Keyword-based product search
- Country-specific Amazon scraping (`us`, `in`, `uk`, etc.)
- Clean, extensible architecture (controllers, models, enums, helpers)
- Multi-threaded scraping for faster performance
- Streamlit interface for ease of use
- Ready for future LLM integration (optional OpenAI module included)

## Project Structure

agentic-ai-scraper/
├── controllers/ # Scraping logic
├── enums/ # Country-specific URL enums
├── helpers/ # Utility functions
├── models/ # Structured product data using dataclasses
├── llm/ # Placeholder for future LLM integration
├── ui/ # Streamlit frontend
├── main.py # Command-line interface (optional)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Setup Instructions

### 1. Clone the Repository


git clone https://github.com/yourusername/agentic-ai-scraper.git
cd agentic-ai-scraper

### 2. Create virtual environment
conda create -n productgenie python=3.10 -y
conda activate productgenie


### 3. Install Dependencies

pip install --break-system-packages -r requirements.txt

### 4. Run the application

streamlit run app.py

Then open your browser and navigate to:
http://localhost:8501

## Tech Stack
Python 3.10

BeautifulSoup4 – HTML parsing

Requests – HTTP client

Streamlit – Frontend interface

Dataclasses – Structured data modeling

Enum – Country-based URL handling

Threading – For concurrent requests

ScrapeOps Proxy – Handles IP rotation and headers

## Use Cases
Product research and comparison

Amazon price tracker or trend analysis

Training data collection for ML models

Building a shopping assistant or recommender system

## Disclaimer
This project is intended for educational and personal research purposes only.
Scraping Amazon may violate their Terms of Service. Use responsibly and ethically.
Consider using delays, proxies, and respectful request rates when scaling.

## Author
Nasrat Jahan
M.Tech in Data & Computational Science, IIT Jodhpur
LinkedIn: https://www.linkedin.com/in/nasrat-jahan-95aa76326/