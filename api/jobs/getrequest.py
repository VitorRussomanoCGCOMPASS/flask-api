"""  Just a simple get_request function to be used by all the webscrapping modules """
from typing import Optional
import http.client


def get_request(
    host: str, url: str, headers: dict[str, str], payload: Optional[str] = None
) -> bytes:
    """

    Parameters
    ----------
    host : str
        Host url
    url : str
        Is the selector urls
    headers : dict[str, str]
        Extra HTTP headers to send with the request

    payload : Optional[str], optional
        by default None

    Returns
    -------
    bytes
    """

    if payload is None:
        payload = ""
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    return res.read()
