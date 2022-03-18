
def personas_tecnicos(trabajadores,sustisuto, *args):

    print("Personas: " + trabajadores)
    print("Sustituto: " + sustisuto)
    for x in args:
          print("perosnas: " + x)

lista_tecnicos=["Andres","Ana","Alejando","Andrea"]
personas_tecnicos("Antonio","Armando", *lista_tecnicos)