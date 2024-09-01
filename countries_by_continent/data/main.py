import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_countries_by_continent(continent: str):
    countries = supabase.table("countries").select("*").eq("continent", continent).execute()
    return countries

def insert_country(data: dict):
    supabase.table("countries").insert([data]).execute()


if __name__ == "__main__":
    response = supabase.table("countries").select("*").eq("name", "Algeria").execute()

    print(response)


  


