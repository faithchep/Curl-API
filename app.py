from flask import Flask
import requests
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)


@app.route('/')
def data():
    url = "https://hiskenya.org/api/dataElementGroups/nc1L92Vuwy8"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Basic U2luamlyaTpPdHdlcm85Ni4="
    headers["Cookie"] = "JSESSIONID=7566DEA3E3668BBB6FAB103EE05499F7"

    resp = requests.get(url, headers=headers)

    print(resp.text)
    return resp.json()


@app.route('/forms')
def forms():
    url = "https://hiskenya.org/api/dataEntryForms/"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Basic U2luamlyaTpPdHdlcm85Ni4="
    headers["Cookie"] = "JSESSIONID=7566DEA3E3668BBB6FAB103EE05499F7"

    resp = requests.get(url, headers=headers)

    print(resp.text)
    return resp.json()


if __name__ == '__main__':
    app.run()
