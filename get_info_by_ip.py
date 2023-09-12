import requests
from datetime import datetime


def get_info_by_ip_func(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}?fields=66846719").json()

        data = {
            "query": response.get("query"),
            "status": response.get("status"),
            "continent": response.get("continent"),
            "continentCode": response.get("continentCode"),
            "country": response.get("country"),
            "countryCode": response.get("countryCode"),
            "region": response.get("region"),
            "regionName": response.get("regionName"),
            "city": response.get("city"),
            "district": response.get("district"),
            "zip": response.get("zip"),
            "lat": response.get("lat"),
            "lon": response.get("lon"),
            "timezone": response.get("timezone"),
            "offset": response.get("offset"),
            "currency": response.get("currency"),
            "isp": response.get("isp"),
            "org": response.get("org"),
            "as": response.get("as"),
            "asname": response.get("asname"),
            "mobile": response.get("mobile"),
            "proxy": response.get("proxy"),
            "hosting": response.get("hosting")
        }

        return data

    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection!")
