class Animal:
    def __init__(self,test1) -> None:
        self.__test1 = test1
    
    def __del__(self)->None:
        return None

    def anima(self)-> None:
        print(f"El animal es:{self.__test1}")


animal = Animal("Leon")
animal.anima()
del animal
