from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def corners(self) -> int:
        pass

    @abstractmethod
    def sides(self) -> int:
        pass

    def name(self) -> str:
        return "Undefined Shape"


class Triangle(Shape):
    def corners(self) -> int:
        return 3

    def sides(self) -> int:
        return 3

    # Optional override
    def name(self) -> str:
        return "Triangle"


class Square(Shape):
    def corners(self) -> int:
        return 4

    def sides(self) -> int:
        return 4

    # This class uses the default 'name' implementation from the base class


class Circle(Shape):
    def corners(self) -> int:
        return 0

    def sides(self) -> int:
        return 1

    def name(self) -> str:
        return "Circle"


class Mystery(Shape):
    def name(self) -> str:
        return "Mystery"
