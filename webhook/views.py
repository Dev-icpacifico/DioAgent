import json
import requests
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from dotenv import load_dotenv

load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@csrf_exempt
def meta_webhook(request):
    if request.method == "GET":
        if request.GET.get("hub.verify_token") == VERIFY_TOKEN:
            print("✅ Webhook verificado")
            return HttpResponse(request.GET.get("hub.challenge"))
        print("❌ Token de verificación incorrecto")
        return HttpResponse("Token inválido", status=403)


    elif request.method == "POST":

        try:

            data = json.loads(request.body)

            print("📥 Payload completo recibido:")

            print(json.dumps(data, indent=2))

            value = data['entry'][0]['changes'][0]['value']

            # ✅ Solo procesa si contiene mensajes (no status)

            if "messages" in value:
                mensaje = value['messages'][0]['text']['body']

                numero = value['messages'][0]['from']

                print("📩 Mensaje recibido:", mensaje)

                print("📞 Desde número:", numero)

                enviar_respuesta(numero, "Mensaje recibido: " + mensaje)

            return JsonResponse({"status": "ok"})


        except Exception as e:

            print("❌ Error procesando mensaje:", str(e))

            return JsonResponse({"error": "error procesando payload"}, status=400)


def enviar_respuesta(numero, mensaje):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensaje}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("📤 Enviando respuesta:", response.status_code, response.text)
