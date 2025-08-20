from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from app.utils.constants import constants
from app.core.config import settings
from app.api.v1.inline.schemas import (
    HotelInlineRequest,
    FlightInlineRequest,
    CarInlineRequest,
)

router = APIRouter(prefix="/inline", tags=["Inline Ads"])


@router.post("/hotel-list")
def get_hotel_list(payload: HotelInlineRequest):
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
    url = constants.BASE_URL_INLINE + constants.HOTEL_LIST_ENDPOINT
    params = {
        "apiKey": settings.INLINE_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent or settings.DEFAULT_USER_AGENT,
        "x-original-client-ip": payload.clientIP,
    }

    payload_data = payload.dict(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies if payload.cookies else {},
    )

    response_data = {
        "status_code": response.status_code,
        "response": response.json(),
        "cookies": dict(response.cookies),
    }
    return JSONResponse(content=response_data)


@router.post("/flight-list")
def get_flight_list(payload: FlightInlineRequest):
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
    url = constants.BASE_URL_INLINE + constants.FLIGHT_LIST_ENDPOINT
    params = {
        "apiKey": settings.INLINE_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent or settings.DEFAULT_USER_AGENT,
        "x-original-client-ip": payload.clientIP,
    }

    payload_data = payload.dict(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies if payload.cookies else {},
    )

    response_data = {
        "status_code": response.status_code,
        "response": response.json(),
        "cookies": dict(response.cookies),
    }
    return JSONResponse(content=response_data)


@router.post("/car-list")
def get_car_list(payload: CarInlineRequest):
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
    url = constants.BASE_URL_INLINE + constants.CAR_LIST_ENDPOINT
    params = {
        "apiKey": settings.INLINE_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent or settings.DEFAULT_USER_AGENT,
        "x-original-client-ip": payload.clientIP,
    }

    payload_data = payload.dict(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies if payload.cookies else {},
    )

    response_data = {
        "status_code": response.status_code,
        "response": response.json(),
        "cookies": dict(response.cookies),
    }
    return JSONResponse(content=response_data)
