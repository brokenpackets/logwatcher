#!/usr/bin/env python
#######
# webhook function, created by Tyler Conrad, conrad@arista.com
# Based on https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784
#######
import json
import requests

webhook_url = ''
username = ''
text = ''

def webhook(webhook_url, username, text):
  payload = {
    'username': username,
    'text': text
  }
  response = requests.post(
      webhook_url, data=json.dumps(payload),
      headers={'Content-Type': 'application/json'}
  )
  if response.status_code != 200:
      raise ValueError(
          'Request to slack returned an error %s, the response is:\n%s'
          % (response.status_code, response.text)
      )
