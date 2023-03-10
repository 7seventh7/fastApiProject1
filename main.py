from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]



fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 3, "user_id": 1, "currency": "BTC", "side": "sell", "price": 5525, "amount": 2.12},
    {"id": 4, "user_id": 1, "currency": "BTC", "side": "sell", "price": 555, "amount": 2.12},
    {"id": 5, "user_id": 1, "currency": "BTC", "side": "buy", "price": 995, "amount": 2.12},
    {"id": 6, "user_id": 1, "currency": "BTC", "side": "sell", "price": 25, "amount": 2.12},
]


@app.get("/trades")
def get_trades(limit: int, offset: int):
    return fake_trades[offset:][:limit]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user1 = list(filter(lambda user: user.get("id") == user_id, fake_users2))
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    print('current_user1', current_user1)
    print('current_user', current_user)
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}