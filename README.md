# Food Price Tracker

A simple Python application to track food prices across different stores.

## Features

- Add and manage stores
- Record food item prices with dates
- View all recorded prices
- Calculate average prices for items
- Web interface for easy access

## Requirements

- Python 3.x
- SQLite (built-in with Python)
- Flask

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Or if using a virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

## Usage

### Command Line Version

Run the CLI application:

```bash
python main.py
```

### Web Interface

Run the web application:

```bash
python app.py
```

Or with virtual environment:

```bash
.venv\Scripts\python.exe app.py
```

Then open your browser to `http://127.0.0.1:5000/`

## Database

The app uses a SQLite database (`food_prices.db`) to store data locally.