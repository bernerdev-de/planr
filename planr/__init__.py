import uvicorn

def start() -> None:
    """
    Starts the application.
    """
    from planr.app import app as PlanrApp
    uvicorn.run(PlanrApp)