import supabase


def buscaDataApi():
    supabase_url = "https://wvsxlwngvsbzfosachht.supabase.co"
    supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind2c3hsd25ndnNiemZvc2FjaGh0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NDIwMzU2MiwiZXhwIjoyMDA5Nzc5NTYyfQ.bNwzCjOu8-l-W92_NpHwuMKSIW5DtBewC7GaQ6A22ms"

    client = supabase.create_client(supabase_url, supabase_key)

    data = client.table("posts").select("*").execute()
    
    return data
