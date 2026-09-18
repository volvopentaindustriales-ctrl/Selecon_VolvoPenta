from flask import Flask
from supabase import create_client, Client

app = Flask(__name__)

# Tus datos reales extraídos de la página de contacto
SUPABASE_URL = "https://naxvisgsqzqqxppaozbp.supabase.co"
SUPABASE_KEY = "sb_publishable_1roH47k0JskCosWdbLufJw_cbmGK_It"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
@app.route("/cron_ping")
def cron_ping():
    try:
        # Hace una consulta mínima a la tabla Contactos para despertar la base de datos
        supabase.table("Contactos").select("id").limit(1).execute()
        return "CRON_OK - Supabase despierta", 200
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)