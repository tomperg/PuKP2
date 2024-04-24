import streamlit as st

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
current_user = st.selectbox(
    'Versuchsperson',
    options = ["Nutzer1", "Nutzer2"], key="sbVersuchsperson")
st.write("Der Name ist: ", st.session_state.current_user)

import read_data # Ergänzen Ihr eigenes Modul

# Legen Sie eine neue Liste mit den Personennamen an indem Sie ihre 
# Funktionen aufrufen
person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)
# bzw: wenn Sie nicht zwei separate Funktionen haben
# person_names = read_data.get_person_list()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")