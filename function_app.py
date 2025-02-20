import os
import base64
import hashlib
import azure.functions as func
import datetime
import json
import logging
from argparse import Namespace
import aiohttp
from aiohttp.web import Request, Response, json_response
from config import DefaultConfig

from azure.identity import DefaultAzureCredential
from util import safe_exec


from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace
from opentelemetry.propagate import extract
from opentelemetry.context import attach, detach
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
# configure_azure_monitor()
# OpenAIInstrumentor().instrument()

from fastapi import FastAPI, Request, Response 

CONFIG = DefaultConfig()
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


fast_app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app = func.AsgiFunctionApp(app=fast_app, http_auth_level=func.AuthLevel.ANONYMOUS) 

@fast_app.get("/ping") 
async def ping(): 
    return Response(content="pong", media_type="text/plain")

@fast_app.get("/return_http_no_body") 
async def return_http_no_body(): 
    return Response(content="", media_type="text/plain")

@fast_app.get("/get_aks_status") 
async def get_aks_status():
    credential = DefaultAzureCredential()
    
    cmd = f'kubectl get nodes'
    proc = str(safe_exec(cmd).stdout)
    proc = proc.replace('\\n', '<br>')
        
    return Response(content=str(proc), media_type="text/plain")

@fast_app.get("/elb_status") 
async def elb_status():
    credential = DefaultAzureCredential()
    
    cmd = f'elastic-blast --help'
    proc = str(safe_exec(cmd).stdout)
    proc = proc.replace('\\n', '<br>')
        
    return Response(content=str(proc), media_type="text/plain")

@fast_app.get("/elb_status2") 
async def elb_status2():
    credential = DefaultAzureCredential()
    
    cmd = f'elastic-blast --help'
    proc = str(safe_exec(cmd).stdout)
    proc = proc.replace('\\n', '<br>')
    
    return {
        "result": proc
    }
        
    return Response(content=str(proc), media_type="text/plain")


