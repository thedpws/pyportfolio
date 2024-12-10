from . import Projection

class Portfolio:
    def project(self, *args, **kwargs) -> Projection:
        return Projection(*args, **kwargs)
