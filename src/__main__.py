import uvicorn

from transport import app

uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)

