import streamlit as st
import read_person_data
import ekgdata
import datetime as dt
import matplotlib.pyplot as plt
from Person import Person 
from ekgdata import EKGdata


#%% Zu Beginn
#Lass den nutzer eine Versuchsperson auswählen und speicher diese als aktuelle Versuchsperson
# Lade die Daten der Versuchsperson


# Lade alle Personen
person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

## TODO: Session State für Pfad zu EKG Daten 
if 'ekg_data_path' not in st.session_state:
    st.session_state.ekg_data_path = 'data/ekg_data/01_Ruhe_short.txt'
#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

# Name der Versuchsperson
st.write("Der Name ist: ", st.session_state.aktuelle_versuchsperson) 

# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen
st.write("Geburtsdatum: ", read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["date_of_birth"])
st.write("Alter: ", Person.calc_age(st.session_state.aktuelle_versuchsperson))
st.write("Die maximale Herzfrequenz von", st.session_state.aktuelle_versuchsperson ,"ist: ", Person.calc_max_heart_rate(st.session_state.aktuelle_versuchsperson))
# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["picture_path"]
    # st.write("Der Pfad ist: ", st.session_state.picture_path) 

#%% Bild anzeigen

from PIL import Image
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Person



#%% EKG-Daten als Matplotlib Plot anzeigen
current_ekg_data = ekgdata.EKGdata(st.session_state.ekg_data_path)
# Erstelle den Plot
fig = current_ekg_data.plot_time_series()

# Zeige den Plot an
st.plotly_chart(fig)
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes

# Zeige den Plot an
plt.plot(current_ekg_data.df["Zeit in ms"], current_ekg_data.df["Messwerte in mV"])


# %% Herzrate bestimmen
# Schätze die Herzrate 
# Zeige die Herzrate an
st.write("Herzrate ist: ", current_ekg_data.estimate_heartrate, " Schläge pro Minute") 
