import json
import os
from supabase import create_client, Client

with open('../secrets/supabase.json') as json_data:
    data = json.load(json_data,) 

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)