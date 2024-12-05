from dataclasses import dataclass, asdict


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: str
    status: str = "в наличии"

    def to_dict(self) -> dict:
        return asdict(self)

    def __repr__(self) -> str:
        return f"ID:{self.id} Название: {self.title}"
