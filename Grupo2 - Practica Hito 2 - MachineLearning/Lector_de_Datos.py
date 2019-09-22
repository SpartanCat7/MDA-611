class Lector_de_Datos:
    def leer_de_excel(self,nombre_excel):
        import xlrd
        from pathlib import Path
        import os
        wb = xlrd.open_workbook(os.path.join(Path().absolute(), nombre_excel))
        sheet = wb.sheet_by_index(0)
        nueva_lista = []
        for i in range(sheet.nrows):
            if(i != 0):
                respuesta = [sheet.cell_value(i, 2),sheet.cell_value(i, 3),sheet.cell_value(i, 4),sheet.cell_value(i, 5),sheet.cell_value(i, 6)]
                nueva_lista.append(respuesta)

        return nueva_lista

    def guardar_a_json(self, datos, personalidades, nombre_archivo):
        import json
        
        data = {}
        data["datos"] = datos
        data["personalidades"] = personalidades

        with open(nombre_archivo,'w') as outfile:
            json.dump(data,outfile)

        return True

    def leer_de_json(self, nombre_archivo):
        import json
        with open(nombre_archivo) as json_file:
            data = json.load(json_file)
            lista_datos = data["datos"]

        return lista_datos

    def leer_personalidades_de_excel(self,nombre_excel):
        import xlrd
        from pathlib import Path
        import os
        wb = xlrd.open_workbook(os.path.join(Path().absolute(), nombre_excel))
        sheet = wb.sheet_by_index(0)
        lista_personalidades = []
        for i in range(sheet.nrows):
            if(i != 0):
                respuesta = sheet.cell_value(i, 7)
                lista_personalidades.append(respuesta)

        return lista_personalidades

    def leer_personalidades_de_json(self, nombre_archivo):
        import json
        with open(nombre_archivo) as json_file:
            data = json.load(json_file)
            lista_personalidades = data["personalidades"]

        return lista_personalidades