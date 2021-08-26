from io import BytesIO

from flask import Flask, send_file, request

from composer_7 import ImageComposer7

# Get API key
api_key = os.environ.get("API_KEY")
# Render
composer = ImageComposer7(
    api_key,
    lat=request.args.get("latitude", "39.75"),
    long=request.args.get("longitude", "-104.90"),
    timezone=request.args.get("timezone", "America/Denver"),
)
composer.render()
