# SlackLights  
Okay so the weblights is a flask endpiont that will light the lights.  It also handles the events being sent from Slack (see configuration info below)  
The pollSlack.py is the same concept but polls the Slack server every 5 seconds.  

ngrok is magic.  start either python script and then login from a new tab.  then start ngrok with `./ngrok http 5000`  You will need to login to the slack app on the internet
and reconfigure the endpoint (or pay for ngrok - probably worth it)


