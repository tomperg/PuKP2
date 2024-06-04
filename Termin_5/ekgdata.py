import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import scipy
from scipy import signal
import numpy as np
import scipy.signal as signal
from scipy.signal import find_peaks
import plotly.graph_objects as go



# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        #self.id = ekg_dict["id"]
        #self.date = ekg_dict["date"]
        #self.data = ekg_dict["result_link"]
        if isinstance(ekg_dict, dict):
            self.id = ekg_dict["id"]
            self.date = ekg_dict["date"]
            self.data = ekg_dict["result_link"]
        elif isinstance(ekg_dict, str):
            self.data = ekg_dict
            self.id = None
            self.date = None
        else:
            raise ValueError("Input should be a dictionary or a file path string.")
        
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])

    def make_plot(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        return self.fig
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
        '''A function that finds the peaks in the EKG data and returns the peaks as an array.'''
        
        peaks, _ = signal.find_peaks(self.df['Messwerte in mV'], height=340) 
        return peaks
    
# Funktion zur Berechnung der Hr anhand der peaks und der Zeit
    def estimate_heartrate(self):
        '''A function that estimates the heart rate from the EKG data and returns the heart rate as an array.'''
        peaks = self.find_peaks()
        
        # calculate the time between the peaks
        time_between_peaks_in_ms = np.arange(0, len(peaks)-1, 1, dtype='int64')
        for i in range(len(peaks)-1):
            time_between_peaks_in_ms[i] = (self.df['Time in ms'][peaks[i+1]] - self.df['Zeit in ms'][peaks[i]])
            
        # convert the time between the peaks to minutes
        time_between_peaks_in_ms = np.array(time_between_peaks_in_ms)
        time_between_peaks = (time_between_peaks_in_ms / 1000) / 60
        
        # calculate the heart rate
        heart_rate = 1 / time_between_peaks

        # plot the heart rate (optional)
        time_ms = self.df['Time in ms'][peaks[1:]]
        time_m = time_ms / 1000 / 60
        fig = px.line(x = time_m, y = heart_rate, title='Heart Rate', labels={'x':'Time in m', 'y':'Heart Rate in bpm'})
        
        # mean heart rate
        mean_heart_rate = np.mean(heart_rate)

        return heart_rate, fig, mean_heart_rate
    
#Plot der EKG-Daten mit gefundenen Peaks
    def plot_time_series(self):
        '''A function that plots the EKG data as a time series.'''

        # create a  empty figure
        fig = go.Figure()
        
        # add the EKG data
        mV = self.df['Messwerte in mV']
        time = self.df['Zeit in ms'] / 1000 / 60
        fig.add_trace(go.Scatter(
            x=time,
            y=mV,
            mode='lines',
            name='EKG Data'
        ))
        
        # add the layout
        fig.update_layout(
            title='EKG Data',
            xaxis_title='Time in m',
            yaxis_title='EKG in mV'
        )
        return fig


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
    ekg.make_plot()
    print(ekg.find_peaks())
