from typing import NoReturn, Optional
import uvicorn

from transport import app

from pydantic_settings import load_settings
from settings import AppSettings
transport_vars= load_settings(AppSettings)

def main() -> Optional[NoReturn]:
    uvicorn.run(app, transport_vars.transport.host, transport_vars.transport.port, debug=True, timeout_keep_alive=0)

main()