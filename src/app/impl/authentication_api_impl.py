from src.app.models.User import User
from src.app.db import get_session
from sqlmodel import Session, select
from src.app.schema.api_v1_auth_signup_post_request import ApiV1AuthSignupPostRequest
from src.app.schema.api_v1_auth_login_post_request import ApiV1AuthLoginPostRequest
from src.app.schema.api_v1_auth_refresh_post_request import ApiV1AuthRefreshPostRequest
from src.app.schema.auth_response import AuthResponse
from src.app.schema.token_response import TokenResponse
from src.app.schema.error import Error

from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings (example)
SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


class AuthenticationApiImpl:
    """Concrete implementation of BaseAuthenticationApi"""

    async def api_v1_auth_signup_post(
        self, api_v1_auth_signup_post_request: ApiV1AuthSignupPostRequest
    ) -> AuthResponse:
        async with get_session() as session:
            # Check if user exists
            statement = select(User).where(User.email == api_v1_auth_signup_post_request.email)
            result = await session.exec(statement)
            existing_user = result.first()
            if existing_user:
                raise Exception("User already exists")

            # Create user
            hashed_password = pwd_context.hash(api_v1_auth_signup_post_request.password)
            new_user = User(
                email=api_v1_auth_signup_post_request.email,
                password=hashed_password,
                name=api_v1_auth_signup_post_request.name
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            # Return auth response
            access_token = self._create_access_token(new_user.id)
            refresh_token = self._create_refresh_token(new_user.id)
            return AuthResponse(
                user_id=new_user.id,
                access_token=access_token,
                refresh_token=refresh_token
            )

    async def api_v1_auth_login_post(
        self, api_v1_auth_login_post_request: ApiV1AuthLoginPostRequest
    ) -> AuthResponse:
        async with get_session() as session:
            statement = select(User).where(User.email == api_v1_auth_login_post_request.email)
            result = await session.exec(statement)
            user = result.first()
            if not user or not pwd_context.verify(api_v1_auth_login_post_request.password, user.password):
                raise Exception("Invalid credentials")

            access_token = self._create_access_token(user.id)
            refresh_token = self._create_refresh_token(user.id)
            return AuthResponse(
                user_id=user.id,
                access_token=access_token,
                refresh_token=refresh_token
            )

    async def api_v1_auth_refresh_post(
        self, api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest
    ) -> TokenResponse:
        payload = jwt.decode(api_v1_auth_refresh_post_request.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise Exception("Invalid refresh token")

        access_token = self._create_access_token(user_id)
        return TokenResponse(access_token=access_token)

    async def api_v1_auth_logout_post(
        self, api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest
    ) -> None:
        # Invalidate refresh token (implementation depends on DB / cache)
        # For simplicity, just return success
        return None

    # --------------------
    # Helper methods
    # --------------------
    def _create_access_token(self, user_id: int):
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": str(user_id), "exp": expire}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def _create_refresh_token(self, user_id: int):
        expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        payload = {"sub": str(user_id), "exp": expire}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
