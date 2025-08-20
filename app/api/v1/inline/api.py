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
