# NTP: Network Time Protocol
import ntplib
from time import ctime

client = ntplib.NTPClient()
response = client.request('time.stdtime.gov.tw')
print(ctime(response.tx_time))
