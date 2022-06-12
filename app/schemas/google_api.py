from pydantic import BaseModel


class GoogleApiReport(BaseModel):
    name: str
    collection_time: str
    description: str
