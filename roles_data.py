# -*- coding: utf-8 -*-
"""Roles de SEDENA México RP.

Orden de ARRIBA hacia ABAJO = jerarquía en Discord:
Fundador (el más alto) ... Ciudadano (el más bajo).
Los roles con "separador": True son solo divisores visuales (sin permisos).
"""


def _rol(nombre, color, permisos=None, hoist=False, mencionable=False):
    return {
        "nombre": nombre,
        "color": color,
        "permisos_guild": permisos or {},
        "hoist": hoist,              # mostrarlo separado en la lista de miembros
        "mencionable": mencionable,  # que cualquiera pueda @mencionarlo
    }


def _sep(titulo):
    return {
        "nombre": f"━━━ {titulo} ━━━",
        "color": "#99AAB5",
        "permisos_guild": {},
        "hoist": False,
        "mencionable": False,
        "separador": True,
    }


# ── Nombres de roles (los usa permisos.py) ───────────────────────────────
ROL_FUNDADOR = "Fundador"
ROL_DIRECTOR_GENERAL = "Director General"
ROL_ALTO_MANDO = "Alto Mando"
ROL_JEFE_ESTADO_MAYOR = "Jefe de Estado Mayor"
ROL_ADMINISTRADOR = "Administrador"
ROL_MODERADOR = "Moderador"
ROL_COORD_PERSONAL = "Coordinador de Personal"
ROL_RECLUTADOR = "Reclutador"
ROL_COORD_EVENTOS = "Coordinador de Eventos"
ROL_INSTRUCTOR = "Instructor"

ROL_EJERCITO = "Ejército Mexicano"
ROL_FUERZA_AEREA = "Fuerza Aérea Mexicana"
ROL_ARMADA = "Armada de México"
ROL_GUARDIA_NACIONAL = "Guardia Nacional"
ROL_UNIDADES_ESPECIALES = "Unidades Especiales"

ROL_DIV_ROBLOX = "División Roblox"
ROL_DIV_02 = "División de Juego 02"
ROL_DIV_03 = "División de Juego 03"
ROL_DIV_MULTI = "División Multijuegos"

ROL_ORG_ALIADA = "Organización Aliada"
ROL_REP_ORG = "Representante de Organización"
ROL_COLAB_EVENTO = "Colaborador de Evento"
ROL_INVITADO = "Invitado"

ROL_VERIFICADO = "Verificado"
ROL_SILENCIADO = "Silenciado"
ROL_CIUDADANO = "Ciudadano"


