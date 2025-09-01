from typing import List, Optional, Dict
from pydantic import BaseModel, Field, constr


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
    date: str


class CarLocation(BaseModel):
    type: str
    locationQuery: str


class HotelInlineRequest(BaseModel):
    """
    Hotel Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        cookies (Dict[str, str] | None): Optional. Cookies dictionary.
        userAgent (str | None): Optional. User agent string.
        cityId (str): Required. City identifier.
        checkinDate (date): Required. Check-in date.
        checkoutDate (date): Required. Check-out date.
        adults (int | None): Optional. Number of adults (default: 2).
        rooms (int | None): Optional. Number of rooms (default: 1).
        children (int | None): Optional. Number of children (default: 0).
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
        backgroundImageDimensions (ImageDimensions | None): Optional. Background image dimensions.
        currencyCode (str | None): Optional. Currency code (3 characters).
    """

    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = "kayakaffiliateapp"

    # Hotel-specific fields
    cityId: str
    checkinDate: str
    checkoutDate: str
    adults: Optional[int] = Field(default=2)
    rooms: Optional[int] = Field(default=1)
    children: Optional[int] = Field(default=0)
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)


class FlightInlineRequest(BaseModel):
    """
    Flight Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        cookies (Dict[str, str] | None): Optional. Cookies dictionary.
        userAgent (str | None): Optional. User agent string.
        legs (List[FlightLeg]): Required. List of flight legs.
        cabin (str | None): Optional. Cabin type (default: "economy").
        passengers (List[str] | None): Optional. List of passenger types (default: ["adult"]).
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
        backgroundImageDimensions (ImageDimensions | None): Optional. Background image dimensions.
        currencyCode (str | None): Optional. Currency code (3 characters).
    """

    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = "kayakaffiliateapp"

    # Flight-specific fields
    legs: List[FlightLeg]
    cabin: str | None = None
    passengers: Optional[List[str]] = Field(
        default=["adult"], description="Default to one adult passenger"
    )
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)


class CarInlineRequest(BaseModel):
    """
    Car Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        cookies (Dict[str, str] | None): Optional. Cookies dictionary.
        userAgent (str | None): Optional. User agent string.
        pickUpLocation (CarLocation): Required. Pick-up location.
        dropOffLocation (CarLocation | None): Optional. Drop-off location.
        pickUpHour (int | None): Optional. Pick-up hour (default: 12, range: 0-23).
        dropOffHour (int | None): Optional. Drop-off hour (default: 12, range: 0-23).
        pickUpDate (date): Required. Pick-up date.
        dropOffDate (date): Required. Drop-off date.
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
        backgroundImageDimensions (ImageDimensions | None): Optional. Background image dimensions.
        currencyCode (str | None): Optional. Currency code (3 characters).
    """

    # Extra request params
    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, str]] = None
    userAgent: Optional[str] = "kayakaffiliateapp"

    # Car-specific fields
    pickUpLocation: CarLocation
    dropOffLocation: Optional[CarLocation] = None
    pickUpHour: Optional[int] = Field(default=12, ge=0, le=23)
    dropOffHour: Optional[int] = Field(default=12, ge=0, le=23)
    pickUpDate: str
    dropOffDate: str
    logoDimensions: Optional[ImageDimensions] = None
    backgroundImageDimensions: Optional[ImageDimensions] = None
    currencyCode: Optional[str] = Field(min_length=3, max_length=3)
