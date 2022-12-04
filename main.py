# Seventh project - Building a Weather Data REST API
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

# Reading and then extracting all the station's IDs and names.
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    # Connecting the 'stations' data frame (which contains all the station's IDs
    # and names) to the 'home.html' file.
    return render_template("home.html", data=stations.to_html())


# For one station for one date.
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Filtering the right filepath according to the 'station' variable the user entered.
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    # Loading all the above file's content. Parsing the 'Date' columns to a Date data type.
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    # Filtering the file's content with the 'loc' condition based on the 'date' variable the user entered
    # and squeezing out (extracting) the temperature value divided by 10.
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# For one station for all dates.
@app.route("/api/v1/<station>")
def all_data(station):
    # Filtering the right filepath according to the 'station' variable the user entered.
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    # Loading all the above file's content.
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    # Converting the data frame to a dictionary.
    result = df.to_dict(orient="records")
    return result


# For one station for one year.
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    # Filtering the right filepath according to the 'station' variable the user entered.
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    # Loading all the above file's content.
    df = pd.read_csv(filepath, skiprows=20)
    # Converting the 'df["    DATE"]' column (which is the 'Date' column) to a string type so that I
    # could use the '.srt.startswith()' string method in the next line.
    df["    DATE"] = df["    DATE"].astype(str)
    # Filtering the date column according to the year variable, and converting the datat frame to a dict.
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
