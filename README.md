# Movie Application and Data Storage Project

## Overview

This project includes a movie application and multiple data storage utilities. The project allows users to manage a movie database and store data in various formats such as JSON and CSV. The application provides functionalities to interact with the movie data, which can be stored and retrieved using different storage mechanisms.

## Features

- **Movie Application**: Manage and interact with a movie database.
- **Data Storage**: Store and retrieve data using JSON and CSV formats.
- **Interface for Storage**: Abstract interface for different storage mechanisms.

## Requirements

- Python 3.x
- JSON
- CSV

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eneh4kene/movie_app.git
   cd movie-data-storage
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```


## Usage

### Movie Application

The `movie_app.py` script provides functionalities to manage and interact with a movie database.

```bash
python movie_app.py
```

### Data Storage

- **JSON Storage**:
  The `storage_json.py` script handles storing and retrieving data in JSON format.

  ```bash
  python storage_json.py
  ```

- **CSV Storage**:
  The `storage_csv.py` script handles storing and retrieving data in CSV format.

  ```bash
  python storage_csv.py
  ```

### Interface for Storage

The `istorage.py` script defines an abstract interface for different storage mechanisms. This script ensures that the storage implementations (JSON and CSV) adhere to a common interface.

### Main Application

The `main.py` script serves as the entry point for the application, integrating the movie application and storage functionalities.

```bash
python main.py
```

## File Structure

```
movie-data-storage/
├── data/                         # Directory to store data files
│   ├── movies.json               # JSON file storing movie data
│   ├── movies.csv                # CSV file storing movie data
├── istorage.py                   # Abstract interface for storage mechanisms
├── main.py                       # Main application entry point
├── movie_app.py                  # Movie application logic
├── storage_csv.py                # CSV storage implementation
├── storage_json.py               # JSON storage implementation
├── requirements.txt              # Required Python packages
└── README.md                     # Project README file
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes you would like to make.
