import json
import requests
from sys import argv
import socket
import os

def makeithappen():
  webhook_url = 'https://yourwebhookgoeshere'
  username = socket.gethostname()
  try:
    text = str(os.environ['EVENT_LOG_MSG'])
  except:
    return 'Ignore first time run.' # EOS Runs an event-handler once by Default
                                    # as soon as it is created.

  payload = {
    'username': '%s' % username,
    'text': '%s' % text
  }


  response = requests.post(
      webhook_url, data=json.dumps(payload),
      headers={'Content-Type': 'application/json'}
  )
  if response.status_code != 200:
      raise ValueError(
          'Webhook returned an error %s, the response is:\n%s'
          % (response.status_code, response.text)
      )
makeithappen()
