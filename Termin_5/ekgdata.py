import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import scipy
from scipy import signal
import numpy as np
from scipy.signal import find_peaks
import scipy.signal



# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])


    def make_plot(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        #return self.fig 
#Instanziiert einen EKG-Test anhand der ID und der Datenbank
    def load_by_id() -> object:
        '''file = open("person_db.json")
        person_data = json.load(file)
        ekg_dict = person_data[0]["ekg_tests"][0]
        ekg = EKGdata(ekg_dict)
        return ekg'''

        with open("person_db.json") as file:
            person_data = json.load(file)
            ekg_dict = person_data[0]["ekg_tests"][0]
            ekg = EKGdata(ekg_dict)
        return ekg
        
#Funktion um die Peaks zu finden
    def find_peaks(self):
        #pass
        # Hier wird ein Peakfinder implementiert
        peaks, _ = EKGdata.find_peaks(self.df['Messwerte in mV'], height=0.5, distance=100)
        # z.B. scipy.signal.find_peaks
        return peaks
    
# Funktion zur Berechnung der Hr anhand der peaks und der Zeit
    def estimate_hr():
        #pass
        # Hier wird die Herzfrequenz berechnet
        peaks = EKGdata.find_peaks()
        time = EKGdata.df['Zeit in ms']
        heart_rate = 60000 / np.mean(np.diff(peaks[0]))
        return heart_rate
    
#Plot der EKG-Daten mit gefundenen Peaks
    def plot_time_series():
        #pass
        # Hier wird ein Plot mit Peaks erstellt
        peaks = EKGdata.find_peaks()
        fig, ax = plt.subplots()
        ax.plot(EKGdata.df['Zeit in ms'], EKGdata.df['Messwerte in mV'])
        ax.plot(EKGdata.df['Zeit in ms'][peaks[0]], EKGdata.df['Messwerte in mV'][peaks[0]], "x")
        return fig


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())

