from typing import List
import json
import base64

from litestar import Litestar, get, post, Router, MediaType, Controller, Request
from litestar.connection import ASGIConnection
from src.schemas import ImportOrders, ExportGiacenze, ImportArticles, GiacenzeACK

from litestar.handlers.base import BaseRouteHandler
from litestar.exceptions import NotAuthorizedException


def basic_auth_guard(connection: ASGIConnection, _: BaseRouteHandler) -> None:
    if not connection.headers.get("authorization", False):
        raise NotAuthorizedException()
    token = connection.headers.get("authorization").replace("Basic ", "")

    credentials = base64.b64decode(token.encode("ascii")).decode("ascii")
    if credentials != "modula:modula":
        raise NotAuthorizedException()


class ExportArticoli(Controller):
    path = "CFG-EXP-GIACENZE/"

    @get()
    async def get_giacenze(self) -> List[ExportGiacenze]:
        with open("data/export-giacenze.json", mode="r") as json_data:
            return ExportGiacenze(**json.load(json_data))

    @post("ACK", media_type=MediaType.TEXT)
    async def get_giacenze_ack(self, data: GiacenzeACK) -> str:
        return "Operazione completata con successo"


@post("CFG-IMP-ARTICOLI", media_type=MediaType.TEXT)
async def import_articles(data: ImportArticles) -> str:
    return "Operazione completata con successo"


@post("CFG-IMP-ORDINI", media_type=MediaType.TEXT)
async def import_orders(data: ImportOrders, request: Request) -> str:
    return "Operazione completata con successo"


mock_router = Router(
    path="api/jobs/",
    route_handlers=[ExportArticoli, import_articles, import_orders],
    guards=[basic_auth_guard],
)


app = Litestar(route_handlers=[mock_router])
