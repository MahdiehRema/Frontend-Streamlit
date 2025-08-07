import streamlit as st
from ui.background import ui_setting
from pages.main_page import initilize_oracle_client
from pages.allgemeine_analyse import main_analyse as main_analyse
from pages.delta_ansicht import delta_ansicht as delta_ansicht



initilize_oracle_client()
ui_setting()   



if "seite" not in st.session_state:
    st.session_state.seite = "🏠 Startseite"


seiten_liste = ["🏠 Startseite", "📊 Allgemeine Analyse", "🔄 Delta Ansicht"]


auswahl = st.sidebar.selectbox(
    "📁 Menü",
    options=seiten_liste,
    index=seiten_liste.index(st.session_state.seite),
    key="menü_auswahl"
)


st.session_state.seite = auswahl


if st.session_state.seite == "🏠 Startseite":
    st.title("📊 Willkommen im PVD Dashboard")
    st.markdown("""
    Mit diesem Dashboard können Sie **historisierte PVD-Daten** ganz einfach nach spezifischen Anforderungen filtern und die **prozentuale Verteilung** innerhalb der jeweiligen
    **Trassenabstandkategorien** anzeigen lassen.

    Zusätzlich steht eine **Delta-Ansicht** zur Verfügung, mit der Sie alle Veränderungen im Zeitverlauf nachvollziehen können.

    ---

    📌 **Bedienungshinweis**  
    Nutzen Sie bitte das Menü auf der linken Seite, um Ihre gewünschte Anforderung auszuwählen.

    ---

    📬 Bei weiteren Fragen wenden Sie sich gerne an:

    - **Patrick Reichert**
    - **Mahdieh Rezaeimahboub**

    im **Customer Data Science Team**
    """)

elif st.session_state.seite == "📊 Allgemeine Analyse":
    main_analyse.zeige_karten()

elif st.session_state.seite == "🔄 Delta Ansicht":
    st.title("🔄 Delta Ansicht")
    st.write("Hier kommt Delta Ansicht")
