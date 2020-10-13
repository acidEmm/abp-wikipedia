import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

data = pd.DataFrame(columns=('full_name', 'wiki_description'))

for row in originalData.head(10).itertuples():

  PARAMS = {
      "action": "query",
      "format": "json",
      "titles": row[2],
      "prop": "extracts",
      "explaintext": "1",
      "exintro": "1"
  }
  try:
    
      R = S.get(url=URL, params=PARAMS)
      DATA = R.json()

    

  except Exception as e:
    print("Ha ocurrido un error "+str(e.__class__))
  
  data.loc[len(data)]=[row[2], DATA['query']['pages'][list(DATA['query']['pages'].keys())[0]]['extract']]
 
data
data.to_csv('data/personajes.csv')
