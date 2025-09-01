from pydantic import BaseModel
from typing import Dict, Optional, Any, List


class ImageDimensions(BaseModel):
    height: int
    width: int


class HotelInlineRequest(BaseModel):
    """
    Hotel Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        userAgent (str | None): Optional. User agent string.
        showOn (str): Required. Where to show the result.
        checkinDate (str): Required. Check-in date (format: YYYY-MM-DD).
        checkoutDate (str): Required. Check-out date (format: YYYY-MM-DD).
        requireIFrameSupport (bool | None): Optional. Whether iFrame support is required.
        adults (int | None): Optional. Number of adults.
        rooms (int | None): Optional. Number of rooms.
        children (int | None): Optional. Number of children.
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
        cityId (str): Required. City identifier.
        cookies (dict | None): Optional. Cookies dictionary.
    """

    userTrackId: str
    clientIP: str
    showOn: str
    userAgent: Optional[str] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    )
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
    """
    Flight Leg Payload

    Fields:
        originAirport (str): Required. Origin airport code.
        destinationAirport (str): Required. Destination airport code.
        date (str): Required. Flight date (format: YYYY-MM-DD).
    """

    originAirport: str
    destinationAirport: str
    date: str


class FlightInlineRequest(BaseModel):
    """
    Flight Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        cookies (Dict[str, Any] | None): Optional. Cookies dictionary.
        showOn (str): Required. Where to show the result.
        legs (List[FlightLeg]): Required. List of flight legs.
        cabin (str | None): Optional. Cabin type (default: "economy").
        passengers (List[str] | None): Optional. List of passenger types (default: ["adult"]).
        requireIFrameSupport (bool | None): Optional. Whether iFrame support is required (default: False).
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
    """

    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, Any]] = None
    userAgent: Optional[str] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    )

    showOn: str
    legs: List[FlightLeg]
    cabin: Optional[str] = "economy"
    passengers: Optional[List[str]] = ["adult"]
    requireIFrameSupport: Optional[bool] = False
    logoDimensions: Optional[ImageDimensions] = None


class CarLocation(BaseModel):
    """
    Car Location Payload

    Fields:
        type (str): Required. Location type ("city" or "airport").
        locationQuery (str): Required. Location query string.
    """

    type: str  # "city" or "airport"
    locationQuery: str


class CarInlineRequest(BaseModel):
    """
    Car Inline API Request Payload

    Fields:
        userTrackId (str): Required. User tracking identifier.
        clientIP (str): Required. Client IP address.
        cookies (Dict[str, Any] | None): Optional. Cookies dictionary.
        showOn (str): Required. Where to show the result.
        pickUpLocation (CarLocation): Required. Pick-up location.
        dropOffLocation (CarLocation | None): Optional. Drop-off location.
        pickUpHour (int | None): Optional. Pick-up hour (default: 12).
        dropOffHour (int | None): Optional. Drop-off hour (default: 12).
        pickUpDate (str): Required. Pick-up date (format: YYYY-MM-DD).
        dropOffDate (str): Required. Drop-off date (format: YYYY-MM-DD).
        requireIFrameSupport (bool | None): Optional. Whether iFrame support is required (default: False).
        logoDimensions (ImageDimensions | None): Optional. Logo image dimensions.
    """

    userTrackId: str
    clientIP: str
    cookies: Optional[Dict[str, Any]] = None
    userAgent: Optional[str] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    )

    showOn: str
    pickUpLocation: CarLocation
    dropOffLocation: Optional[CarLocation] = None
    pickUpHour: Optional[int] = 12
    dropOffHour: Optional[int] = 12
    pickUpDate: str
    dropOffDate: str
    requireIFrameSupport: Optional[bool] = False
    logoDimensions: Optional[ImageDimensions] = None
