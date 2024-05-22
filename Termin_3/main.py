import streamlit as st
from read_pandas import read_my_csv, read_activity_csv, compute_HR_statistics, compute_power_statistics, make_pow_HR_plot, add_HR_zones, make_plot

path = "data/ekg_data/01_Ruhe.txt"

# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df_ekg = read_my_csv(path)
    fig_ekg = make_plot(df_ekg)

    st.plotly_chart(fig_ekg)

with tab2:
    st.header("Power-Data")
    
    df = read_activity_csv(path="data/activities/activity.csv")
    hf_max, hf_mean = compute_HR_statistics(df)
    p_mean, p_max = compute_power_statistics(df)
    df = add_HR_zones(df, hf_max)

    #TODO Färbe die verschiedenen Zonen aus add_HR_zones ein
    
    fig = make_pow_HR_plot(df)
    st.plotly_chart(fig)

    st.write(f"- Maximale Herzfrequenz: {round(hf_max)}")
    st.write(f"- Durchschnittliche Herzfrequenz: {round(hf_mean)}")
    st.write(f"- Durchschnittliche Leistung: {round(p_mean)}")
    st.write(f"- Maximale Leistung: {round(p_max)}")

  

   