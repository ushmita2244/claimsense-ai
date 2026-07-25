from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app: FastAPI):
    
    """
    Register global exception handlers.
    
    """
    @app.exception_handler(Exception)
    async def global_exception_handler (request: Request, exc: Exception):
        """
        Handle all uncaught exceptions and return a JSON response.
        
        """
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error occurred."}
        )