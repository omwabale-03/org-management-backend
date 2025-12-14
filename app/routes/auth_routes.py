from fastapi import APIRouter, HTTPException
from app.models.admin_model import AdminLogin
from app.database import admins_collection
from app.utils.auth import create_token
from app.utils.hash import verify_password

router = APIRouter(prefix="/admin")

@router.post("/login")
def admin_login(data: AdminLogin):
    admin = admins_collection.find_one({"email": data.email})
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    if not verify_password(data.password, admin["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_token({
        "email": admin["email"],
        "organization": admin["organization"]
    })

    return {"token": token}
