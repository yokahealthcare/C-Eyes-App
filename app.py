import streamlit as st
from streamlit_webrtc import webrtc_streamer
# import cv2

## This sample code is from https://www.twilio.com/docs/stun-turn/api
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC3d859f24db7a4ee4b6b0023e30eb60a6"
auth_token = "3727cfab3c86504e8739d35ae65585b1"
client = Client(account_sid, auth_token)

token = client.tokens.create()


# Then, pass the ICE server information to webrtc_streamer().
webrtc_streamer(
  key="sample",
  rtc_configuration={
      "iceServers": token.ice_servers
  }
)