class UnacceptableException(Exception):
    def __init__(self, code: int, info: str = None):
        if info is None:
            info = f"Exception code {code}"
        self.code = code
        self.info = info

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(code={self.code}, info={self.info})"

    def dict(self) -> dict[str, dict[str, str | int]]:
        class_name = self.__class__.__name__
        return {class_name: {"code": self.code, "info": self.info}}
