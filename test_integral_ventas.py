import streamlit as st

st.set_page_config(page_title="Test Integral: Ejecutivo de Ventas", page_icon="🚀", layout="centered")

st.title("🚀 Evaluación Integral: Ejecutivo de Ventas")
st.write("Este test consta de 3 partes. Responde todas las preguntas de cada sección con honestidad.")

# ==========================================
# PARTE 1: SITUACIONAL (Psicotécnico)
# ==========================================
st.header("Parte 1: Juicio Situacional")
preguntas_p1 = [
    {
        "texto": "1. Después de perder una venta importante, tú...",
        "opciones": {"Selecciona...": 0, "Analizo qué salió mal y ajusto mi estrategia.": 5, "Me enfoco inmediatamente en el siguiente prospecto.": 3, "Me desmotivo y hago tareas administrativas.": 1}
    },
    {
        "texto": "2. Un cliente te dice que tu producto es muy caro:",
        "opciones": {"Selecciona...": 0, "Ofrezco descuento de inmediato.": 1, "Destaco el ROI y el valor único.": 5, "Insisto en nuestra calidad.": 3}
    },
    {
        "texto": "3. Llegas a tu meta de ventas en la 3ra semana del mes:",
        "opciones": {"Selecciona...": 0, "Aprovecho para relajarme y organizar bases de datos.": 2, "Ayudo a compañeros a cerrar sus ventas.": 3, "Sigo empujando para superar la cuota al máximo.": 5}
    },
    {
        "texto": "4. Un cliente te llama muy enojado por un retraso:",
        "opciones": {"Selecciona...": 0, "Me disculpo, escucho activamente y busco solución inmediata.": 5, "Le explico que el error es de logística.": 1, "Le ofrezco un descuento en próxima compra.": 3}
    }
]

respuestas_p1 = []
for i, p in enumerate(preguntas_p1):
    st.markdown(f"**{p['texto']}**")
    val = st.radio("Respuesta p1", list(p["opciones"].keys()), key=f"p1_{i}", label_visibility="collapsed")
    respuestas_p1.append(p["opciones"][val])
st.divider()

# ==========================================
# PARTE 2: COMPETENCIAS TÉCNICAS
# ==========================================
st.header("Parte 2: Competencias Comerciales")
preguntas_p2 = [
    {
        "texto": "1. Un cliente pide 20% de descuento para firmar hoy (tu límite es 10%):",
        "opciones": {"Selecciona...": 0, "Digo que es imposible y el precio es fijo.": 1, "Pido al gerente que haga una excepción.": 2, "Ofrezco el 10% y agrego un beneficio sin costo extra para la empresa.": 5}
    },
    {
        "texto": "2. El cliente dice: 'Me encanta. Envíalo por correo y te aviso la próxima semana'.",
        "opciones": {"Selecciona...": 0, "Envío el correo y espero su respuesta.": 1, "Envío el correo y le propongo agendar una llamada de 10 min la próxima semana.": 5, "Le digo que si no firma hoy, pierde los beneficios.": 2}
    },
    {
        "texto": "3. Enviaste una cotización hace 4 días y no responden:",
        "opciones": {"Selecciona...": 0, "Envío un mensaje aportando valor (ej. un artículo) y pregunto dudas.": 5, "Pregunto directamente: '¿Ya tomaste una decisión?'.": 3, "Asumo que no le interesó y busco otros.": 1}
    },
    {
        "texto": "4. En la primera llamada con un cliente, tu objetivo es:",
        "opciones": {"Selecciona...": 0, "Hablar de todos los beneficios de mi producto.": 1, "Hacer preguntas para entender su problema y presupuesto.": 5, "Intentar cerrar la venta en 5 minutos.": 2}
    }
]

respuestas_p2 = []
for i, p in enumerate(preguntas_p2):
    st.markdown(f"**{p['texto']}**")
    val = st.radio("Respuesta p2", list(p["opciones"].keys()), key=f"p2_{i}", label_visibility="collapsed")
    respuestas_p2.append(p["opciones"][val])
st.divider()

