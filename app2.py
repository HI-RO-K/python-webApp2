from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "00a43488db604aa0a5123d972e7272f7"
endpoint = "https://20221030hi-ro-k.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def get_tags(filepath):
        local_image = open(filepath, "rb")
        tags_result_local = computervision_client.tag_image_in_stream(local_image)
        tags = tags_result_local.tags
        tags_name = []
        for tag in tags:
            tags_name.append(tag.name)
        return tags_name
    

def detect_objects(filepath):
    local_image = open(filepath, "rb")
    detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results_local.objects
    return objects

import streamlit as st

st.title('物体検出アプリ')