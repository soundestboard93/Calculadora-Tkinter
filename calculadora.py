import tkinter as tk


def limpiar_entrada():
  global limpiar_despues_de_resultado
  if limpiar_despues_de_resultado:
    entrada.delete(0, tk.END)
    limpiar_despues_de_resultado = False


def agregar_texto(texto):
  global limpiar_despues_de_resultado
  limpiar_entrada()
  entrada.insert(tk.END, texto)


def calcular():
  global limpiar_despues_de_resultado
  try:
    resultado.set(eval(entrada.get()))
    limpiar_despues_de_resultado = True
  except Exception as e:
    resultado.set("Error")


def borrar():
  entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("250x300")
ventana.configure(bg="#F0F0F0")

resultado = tk.StringVar()

limpiar_despues_de_resultado = False

entrada = tk.Entry(ventana,
                   textvariable=resultado,
                   font=("Arial", 20),
                   bd=5,
                   insertwidth=4,
                   width=10,
                   justify="right",
                   bg="#FFFFFF")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("4", 2, 0),
           ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("1", 3, 0), ("2", 3, 1),
           ("3", 3, 2), ("-", 3, 3), ("0", 4, 0), (".", 4, 1), ("=", 4, 2),
           ("+", 4, 3)]

for (texto, fila, columna) in botones:
  boton = tk.Button(ventana,
                    text=texto,
                    font=("Arial", 14),
                    bd=4,
                    padx=10,
                    pady=10,
                    bg="#D3D3D3",
                    activebackground="#B0B0B0",
                    command=lambda t=texto: agregar_texto(t))
  boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_borrar = tk.Button(ventana,
                         text="C",
                         font=("Arial", 14),
                         bd=4,
                         padx=10,
                         pady=10,
                         bg="#FF6347",
                         activebackground="#FF4500",
                         command=borrar)
boton_borrar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

boton_calcular = tk.Button(ventana,
                           text="=",
                           font=("Arial", 14),
                           bd=4,
                           padx=10,
                           pady=10,
                           bg="#90EE90",
                           activebackground="#7CFC00",
                           command=calcular)
boton_calcular.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

ventana.mainloop()
