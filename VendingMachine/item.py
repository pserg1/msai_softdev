from abc import abstractmethod, abstractproperty

class BaseItem:
    @abstractproperty
    def price(self) -> int:
        ...
    
    @classmethod
    @abstractmethod
    def Empty(cls) -> 'BaseItem':
        ...
    
    @abstractmethod
    def IsEmpty(self) -> bool:
        ...
    
    @abstractmethod
    def __add__(self):
        ...

    @abstractmethod
    def __sub__(self):
        ...
    
    @abstractmethod
    def __str__(self):
        ...

class ItemHolder(BaseItem):
    def __init__(self, name: str, price: int):
        self.name = name
        self.count = 1
        self.cost = price

    @property
    def price(self) -> int:
        return self.cost * self.count

    @classmethod
    def Empty(cls) -> 'ItemHolder':
        item = cls('Empty')
        item.count = 0
        item.cost = 0

        return item

    @classmethod
    def CreateMultiple(cls, name: str, count: int, price: int) -> 'ItemHolder':
        item = cls(name)
        item.count = count
        item.cost = price

        return item

    def IsEmpty(self) -> bool:
        return self.name == 'Empty' and self.count == 0

    def __add__(self, x: int) -> int:
        self.count += x
        return self

    def __sub__(self, x: int) -> int:
        self.count -= x

        # Clipping to 0
        self.count = max(self.count, 0)

        if (self.count == 0):
            self.name = 'Empty'

        return self

    def __str__(self) -> str:
        return f"{self.name}.{self.count}.{self.cost}$"