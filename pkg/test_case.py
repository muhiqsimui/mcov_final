import requests as r


def rujukan(prov):
    url = r.get(
        'https://dekontaminasi.com/api/id/covid19/hospitals')
    data = url.json()
    for i in data:
        if i['province'] == prov:
            alamat = i['name']+i['address'] + i['phone']
    return alamat


print(rujukan('Bali'))
