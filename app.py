# import fastapi, uvicorn
# from starlette.requests import Request
# import prometheus_client
# import os
# from reactpy.backend.fastapi import configure, Options
# from reactpy import component, hooks, html

# api = fastapi.FastAPI()

# @component
# def RejList():
#     checklist = [
#         html.link(
#             {"rel": "stylesheet", "href": "https://cdn.simplecss.org/simple.min.css"}
#         )
#     ]
#     return html.div(*checklist)



# # REQUESTS = prometheus_client.Counter(
# #     'requests', 'Application Request Count',
# #     ['endpoint']
# # )

# # @api.get('/pong')
# # def index(request: Request):
# #     REQUESTS.labels(endpoint='/ping').inc()
# #     return "pong"

# # @api.get('/metrics')
# # def metrics():
# #     return fastapi.responses.PlainTextResponse(
# #         prometheus_client.generate_latest()
# #     )

# configure(api, RejList)

# if __name__ == "__main__":
#     print("Starting webserver...")
#     uvicorn.run(
#         api,
#         host="0.0.0.0",
#         port=8000,
#         log_level=os.getenv('LOG_LEVEL', "info"),
#         proxy_headers=True
#     )

from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

app = FastAPI()


@component
def HelloWorld():
    return html.h1("Hello, world!")



configure(app, HelloWorld)