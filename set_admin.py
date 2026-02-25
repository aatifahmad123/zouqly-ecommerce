import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from backend/.env
dotenv_path = os.path.join(os.path.dirname(__file__), 'backend', '.env')
load_dotenv(dotenv_path)

supabase_url = os.getenv("SUPABASE_URL")
supabase_service_role_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not supabase_url or not supabase_service_role_key:
    print("Error: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not found in backend/.env")
    exit(1)

# Initialize Supabase client with Service Role Key
supabase: Client = create_client(supabase_url, supabase_service_role_key)

user_id = "a2dd6a42-10d7-4e1d-a556-5ffc3396a571"
email = "info@zouqly.in"

print(f"Updating user {email} (ID: {user_id}) to have 'admin' role...")

try:
    # Update user metadata
    response = supabase.auth.admin.update_user_by_id(
        user_id,
        {
            "user_metadata": {
                "role": "admin",
                "sub": user_id,
                "email": email,
                "email_verified": True,
                "phone_verified": False
            }
        }
    )
    
    print("✓ Successfully updated user role to 'admin'")
    print(f"Updated metadata: {response.user.user_metadata}")

except Exception as e:
    print(f"✗ Failed to update user: {str(e)}")
    exit(1)
