# -*- coding: utf-8 -*-
"""Categorías y canales de SEDENA México RP.

"acceso" (categoría) y "acceso_canal" (canal) son claves de permisos.py.
Si un canal no tiene "acceso_canal", hereda el acceso de su categoría.
comunidad="reglas"/"actualizaciones": usa el canal que creó Comunidad (se detecta solo).
anuncio=True: canal de tipo Anuncio (requiere Comunidad).
"""


def T(nombre, acceso=None, **extra):
    """Canal de texto."""
    d = {"nombre": nombre, "tipo": "texto"}
    if acceso:
        d["acceso_canal"] = acceso
    d.update(extra)
    return d


def V(nombre, acceso=None):
    """Canal de voz."""
    d = {"nombre": nombre, "tipo": "voz"}
    if acceso:
        d["acceso_canal"] = acceso
    return d


def C(nombre, acceso, canales):
    return {"nombre": nombre, "acceso": acceso, "canales": canales}


# No se usan foros en esta estructura.
TAGS_FORO = []
HILOS_FORO = []

ESTRUCTURA = [
    C("01 │ CENTRO DE INFORMACIÓN", "info", [
        T("📌│bienvenida"),
        T("📢│anuncios", anuncio=True),
        T("📑│reglamento", comunidad="reglas"),   # el canal de reglas que creó Comunidad
        T("🏛️│sobre-la-organizacion"),
        T("🪪│identificacion"),
        T("❓│preguntas-frecuentes"),
        T("🔗│enlaces-oficiales"),
    ]),

    C("02 │ INGRESO Y RECLUTAMIENTO", "info", [
        T("📋│requisitos-de-ingreso"),
        T("📝│solicitudes", "publico"),
        T("📨│entrevistas", "reclutamiento_staff"),
        T("✅│admitidos"),
        T("❌│solicitudes-rechazadas", "reclutamiento_staff"),
        T("🎓│proceso-de-ingreso"),
    ]),

    C("03 │ COMUNIDAD", "publico", [
        T("💬│chat-general"),
        T("👋│presentaciones"),
        T("🎮│videojuegos"),
        T("📸│capturas-y-videos"),
        T("🤝│alianzas"),
        T("💡│sugerencias"),
    ]),

    C("04 │ ALTO MANDO", "mando", [
        T("🔒│chat-del-mando"),
        T("🔒│reuniones-de-mando"),
        T("🔒│decisiones-oficiales"),
        T("🔒│registro-de-ascensos"),
        T("🔒│registro-de-sanciones"),
        T("🔒│planificacion-de-eventos"),
    ]),

    C("05 │ CUARTEL GENERAL", "miembros_lectura", [
        T("🏛️│cuartel-general"),
        T("📋│estructura-organizativa"),
        T("📑│directivas-internas"),
        T("📆│calendario-de-actividades"),
        T("📊│informes-de-unidades"),
        T("📚│archivo-institucional"),
    ]),

    C("06 │ EJÉRCITO MEXICANO", "ejercito", [
        T("🪖│chat-del-ejercito"),
        T("📢│anuncios-del-ejercito", "ejercito_lectura"),
        T("📋│lista-de-miembros", "ejercito_lectura"),
        T("🎓│academia-del-ejercito"),
        T("🎭│actividades-de-rol"),
        T("📊│informes-del-ejercito"),
    ]),

    C("07 │ FUERZA AÉREA MEXICANA", "fuerza_aerea", [
        T("✈️│chat-de-fuerza-aerea"),
        T("📢│anuncios-aereos", "fuerza_aerea_lectura"),
        T("📋│registro-de-pilotos", "fuerza_aerea_lectura"),
        T("🎓│academia-de-vuelo"),
        T("🛩️│rol-de-aviacion"),
        T("📊│informes-de-vuelo"),
    ]),

    C("08 │ ARMADA DE MÉXICO", "armada", [
        T("⚓│chat-de-la-armada"),
        T("📢│anuncios-navales", "armada_lectura"),
        T("📋│registro-de-tripulacion", "armada_lectura"),
        T("🎓│academia-naval"),
        T("🚢│rol-naval"),
        T("📊│informes-navales"),
    ]),

    C("09 │ GUARDIA NACIONAL", "guardia", [
        T("🛡️│chat-de-guardia"),
        T("📢│anuncios-de-guardia", "guardia_lectura"),
        T("📋│lista-de-personal", "guardia_lectura"),
        T("🎓│academia-de-guardia"),
        T("🏙️│rol-de-seguridad"),
        T("📊│informes-de-guardia"),
    ]),

    C("10 │ UNIDADES ESPECIALES", "especiales", [
        T("🎖️│unidades-especiales"),
        T("📢│anuncios-de-unidades", "especiales_lectura"),
        T("📋│registro-de-unidades", "especiales_lectura"),
        T("🎓│formacion-especial"),
        T("🎭│rol-de-unidades"),
        T("📊│informes-de-unidades"),
    ]),

    C("11 │ OPERACIONES CONJUNTAS", "miembros", [
        T("🌐│coordinacion-de-juegos"),
        T("📅│calendario-de-eventos", "miembros_lectura"),
        T("🤝│eventos-conjuntos"),
        T("📝│registro-de-eventos", "miembros_lectura"),
        T("📋│informes-de-eventos", "miembros_lectura"),
        T("🏆│logros-y-reconocimientos", "miembros_lectura"),
    ]),

    C("12 │ DIVISIONES DE JUEGOS", "miembros", [
        T("🎮│directorio-de-juegos", "miembros_lectura"),
        T("🟥│division-de-roblox", "div_roblox"),
        T("🟦│division-de-juegos-02", "div_02"),
        T("🟩│division-de-juegos-03", "div_03"),
        T("📑│reglas-de-servidores", "miembros_lectura"),
        T("📸│evidencias-de-juego"),
    ]),

    C("13 │ ACADEMIA Y FORMACIÓN", "academia_lectura", [
        T("📚│manual-del-miembro"),
        T("🎓│formacion-inicial"),
        T("📖│rangos-y-protocolo"),
        T("🎭│practicas-de-rol", "miembros"),
        T("📝│evaluaciones"),
        T("🏅│graduaciones"),
    ]),

    C("14 │ PERSONAL Y REGISTROS", "personal", [
        T("🪪│expedientes"),
        T("📈│ascensos-y-promociones", "miembros_lectura"),
        T("🔄│cambios-de-rama"),
        T("📋│control-de-asistencia"),
        T("🏅│reconocimientos", "miembros_lectura"),
        T("📦│bajas-y-reingresos"),
    ]),

    C("15 │ ALIANZAS Y DIPLOMACIA", "info", [
        T("🤝│solicitud-de-alianza", "publico"),
        T("🌐│organizaciones-aliadas"),
        T("📢│comunicados-externos", anuncio=True),
        T("📅│eventos-conjuntos", "diplomacia"),
        T("📋│registro-de-alianzas", "supervision"),
    ]),

    C("16 │ CENTRO DE SOPORTE", "info", [
        T("🎫│crear-ticket"),
        T("❓│ayuda-general", "publico"),
        T("⚠️│reportar-problemas", "publico"),
        T("👤│contactar-al-personal"),
        T("📨│tickets-resueltos", "supervision"),
    ]),

    C("17 │ ADMINISTRACIÓN Y MODERACIÓN", "staff", [
        T("🔒│chat-del-personal"),
        T("🔒│anuncios-internos", comunidad="actualizaciones"),  # el canal moderator-only que creó Comunidad
        T("🔒│reportes-de-miembros"),
        T("🔒│registro-de-moderacion"),
        T("🔒│reuniones-del-personal"),
        T("🔒│recursos-administrativos"),
    ]),

    C("18 │ CANALES DE VOZ", "miembros", [
        V("🔊│sala-general", "publico"),
        V("🔊│alto-mando", "mando"),
        V("🔊│ejercito", "ejercito"),
        V("🔊│fuerza-aerea", "fuerza_aerea"),
        V("🔊│armada", "armada"),
        V("🔊│guardia-nacional", "guardia"),
        V("🔊│operaciones-conjuntas"),
        V("🔊│academia"),
        V("🔊│sala-del-personal", "staff"),
        V("🔊│ausentes"),
    ]),

    C("19 │ RELACIONES EXTERNAS", "info", [
        T("🤝│solicitudes-de-afiliacion", "publico"),
        T("📋│registro-de-comunidades", "supervision"),
        T("📢│anuncios-externos", anuncio=True),
        T("📅│colaboraciones", "diplomacia"),
        T("📨│contacto-institucional", "publico"),
    ]),
]
