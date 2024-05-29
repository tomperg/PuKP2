import pandas as pd
import numpy as np

def read_activity_csv(path="activities/activity.csv"):

    df = pd.read_csv(path)
    df['time'] = [i for i in range(len(df))]
    return df

def best_effort(df, t_interval, fs=1):
    """
    Berechnet die beste durchschnittliche Leistung über ein gegebenes Zeitintervall.
    
    Args:
        df (pd.DataFrame): Das DataFrame mit den Leistungsdaten.
        t_interval (int): Das Zeitintervall in Sekunden.
        fs (int): Die Abtastrate in Hz.
    
    Returns:
        float: Die beste durchschnittliche Leistung.
    """
    windowsize = t_interval * fs
    meanpower = df["PowerOriginal"].rolling(window=windowsize).mean()
    bestpower = meanpower.max()
    return bestpower

def our_power_curve(df, fs=1):
    """
    Berechnet die Power Curve aus den Leistungsdaten.
    
    Args:
        df (pd.DataFrame): Das DataFrame mit den Leistungsdaten.
        fs (int): Die Abtastrate in Hz.
    
    Returns:
        pd.DataFrame: Ein DataFrame mit der Power Curve.
    """
    intervall = np.array(range(len(df))) / fs
    powercurve = [best_effort(df, int(i), fs) for i in intervall]
    df_powercurve = pd.DataFrame({"Powercurve": powercurve, "Intervall": intervall / 60})
    return df_powercurve

import pandas as pd
import plotly.express as px
from function import read_activity_csv, our_power_curve
# Plotten der Power Curve
    fig = px.line(df_powercurve, x="Intervall", y="Powercurve", log_x=True, title='Logarithmische Skala auf der X-Achse')
    fig.update_layout(title="Powercurve", xaxis_title="Intervall in Minuten", yaxis_title="Power in Watt")
    fig.show()
if _name_ == "_main_":
    df = read_activity_csv()

    # Berechnung der Power Curve
    df_powercurve = our_power_curve(df, fs=2)
    print(df_powercurve)

    # Plotten der Power Curve
    fig = px.line(df_powercurve, x="Intervall", y="Powercurve", log_x=True, title='Logarithmische Skala auf der X-Achse')
    fig.update_layout(title="Powercurve", xaxis_title="Intervall in Minuten", yaxis_title="Power in Watt")
    fig.show()