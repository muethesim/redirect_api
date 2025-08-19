from pydantic import BaseModel


class HotelInlineRequest(BaseModel):
    userTrackId: str
    clientIP: str
    showOn: str
    checkinDate: str
    checkoutDate: str
    adults: int
    rooms: int
    cityId: str
    cookies: dict | None = None
