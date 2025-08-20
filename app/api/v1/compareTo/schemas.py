from pydantic import BaseModel
from typing import Dict, Optional, Any, List


class ImageDimensions(BaseModel):
    height: int
    width: int


class HotelInlineRequest(BaseModel):
    userTrackId: str
    clientIP: str
    showOn: str
    checkinDate: str
    checkoutDate: str
    requireIFrameSupport: bool | None = None
    adults: int | None = None
    rooms: int | None = None
    children: int | None = None
    logoDimensions: Optional[ImageDimensions] = None
    cityId: str
    cookies: dict | None = None


class FlightLeg(BaseModel):
    originAirport: str
    destinationAirport: str
    date: str


class FlightInlineRequest(BaseModel):
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, Any]] = None

    showOn: str
    legs: List[FlightLeg]
    cabin: Optional[str] = "economy"
    passengers: Optional[List[str]] = ["adult"]
    requireIFrameSupport: Optional[bool] = False
    logoDimensions: Optional[ImageDimensions] = None


class CarLocation(BaseModel):
    type: str  # "city" or "airport"
    locationQuery: str


class CarInlineRequest(BaseModel):
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, Any]] = None

    showOn: str
    pickUpLocation: CarLocation
    dropOffLocation: Optional[CarLocation] = None
    pickUpHour: Optional[int] = 12
    dropOffHour: Optional[int] = 12
    pickUpDate: str
    dropOffDate: str
    requireIFrameSupport: Optional[bool] = False
    logoDimensions: Optional[ImageDimensions] = None
