from ninja import Ninja
from pet import Pet

mike = Pet('mike','dog','triple cork', 100, 100)
jim = Ninja('jim','smith','chocolate','meat', mike)


jim.walk().feed().bathe().walk().walk().bathe()