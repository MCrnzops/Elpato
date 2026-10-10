import streamlit as str_app
from urllib.parse import quote

# ============================================================
# Vanguardia Peruana — Alta Manufactura de Gamarra
# MVP en Streamlit
# ============================================================

str_app.set_page_config(
    page_title="Vanguardia Peruana | Gamarra Select",
    page_icon="🇵🇪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# ESTILOS
# -----------------------------
str_app.markdown("""
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
        font-size: clamp(38px, 5.5vw, 70px);
        line-height: 1.02;
        letter-spacing: -2.5px;
        margin: 0 auto 18px auto;
        max-width: 980px;
        color: #111111;
        font-weight: 800;
    }

    .hero p {
        color: #5f5f5a;
        max-width: 760px;
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
# -----------------------------
EMPRESAS = [
    {
        "id": 1,
        "nombre": "Andes Studio",
        "descripcion": "Taller peruano especializado en básicos premium, alta durabilidad y diseño limpio.",
        "categoria": "Casual",
        "materiales": ["Algodón Pima", "Jersey pesado"],
        "ubicacion": "La Victoria, Lima",
        "especialidad": "Básicos de lujo",
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
                "material": "Algodón Pima",
                "tendencia": "Boxy",
            },
        ],
    },
    {
        "id": 2,
        "nombre": "Lima Norte Atelier",
        "descripcion": "Fabricante de prendas contemporáneas con acabados superiores a marcas de centros comerciales.",
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
        "descripcion": "Enfocados en fibras nativas peruanas, superando en suavidad y calidad a marcas importadas masivas.",
        "categoria": "Premium",
        "materiales": ["Algodón Pima Orgánico"],
        "ubicacion": "La Victoria, Lima",
        "especialidad": "Fibras nobles",
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
                "nombre": "Pima Polo Piqué",
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
        "descripcion": "Streetwear de autor con cortes vanguardistas que marcan tendencia real en el mercado local.",
        "categoria": "Streetwear",
        "materiales": ["Jersey", "Drill pesado"],
        "ubicacion": "Gamarra, Lima",
        "especialidad": "Streetwear de alta gama",
        "whatsapp": "51966666666",
        "verificado": True,
        "productos": [
            {
                "nombre": "Relaxed Cargo Utility",
                "categoria": "Pantalones",
                "precio": 139,
                "material": "Drill",
                "tendencia": "Utility",
            },
            {
                "nombre": "Zip Hoodie Heavyweight",
                "categoria": "Poleras",
                "precio": 149,
                "material": "French Terry",
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
if "empresa_seleccionada" not in str_app.session_state:
    str_app.session_state.empresa_seleccionada = None

if "pagina" not in str_app.session_state:
    str_app.session_state.pagina = "Inicio"


# -----------------------------
# NAVBAR
# -----------------------------
nav1, nav2, nav3, nav4 = str_app.columns([2.4, 1, 1, 1])

with nav1:
    str_app.markdown("### 🇵🇪 VANGUARDIA PERUANA")

with nav2:
    if str_app.button("Descubrir", use_container_width=True):
        str_app.session_state.pagina = "Descubrir"

with nav3:
    if str_app.button("Talleres", use_container_width=True):
        str_app.session_state.pagina = "Empresas"

with nav4:
    if str_app.button("Para Marcas", use_container_width=True):
        str_app.session_state.pagina = "Para empresas"


# ============================================================
# INICIO
# ============================================================
if str_app.session_state.pagina == "Inicio":

    str_app.markdown("""
    <div class="hero">
        <div class="eyebrow">ALTA MANFACTURA NACIONAL · DISEÑO SIN INTERMEDIARIOS</div>
        <h1>El verdadero lujo es vestir mejor con lo mejor del Perú.</h1>
        <p>
            Conectamos directamente a compradores exigentes con los mejores talleres y creadores 
            de Gamarra. Prendas con mejores materiales, cortes en tendencia y sin pagar sobreprecios de centro comercial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = str_app.columns(3)

    with c1:
        str_app.markdown("""
        <div class="metric-box">
            <div class="metric-number">Algodón Pima</div>
            <div class="metric-label">Y materias primas de clase mundial</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        str_app.markdown("""
        <div class="metric-box">
            <div class="metric-number">Sin Colas</div>
            <div class="metric-label">Compra directo desde la comodidad de casa</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        str_app.markdown("""
        <div class="metric-box">
            <div class="metric-number">B2B & Directo</div>
            <div class="metric-label">Conexión exclusiva vía WhatsApp con talleres</div>
        </div>
        """, unsafe_allow_html=True)

    str_app.markdown('<div class="section-title">Destacados de la semana</div>', unsafe_allow_html=True)
    str_app.markdown(
        '<div class="section-subtitle">Piezas clave hechas en talleres peruanos de alta gama.</div>',
        unsafe_allow_html=True
    )

    cols = str_app.columns(3)

    for i, producto in enumerate(TODOS_PRODUCTOS[:3]):
        with cols[i]:
            str_app.markdown(f"""
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

    str_app.write("")
    if str_app.button("Explorar todo el catálogo →", type="primary"):
        str_app.session_state.pagina = "Descubrir"
        str_app.rerun()

    str_app.markdown("""
    <div class="trust">
        <h2>¿Por qué elegir producción peruana local frente a marcas extranjeras masivas?</h2>
        <p>
            Mientras que marcas de fast-fashion importadas cobran precios elevados por plásticos y etiquetas de marketing, 
            la industria local de Gamarra utiliza el codiciado algodón peruano, ofrece acabados impecables y se adapta 
            ágilmente a las nuevas tendencias globales. Es hora de valorar lo nuestro.
        </p>
    </div>
    """, unsafe_allow_html=True)

    str_app.markdown('<div class="section-title">¿Cómo funciona?</div>', unsafe_allow_html=True)

    a, b, c = str_app.columns(3)

    with a:
        str_app.markdown("### 01 · Explora sin ir")
        str_app.write("Visualiza las mejores colecciones y prendas de Gamarra desde tu dispositivo.")

    with b:
        str_app.markdown("### 02 · Calidad Superior")
        str_app.write("Comprueba materiales nobles como el algodón Pima y French Terry de exportación.")

    with c:
        str_app.markdown("### 03 · Conexión Directa")
        str_app.write("Cierra tu pedido o consulta tallas directamente con el fabricante por WhatsApp.")


# ============================================================
# DESCUBRIR
# ============================================================
elif str_app.session_state.pagina == "Descubrir":

    str_app.markdown('<div class="section-title">Catálogo Exclusivo</div>', unsafe_allow_html=True)
    str_app.markdown(
        '<div class="section-subtitle">Filtra y encuentra piezas de nivel superior hechas en Perú.</div>',
        unsafe_allow_html=True
    )

    col_search, col_cat, col_price = str_app.columns([2, 1, 1])

    with col_search:
        busqueda = str_app.text_input(
            "Buscar",
            placeholder="Ej. polo oversized, Pima, hoodie..."
        )

    with col_cat:
        categorias = ["Todas"] + sorted(list(set(p["categoria"] for p in TODOS_PRODUCTOS)))
        categoria = str_app.selectbox("Categoría", categorias)

    with col_price:
        precio_max = str_app.slider("Precio máximo (S/)", 30, 250, 180, 10)

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

    str_app.caption(f"{len(resultados)} prendas disponibles")

    if not resultados:
        str_app.info("No encontramos prendas con esos filtros. Intenta con otros términos.")
    else:
        for inicio in range(0, len(resultados), 3):
            fila = resultados[inicio:inicio + 3]
            cols = str_app.columns(3)

            for i, producto in enumerate(fila):
                with cols[i]:
                    str_app.markdown(f"""
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

                    if str_app.button(
                        f"Pedir {producto['nombre']}",
                        key=f"contact_{producto['empresa_id']}_{producto['nombre']}",
                        use_container_width=True
                    ):
                        empresa = next(
                            e for e in EMPRESAS if e["id"] == producto["empresa_id"]
                        )
                        mensaje = quote(
                            f"Hola, vi en Vanguardia Peruana la prenda "
                            f"'{producto['nombre']}' de {empresa['nombre']} y quisiera "
                            f"coordinar talla y envío."
                        )
                        url = f"https://wa.me/{empresa['whatsapp']}?text={mensaje}"
                        str_app.markdown(
                            f"**[💬 Abrir WhatsApp con {empresa['nombre']}]({url})**"
                        )


# ============================================================
# EMPRESAS
# ============================================================
elif str_app.session_state.pagina == "Empresas":

    str_app.markdown('<div class="section-title">Talleres y Marcas Aliadas</div>', unsafe_allow_html=True)
    str_app.markdown(
        '<div class="section-subtitle">Conoce a los creadores detrás de la alta costura y confección peruana.</div>',
        unsafe_allow_html=True
    )

    filtro = str_app.selectbox(
        "Filtrar por estilo",
        ["Todas"] + sorted(list(set(e["categoria"] for e in EMPRESAS)))
    )

    empresas = EMPRESAS if filtro == "Todas" else [
        e for e in EMPRESAS if e["categoria"] == filtro
    ]

    for empresa in empresas:
        str_app.markdown(f"""
        <div class="company-card">
            <span class="badge">
                {"✓ TALLER VERIFICADO" if empresa["verificado"] else "NUEVO ALIADO"}
            </span>
            <div class="company-name">{empresa["nombre"]}</div>
            <div class="company-meta">
                {empresa["descripcion"]}<br><br>
                <b>Especialidad:</b> {empresa["especialidad"]}<br>
                <b>Ubicación:</b> {empresa["ubicacion"]}<br>
                <b>Materiales clave:</b> {", ".join(empresa["materiales"])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        str_app.write("")

        pcols = str_app.columns(len(empresa["productos"]))

        for i, producto in enumerate(empresa["productos"]):
            with pcols[i]:
                str_app.markdown(f"""
                **{producto["nombre"]}**

                {producto["material"]}

                **S/ {producto["precio"]}**
                """)

        mensaje = quote(
            f"Hola, encontré a {empresa['nombre']} en Vanguardia Peruana y me interesa conocer más su catálogo."
        )
        url = f"https://wa.me/{empresa['whatsapp']}?text={mensaje}"

        str_app.markdown(f"[💬 Contactar directamente a {empresa['nombre']} por WhatsApp]({url})")
        str_app.divider()


# ============================================================
# PARA EMPRESAS
# ============================================================
elif str_app.session_state.pagina == "Para empresas":

    str_app.markdown('<div class="section-title">Únete a la plataforma</div>', unsafe_allow_html=True)
    str_app.markdown(
        '<div class="section-subtitle">'
        'Lleva tu taller o marca de Gamarra directamente hacia clientes que valoran la calidad y pagan lo justo.'
        '</div>',
        unsafe_allow_html=True
    )

    a, b = str_app.columns(2)

    with a:
        str_app.markdown("""
        ### Beneficios para tu negocio

        - Vitrina digital profesional sin intermediarios
        - Conexión directa B2B y B2C con compradores de nivel socioeconómico alto
        - Mayor rentabilidad al posicionar tu marca propia
        - Exposición de tus materiales y especialidades de costura
        - Ventas ágiles mediante enlace directo a WhatsApp
        """)

    with b:
        str_app.markdown("""
        ### Requisitos para postular

        **Buscamos talleres y marcas que:**

        - Fabriquen localmente en Gamarra / Lima
        - Utilicen insumos de alta calidad (Algodón Pima, Jersey pesado, etc.)
        - Cuenten con fotos o catálogo claro de sus prendas
        - Brinden atención rápida y profesional a consultas
        """)

    str_app.write("")
    str_app.markdown("### Registro de Taller o Marca")

    with str_app.form("empresa_form"):
        nombre = str_app.text_input("Nombre de la marca o taller")
        contacto = str_app.text_input("Persona de contacto")
        whatsapp = str_app.text_input("Número de WhatsApp comercial")
        especialidad = str_app.selectbox(
            "Especialidad principal",
            ["Polos y Básico", "Poleras y Hoodies", "Pantalones / Drill", "Streetwear", "Moda Casual", "Premium Pima"]
        )
        descripcion = str_app.text_area("Cuéntanos brevemente qué tipo de prendas produces y qué los diferencia")

        enviar = str_app.form_submit_button(
            "Enviar postulación",
            type="primary",
            use_container_width=True
        )

        if enviar:
            if not nombre or not contacto or not whatsapp:
                str_app.error("Por favor completa los campos obligatorios (Nombre, Contacto y WhatsApp).")
            else:
                str_app.success(
                    "¡Solicitud recibida con éxito! En la versión en producción, estos datos se sincronizarán con tu base de datos."
                )


# -----------------------------
# FOOTER
# -----------------------------
str_app.markdown("""
<div class="footer">
    <b>Vanguardia Peruana</b> · Conectando la alta manufactura de Gamarra con el cliente exigente<br>
    MVP de Streamlit · Hecho en Perú 🇵🇪
</div>
""", unsafe_allow_html=True)
