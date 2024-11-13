from pydantic import BaseModel


class Preferences(BaseModel):
    pontoTuristico: int
    hospedagem: int
    alimentacao: int
    clima: int
