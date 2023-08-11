from fastapi import FastAPI
import uvicorn
import menu
import order


api = FastAPI()

def configure_routing():
    api.include_router(menu.menurouter)
    api.include_router(order.router)


if __name__ == '__main__':
    print(menu.menurouter)
    configure_routing()
    uvicorn.run(api, port=8000, host='127.0.0.1')