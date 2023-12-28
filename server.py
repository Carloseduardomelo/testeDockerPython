from fastapi import FastAPI
import uvicorn
import supabase

supabase_url = "https://wvsxlwngvsbzfosachht.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind2c3hsd25ndnNiemZvc2FjaGh0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NDIwMzU2MiwiZXhwIjoyMDA5Nzc5NTYyfQ.bNwzCjOu8-l-W92_NpHwuMKSIW5DtBewC7GaQ6A22ms"

client = supabase.create_client(supabase_url, supabase_key)

data = client.table("posts").select("*").execute()


def crate():
    client.table("posts").insert({"title": "carlos", "descripton": "passei aqui senpai" , "body": "pasei aqui de novo senpai"}).execute()


app = FastAPI()


@app.get("/")
def pegarDados():
    return data

@app.post("/create")
def insert(title , descripton , body):
    client.table("posts").insert({f"title": {title}, "descripton": {descripton} , "body": {body}}).execute()
    crate()
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
