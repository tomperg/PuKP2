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

    fig.add_hline(y=0.5*hf_max, line_dash="dash", line_color="Light Yellow")
    fig.add_hline(y=0.6*hf_max, line_dash="dash", line_color="LightGreen")
    fig.add_hline(y=0.7*hf_max, line_dash="dash", line_color="Green")
    fig.add_hline(y=0.8*hf_max, line_dash="dash", line_color="Yellow")
    fig.add_hline(y=0.9*hf_max, line_dash="dash", line_color="Red")

    #trying to color the zones:

    fig.add_hrect(y0=0, y1=0.6*hf_max, fillcolor="LightYellow", opacity=0.5, line_width=0)
    fig.add_hrect(y0=0.6*hf_max, y1=0.7*hf_max, fillcolor="LightGreen", opacity=0.5, line_width=0)
    fig.add_hrect(y0=0.7*hf_max, y1=0.8*hf_max, fillcolor="Green", opacity=0.5, line_width=0)
    fig.add_hrect(y0=0.8*hf_max, y1=0.9*hf_max, fillcolor="Yellow", opacity=0.5, line_width=0)
    fig.add_hrect(y0=0.9*hf_max, y1=hf_max, fillcolor="Red", opacity=0.5, line_width=0)

    #benennen von add_hlines
    fig.add_annotation(x=0, y=0.5*hf_max, text="Start Zone 1", showarrow=False)
    fig.add_annotation(x=0, y=0.6*hf_max, text="Start Zone 2", showarrow=False)
    fig.add_annotation(x=0, y=0.7*hf_max, text="Start Zone 3", showarrow=False)
    fig.add_annotation(x=0, y=0.8*hf_max, text="Start Zone 4", showarrow=False)
    fig.add_annotation(x=0, y=0.9*hf_max, text="Start Zone 5", showarrow=False)
    

    fig.update_layout(title="Power and Heart Rate", xaxis_title="Time", yaxis_title="Power/Heart Rate")
    #fig.update_layout(color_zones(df))
    st.plotly_chart(fig)

    st.write(f"- Maximale Herzfrequenz: {round(hf_max)}")
    st.write(f"- Durchschnittliche Herzfrequenz: {round(hf_mean)}")
    st.write(f"- Durchschnittliche Leistung: {round(p_mean)}")
    st.write(f"- Maximale Leistung: {round(p_max)}")

  

   