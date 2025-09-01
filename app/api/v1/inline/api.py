from fastapi import APIRouter, Request
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


@router.post(
    "/hotel-list",
    summary="Retrieve hotel inline ads",
    description="""
Fetch a list of inline hotel advertisements.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `cookies` (dict[str, str], optional): Cookies dictionary.
- `userAgent` (str, optional): User agent string.
- `cityId` (str, required): City identifier.
- `checkinDate` (date, required): Check-in date.
- `checkoutDate` (date, required): Check-out date.
- `adults` (int, optional, default=2): Number of adults.
- `rooms` (int, optional, default=1): Number of rooms.
- `children` (int, optional, default=0): Number of children.
- `logoDimensions` (object, optional): `{height, width}`.
- `backgroundImageDimensions` (object, optional): `{height, width}`.
- `currencyCode` (str, optional, length=3): Currency code.
""",
    response_description="Inline hotel ads response",
)
def get_hotel_list(payload: HotelInlineRequest, request: Request):
    url = constants.BASE_URL_INLINE + constants.HOTEL_LIST_ENDPOINT
    params = {"apiKey": settings.INLINE_ADS_API_KEY, "userTrackId": payload.userTrackId}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = payload.model_dump(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}, exclude_unset=True
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=request.cookies or {},
    )

    cookies = dict(response.cookies)

    json_response = JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
        },
    )

    for key, value in cookies.items():
        json_response.set_cookie(key=key, value=value)

    return json_response


@router.post(
    "/flight-list",
    summary="Retrieve flight inline ads",
    description="""
Fetch a list of inline flight advertisements.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `cookies` (dict[str, str], optional): Cookies dictionary.
- `userAgent` (str, optional): User agent string.
- `legs` (list[FlightLeg], required): Flight legs with origin, destination, date.
- `cabin` (str, optional, default="economy"): Cabin type.
- `passengers` (list[str], optional, default=["adult"]): Passenger types.
- `logoDimensions` (object, optional): `{height, width}`.
- `backgroundImageDimensions` (object, optional): `{height, width}`.
- `currencyCode` (str, optional, length=3): Currency code.
""",
    response_description="Inline flight ads response",
)
def get_flight_list(payload: FlightInlineRequest, request: Request):
    url = constants.BASE_URL_INLINE + constants.FLIGHT_LIST_ENDPOINT
    params = {"apiKey": settings.INLINE_ADS_API_KEY, "userTrackId": payload.userTrackId}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = payload.model_dump(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}, exclude_unset=True
    )

    print(payload_data)

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=request.cookies or {},
    )

    cookies = dict(response.cookies)

    json_response = JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
        },
    )

    for key, value in cookies.items():
        json_response.set_cookie(key=key, value=value)

    return json_response


@router.post(
    "/car-list",
    summary="Retrieve car rental inline ads",
    description="""
Fetch a list of inline car rental advertisements.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `cookies` (dict[str, str], optional): Cookies dictionary.
- `userAgent` (str, optional): User agent string.
- `pickUpLocation` (CarLocation, required): Pick-up location `{type, locationQuery}`.
- `dropOffLocation` (CarLocation, optional): Drop-off location `{type, locationQuery}`.
- `pickUpHour` (int, optional, default=12, range=0-23): Pick-up hour.
- `dropOffHour` (int, optional, default=12, range=0-23): Drop-off hour.
- `pickUpDate` (date, required): Pick-up date.
- `dropOffDate` (date, required): Drop-off date.
- `logoDimensions` (object, optional): `{height, width}`.
- `backgroundImageDimensions` (object, optional): `{height, width}`.
- `currencyCode` (str, optional, length=3): Currency code.
""",
    response_description="Inline car rental ads response",
)
def get_car_list(payload: CarInlineRequest, request: Request):
    url = constants.BASE_URL_INLINE + constants.CAR_LIST_ENDPOINT
    params = {"apiKey": settings.INLINE_ADS_API_KEY, "userTrackId": payload.userTrackId}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = payload.model_dump(
        exclude={"userTrackId", "clientIP", "cookies", "userAgent"}, exclude_unset=True
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=request.cookies or {},
    )

    cookies = dict(response.cookies)
    json_response = JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
        },
    )
    for key, value in cookies.items():
        json_response.set_cookie(key=key, value=value)
    return json_response
