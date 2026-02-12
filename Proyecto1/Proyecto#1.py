#Inputs con print
proyecto = input("Escriba el nombre del proyecto: ")
horas_estimadas = int(input("Escriba las horas estimadas para el proyecto: "))
valor_hora = float(input("Escriba el valor por hora: "))
plazo_estimado = int(input("Escriba el plazo estimado en días: "))
#Outputs con print
print(proyecto)
print(horas_estimadas)
print(valor_hora)
print(plazo_estimado)
#Calculos con python
total_costo = horas_estimadas * valor_hora #Calculo del costo total del proyecto
print(total_costo)
#Generar PDF
from fpdf import FPDF #Importamos la clase FPDF de la libreria fpdf
pdf = FPDF() #Creamos una instancia de la clase FPDF
pdf.add_page() #Agregamos una página al PDF
pdf.set_font("Arial", size=12) #Establecemos la fuente y el tamaño del texto
pdf.image(r"C:\PYTHON\.venv\Template.png", 0, 0) #Agregamos un template para el proyecto
pdf.text(115, 145, proyecto) #Agregamos el nombre del proyecto al PDF
pdf.text(115, 160, str(horas_estimadas)) #Agregamos el nombre del proyecto al PDF
pdf.text(115, 175, str(valor_hora)) #Agregamos el nombre del proyecto al PDF
pdf.text(115, 190, str(plazo_estimado)) #Agregamos el nombre del proyecto al PDF
pdf.text(115, 205, str(total_costo)) #Agregamos el nombre del proyecto al PDF
pdf.output(r"C:\PYTHON\.venv\proyecto.pdf") #Guardamos el PDF con el nombre "proyecto.pdf"