API Pública
***********

Datasets
========

En este momento existen dos datasets:

   * Paradas
   * Rutas

.. automodule:: api pública de datos

Paradas
=======

Para obtener la información de paradas se pueden usar los siguientes endpoints:

/api/parada -- GET
==================

Este endpoint se utiliza para obtener todas las paradas disponibles.

La respuesta es una lista de todas las paradas en formato JSON.

Ejemplo::

  curl -XGET quitoabierto.org:5000/api/parada

Respuesta::

  [
    {
      "location": {"lat": 100, "lng": 100},
      "geoJSON": {
        "type": "Feature",
        "properties": {"name": "Parada 1", "description": "Cerca de la carolina"},
        "geometry": {"coordinates": [100, 100], "type": "Point"}
      },
      "name": "Parada 1",
      "description": "Cerca de la Carolina", "type": "parada"
    }
  ]

/api/parada/cercana -- GET
==========================

Este endpoint se utiliza para retornar la parada más cercana a la unicación que
se provee.

La respuesta es la parada más cercana que se puede encontrar.

Ejemplo::

  curl -XGET quitoabierto.org:5000/api/parada/cercana -d '{"location": {"lat": 100, "lng": 200}}'

Respuesta::

  {
    "location": {"lat": 100, "lng": 100},
    "geoJSON": {
      "type": "Feature",
      "properties": {"name": "Parada 1", "description": "Cerca de la carolina"},
      "geometry": {"coordinates": [100, 100], "type": "Point"}
    },
    "name": "Parada 1",
    "description": "Cerca de la Carolina",
    "type": "parada"
  }

Rutas
=====

Para obtener la información de paradas se pueden usar los siguientes endpoints:

/api/ruta -- GET
================

Este endpoint se utiliza para obtener todas las rutas disponibles.

La respuesta es una lista de todas las rutas en formato JSON.

Ejemplo::

  # TODO

Respuesta::

  # TODO

/api/ruta/<route_name> -- GET
=============================

Este endpoint se utiliza para retornar una ruta por nombre.
La respuesta es la ruta con todos sus puntos.

Ejemplo::

  # TODO

Respuesta::

  # TODO
