import streamlit as st
import pandas as pd
import pydeck as pdk

st.image('Portada.png', use_column_width=True)

st.subheader('', divider='blue')

st.markdown("<h2 style='text-align: center; color:#4682B4; font-size:24px; '>Cifras Poblacionales Proyectadas 2023 y PIB 2020</h2>", unsafe_allow_html=True)

st.subheader('', divider='blue')

st.sidebar.info('Seleccione la Provincia sobre la cual quiere enfatizar, la variable a visualizar y el tipo de mapa que desea visualizar:', icon="ℹ️")

add_selectbox = st.sidebar.selectbox(
"Provincia",
("Todas", "San José", "Alajuela", "Heredia", "Cartago", "Puntarenas", "Guanacaste", "Limón"))

add_selectbox_2 = st.sidebar.selectbox(
"Variable a Visualizar",
("PIB", "PIB per cápita", "Población", "Superficie"))

add_selectbox_1 = st.sidebar.selectbox(
"Tipo de Mapa",
("dark", "light", "road"))

df_cantones = pd.read_excel('Cantones_Listado.xlsx')

if add_selectbox_2 == "PIB":
    var_1 = 'PIB_mill'
    dim_1 = 0.013
    color_1 = df_cantones['PIB_mill'].max()
if add_selectbox_2 == "PIB per cápita":
    var_1 = 'PIB_per_cápita'
    dim_1 = 3000
    color_1 = df_cantones['PIB_per_cápita'].max()
if add_selectbox_2 == "Población":
    var_1 = 'Población'
    dim_1 = 0.15
    color_1 = df_cantones['Población'].max()
if add_selectbox_2 == "Superficie":
    var_1 = 'Superficie_km2'
    dim_1 = 25
    color_1 = df_cantones['Superficie_km2'].max()

if add_selectbox == 'Todas':
    df_cantones = df_cantones
else:
    df_cantones = df_cantones.loc[df_cantones['Provincia'] == add_selectbox]


df_cantones['PIB_mill_1'] = df_cantones['PIB_mill'].apply(lambda x: '{:,.0f}'.format(x).replace(',', '.'))
df_cantones['Poblacion_1'] = df_cantones['Población'].apply(lambda x: '{:,.0f}'.format(x).replace(',', '.'))
df_cantones['Superficie_1'] = df_cantones['Superficie_km2'].apply(lambda x: '{:,.0f}'.format(x).replace(',', '.'))


st.pydeck_chart(pdk.Deck(
    map_style=add_selectbox_1,
    initial_view_state=pdk.ViewState(
        longitude=-84.00,
        latitude=9.8,
        zoom=7,
        max_zoom=10,
        min_zoom=7,
        pitch=50,
        bearing=20,
    ),

    layers=[
        pdk.Layer(
            'ColumnLayer',
            df_cantones,
            get_position=['lng', 'lat'],
            get_elevation=var_1,
            auto_highlight=True,
            extruded=True,
            elevation_scale=dim_1,
            pickable=True,
            get_fill_color=f'[48, 128, {var_1} / {color_1} * 255, 255]',
            coverage=1,
        ),

    ],

    tooltip={
   "html": "<b>{Cantón}</b><br />PIB: {PIB_mill_1} millones<br />PIB per cápita: {PIB_per_cápita} millones<br />Población: {Poblacion_1} hab.<br />Superficie: {Superficie_1} Km2",
   "style": {
        "backgroundColor": "#1e213d",
        "color": "#f6f6f6"
        }   
    }

))
