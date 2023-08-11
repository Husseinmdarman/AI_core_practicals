from fastapi import APIRouter

menurouter = APIRouter()

@menurouter.get('/menu/')
def menu():
    return {'menu': ['pizza', 'pasta', 'salad', 'soup']}
