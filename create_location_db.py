from db import get_db
import requests
from lxml.html import fromstring
import string
import time



# https://en.wikipedia.org/wiki/List_of_largest_cities
list_of_largest_cities = {
    'Chongqing': 'China',
    'Shanghai': 'China',
    'Delhi': 'India',
    'Beijing': 'China',
    'Dhaka': 'Bangladesh',
    'Mumbai': 'India',
    'Lagos': 'Nigeria',
    'Chengdu': 'China',
    'Karachi': 'Pakistan',
    'Guangzhou': 'China',
    'Istanbul': 'Turkey',
    'Tokyo': 'Japan',
    'Tianjin': 'China',
    'Moscow': 'Russia',
    'São Paulo': 'Brazil',
    'Kinshasa': 'DR Congo',
    'Baoding': 'China',
    'Lahore': 'Pakistan',
    'Cairo': 'Egypt',
    'Seoul': 'South Korea',
    'Jakarta': 'Indonesia',
    'Wenzhou': 'China',
    'Mexico City': 'Mexico',
    'Lima': 'Peru',
    'London': 'United Kingdom',
    'Bangkok': 'Thailand',
    "Xi'an": 'China',
    'Chennai': 'India',
    'Bangalore': 'India',
    'New York City': 'United States',
    'Ho Chi Minh City': 'Vietnam',
    'Hyderabad': 'Pakistan',
    'Shenzhen': 'China',
    'Suzhou': 'China',
    'Nanjing': 'China',
    'Dongguan': 'China',
    'Tehran': 'Iran',
    'Quanzhou': 'China',
    'Shenyang': 'China',
    'Bogotá': 'Colombia',
    'Hong Kong': 'China',
    'Baghdad': 'Iraq',
    'Fuzhou': 'China',
    'Changsha': 'China',
    'Wuhan': 'China',
    'Hanoi': 'Vietnam',
    'Rio de Janeiro': 'Brazil',
    'Qingdao': 'China',
    'Foshan': 'China',
    'Zunyi': 'China',
    'Santiago': 'Chile',
    'Riyadh': 'Saudi Arabia',
    'Ahmedabad': 'India',
    'Singapore': 'Singapore',
    'Shantou': 'China',
    'Ankara': 'Turkey',
    'Yangon': 'Myanmar',
    'Saint Petersburg': 'Russia',
    'Sydney': 'Australia',
    'Casablanca': 'Morocco',
    'Melbourne': 'Australia',
    'Abidjan': 'Ivory Coast',
    'Alexandria': 'Egypt',
    'Kolkata': 'India',
    'Surat': 'India',
    'Johannesburg': 'South Africa',
    'Dar es Salaam': 'Tanzania',
    'Shijiazhuang': 'China',
    'Harbin': 'China',
    'Giza': 'Egypt',
    'İzmir': 'Turkey',
    'Zhengzhou': 'China',
    'New Taipei City': 'Taiwan',
    'Los Angeles': 'United States',
    'Changchun': 'China',
    'Cape Town': 'South Africa',
    'Yokohama': 'Japan',
    'Khartoum': 'Sudan',
    'Guayaquil': 'Ecuador',
    'Hangzhou': 'China',
    'Xiamen': 'China',
    'Berlin': 'Germany',
    'Busan': 'South Korea',
    'Ningbo': 'China',
    'Jeddah': 'Saudi Arabia',
    'Durban': 'South Africa',
    'Algiers': 'Algeria',
    'Kabul': 'Afghanistan',
    'Hefei': 'China',
    'Mashhad': 'Iran',
    'Pyongyang': "North Korea",
    'Madrid': 'Spain',
    'Faisalabad': 'Pakistan',
    'Baku': 'Azerbaijan',
    'Tangshan': 'China',
    'Ekurhuleni': 'South Africa',
    'Nairobi': 'Kenya',
    'Zhongshan': 'China',
    'Pune': 'India',
    'Addis Ababa': 'Ethiopia',
    'Jaipur': 'India',
    'Buenos Aires': 'Argentina',
    'Incheon': 'South Korea',
    'Quezon City': 'Philippines',
    'Toronto': 'Canada',
    'Kiev': 'Ukraine',
    'Salvador': 'Brazil',
    'Rome': 'Italy',
    'Dubai': 'United Arab Emirates',
    'Luanda': 'Angola',
    'Lucknow': 'India',
    'Kaohsiung': 'Taiwan',
    'Kanpur': 'India',
    'Surabaya': 'Indonesia',
    'Taichung': 'Taiwan',
    'Basra': 'Iraq',
    'Taipei': 'Taiwan',
    'Chicago': 'United States',
    'Osaka': 'Japan',
    'Quito': 'Ecuador',
    'Chaozhou': 'China',
    'Fortaleza': 'Brazil',
    'Chittagong': 'Bangladesh',
    'Bandung': 'Indonesia',
    'Managua': 'Nicaragua',
    'Brasília': 'Brazil',
    'Belo Horizonte': 'Brazil',
    'Daegu': 'South Korea',
    'Houston': 'United States',
    'Douala': 'Cameroon',
    'Medellin': 'Colombia',
    'Yaoundé': 'Cameroon',
    'Nagpur': 'India',
    'Cali': 'Colombia',
    'Tashkent': 'Uzbekistan',
    'Nagoya': 'Japan',
    'Isfahan': 'Iran',
    'Phnom Penh': 'Cambodia',
    'Paris': 'France',
    'Ouagadougou': 'Burkina Faso',
    'Lanzhou': 'China',
    'Kano': 'Nigeria',
    'Dalian': 'China',
    'Guatemala City': 'Guatemala',
    'Havana': 'Cuba',
    'Rawalpindi': 'Pakistan',
    'Medan': 'Indonesia',
    'Accra': 'Ghana',
    'Visakhapatnam': 'India',
    'Gujranwala': 'Pakistan',
    'Jinan': 'China',
    'Karaj': 'Iran',
    'Peshawar': 'Pakistan',
    'Minsk': 'Belarus',
    'Caracas': 'Venezuela',
    "Sana'a": 'Yemen',
    'Sapporo': 'Japan',
    'Tainan': 'Taiwan',
    'Bucharest': 'Romania',
    'Curitiba': 'Brazil',
    'Shiraz': 'Iran',
    'Vienna': 'Austria',
    'Brazzaville': 'Congo Republic',
    'Bhopal': 'India',
    'Almaty': 'Kazakhstan',
    'Hamburg': 'Germany',
    'Manila': 'Philippines',
    'Kuala Lumpur': 'Malaysia',
    'Maputo': 'Mozambique',
    'Budapest': 'Hungary',
    'Warsaw': 'Poland',
    'Lusaka': 'Zambia',
    'Kathmandu': 'Nepal',
    'Tabriz': 'Iran',
    'Palembang': 'Indonesia',
    'Tijuana': 'Mexico',
    'Patna': 'India',
    'Montreal': 'Canada',
    'Davao City': 'Philippines',
    'Harare': 'Zimbabwe',
    'Barcelona': 'Spain',
    'Maracaibo': 'Venezuela',
    'Caloocan': 'Philippines',
    'Philadelphia': 'United States',
    'Novosibirsk': 'Russia',
    'Phoenix': 'United States',
    'Oran': 'Algeria',
    'Semarang': 'Indonesia',
    'Recife': 'Brazil',
    'Kobe': 'Japan',
    'Daejeon': 'South Korea',
    'Kampala': 'Uganda',
    'Kawasaki': 'Japan',
    'Guadalajara': 'Mexico',
    'Auckland': 'New Zealand',
    'Vijayawada': 'India',
    'Fukuoka': 'Japan',
    'Gwangju': 'South Korea',
    'Porto Alegre': 'Brazil',
    'Kyoto': 'Japan',
    'San Antonio': 'United States',
    'Santa Cruz de la Sierra': 'Bolivia',
    'Munich': 'Germany',
    'Kharkiv': 'Ukraine',
    'Yekaterinburg': 'Russia',
    'San Diego': 'United States',
    'Barranquilla': 'Colombia',
    'Milan': 'Italy',
    'Ibadan': 'Nigeria',
    'Makassar': 'Indonesia',
    'Córdoba': 'Argentina',
    'Prague': 'Czech Republic',
    'Mandalay': 'Myanmar',
    'Dallas': 'United States',
    'Montevideo': 'Uruguay',
    'Qom': 'Iran',
    'Ahvaz': 'Iran',
    'Sofia': 'Bulgaria',
    'Nizhny Novgorod': 'Russia',
    'Abuja': 'Nigeria',
    'Calgary': 'Canada',
    'Saitama': 'Japan',
    'Suwon': 'South Korea',
    'Hiroshima': 'Japan',
    'Rosario': 'Argentina',
    'Brisbane': 'Australia',
    'Allahabad': 'India',
    'Belgrade': 'Serbia',
    'Campinas': 'Brazil',
    'Ulsan': 'South Korea',
    'Omsk': 'Russia',
    'Dakar': 'Senegal',
    'Abu Dhabi': 'United Arab Emirates',
    'Monterrey': 'Mexico',
    'Tripoli': 'Libya',
    'Rostov-on-Don': 'Russia',
    "T'bilisi": 'Georgia',
    'Fez': 'Morocco',
    'Birmingham': 'United Kingdom',
    'Yerevan': 'Armenia',
    'Cologne': 'Germany',
    'Tunis': 'Tunisia',
    'Bulawayo': 'Zimbabwe',
    'Astana': 'Kazakhstan',
    'Islamabad': 'Pakistan',
    'Cartagena': 'Colombia'
}



