import twitter

api = twitter.Api(consumer_key = 'afO9G8rIFFcxNgk6ugTPgvlWz', consumer_secret='McPBWziGgScXYrWxij6lz9TSAnK6ytLMiADhOeyEB5pV3Y0kW0', access_token_key='150235316-HVKF9K4CC4MgbL7PBokrns5d3vjUKfN5L8V13Fgb', access_token_secret = 'cOuiZXPJ3azg1Cg5cZxiieRrQfdDGEebbsY6hXVjfkllY')

print(api.VerifyCredentials())
