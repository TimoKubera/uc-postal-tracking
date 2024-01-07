from fastapi import FastAPI, Depends, HTTPException, status
from . import auth, models, schemas

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "Service is up and running"}

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.TokenRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user