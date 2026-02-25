import os
from supabase import create_client, Client
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'backend', '.env')
load_dotenv(dotenv_path)

supabase_url = os.getenv("SUPABASE_URL")
supabase_service_role_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(supabase_url, supabase_service_role_key)

user_id = "a2dd6a42-10d7-4e1d-a556-5ffc3396a571"

print(f"Verifying role for user ID: {user_id}...")

try:
    response = supabase.auth.admin.get_user_by_id(user_id)
    user = response.user
    role = user.user_metadata.get("role")
    
    if role == "admin":
        print(f"✅ SUCCESS: User {user.email} is an ADMIN.")
        print(f"Metadata: {user.user_metadata}")
    else:
        print(f"❌ FAILURE: User {user.email} role is '{role}'.")
except Exception as e:
    print(f"✗ Error: {str(e)}")
