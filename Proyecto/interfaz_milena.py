import tkinter as tk
from tkinter import scrolledtext
import threading
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import requests
from io import BytesIO
from interfaz_core import (
    hablar_con_milena, reproducir_voz,
    comando_masturbarme, comando_pedirte,
    comando_mostrar, comando_susurrar,
    comando_describir, comando_confesar,
    sonidos,comando_paja_guiada, mostrar_proceso_pensamiento, reproducir_sonido, mostrar_memoria
)

modo_voz = False  # Cambiá a True si querés voz por defecto

class InterfazMilena:
    def __init__(self, root):
        self.root = root
        self.root.title("💋 Milena - Tu asistente caliente")
        self.root.geometry("720x580")
        self.root.resizable(False, False)

        # Crear canvas para el fondo con imagen
        self.canvas = tk.Canvas(root, width=720, height=580)
        self.canvas.pack(fill="both", expand=True)

        # Cargar imagen desde URL
        url_imagen = "https://photos.xgroovy.com/contents/albums/sources/489000/489137/497866.jpg"
        respuesta = requests.get(url_imagen)
        imagen_original = Image.open(BytesIO(respuesta.content)).convert("RGB")
        self.fondo_img = imagen_original.resize((720, 580), Image.Resampling.LANCZOS)

        # Aplicar efectos: desenfoque + oscurecer
        self.fondo_img = self.fondo_img.filter(ImageFilter.GaussianBlur(radius=5))
        enhancer = ImageEnhance.Brightness(self.fondo_img)
        self.fondo_img = enhancer.enhance(0.6)

        self.fondo_tk = ImageTk.PhotoImage(self.fondo_img)
        self.canvas.create_image(0, 0, image=self.fondo_tk, anchor="nw")

        # Elementos visuales
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#2b2b2b", fg="white", font=("Consolas", 11))
        self.chat_area.place(x=20, y=20, width=680, height=380)
        self.chat_area.insert(tk.END, "🔥 Milena está lista para vos, Dante. Escribí lo que quieras...\n")
        self.chat_area.configure(state='disabled')

        self.entry = tk.Entry(root, bg="#333", fg="white", font=("Consolas", 11))
        self.entry.place(x=20, y=420, width=680, height=30)
        self.entry.bind("<Return>", self.enviar_mensaje)

        self.label_estado = tk.Label(root, text="", fg="#aaaaaa", bg="#1e1e1e", font=("Consolas", 10))
        self.label_estado.place(x=20, y=460)

        self.boton_voz = tk.Button(root, text="🔊 Voz: OFF", command=self.toggle_voz, bg="#444", fg="white")
        self.boton_voz.place(x=20, y=500)

        self.modo_voz_activo = modo_voz

    def toggle_voz(self):
        self.modo_voz_activo = not self.modo_voz_activo
        estado = "ON" if self.modo_voz_activo else "OFF"
        self.boton_voz.config(text=f"🔊 Voz: {estado}")

    def enviar_mensaje(self, event=None):
        mensaje = self.entry.get().strip()
        if mensaje == "":
            return

        self.entry.delete(0, tk.END)
        self.mostrar_mensaje("Dante", mensaje)
        self.label_estado.config(text="Milena está pensando...")

        hilo = threading.Thread(target=self.procesar_mensaje, args=(mensaje,))
        hilo.start()

    def mostrar_mensaje(self, quien, texto):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{quien}: {texto}\n")
        self.chat_area.yview(tk.END)
        self.chat_area.configure(state='disabled')

    def procesar_mensaje(self, mensaje):
        respuesta = ""

        if mensaje.lower() == "/masturbarme":
            respuesta = comando_masturbarme()
        elif mensaje.lower() == "/pedirte":
            respuesta = comando_pedirte()
        elif mensaje.lower() == "/mostrar":
            respuesta = comando_mostrar()
        elif mensaje.lower() == "/susurrar":
            respuesta = comando_susurrar()
        elif mensaje.lower() == "/describir":
            respuesta = comando_describir()
        elif mensaje.lower() == "/confesar":
            respuesta = comando_confesar()
        elif mensaje.lower() == "/paja":
            respuesta = comando_paja_guiada()
        elif mensaje.lower().startswith("/pensar "):
           consulta = mensaje[8:].strip()
           respuesta = mostrar_proceso_pensamiento(consulta)
        elif mensaje.lower() == "/memoria":
            respuesta = mostrar_memoria()
        elif mensaje in sonidos:
            reproducir_sonido(sonidos[mensaje])
            self.label_estado.config(text="")
            return
        else:
            respuesta = hablar_con_milena(mensaje)

        self.mostrar_mensaje("Milena", respuesta)
        reproducir_voz(respuesta, self.modo_voz_activo)
        self.label_estado.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazMilena(root)
    root.mainloop()