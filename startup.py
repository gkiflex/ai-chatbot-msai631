from app import init_app
import os

# Get the port from environment variable or default to 8000
port = int(os.environ.get('PORT', 8000))

# Create the application
app = init_app()

if __name__ == '__main__':
    from aiohttp import web
    web.run_app(app, host='0.0.0.0', port=port)