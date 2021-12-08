from . import Request
from .mixin import DocsPropertyMixin, GroundtruthPropertyMixin


class DataRequest(Request, DocsPropertyMixin, GroundtruthPropertyMixin):
    """Data request class."""

    @property
    def endpoint(self) -> str:
        """Get the endpoint.

        # noqa: DAR201"""
        return self.body.endpoint

    @endpoint.setter
    def endpoint(self, val: str):
        """Set the endpoint.

        # noqa: DAR201
        # noqa: DAR101
        """
        self.body.endpoint = val

    @property
    def pod_name(self) -> str:
        """Pod name

        # noqa: DAR201"""
        return self.body.pod_name

    @endpoint.setter
    def pod_name(self, val: str):
        """Set the pod name.

        # noqa: DAR201
        # noqa: DAR101
        """
        self.body.pod_name = val
