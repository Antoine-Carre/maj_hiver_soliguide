import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta
import datetime
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

@st.cache(allow_output_mutation=True)
def load_df(url):
    df = pd.read_csv(url)
    return df

# option
st.set_page_config(page_title="Soliguide - Mise à jour hiver 2021-2022",
                   page_icon="https://pbs.twimg.com/profile_images/1321098074765361153/F4UFTeix.png",
                   initial_sidebar_state="expanded",
                   layout="wide",)


#############
## sidebar ##
############# 
st.sidebar.image("https://soliguide.fr/assets/images/logo.png", use_column_width=True)
st.sidebar.title('Soliguide 2021')
st.sidebar.subheader('❄️ Mise à jour hiver ❄️')

categorie = st.sidebar.selectbox("Choisissez votre territoire :", ("France", "Alpes-Maritimes (06)",
                                            "Ardèche (07)","Bouche-du-Rhône (13)","Cantal (15)",
                                            "Drôme (26)", "Gironde (33)","Hérault (34)",
                                            "Indre (36)", "Loire-Atlantique (44)", "Puy-de-Dôme (63)",
                                            "Bas-Rhin (67)", "Paris (75)", "Seine-Maritime (76)","Seine-et-Marne (77)",
                                            "Yvelines (78)","Essonne (91)", "Hauts-de-Seine (92)",
                                            "Seine-Saint-Denis (93)","Val-de-Marne (94)",
                                            "Val-d'Oise (95)"))

categorie_2 = st.sidebar.radio("Sections", ("Mails", "Structures",
                                            "Organisations", 'Les comptes pro'))


##########
## DATA ##
##########

# modifier selon la localisation de la BD
mails = './pilotage màj hiver 2021/df_mails_data.csv'
fiches = './pilotage màj hiver 2021/df_fiches_data.csv'
orga = './pilotage màj hiver 2021/df_orga_data.csv'
cpe_pro = './pilotage màj hiver 2021/df_cpte_pro_data.csv'
fiche_cpte_pro = './pilotage màj hiver 2021/df_fiche_with_cpte_pro_data.csv'
fiche_cpte_pro_valide = './pilotage màj hiver 2021/df_cpte_pro_valide_data.csv'

df_mails = load_df(mails)
df_mails = df_mails.fillna(0)
df_mails.set_index('territory', inplace=True)

df_fiches = load_df(fiches)
df_fiches_màj = df_fiches

df_orga = load_df(orga)

df_cpe_pro = load_df(cpe_pro)

df_fiche_cpe_pro = load_df(fiche_cpte_pro)

df_fiche_cpte_pro_valide = load_df(fiche_cpte_pro_valide)



cat_dict = {"France":'Total', "Alpes-Maritimes (06)" :"06", "Ardèche (07)":"07",
            "Bouche-du-Rhône (13)": "13","Cantal (15)":"15", "Drôme (26)":"26",
            "Gironde (33)":"33","Hérault (34)":"34","Indre (36)":"36",
            "Loire-Atlantique (44)" : "44", "Puy-de-Dôme (63)":"63",
            "Bas-Rhin (67)":"67", "Paris (75)" : "75", "Seine-Maritime (76)":"76",
            "Seine-et-Marne (77)":'77', "Yvelines (78)":"78", "Essonne (91)" :"91", 
            "Hauts-de-Seine (92)":"92","Seine-Saint-Denis (93)": "93","Val-de-Marne (94)": "94", 
            "Val-d'Oise (95)":"95"}


            
################
## MAILS PAGE ##
################

