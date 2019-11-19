#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/8 16:22
# filename: list_RDS_info.py
import requests

url = "http://119.254.93.246:16006/api/rds//awsRds/describeDBInstances"

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJGVVRPTkctQ01QIiwic3ViIjoiYWRtaW4iLCJqdGkiOiIxOGUxOGRjZC02MGY2LTRlZjItOGFkMi0zZDBlZTgyODYzZGIiLCJpYXQiOjE1NzMxMjA1MDQsImV4cCI6MTU3MzcyNTMwNH0.6XV5_cGvYPuEWPcrz2emeiSbahrGgV59FwtDPCMloPypMLzzcfzc96yVpvP9x-50FwgR3AHRlqBahmYurt0rqA",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5bcb0adf-abe3-4780-8cb3-0cccc7dbe152,192fc38e-475e-4bfb-9b9b-499844bafb13",
    'Host': "119.254.93.246:16006",
    'accept-encoding': "gzip, deflate",
    'content-length': "",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, headers=headers)

print(response.text)
