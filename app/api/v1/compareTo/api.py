from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from app.utils.constants import constants
from app.core.config import settings
from app.api.v1.compareTo.schemas import HotelInlineRequest, CarInlineRequest, FlightInlineRequest

router = APIRouter(prefix="/compareTo", tags=["Compare To"])


@router.post("/hotel-list")
def get_hotel_list(payload: HotelInlineRequest):
    url = constants.BASE_URL_COMPARETO + constants.HOTEL_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
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
    url = constants.BASE_URL_COMPARETO + constants.FLIGHT_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0.0.0 Safari/537.36",
        "x-original-client-ip": payload.clientIP,
    }

    payload_data = payload.dict(exclude={"userTrackId", "clientIP", "cookies"})

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
    url = constants.BASE_URL_COMPARETO + constants.CAR_LIST_ENDPOINT
    params = {
        "apiKey": settings.COMPARETO_ADS_API_KEY,
        "userTrackId": payload.userTrackId,
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0.0.0 Safari/537.36",
        "x-original-client-ip": payload.clientIP,
    }

    payload_data = payload.dict(exclude={"userTrackId", "clientIP", "cookies"})

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