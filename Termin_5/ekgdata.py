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
        self.df_ekg = pd.read_csv(self.data, sep='\t', header=None, names=['Amplitude in [mV]','Time in ms',])


    def make_plot(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        return self.fig
#Instanziiert einen EKG-Test anhand der ID und der Datenbank
    def load_by_id(PersonID, EKGID = "None"):
        '''A function that loads the EKG Data by id and returns the Data as a dictionary.'''

        # load the person data
        file = open("person_db.json")
        person_data = json.load(file)

        # get the ekg data
        if PersonID  == "None":
            return None
        
        if EKGID == "None":
            for eintrag in person_data:
                if eintrag["id"] == PersonID:
                    return eintrag["ekg_tests"]
            else:
                return {}
            
        for eintrag in person_data:
            if eintrag["id"] == PersonID:
                for ekg_test in eintrag["ekg_tests"]:
                    if ekg_test["id"] == EKGID:  
                        return ekg_test
        else:
            return {}
        
#Funktion um die Peaks zu finden
    def find_peaks(self):        
        # erstelle eine liste mit den Daten
        np_array = self.df_ekg["Amplitude in [mV]"].values

        # Liste peaks, die den index der peaks speichern
        peaks = []

        # erstellt einen laufindex vom 1. bis zum
        # vor-letzten element der liste
        for index in range(1,len(np_array)-1):
            #print("index ist:", index)
            #print("wert ist:", np_array[index])
            vorgaenger = np_array[index-1]
            nachfolger = np_array[index+1]
            kandidat = np_array[index]

            #  vergleiche die drei Werte
            # wenn Kadidat höher als beide anderen

            if kandidat > nachfolger and kandidat >vorgaenger:
                # dann füge es einer liste hinzu
                peaks.append(index)
        # Erstelle Dataframe

        self.df_peaks = pd.DataFrame(peaks, columns=["Indizes"])
        return peaks
#Funktion um die Herzfrequenz zu schätzen anhand der Peaks und der Zeit zwischen den Peaks
    def estimate_heartrate(self):
        peaks = self.find_peaks()
        time_between_peaks = np.diff(peaks)
        heart_rate = sum(1 / time_between_peaks)
        return heart_rate, time_between_peaks
   
    
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
    
    print("Hr: ", ekg.estimate_heartrate())
