from fastapi import APIRouter

router = APIRouter()

@router.post('/order/')
def order(item: str, quantity: int): 
    print(f'Order received for {quantity} of {item}')
