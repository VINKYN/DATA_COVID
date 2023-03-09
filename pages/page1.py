import pandas
import streamlit as st
import reportingFonction as rF
import plotly.express as px
import plotly.figure_factory as ff
col1, col2= st.columns(2)

with st.container():
    with col1:
        total1 = rF.count_Collection("ClinicalTrials_ObsStudies")
        total2 = rF.count_Collection("ClinicalTrials_RandTrials")
        st.header("Nombre d'essai : "+str(total1+total2))
        st.subheader("ObsStudies : "+str(total1))
        st.subheader("RandTrials : "+str(total2))

    with col2:
        total3 = rF.count_Collection("Publications_ObsStudies")
        total4 = rF.count_Collection("Publications_RandTrials")
        st.header("Nombre d'essai : "+str(total3 + total4))
        st.subheader("ObsStudies : "+str(total3))
        st.subheader("RandTrials : "+str(total4))

nbListe = [total1,total2,total3,total4]
nomListe = ["ClinicalTrials_ObsStudies","ClinicalTrials_RandTrials","Publications_ObsStudies","Publications_RandTrials"]

dataNb = pandas.DataFrame(nbListe,nomListe)
st.write(dataNb)
fig = px.pie(dataNb)
st.plotly_chart(fig)

with st.container():
    data = rF.nb_par_Mois("ClinicalTrials_ObsStudies")
    d = pandas.DataFrame(data)
    count = []
    boup = []
    for i in range(len(d)):
        count.append((d['count'][i]))
        boup.append(d['_id'][i])
    final = []
    for j in range(len(boup)):
        a = boup[j].get('mois')
        b = boup[j].get('annee')
        date = str(a)+'/'+str(b)
        final.append(date)
    data = pandas.DataFrame({'date':final,'nb':count})
    g = data.set_index('date')
    st.area_chart(g)