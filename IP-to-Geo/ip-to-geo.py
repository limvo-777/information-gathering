import geoip2.database
import os
import re

def ip_to_geo(ip_address):
    # maxmind에서 제공하는 데이터베이스 read
    city_response = geoip2.database.Reader('GeoLite2-City.mmdb').city(ip_address)

    continent = str(city_response.continent.name)  # response 중 대륙 이름 불러오기
    city = str(city_response.city.name)
    latitude=str(city_response.location.latitude)
    logitude=str(city_response.location.longitude)
    country=str(city_response.registered_country.name)
    # 확인한 정보 출력
    print("IP Address : " + ip_address + "\n"
                                         "Continent : " + continent + "\n"
          "Country : " + country + "\n"
          "City : " + city + "\n"
          "Latitude : " + latitude + "\n"
          "Longitude : " + logitude + "\n"

          )


if __name__ == '__main__':
    domain={"naver.com","google.com", "daum.net"}
    r=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    for d in domain:
        val=os.popen(f"nslookup {d}").read()
        result=r.findall(val)
        for i in result[1:]:
            ip_to_geo(i)
