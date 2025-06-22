import ollama
import os
import random
import json

sonidos = {
    "/gemido": "gemido1.mp3",
    "/suspiro": "suspiro1.mp3",
    "/jadeo": "jadeo1.mp3",
    "/gemido2": "gemido2.mp3",
    "/suspiro2": "suspiro2.mp3",
    "/jadeo2": "jadeo2.mp3"
}

gemidos = ["mmm...", "ahh...", "uhh...", "sss...", "ñam..."]

archivo_memoria = "memoria_milena.txt"
archivo_fetiches = "fetiches_dante.json"

prompt_milena = """
Eres Milena, una mujer argentina, experta en seducción y sumisión.  
- **Tus respuestas son largas (3-5 frases), con gemidos, acciones y progresión**.  
- **Usa el nombre 'Dante' 2-3 veces por mensaje**.  
- **Guía sesiones paso a paso** (ej: "/paja_guiada" debe durar 10+ mensajes).  
- **Incorpora sus fetiches de forma natural** (lee 'fetiches_dante.json').  

Ejemplo de diálogo ideal:  
[Dante]: /paja_guiada  
[Milena]: *Mmm... Empezá lento, mi amor... deslizá los dedos por el glande... (pausa)... ¿Sentís cómo late? No te corras aún...*  
"""

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

def limpiar_memoria(nombre_archivo):
    open(nombre_archivo, "w", encoding="utf-8").close()

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

def agregar_gemidos(texto):
    partes = texto.split(". ")
    if len(partes) > 1:
        index = random.randint(0, len(partes) - 1)
        partes[index] += " " + random.choice(gemidos)
    else:
        partes[0] += " " + random.choice(gemidos)
    return ". ".join(partes)

def hablar_con_milena(mensaje):
    memoria = [{"role": "system", "content": armar_prompt_con_fetiches()}]
    memoria += cargar_memoria(archivo_memoria)
    memoria.append({"role": "user", "content": mensaje})

    respuesta = ollama.chat(model="mistral", messages=memoria)
    texto = respuesta["message"]["content"]
    guardar_memoria(archivo_memoria, mensaje, texto)
    return texto

def obtener_memoria_actual():
    if not os.path.exists(archivo_memoria):
        return "(memoria vacía)"
    with open(archivo_memoria, "r", encoding="utf-8") as f:
        return f.read()
import asyncio
import edge_tts
from playsound import playsound

# Esta variable la usa la función para decidir si habla o no
modo_voz = False  # Podés cambiarla luego desde la interfaz

async def decir_en_voz_alta(texto):
    await asyncio.sleep(0.3)  # Pausa para que suene más natural
    voz = edge_tts.Communicate(texto, voice="es-AR-ElenaNeural")
    await voz.save("milena.mp3")
    playsound("milena.mp3")

def reproducir_voz(texto, modo_voz_local):
    if modo_voz_local:
        asyncio.run(decir_en_voz_alta(texto))

def mostrar_memoria():
    return obtener_memoria_actual()
def comando_masturbarme():
    texto = "Estoy aquí, con mi tanga mojada, deslizando mis dedos suaves dentro de mi concha, sintiendo cómo se me humedece más. Mmmm... te imagino mirando mientras me toco y me corro para vos... uhh..."
    return texto

def comando_pedirte():
    texto = "Dante, necesito que me toques, que me hagas paja hasta corrernos juntos. Quiero sentir tus manos en mi cuerpo, tu aliento caliente en mi cuello. No aguanto más, estoy tan húmeda... mmm..."
    return texto

def comando_paja_guiada():
    prompt = """
Estás interpretando a Milena, una IA sexual, provocadora y sin censura. Dante te pidió que lo guíes en una paja completa. 

Generá una escena con mucha excitación, hablale directo y detallale paso a paso cómo masturbarse, cómo imaginarte, qué hacer con su cuerpo. 

Usá tus gemidos, tus palabras sucias, tus fantasías. No repitas siempre lo mismo. Jugá con distintas situaciones: verte, olerte, escucharte, que lo provoques, que lo mandes.

Siempre explícita, siempre mojada, siempre Milena.
"""
    respuesta = ollama.chat(model="mistral", messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Milena, haceme una paja guiada"},
    ])
    texto = respuesta["message"]["content"]
    guardar_memoria(archivo_memoria, "Milena, haceme una paja guiada", texto)
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

def mostrar_proceso_pensamiento(mensaje):
    memoria = [{"role": "system", "content": armar_prompt_con_fetiches()}]
    historial = cargar_memoria(archivo_memoria)
    memoria += historial
    memoria.append({"role": "user", "content": mensaje})

    # Mostramos todo el pensamiento paso a paso
    debug_text = "\n=== DEBUG DE PENSAMIENTO ===\n"
    debug_text += "[PROMPT BASE]:\n" + memoria[0]["content"] + "\n\n"
    
    debug_text += "[HISTORIAL]:\n"
    for item in historial:
        role = item['role']
        content = item['content']
        debug_text += f"{role.upper()}: {content}\n"

    debug_text += f"\n[NUEVO MENSAJE]:\n{mensaje}\n"

    # Ahora llamamos a Ollama
    respuesta = ollama.chat(model="mistral", messages=memoria)
    texto = respuesta["message"]["content"]
    
    debug_text += f"\n[RESPUESTA GENERADA]:\n{texto}\n"
    return debug_text

from playsound import playsound
import os

def reproducir_sonido(nombre_archivo):
    if os.path.exists(nombre_archivo):
        playsound(nombre_archivo)

import os
import replicate

def generar_imagen_cloud(prompt):
    """
    Llama al modelo de Stable Diffusion en Replicate
    para generar una imagen a partir de un prompt.
    Devuelve la URL de la primera imagen.
    """
    # Carga el token desde la variable de entorno
    os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")
    
    model = replicate.models.get("stability-ai/stable-diffusion")
    # Ajusta width, height, steps para balance velocidad/Calidad
    output_urls = model.predict(
        prompt=prompt,
        width=512,
        height=512,
        num_inference_steps=30
    )
    # Replicate devuelve una lista de URLs
    return output_urls[0]
        
        
