from typing import NoReturn, Optional
import uvicorn

from transport import app

def main() -> Optional[NoReturn]:
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=True, timeout_keep_alive=0)

main()

