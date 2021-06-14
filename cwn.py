import requests
from datetime import date

def main():
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

    r = requests.get(url, { 'district_id' : 307, 'date' : date.today().strftime("%d-%m-%Y")})
    result = r.json()

    for center in result['centers']:
        for session in center['sessions']:
            dose1_capacity = session['available_capacity_dose1']
            dose2_capacity = session['available_capacity_dose2']
            if dose1_capacity > 0 or dose2_capacity > 0:
                print("{:30} {} {:15} {}+ {:>4} {:>4}".format(center['name'], session['date'], session['vaccine'], session['min_age_limit'], dose1_capacity, dose2_capacity))

if __name__ == '__main__':
    main()