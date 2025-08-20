from typing import List, Optional, Dict
from pydantic import BaseModel, Field, constr
from datetime import date


class ImageDimensions(BaseModel):
    height: int
    width: int


class Price(BaseModel):
    price: float
    currency: str
    localizedPrice: str


class FlightLeg(BaseModel):
    originAirport: str
    destinationAirport: str
    date: date


class CarLocation(BaseModel):
    type: str
    locationQuery: str


class HotelInlineRequest(BaseModel):
    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = None

    # Hotel-specific fields
    cityId: str
    checkinDate: date
    checkoutDate: date
    adults: Optional[int] = Field(default=2)
    rooms: Optional[int] = Field(default=1)
    children: Optional[int] = Field(default=0)
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)


class FlightInlineRequest(BaseModel):
    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = None

    # Flight-specific fields
    legs: List[FlightLeg]
    cabin: Optional[str] = Field(
        default="economy",
    )
    passengers: Optional[List[str]] = Field(
        default=["adult"], description="Default to one adult passenger"
    )
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)


class CarInlineRequest(BaseModel):
    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = None

    # Car-specific fields
    pickUpLocation: CarLocation
    dropOffLocation: Optional[CarLocation] = None
    pickUpHour: Optional[int] = Field(default=12, ge=0, le=23)
    dropOffHour: Optional[int] = Field(default=12, ge=0, le=23)
    pickUpDate: date
    dropOffDate: date
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)
