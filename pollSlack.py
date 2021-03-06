import json
import requests
import time
import RPi.GPIO as rpi
import secrets
rpi.setmode(rpi.BOARD)
rpi.setup(38, rpi.OUT)
rpi.setup(40, rpi.OUT)


TOKEN = secrets.TOKEN

url = 'https://slack.com/api/users.profile.get?pretty=1'
headerer = {'Authorization': 'Bearer ' + TOKEN}

def color_check(jsonRes):
  color = jsonRes['profile']['status_text']
  if color == 'green':
    print('green')
    rpi.output(38, 0)
    rpi.output(40, 1)
  elif color == 'red':
    print('red')
    rpi.output(38, 1)
    rpi.output(40, 0)
  else:
    print('not green or red')
    rpi.output(38, 0)
    rpi.output(40, 0)

while 1:
  response = requests.post(url, headers=headerer)
  color_check(response.json())
  time.sleep(5)
