import streamlit as st
from streamlit_webrtc import webrtc_streamer
# import cv2

webrtc_streamer(
    key="sample",
    rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)