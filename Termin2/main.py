import streamlit as st
from read_data import get_person_data, get_person_names, find_person_data_by_name
from PIL import Image


person_data = get_person_data()
person_names_list = get_person_names(person_data)
print(person_names_list)

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")
if "current-user" not in st.session_state:
    st.session_state.current_user ="None"

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names_list, key="sbVersuchsperson")

st.write(st.session_state.current_user,"wird zurzeit gewählt")
current_user_list = find_person_data_by_name(st.session_state.current_user) 



# Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'



# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names_list:
    image = Image.open(current_user_list["picture_path"])
# Anzeigen eines Bilds mit Caption
    st.image(image, caption=st.session_state.current_user)