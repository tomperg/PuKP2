#read_pandas_Aufgabe_3

# Paket für Bearbeitung von Tabellen
import pandas as pd


# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px

def read_my_csv(path="data/activities/activity.csv"): #TODO change path to EKG data
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv(path, sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV", "Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

def read_activity_csv(path="data/activities/activity.csv"):
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv(path)

    #TODO add 'time' column
    # df['time'] = ...

    # Gibt den geladen Dataframe zurück
    return df


def compute_power_statistics(df):
    # compute mean and max

    return p_mean, p_max


def make_pow_HR_plot(df):

    #fig = px.line ... x='time', y=['HR', 'Pow']


    return fig


def add_HR_zones(df, hf_max):

    df['zone_1'] = df['HeartRate'] > zone_1_min and  df['HeartRate'] < zone_2_min

    return df


def compute_time_in_zones(df):

    t_1 = df['zone_1'].sum()

    return t_1, t_2 .....


def compute_power_in_zones(df):


    p_1 = df['PowerOriginal'].mean() where zone_1

    return p_1, p_2 ....


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig


if __name__ == '__main__':
    # Test all blocks
    df = read_activity_csv()
    print(df.head())
    
