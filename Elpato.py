import streamlit as st
from urllib.parse import quote

# ============================================================
# Gamarra Select — Marketplace de moda peruana
# MVP en Streamlit
# ============================================================

st.set_page_config(
    page_title="Gamarra Select | Moda peruana",
    page_icon="🇵🇪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# ESTILOS
# -----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #f7f7f5;
    }

    .hero {
        padding: 58px 8px 38px 8px;
        text-align: center;
    }

    .eyebrow {
        color: #9b1c1c;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 14px;
    }

    .hero h1 {
        font-size: clamp(42px, 6vw, 76px);
        line-height: .98;
        letter-spacing: -3px;
        margin: 0 auto 18px auto;
        max-width: 950px;
        color: #111111;
        font-weight: 800;
    }

    .hero p {
        color: #5f5f5a;
        max-width: 720px;
        margin: auto;
        font-size: 18px;
        line-height: 1.6;
    }

    .badge {
        display: inline-block;
        background: #111;
        color: white;
        border-radius: 999px;
        padding: 7px 13px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 800;
        color: #111;
        letter-spacing: -1px;
        margin: 20px 0 6px;
    }

    .section-subtitle {
        color: #777;
        margin-bottom: 24px;
    }

    .company-card, .product-card {
        background: white;
        border: 1px solid #e9e9e5;
        border-radius: 18px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 5px 20px rgba(0,0,0,.035);
    }

    .company-name, .product-name {
        font-size: 20px;
        font-weight: 800;
        color: #151515;
        margin: 3px 0 7px;
    }

    .company-meta, .product-meta {
        color: #777;
        font-size: 13px;
        line-height: 1.55;
    }

    .price {
        font-size: 22px;
        font-weight: 800;
        color: #111;
        margin-top: 13px;
    }

    .tag {
        display: inline-block;
        border: 1px solid #deded9;
        border-radius: 999px;
        padding: 5px 9px;
        margin: 3px 3px 3px 0;
        color: #555;
        font-size: 11px;
        font-weight: 600;
    }

    .trust {
        background: #111;
        color: white;
        border-radius: 22px;
        padding: 34px;
        margin: 50px 0 35px;
    }

    .trust h2 {
        font-size: 30px;
        margin-top: 0;
        letter-spacing: -1px;
    }

    .trust p {
        color: #cfcfcf;
        line-height: 1.6;
    }

    .footer {
        border-top: 1px solid #ddd;
        padding: 28px 0;
        margin-top: 50px;
        color: #777;
        text-align: center;
        font-size: 13px;
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: 700;
        min-height: 42px;
    }

    .metric-box {
        background: white;
        border: 1px solid #e9e9e5;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
    }

    .metric-number {
        font-size: 28px;
        font-weight: 800;
        color: #111;
    }

    .metric-label {
        color: #777;
        font-size: 12px;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# DATOS DEMO
# Reemplaza estos datos por datos reales cuando tengas proveedores.
# -----------------------------
EMPRESAS = [
    {
        "id": 1,
        "nombre": "Andes Studio",
        "descripcion": "Taller peruano especializado en básicos premium y prendas urbanas.",
        "categoria": "Casual",
        "materiales": ["Algodón peruano", "Jersey"],
        "ubicacion": "La Victoria, Lima",
        "especialidad": "Básicos premium",
        "whatsapp": "51999999999",
        "verificado": True,
        "productos": [
            {
                "nombre": "Oversized Heavy Tee",
                "categoria": "Polos",
                "precio": 69,
                "material": "Algodón peruano 24/1",
                "tendencia": "Oversized",
            },
            {
                "nombre": "Boxy Tee Premium",
                "categoria": "Polos",
                "precio": 62,
                "material": "Algodón peruano",
                "tendencia": "Boxy",
            },
        ],
    },
    {
        "id": 2,
        "nombre": "Lima Norte Atelier",
        "descripcion": "Fabricante de prendas contemporáneas con producción para marcas independientes.",
        "categoria": "Contemporáneo",
        "materiales": ["Algodón", "French Terry"],
        "ubicacion": "Gamarra, Lima",
        "especialidad": "Moda contemporánea",
        "whatsapp": "51988888888",
        "verificado": True,
        "productos": [
            {
                "nombre": "French Terry Hoodie",
                "categoria": "Poleras",
                "precio": 119,
                "material": "French Terry",
                "tendencia": "Relaxed fit",
            },
            {
                "nombre": "Cargo Wide Leg",
                "categoria": "Pantalones",
                "precio": 129,
                "material": "Drill premium",
                "tendencia": "Wide leg",
            },
        ],
    },
    {
        "id": 3,
        "nombre": "Sierra Cotton Co.",
        "descripcion": "Productor enfocado en fibras peruanas y prendas casuales de mayor gramaje.",
        "categoria": "Premium",
        "materiales": ["Algodón peruano", "Pima"],
        "ubicacion": "La Victoria, Lima",
        "especialidad": "Algodón premium",
        "whatsapp": "51977777777",
        "verificado": False,
        "productos": [
            {
                "nombre": "Pima Essential Tee",
                "categoria": "Polos",
                "precio": 79,
                "material": "Algodón Pima",
                "tendencia": "Minimal",
            },
            {
                "nombre": "Pima Polo",
                "categoria": "Polos",
                "precio": 89,
                "material": "Algodón Pima",
                "tendencia": "Classic",
            },
        ],
    },
    {
        "id": 4,
        "nombre": "Distrito 43",
        "descripcion": "Taller orientado a streetwear, cortes actuales y producción flexible.",
        "categoria": "Streetwear",
        "materiales": ["Jersey", "Drill"],
        "ubicacion": "Gamarra, Lima",
        "especialidad": "Streetwear",
        "whatsapp": "51966666666",
        "verificado": True,
        "productos": [
            {
                "nombre": "Relaxed Cargo",
                "categoria": "Pantalones",
                "precio": 139,
                "material": "Drill",
                "tendencia": "Utility",
            },
            {
                "nombre": "Zip Hoodie",
                "categoria": "Poleras",
                "precio": 149,
                "material": "Algodón / French Terry",
                "tendencia": "Layering",
            },
        ],
    },
]

TODOS_PRODUCTOS = []
for empresa in EMPRESAS:
    for producto in empresa["productos"]:
        producto_copy = producto.copy()
        producto_copy["empresa"] = empresa["nombre"]
        producto_copy["empresa_id"] = empresa["id"]
        TODOS_PRODUCTOS.append(producto_copy)


# -----------------------------
# ESTADO
# -----------------------------
if "empresa_seleccionada" not in st.session_state:
    st.session_state.empresa_seleccionada = None

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"


# -----------------------------
# NAVBAR
# -----------------------------
nav1, nav2, nav3, nav4 = st.columns([2.4, 1, 1, 1])

with nav1:
    st.markdown("### 🇵🇪 GAMARRA SELECT")

with nav2:
    if st.button("Descubrir", use_container_width=True):
        st.session_state.pagina = "Descubrir"

with nav3:
    if st.button("Empresas", use_container_width=True):
        st.session_state.pagina = "Empresas"

with nav4:
    if st.button("Para empresas", use_container_width=True):
        st.session_state.pagina = "Para empresas"


# ============================================================
# INICIO
# ============================================================
if st.session_state.pagina == "Inicio":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">HECHO EN PERÚ · CURADO PARA TI</div>
        <h1>Descubre el talento de Gamarra sin tener que ir a Gamarra.</h1>
        <p>
            Conectamos compradores con fabricantes y marcas peruanas que crean
            prendas actuales, materiales de calidad y producción local.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">100%</div>
            <div class="metric-label">Producción local en el marketplace</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">Directo</div>
            <div class="metric-label">Conexión con el proveedor</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">Actual</div>
            <div class="metric-label">Prendas alineadas a tendencias</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Lo que está moviendo la moda local</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Una selección inicial de prendas y fabricantes.</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for i, producto in enumerate(TODOS_PRODUCTOS[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <span class="badge">{producto["tendencia"]}</span>
                <div class="product-name">{producto["nombre"]}</div>
                <div class="product-meta">
                    {producto["empresa"]}<br>
                    {producto["material"]} · {producto["categoria"]}
                </div>
                <div class="price">S/ {producto["precio"]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    if st.button("Explorar todo el catálogo →", type="primary"):
        st.session_state.pagina = "Descubrir"
        st.rerun()

    st.markdown("""
    <div class="trust">
        <h2>El valor está en conectar.</h2>
        <p>
            Gamarra concentra conocimiento, manufactura y proveedores que muchas
            veces no son fáciles de descubrir desde fuera. Esta plataforma busca
            convertir ese ecosistema en una experiencia digital: descubrir,
            comparar y contactar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">¿Qué hace diferente a la plataforma?</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.markdown("### 01 · Descubrimiento")
        st.write("Encuentra empresas y prendas sin recorrer físicamente cientos de tiendas.")

    with b:
        st.markdown("### 02 · Curaduría")
        st.write("Una vitrina enfocada en calidad, materiales, cortes y tendencias.")

    with c:
        st.markdown("### 03 · Conexión")
        st.write("Habla directamente con el vendedor y solicita información o pedidos.")


# ============================================================
# DESCUBRIR
# ============================================================
elif st.session_state.pagina == "Descubrir":

    st.markdown('<div class="section-title">Descubre prendas</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Explora productos de fabricantes y marcas peruanas.</div>',
        unsafe_allow_html=True
    )

    col_search, col_cat, col_price = st.columns([2, 1, 1])

    with col_search:
        busqueda = st.text_input(
            "Buscar",
            placeholder="Ej. polo oversized, algodón Pima..."
        )

    with col_cat:
        categorias = ["Todas"] + sorted(list(set(p["categoria"] for p in TODOS_PRODUCTOS)))
        categoria = st.selectbox("Categoría", categorias)

    with col_price:
        precio_max = st.slider("Precio máximo", 30, 250, 180, 10)

    resultados = TODOS_PRODUCTOS.copy()

    if busqueda:
        termino = busqueda.lower()
        resultados = [
            p for p in resultados
            if termino in p["nombre"].lower()
            or termino in p["empresa"].lower()
            or termino in p["material"].lower()
            or termino in p["tendencia"].lower()
        ]

    if categoria != "Todas":
        resultados = [p for p in resultados if p["categoria"] == categoria]

    resultados = [p for p in resultados if p["precio"] <= precio_max]

    st.caption(f"{len(resultados)} prendas encontradas")

    if not resultados:
        st.info("No encontramos prendas con esos filtros. Prueba otra búsqueda.")
    else:
        for inicio in range(0, len(resultados), 3):
            fila = resultados[inicio:inicio + 3]
            cols = st.columns(3)

            for i, producto in enumerate(fila):
                with cols[i]:
                    st.markdown(f"""
                    <div class="product-card">
                        <span class="badge">{producto["tendencia"]}</span>
                        <div class="product-name">{producto["nombre"]}</div>
                        <div class="product-meta">
                            <b>{producto["empresa"]}</b><br>
                            {producto["material"]}<br>
                            Categoría: {producto["categoria"]}
                        </div>
                        <div class="price">S/ {producto["precio"]}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(
                        f"Contactar por {producto['nombre']}",
                        key=f"contact_{producto['empresa_id']}_{producto['nombre']}",
                        use_container_width=True
                    ):
                        empresa = next(
                            e for e in EMPRESAS if e["id"] == producto["empresa_id"]
                        )
                        mensaje = quote(
                            f"Hola, vi en Gamarra Select la prenda "
                            f"'{producto['nombre']}' de {empresa['nombre']} y quisiera "
                            f"más información."
                        )
                        url = f"https://wa.me/{empresa['whatsapp']}?text={mensaje}"
                        st.markdown(
                            f"**[Abrir WhatsApp con {empresa['nombre']}]({url})**"
                        )


# ============================================================
# EMPRESAS
# ============================================================
elif st.session_state.pagina == "Empresas":

    st.markdown('<div class="section-title">Empresas y fabricantes</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Conoce quién está detrás de cada prenda.</div>',
        unsafe_allow_html=True
    )

    filtro = st.selectbox(
        "Filtrar por especialidad",
        ["Todas"] + sorted(list(set(e["categoria"] for e in EMPRESAS)))
    )

    empresas = EMPRESAS if filtro == "Todas" else [
        e for e in EMPRESAS if e["categoria"] == filtro
    ]

    for empresa in empresas:
        st.markdown(f"""
        <div class="company-card">
            <span class="badge">
                {"✓ VERIFICADO" if empresa["verificado"] else "NUEVO PROVEEDOR"}
            </span>
            <div class="company-name">{empresa["nombre"]}</div>
            <div class="company-meta">
                {empresa["descripcion"]}<br><br>
                <b>Especialidad:</b> {empresa["especialidad"]}<br>
                <b>Ubicación:</b> {empresa["ubicacion"]}<br>
                <b>Materiales:</b> {", ".join(empresa["materiales"])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        pcols = st.columns(len(empresa["productos"]))

        for i, producto in enumerate(empresa["productos"]):
            with pcols[i]:
                st.markdown(f"""
                **{producto["nombre"]}**

                {producto["material"]}

                **S/ {producto["precio"]}**
                """)

        mensaje = quote(
            f"Hola, encontré {empresa['nombre']} en Gamarra Select y quisiera "
            f"conocer más sobre sus productos."
        )
        url = f"https://wa.me/{empresa['whatsapp']}?text={mensaje}"

        st.markdown(f"[💬 Contactar a {empresa['nombre']} por WhatsApp]({url})")
        st.divider()


# ============================================================
# PARA EMPRESAS
# ============================================================
elif st.session_state.pagina == "Para empresas":

    st.markdown('<div class="section-title">Lleva tu negocio al mundo digital.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">'
        'Una vitrina para que compradores encuentren tus productos sin tener que visitar tu tienda.'
        '</div>',
        unsafe_allow_html=True
    )

    a, b = st.columns(2)

    with a:
        st.markdown("""
        ### ¿Qué obtiene tu empresa?

        - Perfil digital de tu negocio
        - Catálogo de productos
        - Presentación de materiales y especialidades
        - Contacto directo con compradores
        - Mayor visibilidad fuera de Gamarra
        - Presencia frente a clientes que buscan propuestas diferentes
        """)

    with b:
        st.markdown("""
        ### ¿Qué buscamos?

        **Fabricantes y marcas peruanas que:**

        - Produzcan localmente
        - Tengan prendas de calidad
        - Sean capaces de mostrar catálogo
        - Respondan consultas de compradores
        - Quieran crecer más allá del tráfico físico
        """)

    st.write("")
    st.markdown("### Cuéntanos sobre tu empresa")

    with st.form("empresa_form"):
        nombre = st.text_input("Nombre de la empresa")
        contacto = st.text_input("Nombre de contacto")
        whatsapp = st.text_input("WhatsApp")
        especialidad = st.selectbox(
            "Especialidad",
            ["Polos", "Poleras", "Pantalones", "Streetwear", "Moda femenina",
             "Moda masculina", "Premium", "Otro"]
        )
        descripcion = st.text_area("Cuéntanos qué produces")

        enviar = st.form_submit_button(
            "Enviar solicitud",
            type="primary",
            use_container_width=True
        )

        if enviar:
            if not nombre or not contacto or not whatsapp:
                st.error("Completa nombre, contacto y WhatsApp.")
            else:
                st.success(
                    "Solicitud registrada en este MVP. "
                    "En la versión productiva estos datos se guardarían en una base de datos."
                )


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
    <b>Gamarra Select</b> · Marketplace de moda y manufactura peruana<br>
    MVP conceptual · Los datos mostrados son de demostración.
</div>
""", unsafe_allow_html=True)

