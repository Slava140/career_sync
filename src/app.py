from fastapi import FastAPI, Depends

from users.models import User
from users.dependecies import current_active_user

from users.routes import router as users_router


app = FastAPI()
app.include_router(users_router)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}