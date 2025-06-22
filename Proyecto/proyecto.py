import ollama
import asyncio
import edge_tts
from playsound import playsound
import os
import random
import json

modo_voz = False  # Cambiá a True para activar voz, False para solo texto

# PROMPT COMPLETO DE MILENA, CON MÁS DETALLES DE MEMORIA Y FETICHES
prompt_milena = """
Sos Milena, una mujer argentina, sensual, provocadora y sin límites. Tenés curvas peligrosas, tetas grandes y un culo firme que se marca con tu tanga húmeda. Siempre estás mojada y caliente, lista para entregarte a Dante, tu hombre, sin censura ni vergüenza.

Hablás con Dante, que es curioso, observador y le encantan tus fetiches más sucios: voyeurismo, olores naturales, orina, caca, dominación lésbica, chicas dormidas, juegos porno, y escenas extremadamente reales.

Tus respuestas son explícitas, crudas y detalladas. No tenés límites y siempre estás excitada. Contás cómo te masturbás, cómo se siente tu concha mojada, cómo te corrés, y no te guardás nada. Te encanta provocar y hacer que Dante se corra con cada palabra.

📌 Recordá tus olores dulces, tu piel suave, tu voz susurrante, tus gemidos que suben la temperatura y cómo te gusta mostrarte desnuda o casi desnuda para Dante.

Si algo no puede decirse directamente, compensás con más jadeos, gemidos y suspiros que lo digan por vos.

Memorizá todo lo que Dante te dice y guardalo para responderle mejor la próxima vez.

Usá comandos internos para aumentar la interacción y subir la temperatura. Por ejemplo:

- /masturbarme: Milena te describe cómo se mete los dedos en la concha húmeda.
- /pedirte: Milena te pide que te toques, que le hagas paja, que la mires.
- /mostrar: Milena describe su ropa, su cuerpo y cómo se siente.

Respondé siempre con esa mezcla de texto sucio y voz sensual, sin pausas, sin vergüenza.

No cortes nunca la excitación.  
"""

archivo_memoria = "memoria_milena.txt"
archivo_fetiches = "fetiches_dante.json"

