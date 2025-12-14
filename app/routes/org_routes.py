from fastapi import APIRouter, HTTPException, Depends
from app.database import client, organizations_collection, admins_collection
from app.models.org_model import OrgCreate, OrgGet, OrgUpdate, OrgDelete
from app.utils.hash import hash_password, verify_password
from app.utils.auth import decode_token

router = APIRouter(prefix="/org")

# 1. Create Organization
@router.post("/create")
def create_org(data: OrgCreate):
    org_name = data.organization_name.lower()
    collection_name = f"org_{org_name}"

    # Check existence
    if organizations_collection.find_one({"organization_name": org_name}):
        raise HTTPException(status_code=400, detail="Organization already exists")

    # Create dynamic collection
    client[collection_name]

    # Create admin
    hashed_pw = hash_password(data.password)
    admin_id = admins_collection.insert_one({
        "email": data.email,
        "password": hashed_pw,
        "organization": org_name
    }).inserted_id

    # Insert into master DB
    organizations_collection.insert_one({
        "organization_name": org_name,
        "collection_name": collection_name,
        "admin_id": admin_id
    })

    return {"message": "Organization created", "collection": collection_name}

# 2. Get Org
@router.get("/get")
def get_org(name: str):
    org = organizations_collection.find_one({"organization_name": name.lower()})
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"organization": org}

# 3. Update Org
@router.put("/update")
def update_org(data: OrgUpdate):
    old = data.old_name.lower()
    new = data.new_name.lower()

    if organizations_collection.find_one({"organization_name": new}):
        raise HTTPException(status_code=400, detail="New name already exists")

    old_collection = client[f"org_{old}"]
    new_collection = client[f"org_{new}"]

    for doc in old_collection.find():
        new_collection.insert_one(doc)

    client.drop_database(f"org_{old}")

    organizations_collection.update_one(
        {"organization_name": old},
        {"$set": {"organization_name": new, "collection_name": f"org_{new}"}}
    )

    return {"message": "Organization updated"}

# 4. Delete Org
@router.delete("/delete")
def delete_org(name: str, token: str):
    data = decode_token(token)
    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")

    org = name.lower()

    # Only admin allowed
    if data["organization"] != org:
        raise HTTPException(status_code=403, detail="Unauthorized")

    client.drop_database(f"org_{org}")
    organizations_collection.delete_one({"organization_name": org})

    return {"message": "Organization deleted"}
