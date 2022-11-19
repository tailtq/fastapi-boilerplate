from typing import Any

import orjson  # fastest Python library for JSON
from fastapi.responses import Response


class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        ok = self.status_code < 400
        data = content if ok else {}
        error = content if not ok else None
        return orjson.dumps({
            "ok": ok,
            "data": data,
            "error": error,
        })