# ==========================================
# PARTE 3: PERSONALIDAD (Estilo DISC)
# ==========================================
st.header("Parte 3: Perfil de Personalidad")
st.write("Selecciona la frase con la que te sientas MÁS identificado.")
preguntas_p3 = [
    {
        "texto": "1. Cuando te enfrentas a un problema nuevo:",
        "opciones": {"Selecciona...": "", "Busco resolverlo inmediatamente tomando la iniciativa.": "D", "Lo comento con otros para buscar ideas juntos.": "I", "Espero instrucciones claras o veo cómo lo hacen otros.": "S", "Analizo toda la información disponible antes de actuar.": "C"}
    },
    {
        "texto": "2. Bajo presión, mi mayor fortaleza es:",
        "opciones": {"Selecciona...": "", "Mi determinación para lograr la meta.": "D", "Mi optimismo y habilidad para persuadir.": "I", "Mi paciencia para calmar la situación.": "S", "Mi capacidad para no cometer errores y ser preciso.": "C"}
    },
    {
        "texto": "3. ¿Qué te frustra más en el trabajo?",
        "opciones": {"Selecciona...": "", "La lentitud y falta de resultados.": "D", "El aislamiento y no poder interactuar con gente.": "I", "Los cambios constantes e impredecibles.": "S", "La desorganización y falta de reglas claras.": "C"}
    },
    {
        "texto": "4. Al comunicarte con un cliente, tú tiendes a:",
        "opciones": {"Selecciona...": "", "Ir directo al grano y hablar de negocios.": "D", "Ser muy amigable y construir una relación personal rápida.": "I", "Escuchar con mucha atención y no interrumpir.": "S", "Presentar datos, números y detalles técnicos.": "C"}
    }
]

respuestas_p3 = []
for i, p in enumerate(preguntas_p3):
    st.markdown(f"**{p['texto']}**")
    val = st.radio("Respuesta p3", list(p["opciones"].keys()), key=f"p3_{i}", label_visibility="collapsed")
    respuestas_p3.append(p["opciones"][val])

st.write("")
if st.button("Enviar y Ver Informe Completo", type="primary", use_container_width=True):
    if (0 in respuestas_p1) or (0 in respuestas_p2) or ("" in respuestas_p3):
        st.warning("⚠️ Por favor, responde todas las preguntas de todas las partes antes de enviar.")
    else:
        st.success("¡Test completado con éxito!")
        
        # Cálculos P1 y P2
        pts_p1 = sum(respuestas_p1)
        pts_p2 = sum(respuestas_p2)
        
        # Cálculos P3 (DISC)
        conteo_disc = {"D": respuestas_p3.count("D"), "I": respuestas_p3.count("I"), "S": respuestas_p3.count("S"), "C": respuestas_p3.count("C")}
        
        st.title("📋 Informe de Resultados")
        
        # P1
        st.subheader("1. Juicio Situacional (Resolución de Conflictos)")
        if pts_p1 >= 16:
            st.info(f"**Puntaje: {pts_p1}/20 - Perfil Resiliente:**\nExcelente manejo de la frustración, alta motivación y gran empatía con el cliente.")
        elif pts_p1 >= 10:
            st.warning(f"**Puntaje: {pts_p1}/20 - Perfil Promedio:**\nTiene buenas intenciones, pero a veces cede ante la presión o le falta empuje.")
        else:
            st.error(f"**Puntaje: {pts_p1}/20 - Perfil Reactivo:**\nBaja tolerancia a la frustración. No recomendado para ambientes de alta presión.")
            
        # P2
        st.subheader("2. Competencias Técnicas B2B")
        if pts_p2 >= 16:
            st.info(f"**Puntaje: {pts_p2}/20 - Perfil Senior:**\nDomina la técnica de ventas. Califica bien, hace seguimiento efectivo y no regala el margen.")
        elif pts_p2 >= 10:
            st.warning(f"**Puntaje: {pts_p2}/20 - Perfil Junior:**\nTiene nociones comerciales pero comete errores tácticos. Requiere capacitación técnica.")
        else:
            st.error(f"**Puntaje: {pts_p2}/20 - Perfil Deficiente:**\nFalta de estructura comercial y mal manejo de cierres.")

        # P3
        st.subheader("3. Estilo de Personalidad Dominante")
        perfiles_activos = conteo_disc["D"] + conteo_disc["I"]
        perfiles_pasivos = conteo_disc["S"] + conteo_disc["C"]
        
        if conteo_disc["C"] >= 3:
            st.info("**Vendedor Técnico (Analítico):**\nSe basa en datos y detalles. Excelente para ventas de software complejo o ingeniería, pero puede tardar en cerrar negocios rápidos.")
        elif perfiles_activos > perfiles_pasivos:
            st.info("**Vendedor 'Cazador' (Hunter - Directo/Sociable):**\nProactivo, persuasivo y muy orientado a resultados. Ideal para abrir mercado, prospección en frío y conseguir nuevos clientes.")
        else:
            st.info("**Vendedor 'Granjero' (Farmer - Paciente/Estructurado):**\nExcelente escuchando y siguiendo procesos. Ideal para mantener clientes existentes (Account Manager) o servicio al cliente, pero no le gusta la venta agresiva.")
