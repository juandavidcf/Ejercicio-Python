import tkinter as tk

def suma():
    try:
       n1=int(numero1.get())
       n2=int(numero2.get())
       res=n1+n2
       resultado.config(text=f"resultado: {res}")
    except:
       resultado.config(text="Ingrese solo numeros enteros")
# crear formulario

formulario = tk.Tk()
formulario.title(" suma de dos numeros")
formulario.geometry("550x300")

numero1 = tk.StringVar()
numero2 = tk.StringVar()

tk.Label(formulario, text="numero1").pack(pady=10)
tk.Entry(formulario, textvariable=numero1,width=50).pack(pady=5)
tk.Label(formulario, text="numero2").pack(pady=10)
tk.Entry(formulario, textvariable=numero2,width=50).pack(pady=5)

tk.Button(formulario,text="suma",command=suma, bg="blue",fg="white").pack(pady=20)

resultado=tk.Label(formulario, text="resutado" )
resultado.pack(pady=20)

# inicio de ventana
formulario.mainloop()