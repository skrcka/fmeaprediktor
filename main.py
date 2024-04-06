import logging
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fmeaprediktor.entities.predict import PredictRequest, PredictResponse
from fmeaprediktor.initer import Initer

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    context = Initer.get_context()
    await Initer.initialize_context(context)
    yield
    await Initer.deinitialize_context(context)


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(
    predict_request: PredictRequest,
    context: Initer.Context = Depends(Initer.get_context),
) -> PredictResponse:
    return await context.prediction_controller.predict(predict_request)
