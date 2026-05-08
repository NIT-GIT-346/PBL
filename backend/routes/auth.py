from fastapi import APIRouter, HTTPException, status
from schemas.auth import TokenRequest, TokenResponse
from utils.auth import DEMO_USERS, verify_password, create_access_token

router = APIRouter()


@router.post("/auth/token", response_model=TokenResponse)
async def login(request: TokenRequest):
    user = DEMO_USERS.get(request.username)
    if not user or not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}
    )
    return TokenResponse(access_token=token)
