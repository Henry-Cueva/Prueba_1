import streamlit as st

st.set_page_config(page_title="Conectores Booleanos en PubMed", layout="centered")

st.title("🔍 Conectores Booleanos en Búsquedas Bibliográficas")
st.markdown("""
Los conectores booleanos permiten combinar términos de búsqueda en bases de datos como **PubMed** para refinar los resultados.

Selecciona un conector para ver cómo se usa con ejemplos reales.
""")

# Selección del conector
conector = st.radio("Selecciona un conector booleano:", ["AND", "OR", "NOT"])

# Contenido de cada conector
ejemplos_pubmed = {
    "AND": {
        "descripcion": (
            "🔹 El conector **AND** se usa para buscar artículos que contengan **todos los términos especificados**. "
            "Reduce la cantidad de resultados, aumentando la especificidad."
        ),
        "ejemplos": [
            '"occupational health" AND "mental health"',
            '"nursing staff" AND "work stress"',
            '"air pollution" AND "lung cancer" AND "epidemiology"'
        ],
        "explicacion": (
            "✔️ **PubMed buscará artículos que incluyan *todos* los términos**. "
            "Por ejemplo, el primer ejemplo encuentra artículos que tratan sobre salud ocupacional **y también** salud mental."
        )
    },
    "OR": {
        "descripcion": (
            "🔹 El conector **OR** se usa para buscar artículos que contengan **cualquiera de los términos especificados**. "
            "Aumenta la cantidad de resultados, útil para sinónimos o términos relacionados."
        ),
        "ejemplos": [
            '"depression" OR "anxiety"',
            '"cardiovascular disease" OR "heart disease"',
            '"PPE" OR "personal protective equipment"'
        ],
        "explicacion": (
            "✔️ **PubMed incluirá resultados que contengan al menos uno de los términos**. "
            "Ideal cuando quieres ampliar tu búsqueda usando sinónimos o términos equivalentes."
        )
    },
    "NOT": {
        "descripcion": (
            "🔹 El conector **NOT** excluye términos de la búsqueda. "
            "Se utiliza para eliminar información no relevante."
        ),
        "ejemplos": [
            '"COVID-19" NOT "vaccine"',
            '"cancer" NOT "animal studies"',
            '"diabetes" NOT "type 1"'
        ],
        "explicacion": (
            "⚠️ **PubMed excluirá resultados que contengan el término después de NOT**. "
            "Por ejemplo, se pueden buscar artículos sobre COVID-19 excluyendo los que hablan de vacunas."
        )
    }
}

# Mostrar contenido según el conector elegido
st.subheader(f"🧠 ¿Cómo usar el conector **{conector}**?")
st.markdown(ejemplos_pubmed[conector]["descripcion"])

st.markdown("**Ejemplos en PubMed:**")
for ejemplo in ejemplos_pubmed[conector]["ejemplos"]:
    st.code(ejemplo, language="text")

st.markdown(ejemplos_pubmed[conector]["explicacion"])
