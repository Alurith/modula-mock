from typing import List
from pydantic import BaseModel
from enum import Enum


class OrderAction(str, Enum):
    versamento = "V"
    prelievo = "P"


class Article(BaseModel):
    ART_ARTICOLO: str
    ART_UMI: str = "PZ"
    ART_DES: str
    ART_NOTE: str


class Order(BaseModel):
    ORD_ORDINE: str
    ORD_DES: str
    ORD_TIPOOP: str
    ORD_CLIENTE: str


class OrderRow(BaseModel):
    RIG_ORDINE: str
    RIG_ARTICOLO: str
    RIG_QTAR: str
    RIG_DSCAD: str | None
    RIG_REG_NOTE: str | None


class ImportArticles(BaseModel):
    IMP_ARTICOLI: List[Article]


class ImportOrders(BaseModel):
    IMP_ORDINI: List[Order]
    IMP_ORDINI_RIGHE: List[OrderRow]


class GiacenzaArticle(BaseModel):
    GIA_ARTICOLO: str
    GIA_GIAC: float
    GIA_VER: float
    GIA_PRE: float
    GIA_ARTICOLO_DES: str | None
    GIA_ARTICOLO_NOTE: str | None


class Giacenze(BaseModel):
    EXP_GIACENZE: List[GiacenzaArticle]


class ExportGiacenze(BaseModel):
    GUID: str
    DATA: Giacenze
    TransactionStatus: str


class GiacenzeACK(BaseModel):
    GUID: str


class StatoOrdini(BaseModel):
    ORD_ORDINE: str
    ORD_DES: str
    ORD_TIPOOP: str
    ORD_STATO: str
    EXP_ORDINI_Id: int


class StatoOrdiniRiga(BaseModel):
    RIG_ORDINE: str
    RIG_ORDINE: str
    RIG_ARTICOLO: str
    RIG_QTAR: str
    RIG_QTAE: str
    RIG_STARIORD: str
    EXP_ORDINI_Id: int


class DataOrders(BaseModel):
    EXP_ORDINI: List[StatoOrdini]
    EXP_ORDINI_RIGHE: List[StatoOrdiniRiga]
    EXP_ORDINI_RIGHE_STO: List
    EXP_ORDINI_UDS: List
    EXP_ORDINI_UDS_SCOMPARTI: List


class ExportOrdini(BaseModel):
    GUID: str
    DATA: DataOrders
    TransactionStatus: str
