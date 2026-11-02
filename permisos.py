# -*- coding: utf-8 -*-
"""Permisos de categorías y canales.

Cada "acceso" se define como (quién VE el canal, quién ESCRIBE).
 - Si ver == escribir: todos los que ven pueden escribir (no se toca nada más).
 - Si escribir es más corto que ver: es un canal de solo lectura para el resto.
 - "@everyone" significa canal público.

El rol Silenciado queda sin poder escribir, reaccionar ni hablar en todos los canales.
"""

import discord

from roles_data import (
    GRUPO_DIPLOMACIA, GRUPO_DIRECCION, GRUPO_MANDO, GRUPO_MIEMBROS,
    GRUPO_STAFF, GRUPO_SUPERVISION,
    ROL_ARMADA, ROL_COORD_EVENTOS, ROL_COORD_PERSONAL, ROL_DIV_02, ROL_DIV_03,
    ROL_DIV_MULTI, ROL_DIV_ROBLOX, ROL_EJERCITO, ROL_FUERZA_AEREA,
    ROL_GUARDIA_NACIONAL, ROL_INSTRUCTOR, ROL_RECLUTADOR, ROL_SILENCIADO,
    ROL_UNIDADES_ESPECIALES,
)

EVERYONE = "@everyone"

_ESCRITURA_NEGADA = dict(
    send_messages=False, send_messages_in_threads=False,
    create_public_threads=False, create_private_threads=False,
)
_ESCRITURA_PERMITIDA = dict(
    send_messages=True, send_messages_in_threads=True, create_public_threads=True,
)
_SILENCIADO = dict(
    send_messages=False, send_messages_in_threads=False, add_reactions=False,
    create_public_threads=False, create_private_threads=False,
    speak=False, stream=False,
)

_PERSONAL = GRUPO_SUPERVISION + [ROL_COORD_PERSONAL, ROL_RECLUTADOR]

ACCESOS = {
    # Público: todos lo ven; solo la dirección escribe
    "info": ([EVERYONE], GRUPO_DIRECCION),
    # Público: todos lo ven y escriben
    "publico": ([EVERYONE], [EVERYONE]),
    # Privados
    "mando": (GRUPO_MANDO, GRUPO_MANDO),
    "supervision": (GRUPO_SUPERVISION, GRUPO_SUPERVISION),
    "staff": (GRUPO_STAFF, GRUPO_STAFF),
    "personal": (_PERSONAL, _PERSONAL),
    "reclutamiento_staff": (_PERSONAL, _PERSONAL),
    # Áreas de miembros (necesitan el rol Verificado)
    "miembros": (GRUPO_MIEMBROS, GRUPO_MIEMBROS),
    "miembros_lectura": (GRUPO_MIEMBROS, GRUPO_DIRECCION),
    "academia_lectura": (GRUPO_MIEMBROS, GRUPO_SUPERVISION + [ROL_INSTRUCTOR]),
    # Organizaciones externas + dirección
    "diplomacia": (
        GRUPO_SUPERVISION + [ROL_COORD_EVENTOS] + GRUPO_DIPLOMACIA,
        GRUPO_SUPERVISION + [ROL_COORD_EVENTOS] + GRUPO_DIPLOMACIA,
    ),
}

# Ramas: la rama + la supervisión. "<rama>" escribe todos; "<rama>_lectura" solo la supervisión.
_RAMAS = {
    "ejercito": ROL_EJERCITO,
    "fuerza_aerea": ROL_FUERZA_AEREA,
    "armada": ROL_ARMADA,
    "guardia": ROL_GUARDIA_NACIONAL,
    "especiales": ROL_UNIDADES_ESPECIALES,
}
for _clave, _rol in _RAMAS.items():
    _ver = [_rol] + GRUPO_SUPERVISION
    ACCESOS[_clave] = (_ver, _ver)
    ACCESOS[f"{_clave}_lectura"] = (_ver, GRUPO_SUPERVISION)

# Divisiones de juegos: su división + Multijuegos + la supervisión
for _clave, _rol in {"div_roblox": ROL_DIV_ROBLOX, "div_02": ROL_DIV_02, "div_03": ROL_DIV_03}.items():
    _ver = [_rol, ROL_DIV_MULTI] + GRUPO_SUPERVISION
    ACCESOS[_clave] = (_ver, _ver)


def _construir(clave, guild):
    if clave not in ACCESOS:
        raise ValueError(f"Acceso desconocido: '{clave}'")

    ver, escribir = ACCESOS[clave]
    ver = list(dict.fromkeys(ver))
    escribir = list(dict.fromkeys(escribir))

    roles = {}
    for r in guild.roles:
        roles.setdefault(r.name, r)

    def buscar(nombre):
        if nombre == EVERYONE:
            return guild.default_role
        rol = roles.get(nombre)
        if rol is None:
            raise ValueError(f"No existe el rol «{nombre}» en el servidor (¿falló su creación?)")
        return rol

    publico = EVERYONE in ver
    solo_lectura = set(escribir) != set(ver)

    permisos = {guild.default_role: {"view_channel": publico}}
    if solo_lectura:
        permisos[guild.default_role].update(_ESCRITURA_NEGADA)

    if not publico:
        for nombre in ver:
            permisos.setdefault(buscar(nombre), {})["view_channel"] = True

    if solo_lectura:
        for nombre in escribir:
            if nombre != EVERYONE:
                permisos.setdefault(buscar(nombre), {}).update(_ESCRITURA_PERMITIDA)

    permisos.setdefault(buscar(ROL_SILENCIADO), {}).update(_SILENCIADO)

    return {rol: discord.PermissionOverwrite(**kw) for rol, kw in permisos.items()}


def overwrites_categoria(acceso, guild):
    return _construir(acceso, guild)


def overwrites_canal_especifico(clave, guild):
    if not clave:
        return None
    return _construir(clave, guild)
