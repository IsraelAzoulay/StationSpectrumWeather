## WeatherRESTful API

WeatherRESTful API is a Flask-based web application that provides access to temperature data from various weather stations around the world. The application allows you to fetch temperature readings for specific dates, all dates, or based on a specific year for a given station.

## Features

- View list of weather stations available in the dataset
- Fetch temperature data for a specific date for a given station
- Fetch all temperature data available for a particular station
- Retrieve yearly temperature data for a given station

## Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- pip

## Installation & Usage

1. Clone the repository:
git clone https://github.com/IsraelAzoulay/station-spectrum-weather.git

2. Navigate to the project directory:
cd WeatherRESTful-API

3. Install the necessary dependencies:
pip install -r requirements.txt

4. Run the Flask application:
python main.py

Once the server is running, open your browser and visit http://127.0.0.1:5000/ to access the application.

## API Endpoints

- Home Page: 'http://127.0.0.1:5000/'
- Specific Station & Date: 'http://127.0.0.1:5000/api/v1/<station>/<date>'
- All Data for a Station: 'http://127.0.0.1:5000/api/v1/<station>'
- Yearly Data for a Station: 'http://127.0.0.1:5000/api/v1/yearly/<station>/<year>'

## Data Source

The temperature data is sourced from text files in the data_small directory. Each file corresponds to a specific weather station.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