if categorie_2 == 'Mails':
    st.title('Les Mails')


    col1, col2, col3 = st.columns(3)

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'emails envoyés'])}</font>
    <br/><font size='3'>emails envoyés<br></font></center>
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Relance envoyées'])}</font>
    <br/><font size='3'>dont emails de relance envoyés<br></font></center>
    """

    html_string_3 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Mails rejetés'])}</font>
    <br/><font size='3'>emails rejetés<br></font></center>
    """

    col1.markdown(html_string_1, unsafe_allow_html=True)

    col2.markdown(html_string_2, unsafe_allow_html=True)
 
    col3.markdown(html_string_3, unsafe_allow_html=True)


    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
    st.markdown(html_string, unsafe_allow_html=True)



    col1, col2, col3 = st.columns(3)

    html_string_4 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Mails ouverts'])}</font>
    <br/><font size='3'>emails ouverts<br></font></center>
    """
    

    html_string_5 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Mails cliqués'])}</font>
    <br/><font size='3'>emails cliqués<br></font></center>
    """

    html_string_6 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Rappels demandées'])}</font>
    <br/><font size='3'>demandes de rappels effectuées<br></font></center>
    """
    
    col1.markdown(html_string_4, unsafe_allow_html=True)

    col2.markdown(html_string_5, unsafe_allow_html=True)

    col3.markdown(html_string_6, unsafe_allow_html=True)
    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
    st.markdown(html_string, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    html_string_7 = f"""<br>
    <center><font face='Helvetica' size='7'>{int(df_mails.loc[{(cat_dict[categorie])},'Mails répondus'])}</font>
    <br/><font size='3'>nombre de retours par e-mail
    <br></font></center>

    """
       
    col1.markdown(html_string_7, unsafe_allow_html=True)


#####################
## STRUCTURES PAGE ##
#####################

if categorie_2 == 'Structures':
    st.title('Les Structures')

    if categorie == "France":
        df_fiches_màj = df_fiches_màj
    else:
        df_fiches_màj = df_fiches_màj[df_fiches_màj.territory == int(cat_dict[categorie])]

    # #### Combien de fiches ont été mises à jour totalement ?
    df_fiches_màj_vf = df_fiches_màj[['territory','sections.closed.updated','sections.hours.updated','sections.services.updated','sections.tempMessage.updated']]
    df_fiches_màj_vf.replace({True:1, False:0}, inplace=True)
    df_fiches_màj_vf['A jour'] = df_fiches_màj_vf[['sections.closed.updated','sections.hours.updated','sections.services.updated','sections.tempMessage.updated']].sum(axis=1)
    df_fiches_màj_pie = df_fiches_màj_vf['A jour'].map(lambda x: 'Fiches totalement à jour' if x == 4 else ('Fiches partiellement à jour' if x == 3 else ('Fiches partiellement à jour' if x == 2 else ('Fiches partiellement à jour' if x == 1 else x== 'à mettre à jour'))))
    df_fiches_màj_pie.replace({False : "Fiches à mettre à jour"}, inplace=True)
    df_fiches_màj_pie = pd.DataFrame(df_fiches_màj_pie.value_counts())

    st.markdown('### Combien de fiches ont été mises à jour totalement ?')

    if df_fiches_màj_pie['A jour'].empty:
        st.markdown("#### Il y a actuellement aucune fiche en ligne sur ce territoire")
    else:
        fig = px.pie(values=df_fiches_màj_pie['A jour'], names=df_fiches_màj_pie.index, color_discrete_sequence= [ '#7201a8', '#d8576b'],)
        fig.update_traces(textinfo="percent+label")
        fig.update_traces(hovertemplate = "%{label}: <br>Nbre de fiches: %{value}")

        st.plotly_chart(fig, use_container_width=True)


        # Qu'est-ce qui est mis à jour ? Qu'est-ce qui ne l'est pas ?

        # Fiches à jour
        df_fiches_màj['A jour'] = df_fiches_màj_vf[['sections.closed.updated','sections.hours.updated','sections.services.updated','sections.tempMessage.updated']].sum(axis=1)

        df_fiches_màj_final = df_fiches_màj[['sections.tempMessage.date','A jour']]
        df_fiches_màj_final['date'] =  pd.to_datetime(df_fiches_màj_final['sections.tempMessage.date'])
        df_fiches_màj_final['date'] = df_fiches_màj_final['date'].dt.strftime('%Y-%m-%d')

        df_fiches_màj_final['A jour'].replace({4:'A jour', 0:'A mettre à jour', 1:'A mettre à jour', 2:'A mettre à jour', 3:'A mettre à jour'}, inplace=True)

        table = pd.pivot_table(df_fiches_màj_final, values='A jour', index=['date'], columns=['A jour'], aggfunc=np.count_nonzero)

        st.markdown("### Qu'est-ce qui est mis à jour ? Qu'est-ce qui ne l'est pas ?")

        if table.index.empty:
            st.markdown("#### Il y a actuellement aucune fiche à jour sur ce territoire")
        else:    
            table["Fiches actualisées"] = table['A jour'].cumsum()
            table['Fiches à mettre à jour'] = df_fiches_màj.lieu_id.count() - table['Fiches actualisées']
            table.reset_index(inplace=True)
        
        # Nbre de fiches màj par jour
            
            fig_2 = px.bar(table, x="date", y=["Fiches actualisées", "Fiches à mettre à jour"], color_discrete_sequence= [ '#7201a8', '#d8576b']) 
            fig_2.update_traces(hovertemplate = "Date du dernier relevé des mises à jour : le %{x}<br>Nbre de fiches: %{value}")
            fig_2.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de fiches",)          
            
            dt_all = pd.date_range(start=table['date'].iloc[0],end=table['date'].iloc[-1])
            dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(table['date'])]
            dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

            fig_2.update_xaxes(rangebreaks=[dict(values=dt_breaks)])


            st.plotly_chart(fig_2, use_container_width=True)

            # Qui a fait la màj ?rangebreaks=[dict(values=dt_breaks)]

            df_history_campaign_users_final = df_fiches_màj[['status','created_at','territory']]
            
            df_history_campaign_users_final.replace({"status":{'ADMIN_SOLIGUIDE':"l'équipe Soliguide","PRO":"les acteurs"}}, inplace=True)

            table_2 = pd.pivot_table(df_history_campaign_users_final, values='status', index=['created_at'], columns=['status'], aggfunc=np.count_nonzero)

            table_2.reset_index(inplace=True)

            table_2.fillna(0, inplace=True)

            if not "l'équipe Soliguide" in list(table_2.columns):
                fig3 = px.bar(table_2, x="created_at", y=["les acteurs"], color_discrete_sequence= ['#3E3A71', '#2896A0'], title="Nombre de fiches mise à jour par jour et status") 
            elif not "les acteurs" in list(table_2.columns):
                fig3 = px.bar(table_2, x="created_at", y=["l'équipe Soliguide"], color_discrete_sequence= ['#3E3A71', '#2896A0'], title="Nombre de fiches mise à jour par jour et status") 
            else:
                fig3 = px.bar(table_2, x="created_at", y=["l'équipe Soliguide", "les acteurs"], color_discrete_sequence= ['#3E3A71', '#2896A0'], title="Nombre de fiches mise à jour par jour et status") 

            fig3.update_traces(hovertemplate = "Date de la mise à jour : le %{x}<br>Nbre de fiches: %{value}")
            fig3.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de fiches",)
                     
            dt_all = pd.date_range(start=table_2['created_at'].iloc[0],end=table_2['created_at'].iloc[-1])
            dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(table_2['created_at'])]
            dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

            fig3.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

            tabs = pd.DataFrame(df_history_campaign_users_final.status.value_counts())
            
            fig3bis = px.pie(values=tabs.status, names=tabs.index, color_discrete_sequence= ['#3E3A71', '#2896A0'], title="Nombre de fiches mise à jour par status")
            fig3bis.update_traces(textinfo="percent+label")
            fig3bis.update_traces(hovertemplate = "%{label}: <br>Nbre de fiches: %{value}")
                               

            st.markdown("### Qui a fait la màj ?")

            st.plotly_chart(fig3, use_container_width=True)
            
            st.plotly_chart(fig3bis, use_container_width=True)


            #Le nombre et le type de modifications dûes à la màj : fermetures (avec durée), changement des horaires, des services, pas de changement, etc.
            # Creation colonne pasDeChangement
            df_fiches_màj['pasDeChangement'] = np.where((df_fiches_màj['sections.tempMessage.updated'] == True) & (df_fiches_màj['sections.tempMessage.changes'] == False) 
                                                        & (df_fiches_màj['sections.services.updated'] == True) & (df_fiches_màj['sections.services.changes'] == False) 
                                                        & (df_fiches_màj['sections.hours.updated'] == True) & (df_fiches_màj['sections.hours.changes'] == False)
                                                        & (df_fiches_màj['sections.closed.updated'] == True) & (df_fiches_màj['sections.closed.changes'] == False),
                                                        1, 0)

            # Creation colonne changementHoraire
            df_fiches_màj['changementHoraire'] = np.where((df_fiches_màj['sections.hours.updated'] == True) & (df_fiches_màj['sections.hours.changes'] == True), 1, 0)

            # Creation colonne changementServices
            df_fiches_màj['changementServices'] = np.where((df_fiches_màj['sections.services.updated'] == True) & (df_fiches_màj['sections.services.changes'] == True), 1, 0)

            # Creation colonne fermeture
            df_fiches_màj['fermeture'] = np.where((df_fiches_màj['sections.closed.updated'] == True) & (df_fiches_màj['sections.closed.changes'] == True), 1, 0)

            df_fiches_màj['dateFin'] = pd.to_datetime(df_fiches_màj['dateFin'], errors = 'coerce',  utc=True)
            df_fiches_màj['dateFin'] = df_fiches_màj['dateFin'].dt.strftime('%Y-%m-%d')

            df_fiches_màj['dateDebut'] = pd.to_datetime(df_fiches_màj['dateDebut'],errors = 'coerce',  utc=True)
            df_fiches_màj['dateDebut'] = df_fiches_màj['dateDebut'].dt.strftime('%Y-%m-%d')

            df_fiches_màj['durée'] = (pd.to_datetime(df_fiches_màj['dateFin'], errors = 'coerce',  utc=True) - pd.to_datetime(df_fiches_màj['dateDebut'], errors = 'coerce', utc=True))

            # Creation colonne pasDeChangement
            df_fiches_màj['Fermeture_1_semaine'] = np.where((df_fiches_màj.durée >= '5 days') & (df_fiches_màj.durée <= '7 days') & (df_fiches_màj.fermeture == 1), 1, 0)
            df_fiches_màj['Fermeture_2_semaines'] = np.where((df_fiches_màj.durée > '7 days') & (df_fiches_màj.durée < '15 days')& (df_fiches_màj.fermeture == 1), 1, 0)
            df_fiches_màj['Fermeture_PLUS_de_2_semaines'] = np.where((df_fiches_màj.durée > '14 days') & (df_fiches_màj.fermeture == 1), 1, 0)
            df_fiches_màj['Fermeture_MOINS_de_1_semaine'] = np.where((df_fiches_màj.durée < '5 days') & (df_fiches_màj.fermeture == 1), 1, 0)

            df_fiches_màj_changing = df_fiches_màj[['territory','pasDeChangement','changementHoraire','changementServices','fermeture','Fermeture_MOINS_de_1_semaine',
                                                'Fermeture_1_semaine','Fermeture_2_semaines','Fermeture_PLUS_de_2_semaines']]

            df_fiches_màj_changing_total = df_fiches_màj_changing.groupby(['territory']).sum()
            df_fiches_màj_changing_total.loc["Total"] = df_fiches_màj_changing_total.sum()
            df_fiches_màj_changing_total.reset_index(inplace=True)

            fig4 = px.bar(df_fiches_màj_changing_total[df_fiches_màj_changing_total.territory == 'Total'], x="territory", y=["pasDeChangement","changementHoraire", "changementServices", 
            "Fermeture_MOINS_de_1_semaine", "Fermeture_1_semaine","Fermeture_2_semaines", "Fermeture_PLUS_de_2_semaines"],barmode='group', color_discrete_sequence=px.colors.sequential.Plasma,) 

            newnames = {"pasDeChangement" : "Aucun changement","changementHoraire":"changement d'horaire", "changementServices": 'Offre de services modifiés', 
            "Fermeture_MOINS_de_1_semaine":"Fermeture inférieure à une semaine", "Fermeture_1_semaine":"Fermeture d'une semaine","Fermeture_2_semaines" :"Fermeture de 2 semaines", 
            "Fermeture_PLUS_de_2_semaines":"Fremeture supérieur à 2 semaines"}
            fig4.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
            fig4.update_traces(hovertemplate = "Nbre de fiches: %{value}")
            fig4.update_layout(xaxis_title=f"{categorie}", yaxis_title="Nombre de fiches", legend_title="Types de modification",)
            fig4.update_xaxes(visible=True, showticklabels=False)


            st.markdown("### Le nombre et le type de modifications dûs à la màj : fermetures (avec durée), changements des horaires, changements des services, pas de changement, etc")
            st.plotly_chart(fig4, use_container_width=True)


            df_fiches_màj['update_level'] = df_fiches_màj_vf[['sections.closed.updated','sections.hours.updated','sections.services.updated','sections.tempMessage.updated']].sum(axis=1)
            df_fiches_màj['màj_incomplete'] = np.where((df_fiches_màj['update_level']> 0) & (df_fiches_màj['update_level'] < 4), 1, 0)
            formulaire_en_stand_by = pd.DataFrame(df_fiches_màj['màj_incomplete'] .value_counts())

            if formulaire_en_stand_by.count()[0] == 1:
                pass
            else:
                html_string_10 = f"""<br>
                <center><font face='Helvetica' size='7'>{formulaire_en_stand_by.loc[1,'màj_incomplete']}</font>
                <br/><font size='3'>Nombre de formulaires incomplets<br></font></center>
                """

                st.markdown(html_string_10, unsafe_allow_html=True)

#######################
## ORGANISATION PAGE ##
#######################

if categorie_2 == 'Organisations':
    st.title('Les Organisations')


    st.markdown("### Qui fait le mieux les mises à jours ?")
   
    if categorie == "France":
        df_orga = df_orga
    else:
        df_orga = df_orga[df_orga.territory == int(cat_dict[categorie])]
        
    test = df_orga[['categorie','Orga','lieu_id','PRO','updated']]
    
    test = test.join(pd.get_dummies(test.updated))
    
    if not 'Fiches à jour' in test.columns:
        st.markdown("Aucune fiche n'a été mise à jour pour le moment")
    else:
        test2 = test.groupby('categorie').agg({'Orga': 'nunique','lieu_id': 'count','Fiches à jour':'sum','PRO':'sum'})#.reset_index().rename(columns={'count':'categorieCount', 'sum':'Nombre de fiches'})
        test2['taux_de_màj'] = round((test2['PRO'] / test2['Fiches à jour'])*100, 2)
        test2 = test2.reset_index()

        test2.rename(columns={"Fiches à jour": "Nombre de fiches mises à jour", "PRO": "Nombre de fiches mises à jour par les pro"}, inplace=True)

        test2.replace({'grande organisation':'grande organisation (+ de 5 fiches)', 
                   'organisation moyenne':'organisation moyenne (de 2 à 5 fiches)',
                  'petite organisation':'petite organisation (1 fiche)'}, inplace=True)

        fig5 = px.bar(test2, x="categorie", y="taux_de_màj", custom_data=['Nombre de fiches mises à jour'], hover_data=['Nombre de fiches mises à jour par les pro'], color='categorie', color_discrete_sequence=px.colors.sequential.Plasma_r,) 
        fig5.update_traces(hovertemplate = "<b>%{x}</b><br><br>Taux de mise à jour par les pros: <b>%{y}%</b><br>Nombre de fiches à jour liées à une %{x}:  %{customdata[0]}<br>Nombre de fiches mises à jour par les pro:  %{customdata[1]}<br>")

        fig5.update_layout(xaxis_title=f"{categorie}", yaxis_title="Pourcentage des structures à jour", legend_title="Types d'organisation",)
        fig5.update_xaxes(visible=True, )


        st.plotly_chart(fig5, use_container_width=True)


#####################
## COMPTE PRO PAGE ##
#####################

if categorie_2 == 'Les comptes pro':
    st.title('Les Comptes Professionnels')

    st.markdown("### Combien de comptes pro invités depuis le début de la mise à jour hiver ?")

    new_header = df_cpe_pro.iloc[0] #grab the first row for the header
    df_cpe_pro = df_cpe_pro[1:] #take the data less the header row
    df_cpe_pro.columns = new_header #set the header row as the df header
    df_cpe_pro.rename(columns={ df_cpe_pro.columns[1]: "createdAt" }, inplace = True)
    df_cpe_pro.rename(columns={ df_cpe_pro.columns[-1]: "Total" }, inplace = True)


    if categorie == "France":
       
        fig = go.Figure(data=[
            go.Bar(x=df_cpe_pro['createdAt'], y=df_cpe_pro["Total"]),
        ])

        fig.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de compte pro",)
        fig.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")

        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
        
        
        st.plotly_chart(fig, use_container_width=True)

    elif float(cat_dict[categorie]) in df_cpe_pro.columns:
        df_cpe_pro = df_cpe_pro[['createdAt',float(cat_dict[categorie])]]
        df_cpe_pro.dropna(inplace=True)
  
        figCompteProTerritoire = go.Figure(data=[
            go.Bar(x=df_cpe_pro['createdAt'], y=df_cpe_pro[float(cat_dict[categorie])]),
        ])

        figCompteProTerritoire.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de compte pro",)
        figCompteProTerritoire.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")

        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figCompteProTerritoire.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
        
        
        st.plotly_chart(figCompteProTerritoire, use_container_width=True)

    else:
        st.markdown("#### Aucun compte pro a été invité depuis le début de la mise à jour")
        
    st.markdown('## Veuillez cliquer sur le bandeau, ci-dessous, pour afficher les comptes pro invités en cumulé :')
    expander = st.expander("Comptes pro invités cumulés")
    expander.write(f'Voici les comptes pro invités cumulés en {categorie} : ')

    if categorie == "France":
        figComptePro = px.bar(df_cpe_pro, x='createdAt', y=df_cpe_pro.Total.fillna(method="ffill").cumsum())

        figComptePro.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figComptePro.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)
      
        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figComptePro.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

        expander.plotly_chart(figComptePro, use_container_width=True)
        
    elif float(cat_dict[categorie]) in df_cpe_pro.columns:

        df_cpe_pro_cum = pd.merge(df_cpe_pro.createdAt,df_cpe_pro[int(cat_dict[categorie])].cumsum(), left_index=True, right_index=True)

        figCompteProCum = px.bar(df_cpe_pro_cum, x='createdAt', y=float(cat_dict[categorie]))

        figCompteProCum.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figCompteProCum.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)

        dt_all = pd.date_range(start=df_cpe_pro_cum['createdAt'].iloc[0],end=df_cpe_pro_cum['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro_cum['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figCompteProCum.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
            

        expander.plotly_chart(figCompteProCum, use_container_width=True)

    else:
        expander.markdown("#### Aucun compte pro a été invités depuis le début de la mise à jour")      
        
######
    st.markdown("### Combien de comptes pro invités ont créé leur compte depuis le début de la mise à jour ?")

    new_header = df_fiche_cpte_pro_valide.iloc[0] #grab the first row for the header
    df_cpe_pro = df_fiche_cpte_pro_valide[1:] #take the data less the header row
    df_cpe_pro.columns = new_header #set the header row as the df header
    df_cpe_pro.rename(columns={ df_cpe_pro.columns[1]: "createdAt" }, inplace = True)
    df_cpe_pro.rename(columns={ df_cpe_pro.columns[-1]: "Total" }, inplace = True)


    if categorie == "France":
        figComptePro = px.bar(df_cpe_pro, x='createdAt', y=df_cpe_pro.Total, color_discrete_sequence= [ '#7201a8'])

        figComptePro.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figComptePro.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)

        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figComptePro.update_xaxes(rangebreaks=[dict(values=dt_breaks)])  
        
        st.plotly_chart(figComptePro, use_container_width=True)

    elif float(cat_dict[categorie]) in df_cpe_pro.columns:
        figComptePro = px.bar(df_cpe_pro, x='createdAt', y=float(cat_dict[categorie]), color_discrete_sequence= [ '#7201a8'])

        figComptePro.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figComptePro.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)

        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figComptePro.update_xaxes(rangebreaks=[dict(values=dt_breaks)])  
                
        st.plotly_chart(figComptePro, use_container_width=True)

    else:
        st.markdown("#### Aucun compte pro a été invité depuis le début de la mise à jour")
        
    st.markdown('## Veuillez cliquer sur le bandeau, ci-dessous, pour afficher les comptes pro invités qui ont créé leur compte, en cumulé :')
    expander = st.expander("Comptes pro invités qui ont créé leur compte cumulés")
    expander.write(f'Voici les comptes pro invités qui ont créé leur compte, en cumulés, en {categorie} : ')

    if categorie == "France":
        figComptePro = px.bar(df_cpe_pro, x='createdAt', y=df_cpe_pro.Total.fillna(method="ffill").cumsum(),  color_discrete_sequence= [ '#7201a8'])

        figComptePro.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figComptePro.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)
        
        dt_all = pd.date_range(start=df_cpe_pro['createdAt'].iloc[0],end=df_cpe_pro['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figComptePro.update_xaxes(rangebreaks=[dict(values=dt_breaks)])  
        
        expander.plotly_chart(figComptePro, use_container_width=True)
        
    elif float(cat_dict[categorie]) in df_cpe_pro.columns:

        df_cpe_pro_cum = pd.merge(df_cpe_pro.createdAt,df_cpe_pro[int(cat_dict[categorie])].cumsum(), left_index=True, right_index=True)

        figCompteProCum = px.bar(df_cpe_pro_cum, x='createdAt', y=float(cat_dict[categorie]), color_discrete_sequence= [ '#7201a8'])

        figCompteProCum.update_traces(hovertemplate = "Date d'invitation des comptes pro : le %{x}<br>Nbre de comptes: %{value}")
        figCompteProCum.update_layout(xaxis=dict(tickformat="%d %B %Y"), xaxis_title="", yaxis_title="Nombre de comptes",)

        dt_all = pd.date_range(start=df_cpe_pro_cum['createdAt'].iloc[0],end=df_cpe_pro_cum['createdAt'].iloc[-1])
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df_cpe_pro_cum['createdAt'])]
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

        figCompteProCum.update_xaxes(rangebreaks=[dict(values=dt_breaks)])  
        

        expander.plotly_chart(figCompteProCum, use_container_width=True)

    else:
        expander.markdown("#### Aucun compte pro a été invités depuis le début de la mise à jour")             
#####

    if categorie != 'Ardèche (07)' and categorie != 'Drôme (26)' and categorie != 'Hérault (34)' and categorie != 'Indre (36)' and categorie != 'Puy-de-Dôme (63)' and categorie != 'Saine-Maritime (76)' :

        st.markdown("### Combien de fiches sont reliées aux comptes pro ?")

        df_fiches_reliées_2 = df_fiche_cpe_pro.copy()

        if categorie == "France":
            df_fiches_reliées_2 = df_fiches_reliées_2
        else:
            df_fiches_reliées_2 = df_fiches_reliées_2[df_fiches_reliées_2.territory == int(cat_dict[categorie])]

        df_fiches_reliées_2.replace({'Niveau de validation des comptes':{ 0 : "Fiches dont le.s compte.s lié.s n'ont pas répondu à l'invitation", 1 : "Fiches dont au moins un compte lié est actif", 2 : "Fiches dont le.s compte.s lié.s n'a.ont pas confirmé.s son.leur invitation.s", 3:"Fiches sans compte lié"} }, inplace=True)

        test = pd.DataFrame(df_fiches_reliées_2['Niveau de validation des comptes'].value_counts()).rename_axis('Status').reset_index()

        fig6 = px.pie(values=test['Niveau de validation des comptes'], names=test.Status, title='Répartition des fiches par statut des comptes liés')
        fig6.update_traces(textinfo="percent", textposition='inside', textfont_size=18,)
        fig6.update_traces(hovertemplate = "%{label}: <br>Nbre de fiches: %{value}")
        fig6.update_layout(legend = dict(font = dict(family = "arial", size = 16)), legend_title="", )
        fig6.update_layout(font=dict(
            family="arial",
            size=16,))

        col1, col2 = st.columns(2)

        html_string_1 = f"""<br>
        <center><font face='Helvetica' size='7'>{((test['Niveau de validation des comptes'].sum())-(test.loc[int(str(test.index[test.Status == 'Fiches sans compte lié'].tolist())[1:-1]),'Niveau de validation des comptes']))}</font>
        <br/><font size='3'>Nombre de fiches liées à un compte pro<br></font></center>
        """

        html_string_2 = f"""<br>
        <center><font face='Helvetica' size='7'>{test['Niveau de validation des comptes'].sum()}</font>
        <br/><font size='3'>Nombre de fiches à mettre à jour<br></font></center>
        """

        col1.markdown(html_string_2, unsafe_allow_html=True)
        col2.markdown(html_string_1, unsafe_allow_html=True)



        st.plotly_chart(fig6, use_container_width=True)
