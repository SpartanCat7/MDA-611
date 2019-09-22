from Lector_de_Datos import Lector_de_Datos

lector = Lector_de_Datos()

lector.guardar_a_json(lector.leer_de_excel("Mineria de datos.xlsx"),lector.leer_personalidades_de_excel("Mineria de datos.xlsx"),"archivo.txt")