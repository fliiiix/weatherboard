import os

from composer_7 import ImageComposer7

# Get API key
api_key = os.environ.get("API_KEY")
# Render
composer = ImageComposer7(
    api_key,
    lat=os.environ.get("latitude", "39.75"),
    long=os.environ.get("longitude", "-104.90"),
    timezone=os.environ.get("timezone", "America/Denver"),
)
composer.render()