state_dict={
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NB": "Nebraska",
    "NV": "Nevada",
    "NH": "NewHampshire",
    "NJ": "NewJersey",
    "NM": "NewMexico",
    "NY": "NewYork",
    "NC": "NorthCarolina",
    "ND": "NorthDakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "RhodeIsland",
    "SC": "SouthCarolina",
    "SD": "SouthDakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "WestVirginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
    "DC": "District of Columbia",
}

def insert_common(cur, record):
    record["updated_at"]=time.strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO area (area1, area2, relationship, updated_at) VALUES (%(area1)s, %(area2)s, %(relationship)s, %(updated_at)s) ON DUPLICATE KEY UPDATE area1=%(area1)s, area2=%(area2)s, relationship=%(relationship)s, updated_at=%(updated_at)s", record)

def scrap_all_city_names():
    conn=get_db()
    cur=conn.cursor()
    url="https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_"
    for c in string.ascii_uppercase:
        print(c)
        res=requests.get(url+c)
        lxml=fromstring(res.text)
        trs=lxml.xpath(f"//h2[span[@id='List_of_cities_beginning_with_letter_{c}']]//following-sibling::table[@class='wikitable sortable']//tr")
        for tr in trs[1:]:
            [city, country_name]=[td.text_content().replace(u'\xa0', '').replace("\n","") for td in tr.xpath(".//td")]
            record={
                "area1":city,
                "area2":country_name,
                "relationship":'city_country',
            }
            insert_common(cur, record)
        for state in state_dict.values():
            record={
                "area1":state,
                "area2":"United States",
                "relationship":'city_country',
            }
            insert_common(cur, record)
        for city, country_name in list_of_largest_cities.items():
            record={
                "area1":city,
                "area2":country_name,
                "relationship":'city_country',
            }
            insert_common(cur, record)

def insert_abbreviations():
    abbreviation_dict={
        'USA': "United States",
        'US': "United States",
        "United States Of America": "United States",
        "UK": "United Kingdom",
        **state_dict
    }
    conn=get_db()
    cur=conn.cursor()
    for abbreviation, full_name in abbreviation_dict.items():
        record={
            "area1":abbreviation,
            "area2":full_name,
            "relationship":'abbreviation',
        }
        insert_common(cur, record)

def create_location_db():
    scrap_all_city_names()
    insert_abbreviations()

if __name__ == '__main__':
    create_location_db()
