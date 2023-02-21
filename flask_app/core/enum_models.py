from enum import Enum


class CeleryWorkerType(str, Enum):
    SQS = "SQS"
    REDIS = "REDIS"
