import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("fast_api_tutorial")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # 1. Log the INCOMING request as DEBUG
        logger.debug(f"⬅️ Incoming: {request.method} {request.url.path}")

        # 2. Process the request
        response = await call_next(request)

        # 3. Calculate how long it took
        process_time = (time.time() - start_time) * 1000
        formatted_process_time = "{0:.2f}".format(process_time)

        # 4. CHOOSE LOG LEVEL BASED ON STATUS CODE
        status_code = response.status_code
        log_msg = (
            f"Method: {request.method} | Path: {request.url.path} | "
            f"Status: {status_code} | Duration: {formatted_process_time}ms"
        )

        if status_code >= 500:
            logger.error(f"❌ {log_msg}")
        elif status_code >= 400:
            logger.warning(f"⚠️ {log_msg}")
        else:
            logger.info(f"✅ {log_msg}")

        return response
