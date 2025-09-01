from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from app.utils.constants import constants
from app.core.config import settings
from app.api.v1.compareTo.schemas import (
    HotelInlineRequest,
    CarInlineRequest,
    FlightInlineRequest,
)

router = APIRouter(prefix="/compareTo", tags=["Compare To"])


@router.post(
    "/hotel-list",
    summary="Retrieve hotel compareTo ads",
    description="""
Fetch a list of **CompareTo hotel advertisements**.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `userAgent` (str, optional): User agent string.
- `showOn` (str, required): Where to show the result (e.g. `frontDoor`, `resultsPage`).
- `checkinDate` (str, required): Check-in date (format: `YYYY-MM-DD`).
- `checkoutDate` (str, required): Check-out date (format: `YYYY-MM-DD`).
- `requireIFrameSupport` (bool, optional): Whether iFrame support is required.
- `adults` (int, optional): Number of adults.
- `rooms` (int, optional): Number of rooms.
- `children` (int, optional): Number of children.
- `logoDimensions` (object, optional): Logo image dimensions `{height, width}`.
- `cityId` (str, required): City identifier.
- `cookies` (dict, optional): Cookies dictionary.
""",
    response_description="CompareTo hotel ads response",
)
def get_hotel_list(payload: HotelInlineRequest):
    url = constants.BASE_URL_COMPARETO + constants.HOTEL_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = {
        "showOn": payload.showOn,
        "checkinDate": payload.checkinDate,
        "checkoutDate": payload.checkoutDate,
        "cityId": payload.cityId,
    }

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies or {},
    )

    return JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
            "cookies": dict(response.cookies),
        }
    )


@router.post(
    "/flight-list",
    summary="Retrieve flight compareTo ads",
    description="""
Fetch a list of **CompareTo flight advertisements**.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `cookies` (dict, optional): Cookies dictionary.
- `userAgent` (str, optional): User agent string.
- `showOn` (str, required): Where to show the result (e.g. `resultsPage`, `modal`).
- `legs` (list[FlightLeg], required): Flight legs:
  - `originAirport` (str): Departure airport.
  - `destinationAirport` (str): Arrival airport.
  - `date` (str): Flight date (format: `YYYY-MM-DD`).
- `cabin` (str, optional, default="economy"): Cabin type.
- `passengers` (list[str], optional, default=["adult"]): Passenger types.
- `requireIFrameSupport` (bool, optional, default=False): iFrame support flag.
- `logoDimensions` (object, optional): Logo dimensions `{height, width}`.
""",
    response_description="CompareTo flight ads response",
)
def get_flight_list(payload: FlightInlineRequest):
    url = constants.BASE_URL_COMPARETO + constants.FLIGHT_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = payload.model_dump(
        exclude={"userTrackId", "clientIP", "cookies"}, exclude_unset=True
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies or {},
    )

    return JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
            "cookies": dict(response.cookies),
        }
    )


@router.post(
    "/car-list",
    summary="Retrieve car rental compareTo ads",
    description="""
Fetch a list of **CompareTo car rental advertisements**.

**Request Body Fields**:
- `userTrackId` (str, required): User tracking identifier.
- `clientIP` (str, required): Client IP address.
- `cookies` (dict, optional): Cookies dictionary.
- `userAgent` (str, optional): User agent string.
- `showOn` (str, required): Where to show the result (e.g. `panel`, `search`).
- `pickUpLocation` (CarLocation, required): Pick-up location `{type, locationQuery}`.
- `dropOffLocation` (CarLocation, optional): Drop-off location `{type, locationQuery}`.
- `pickUpHour` (int, optional, default=12): Pick-up hour (0–23).
- `dropOffHour` (int, optional, default=12): Drop-off hour (0–23).
- `pickUpDate` (str, required): Pick-up date (format: `YYYY-MM-DD`).
- `dropOffDate` (str, required): Drop-off date (format: `YYYY-MM-DD`).
- `requireIFrameSupport` (bool, optional, default=False): iFrame support flag.
- `logoDimensions` (object, optional): Logo image dimensions `{height, width}`.
""",
    response_description="CompareTo car rental ads response",
)
def get_car_list(payload: CarInlineRequest):
    url = constants.BASE_URL_COMPARETO + constants.CAR_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.userAgent,
        "x-original-client-ip": payload.clientIP,
    }
    payload_data = payload.model_dump(
        exclude={"userTrackId", "clientIP", "cookies"}, exclude_unset=True
    )

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload_data,
        cookies=payload.cookies or {},
    )

    return JSONResponse(
        content={
            "status_code": response.status_code,
            "response": response.json(),
            "cookies": dict(response.cookies),
        }
    )
