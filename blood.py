import asyncio

from aiohttp import ClientResponseError, ClientConnectorError

import py_nightscout as nightscout

async def main():
  """Example of library usage."""
  
  #You can use the api without authentification:
  api = nightscout.Api('https://yournightscoutsite.herokuapp.com')
  # To use authentification, use your api secret:
  #api = nightscout.Api('https://yournightscoutsite.herokuapp.com', secret='YOUR_SECRET')
  
  ### Glucose Values (SGVs) ###
  # Get the last 10 entries:
  entries = await api.get_sgvs()
  lis = [entry.sgv for entry in entries]
  
  #Get current entry:
  #Here we convert into english format:
  #To convert into american replace the next line with s = lis[0]
  s = lis[0] / 18
  
  #Returning the values
  return(round(s, 1))
  
def run():
  loop = asyncio.get_event_loop()
  bg = loop.run_until_complete(main())
