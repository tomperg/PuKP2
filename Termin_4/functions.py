import pandas as pd
import plotly.express as px
import numpy as np


def read_activity_csv(path="activities/activity.csv"):
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv(path)
    #TODO add 'time' column DONE
    df['time'] = [i for i in range(len(df))]
    return df

def best_effort(df, t_interval, fs =1):
    windowsize = t_interval * fs
    meanpower = df["PowerOriginal"].rolling(window = windowsize).mean()
    bestpower = meanpower.max()

    return bestpower

 
def our_power_curve(df, fs = 1):
    intervall = np.array(range(len(df))) / fs
    powercurve = []
    
    for i in intervall:
        i = int(i)
        powercurve.append(best_effort(df, i, fs))
    

    df_powercurve = pd.DataFrame({"Powercurve": powercurve, "Intervall": intervall/60})
    return df_powercurve

if __name__ == "__main__":
    df = read_activity_csv()
    #print(find_best_effort(df, 30))
    #print(df.head())
    print(our_power_curve(df, 2))


    #plotten
    time_intervals = [1, 5, 10, 30, 60, 300, 600, 1800, 3600]
    fig = px.line(our_power_curve(df, 1), x= "Intervall", y="Powercurve", log_x=True, title='Logarithmische Skala auf der X-Achse')
    layout = fig.update_layout(title="Powercurve", xaxis_title="Intervall in Minuten", yaxis_title="Power in Watt")
   

    fig.show()