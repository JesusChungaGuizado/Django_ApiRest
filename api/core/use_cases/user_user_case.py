from ...db import user_db
from ..entities.users import User

def listUser():
    resultado = user_db.listar_usuario()
    return resultado

def showUser(id:int):
    result=user_db.showUser(id)
    if(result):
        return result
    else:
       return None

def updateUser(user:User):
    result=user_db.updateUser(user);
    if(result):
        return result
    
def loginUser(email,password):
    result=user_db.loginUser(email,password)
    # user_model = get_user_model()
    # user = user_model.objects.get(email=email, password=password)
    if(result):
        return result
    else:
       return None

