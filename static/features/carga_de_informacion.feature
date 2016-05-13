# language: es

Característica: Cargar información
  Escenario: Abriendo la página de inicio
    Dado que ingreso a la aplicación
    Cuando estoy en la página de inicio
    Entonces veo un mapa

  Escenario: Guardar una ubicación
    Dado que ingreso a la aplicación
    Cuando estoy en la página de inicio
    Y lleno el formulario con los siguientes datos:
      | nombre             | descripción                       |
      | Parada la carolina | Esta es una parada de la linea #5 |
    Cuando envío el formulario
    Entonces veo un mensaje de confirmación
