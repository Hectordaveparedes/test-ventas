import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Test: Ejecutivo de Ventas", page_icon="💼")

st.title("💼 Test Psicotécnico: Ejecutivo de Ventas")
st.write("Por favor, lee cada situación y elige la respuesta que mejor describa tu forma de actuar natural.")

# Definir las preguntas, opciones y sus puntajes
preguntas = [
    {
        "texto": "1. Después de perder una venta importante en la que trabajaste por meses, tú...",
        "opciones": {
            "Selecciona una opción...": 0,
            "Analizo qué salió mal, pido feedback al cliente y ajusto mi estrategia.": 5,
            "Me enfoco inmediatamente en el siguiente prospecto para olvidar el mal rato.": 3,
            "Me desmotivo un poco y prefiero hacer tareas administrativas el resto del día.": 1
        }
    },
    {
        "texto": "2. Un cliente potencial te dice que tu producto es muy caro:",
        "opciones": {
            "Selecciona una opción...": 0,
            "Le ofrezco un descuento inmediatamente para no perder la venta.": 1,
            "Le destaco el Retorno de Inversión (ROI) y el valor único frente a la competencia.": 5,
            "Insisto en que nuestra calidad es la mejor del mercado.": 3
        }
    },
    {
        "texto": "3. Llegas a tu meta de ventas mensual en la tercera semana del mes:",
        "opciones": {
            "Selecciona una opción...": 0,
            "Aprovecho para relajarme un poco y organizar mi base de datos para el próximo mes.": 2,
            "Ayudo a otros compañeros a cerrar sus ventas para que el equipo gane.": 3,
            "Sigo empujando para superar la cuota al máximo y ganar más comisiones.": 5
        }
    },
    {
        "texto": "4. Un cliente te llama muy enojado por un retraso en la entrega:",
        "opciones": {
            "Selecciona una opción...": 0,
            "Me disculpo, lo escucho activamente y busco una solución inmediata.": 5,
            "Le explico amablemente que el error es del departamento de logística.": 1,
            "Le ofrezco un descuento en su próxima compra para calmarlo.": 3
        }
    },
    {
        "texto": "5. Tienes 50 nuevos prospectos (leads) para contactar hoy:",
        "opciones": {
            "Selecciona una opción...": 0,
            "Los llamo en orden alfabético o como fueron llegando.": 2,
            "Los califico rápidamente y priorizo a los que tienen mayor potencial de cierre.": 5,
            "Les envío un correo masivo primero para ver quién responde.": 1
        }
    },
    {
        "texto": "6. ¿Cómo prefieres medir tu éxito profesional?",
        "opciones": {
            "Selecciona una opción...": 0,
            "Por la calidad de las relaciones a largo plazo construidas con los clientes.": 3,
            "Por superar los objetivos comerciales y mis ingresos financieros.": 5,
            "Por tener un trabajo estable, predecible y con buen ambiente.": 1
        }
    }
]

# Recolectar respuestas
respuestas = []
for i, p in enumerate(preguntas):
    st.subheader(p["texto"])
    opcion_elegida = st.radio("Elige tu respuesta:", list(p["opciones"].keys()), key=f"q{i}", label_visibility="collapsed")
    puntaje = p["opciones"][opcion_elegida]
    respuestas.append(puntaje)
    st.divider()

# Botón de envío
if st.button("Enviar Respuestas y Ver Resultados", type="primary"):
    if 0 in respuestas:
        st.warning("⚠️ Por favor, responde todas las preguntas antes de enviar.")
    else:
        puntaje_total = sum(respuestas)
        st.success(f"¡Test completado! Puntaje Total: {puntaje_total} / 30")
        
        st.header("📊 Interpretación del Perfil")
        if puntaje_total >= 26:
            st.info("**Perfil Cazador / Closer (26-30 pts):**\nAltamente orientado a resultados, resiliente y persuasivo. Sabe manejar objeciones y tiene un gran empuje. Ideal para captación de nuevos clientes.")
        elif puntaje_total >= 18:
            st.info("**Perfil Granjero / Consultivo (18-25 pts):**\nBuen perfil, se enfoca más en la relación que en la venta agresiva. Excelente para mantenimiento de cuentas (Account Manager), pero podría requerir apoyo en cierres duros.")
        else:
            st.error("**Perfil No Comercial (< 18 pts):**\nPerfil más reactivo. Tiende a evitar la confrontación comercial. Podría encajar mejor en roles de soporte al cliente o áreas administrativas.")
