import streamlit as st

st.set_page_config(page_title="Conectores Booleanos", layout="centered")

st.title("🤖 Conectores Booleanos: AND, OR, NOT")
st.markdown("Aprende cómo se usan los conectores booleanos con ejemplos prácticos.")

# Botones de selección
conector = st.radio("Selecciona un conector booleano para ver ejemplos:", ["AND", "OR", "NOT"])

# Diccionario de ejemplos
ejemplos = {
    "AND": {
        "descripcion": "El conector **AND** devuelve `True` solo si ambas condiciones son verdaderas.",
        "codigo": [
            "True and True   → True",
            "True and False  → False",
            "False and True  → False",
            "False and False → False"
        ]
    },
    "OR": {
        "descripcion": "El conector **OR** devuelve `True` si al menos una de las condiciones es verdadera.",
        "codigo": [
            "True or True    → True",
            "True or False   → True",
            "False or True   → True",
            "False or False  → False"
        ]
    },
    "NOT": {
        "descripcion": "El conector **NOT** invierte el valor lógico de la condición.",
        "codigo": [
            "not True        → False",
            "not False       → True"
        ]
    }
}

# Mostrar la descripción y los ejemplos según la opción elegida
st.subheader(f"Ejemplos del conector: {conector}")
st.markdown(ejemplos[conector]["descripcion"])
st.code("\n".join(ejemplos[conector]["codigo"]), language="python")
