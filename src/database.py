from supabase import create_client, Client

# Substitua o texto dentro das aspas pelas suas credenciais reais do Supabase:
SUPABASE_URL = "https://zdchqghircfzsiqxytpr.supabase.co/rest/v1/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpkY2hxZ2hpcmNmenNpcXh5dHByIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0NTg3ODksImV4cCI6MjA5NzAzNDc4OX0.Gk2C6Dm9xcPrdmiaKNaa_fMRBtKHEm8Z3RKXcREuHtE"

def obter_conexao() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)