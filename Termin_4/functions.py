import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.signal import find_peaks

def read_my_csv(): #TODO change path to EKG data
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in Watt", "Zeit in Sekunden"]
    
    # Gibt den geladen Dataframe zurück
    return df


  

def find_peaks_ekg(df):
    #TODO implement peak detection
    find_peaks(df['Messwerte in Watt'], height=0.5, distance=100)
    return df


    




def read_activity_csv(path="activities/activity.csv"):
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv(path)
    #TODO add 'time' column DONE
    df['time'] = [i for i in range(len(df))]
    return df

