import random

print('Иммитация условного рефлекса')

class Reflecio:
    """
        Рефлекс реализуемый следующей схемой

        A --------#-------|>----#----------> C
                  |             |
                [ БС ]----------/ k
                  |             |
        B --------#-------|>----|

        где
            A - безусловный раздражитель, однозначно вызывающий реакцию C
            B - условный сигнал
            БС - блок сравнения. При многократном поступлении A и B, перемыкает K
        
        reinforcements - парметр подкрепления
        k - параметр фиксирующий условный рефлекс 
    """

    def __init__(self) -> None:
        """
            Конструтор рефлекса
        """
        self.reinforcements = 0
        self.k = False


    def compare_block(self, a, b):
        """
            Имитирует блок сравнения

            Тем самым реализует подкрепление условия
        """
        if a and b:
            self.reinforcements += 1
        else:
            if self.reinforcements > 0:
                self.reinforcements -= 1


    def do(self, a, b):
        """
            Имитация работы рефлекса
        """
        self.compare_block(a, b)

        if self.reinforcements >= 2: # Проверка закреплённости условия
            self.k = True
        else:
            self.k = False
        
        if a and not b: # Безусловность сигнала A
            return True
        elif a or b and self.k: # Условность сигнала B
            return True

        return False



reflex = Reflecio()

print('Подача безусловного сигнала')
for i in range(5):
    r = reflex.do(True, False)
    print(f'Реакция А(1) и В(0) = {r}')

print('Подкрепление')
for i in range(5):
    r = reflex.do(True, True)
    print(f'Реакция А(1) и В(1) = {r}')

print('Подача условного сигнала')
for i in range(5):
    r = reflex.do(False, True)
    print(f'Реакция А(0) и В(1) = {r}')

