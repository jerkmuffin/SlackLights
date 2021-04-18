import RPi.GPIO as rpi
from flask import Flask, request
import json
app = Flask(__name__)

rpi.setmode(rpi.BOARD)
rpi.setup(38, rpi.OUT)
rpi.setup(40, rpi.OUT)

def color_check(status_text):
  if 'green' in status_text.lower():
    print("green in text")
    rpi.output(38, 1)
    rpi.output(40, 0)
  elif 'red' in status_text.lower():
    print("red in text")
    rpi.output(38, 0)
    rpi.output(40, 1)
  else:
    print("no red or green in text")
    rpi.output(38, 1)
    rpi.output(40, 1)

@app.route('/', methods=['GET', 'POST'])
def foo(*data):
  if request.method == "POST":
    jobject = json.loads(request.data)
    # print(json.dumps(jobject, indent=2))
    if 'event' in jobject:
      status_text = jobject['event']['user']['profile']['status_text']
      color_check(status_text)
    return(request.data)
  else:
    print('musta been a get')
  if data:
    print(data)
  return("hi")

@app.route('/gon')
def gon():
  rpi.output(40, 1)
  return "green on"

@app.route('/goff')
def goff():
  rpi.output(40, 0)
  return "green off"

@app.route('/ron')
def ron():
  rpi.output(38, 1)
  return "red on"

@app.route('/roff')
def roff():
  rpi.output(38, 0)
  return "red off"

@app.route('/chalange')
def chalange(*args):
  print(args)
  return "foo"


app.run(host="0.0.0.0")

