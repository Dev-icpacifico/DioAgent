import streamlit as st
from agent.agent_executor import executor  # 👈 Importa el agente

st.set_page_config(page_title="Asistente Dio", page_icon="🤖")
st.title("🤖 Asistente Virtual - Condominio Altavista Norte")

st.markdown("""
Hola, soy **Dio**, el asistente virtual de Inmobiliaria Costanera Pacífico.
Estoy aquí para responder tus dudas sobre el proyecto **Altavista Norte**.
""")

# Estado de la conversación
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:", placeholder="Ej: ¿Cuál es la dirección del proyecto?", key="input")

# Al enviar
if st.button("Enviar") and user_input:
    with st.spinner("Dio está escribiendo..."):
        result = executor.invoke({"input": user_input})
        respuesta = result["output"]

    # Guardar la conversación
    st.session_state.chat_history.append(("Tú", user_input))
    st.session_state.chat_history.append(("Dio", respuesta))

# Mostrar historial
for autor, mensaje in reversed(st.session_state.chat_history):
    st.markdown(f"**{autor}:** {mensaje}")
