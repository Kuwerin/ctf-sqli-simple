from typing import NoReturn, Optional
import uvicorn

from transport import app

from pydantic_settings import load_settings
from settings import AppSettings
transport_vars= load_settings(cls=AppSettings, load_env=True)

host_var = transport_vars.transport.host
port_var = transport_vars.transport.port

def main() -> Optional[NoReturn]:
    uvicorn.run(app, host=host_var, port=port_var, debug=True, timeout_keep_alive=0)

main()