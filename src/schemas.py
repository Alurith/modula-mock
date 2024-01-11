from typing import List
from pydantic import BaseModel


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
