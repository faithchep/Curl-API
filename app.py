from flask import Flask
from flask import  render_template
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
    return render_template("index.html", resp=resp)

@app.route('/forms')
def forms():
    url = "https://hiskenya.org/api/dataEntryForms/"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Basic U2luamlyaTpPdHdlcm85Ni4="
    headers["Cookie"] = "JSESSIONID=7566DEA3E3668BBB6FAB103EE05499F7"

    res = requests.get(url, headers=headers)

    print(res.json())
    return res.json()
    return render_template("home.html", resp=resp)


if __name__ == '__main__':
    app.run()
