from pydantic_settings import BaseSettings


class Constants:
    BASE_URL_INLINE = "https://affiliate-en-us.kayakaffiliates.com/i/api/ads/inline/v1"
    BASE_URL_COMPARETO = (
        "https://affiliate-en-us.kayakaffiliates.com/i/api/ads/compareTo/v1"
    )
    HOTEL_LIST_ENDPOINT = "/hotel/list"


constants = Constants()