ROLES = [
    # ── Máxima autoridad ────────────────────────────────────────────────
    _rol(ROL_FUNDADOR, "#F1C40F", {"administrator": True}, hoist=True),

    # ── 01 · Dirección y administración ─────────────────────────────────
    _sep("DIRECCIÓN Y ADMINISTRACIÓN"),
    _rol(ROL_DIRECTOR_GENERAL, "#9B59B6", {
        "manage_messages": True, "manage_threads": True, "manage_events": True,
        "mention_everyone": True, "move_members": True,
    }, hoist=True),
    _rol(ROL_ALTO_MANDO, "#8E44AD", {
        "manage_messages": True, "manage_threads": True, "manage_events": True,
        "mention_everyone": True,
    }, hoist=True),
    _rol(ROL_JEFE_ESTADO_MAYOR, "#6C3483", {
        "manage_messages": True, "manage_threads": True, "manage_events": True,
    }, hoist=True),
    _rol(ROL_ADMINISTRADOR, "#E91E63", {
        "manage_guild": True, "manage_channels": True, "manage_roles": True,
        "manage_messages": True, "manage_events": True, "kick_members": True,
        "ban_members": True, "moderate_members": True, "view_audit_log": True,
    }, hoist=True),
    _rol(ROL_MODERADOR, "#00BCD4", {
        "manage_messages": True, "manage_threads": True, "kick_members": True,
        "moderate_members": True, "view_audit_log": True,
        "mute_members": True, "deafen_members": True, "move_members": True,
    }, hoist=True),
    _rol(ROL_COORD_PERSONAL, "#E67E22", {"manage_nicknames": True}),
    _rol(ROL_RECLUTADOR, "#48C9B0", mencionable=True),
    _rol(ROL_COORD_EVENTOS, "#AF7AC5", {"manage_events": True}, mencionable=True),
    _rol(ROL_INSTRUCTOR, "#F5B041"),

    # ── 02 · Rangos militares de roleplay (de mayor a menor) ────────────
    _sep("RANGOS MILITARES"),
    _rol("General de División", "#8E0000"),
    _rol("General de Brigada", "#A93226"),
    _rol("General Brigadier", "#B03A2E"),
    _rol("Coronel", "#B9770E"),
    _rol("Teniente Coronel", "#CA6F1E"),
    _rol("Mayor", "#D4AC0D"),
    _rol("Capitán Primero", "#2874A6"),
    _rol("Capitán Segundo", "#2E86C1"),
    _rol("Teniente", "#3498DB"),
    _rol("Subteniente", "#5DADE2"),
    _rol("Sargento Primero", "#117864"),
    _rol("Sargento Segundo", "#148F77"),
    _rol("Cabo", "#229954"),
    _rol("Soldado de Primera", "#626567"),
    _rol("Soldado", "#797D7F"),
    _rol("Recluta", "#A6ACAF"),

    # ── 03 · Ramas ──────────────────────────────────────────────────────
    _sep("RAMAS"),
    _rol(ROL_EJERCITO, "#556B2F", mencionable=True),
    _rol(ROL_FUERZA_AEREA, "#85C1E9", mencionable=True),
    _rol(ROL_ARMADA, "#1F618D", mencionable=True),
    _rol(ROL_GUARDIA_NACIONAL, "#5D6D7E", mencionable=True),
    _rol(ROL_UNIDADES_ESPECIALES, "#922B21", mencionable=True),

    # ── 04 · Divisiones de juegos ───────────────────────────────────────
    _sep("DIVISIONES DE JUEGOS"),
    _rol(ROL_DIV_ROBLOX, "#5865F2", mencionable=True),
    _rol(ROL_DIV_02, "#5865F2", mencionable=True),
    _rol(ROL_DIV_03, "#5865F2", mencionable=True),
    _rol(ROL_DIV_MULTI, "#5865F2", mencionable=True),

    # ── 05 · Académicos ─────────────────────────────────────────────────
    _sep("ACADEMIA Y FORMACIÓN"),
    _rol("Graduado de Academia", "#1ABC9C"),
    _rol("Alumno en Formación", "#D4AC0D"),
    _rol("Cadete", "#A6ACAF"),
    _rol("Aspirante", "#D5D8DC"),

    # ── 05 · Actividad ──────────────────────────────────────────────────
    _sep("ESTADO DE MIEMBRO"),
    _rol("Miembro Activo", "#27AE60"),
    _rol("Miembro en Reserva", "#7F8C8D"),
    _rol("Ausente Autorizado", "#95A5A6"),

    # ── 06 · Relaciones externas ────────────────────────────────────────
    _sep("RELACIONES EXTERNAS"),
    _rol(ROL_ORG_ALIADA, "#16A085"),
    _rol(ROL_REP_ORG, "#148F77"),
    _rol(ROL_COLAB_EVENTO, "#8E44AD"),
    _rol(ROL_INVITADO, "#95A5A6"),

    # ── 08 · Notificaciones ─────────────────────────────────────────────
    _sep("NOTIFICACIONES"),
    _rol("Avisos Generales", "#7289DA", mencionable=True),
    _rol("Avisos de Eventos", "#7289DA", mencionable=True),
    _rol("Avisos de Reclutamiento", "#7289DA", mencionable=True),
    _rol("Avisos de Roblox", "#7289DA", mencionable=True),
    _rol("Avisos de Otras Divisiones", "#7289DA", mencionable=True),

    # ── Acceso y seguridad ──────────────────────────────────────────────
    _sep("ACCESO Y SEGURIDAD"),
    _rol(ROL_VERIFICADO, "#2ECC71"),
    _rol(ROL_SILENCIADO, "#7F8C8D"),

    # ── Rol base (el más bajo) ──────────────────────────────────────────
    _rol(ROL_CIUDADANO, "#BDC3C7"),
]


# ── Grupos de roles (los usa permisos.py para armar el acceso a canales) ─
# Administración de Discord
GRUPO_STAFF = [ROL_FUNDADOR, ROL_DIRECTOR_GENERAL, ROL_ADMINISTRADOR, ROL_MODERADOR]

# Dirección que supervisa todo el servidor (ve todas las áreas internas)
GRUPO_SUPERVISION = [
    ROL_FUNDADOR, ROL_DIRECTOR_GENERAL, ROL_ALTO_MANDO, ROL_JEFE_ESTADO_MAYOR,
    ROL_ADMINISTRADOR, ROL_MODERADOR,
]

# Alto mando (sin moderadores)
GRUPO_MANDO = [
    ROL_FUNDADOR, ROL_DIRECTOR_GENERAL, ROL_ALTO_MANDO, ROL_JEFE_ESTADO_MAYOR,
    ROL_ADMINISTRADOR,
]

# Toda la sección "Dirección y administración"
GRUPO_DIRECCION = [
    ROL_FUNDADOR, ROL_DIRECTOR_GENERAL, ROL_ALTO_MANDO, ROL_JEFE_ESTADO_MAYOR,
    ROL_ADMINISTRADOR, ROL_MODERADOR, ROL_COORD_PERSONAL, ROL_RECLUTADOR,
    ROL_COORD_EVENTOS, ROL_INSTRUCTOR,
]

# Quien entra a las áreas internas de miembros: Verificado + la dirección
GRUPO_MIEMBROS = [ROL_VERIFICADO] + GRUPO_DIRECCION

# Organizaciones externas
GRUPO_DIPLOMACIA = [ROL_ORG_ALIADA, ROL_REP_ORG]
