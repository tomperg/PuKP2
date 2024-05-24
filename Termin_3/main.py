import streamlit as st
from read_pandas import read_my_csv, read_activity_csv, compute_HR_statistics, compute_power_statistics, make_pow_HR_plot, add_HR_zones, make_plot #,color_zones



# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df_ekg = read_my_csv()
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

    #einfügen von durchgezogenen waagrechen Linien bei verschiednen Zonen-Werten von hf_max

    fig.add_hline(y=0.5*hf_max, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.6*hf_max, line_dash="dash", line_color="red")
    fig.add_hline(y=0.7*hf_max, line_dash="dash", line_color="orange")
    fig.add_hline(y=0.8*hf_max, line_dash="dash", line_color="yellow")
    fig.add_hline(y=0.9*hf_max, line_dash="dash", line_color="green")

    #benennen von add_hlines
    fig.add_annotation(x=0, y=0.5*hf_max, text="Zone 1", showarrow=False)
    fig.add_annotation(x=0, y=0.6*hf_max, text="Zone 2", showarrow=False)
    fig.add_annotation(x=0, y=0.7*hf_max, text="Zone 3", showarrow=False)
    fig.add_annotation(x=0, y=0.8*hf_max, text="Zone 4", showarrow=False)
    fig.add_annotation(x=0, y=0.9*hf_max, text="Zone 5", showarrow=False)
    

    fig.update_layout(title="Power and Heart Rate", xaxis_title="Time", yaxis_title="Power/Heart Rate")
    #fig.update_layout(color_zones(df))
    st.plotly_chart(fig)

    st.write(f"- Maximale Herzfrequenz: {round(hf_max)}")
    st.write(f"- Durchschnittliche Herzfrequenz: {round(hf_mean)}")
    st.write(f"- Durchschnittliche Leistung: {round(p_mean)}")
    st.write(f"- Maximale Leistung: {round(p_max)}")

  

   