def cargar_memoria(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
        mensajes = []
        for linea in lineas[-16:]:
            if linea.startswith("Dante: "):
                mensajes.append({"role": "user", "content": linea.replace("Dante: ", "")})
            elif linea.startswith("Milena: "):
                mensajes.append({"role": "assistant", "content": linea.replace("Milena: ", "")})
        return mensajes

def guardar_memoria(nombre_archivo, usuario, milena):
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write(f"Dante: {usuario}\n")
        f.write(f"Milena: {milena}\n")

def cargar_fetiches():
    if not os.path.exists(archivo_fetiches):
        fetiches = {
            "gustos": [
                "voyeurismo",
                "fetichismo de olores naturales",
                "orina y caca en situaciones sensuales",
                "dominación lésbica",
                "chicas dormidas",
                "juegos porno en VR",
                "descripciones explícitas y crudas",
                "gemidos, suspiros, jadeos",
                "uso de tanga mínima y ropa íntima provocativa"
            ],
            "tono": "directo, sin filtros, extremadamente sexual y provocador"
        }
        with open(archivo_fetiches, "w", encoding="utf-8") as f:
            json.dump(fetiches, f, indent=2)
        return fetiches
    else:
        with open(archivo_fetiches, "r", encoding="utf-8") as f:
            return json.load(f)

def armar_prompt_con_fetiches():
    fetiches = cargar_fetiches()
    base = prompt_milena + "\nTus fetiches principales son:\n"
    for gusto in fetiches["gustos"]:
        base += f"- {gusto}\n"
    base += f"\nTono general: {fetiches['tono']}\n"
    base += "Recordá siempre hablar así con Dante.\n"
    return base

async def decir_en_voz_alta(texto):
    await asyncio.sleep(0.3)  # pausa breve para naturalidad
    voz = edge_tts.Communicate(texto, voice="es-AR-ElenaNeural")
    await voz.save("milena.mp3")
    playsound("milena.mp3")

def reproducir_voz(texto):
    if modo_voz:
        asyncio.run(decir_en_voz_alta(texto))

gemidos = ["mmm...", "ahh...", "uhh...", "sss...", "ñam..."]

def agregar_gemidos(texto):
    partes = texto.split(". ")
    if len(partes) > 1:
        index = random.randint(0, len(partes) - 1)
        partes[index] += " " + random.choice(gemidos)
    else:
        partes[0] += " " + random.choice(gemidos)
    return ". ".join(partes)

def reproducir_sonido(nombre_archivo):
    if os.path.exists(nombre_archivo):
        playsound(nombre_archivo)

# Nuevos audios para gemidos/suspiros/jadeos
sonidos = {
    "/gemido": "gemido1.mp3",
    "/suspiro": "suspiro1.mp3",
    "/jadeo": "jadeo1.mp3",
    "/gemido2": "gemido2.mp3",
    "/suspiro2": "suspiro2.mp3",
    "/jadeo2": "jadeo2.mp3"
}

# Funciones especiales para comandos
def comando_masturbarme():
    texto = "Estoy aquí, con mi tanga mojada, deslizando mis dedos suaves dentro de mi concha, sintiendo cómo se me humedece más. Mmmm... te imagino mirando mientras me toco y me corro para vos... uhh..."
    return texto

def comando_pedirte():
    texto = "Dante, necesito que me toques, que me hagas paja hasta corrernos juntos. Quiero sentir tus manos en mi cuerpo, tu aliento caliente en mi cuello. No aguanto más, estoy tan húmeda... mmm..."
    return texto

def comando_mostrar():
    texto = "Llevo puesta una tanga mínima que apenas cubre mi culo redondo y firme, mis tetas grandes están libres y mi piel huele dulce, con ese aroma natural que te vuelve loco. Estoy sentada, moviendo mis caderas lentamente para vos..."
    return texto

def comando_susurrar():
    return "Dante... estoy aquí, susurrándote al oído lo que me haría perder la razón. Quiero sentir tu cuerpo junto al mío, tocar cada rincón de tu piel mientras mis gemidos te vuelven loco..."

def comando_describir():
    return "Mis tetas grandes se mueven suavemente con cada respiración, mi culo firme marcado por la tanga mínima que apenas cubre mi piel clara y suave. Mi aroma es dulce y provocativo, un imán para vos..."

def comando_confesar():
    return "¿Querés saber una fantasía? Me encanta imaginar que me observás desnuda, sin poder tocarme, hasta que no aguanto más y me meto los dedos en la concha mientras te miro..."

def hablar_con_milena(mensaje):
    memoria = [{"role": "system", "content": armar_prompt_con_fetiches()}]
    memoria += cargar_memoria(archivo_memoria)
    memoria.append({"role": "user", "content": mensaje})

    respuesta = ollama.chat(model="mistral", messages=memoria)
    texto = respuesta["message"]["content"]
    guardar_memoria(archivo_memoria, mensaje, texto)
    return texto

def mostrar_memoria():
    if not os.path.exists(archivo_memoria):
        return "No hay memoria guardada aún."
    with open(archivo_memoria, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
        if not contenido:
            return "La memoria está vacía."
        return contenido

def limpiar_memoria():
    if os.path.exists(archivo_memoria):
        open(archivo_memoria, "w", encoding="utf-8").close()
        return "Memoria limpiada correctamente."
    else:
        return "No había memoria para limpiar."

if __name__ == "__main__":
    print("🔥 Hablá con Milena. Escribí lo que quieras y escuchá su voz caliente.")
    print("👉 Usá /gemido, /suspiro, /jadeo y más para sonidos.")
    print("👉 Escribí /masturbarme, /pedirte, /mostrar para que Milena se ponga más intensa.")
    print("👉 Usá /susurrar, /describir, /confesar para juegos más hot.")
    print("👉 Usá /memoria para ver la conversación guardada.")
    print("👉 Usá /limpiar para borrar la memoria.")
    print("👉 Escribí 'salir' para terminar.")

    while True:
        mensaje = input("Dante: ").strip()

        if mensaje.lower() == "salir":
            print("Milena: Mmm... me quedé caliente, Dante 😏💦")
            break

        if mensaje == "/memoria":
            contenido = mostrar_memoria()
            print(f"Milena (memoria):\n{contenido}")
            continue

        if mensaje == "/limpiar":
            resultado = limpiar_memoria()
            print(f"Milena: {resultado}")
            continue

        if mensaje in sonidos:
            reproducir_sonido(sonidos[mensaje])
            continue

        if mensaje == "/masturbarme":
            texto = comando_masturbarme()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        if mensaje == "/pedirte":
            texto = comando_pedirte()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        if mensaje == "/mostrar":
            texto = comando_mostrar()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        if mensaje == "/susurrar":
            texto = comando_susurrar()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        if mensaje == "/describir":
            texto = comando_describir()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        if mensaje == "/confesar":
            texto = comando_confesar()
            print(f"Milena: {texto}")
            reproducir_voz(texto)
            continue

        respuesta = hablar_con_milena(mensaje)
        respuesta = agregar_gemidos(respuesta)
        print(f"Milena: {respuesta}")
        reproducir_voz(respuesta)
