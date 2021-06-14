import requests

def main():
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=307&date=14-06-2021'

    r = requests.get(url)
    result = r.json()

    for center in result['centers']:
        for session in center['sessions']:
            dose1_capacity = session['available_capacity_dose1']
            dose2_capacity = session['available_capacity_dose2']

            if dose1_capacity > 0 or dose2_capacity > 0:
                print(center['name'], session['vaccine'], dose1_capacity, dose2_capacity)

if __name__ == '__main__':
    main()