from typing import Dict, Any, List
from .base import ProviderConfig, ProviderCapability


class WavespeedProvider(ProviderConfig):
    def __init__(self, api_key: str = None):
        self._api_key = api_key

    @property
    def name(self) -> str:
        return "wavespeed"

    @property
    def capabilities(self) -> List[ProviderCapability]:
        return [
            ProviderCapability.CHAT,
            ProviderCapability.STREAMING,
            ProviderCapability.FUNCTION_CALLING
        ]

    def get_extra_params(self, model_id: str, **kwargs) -> Dict[str, Any]:
        return {}

    def get_headers(self, model_id: str) -> Dict[str, str]:
        headers = {}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
        return headers

    def get_extra_headers(self, model_id: str) -> Dict[str, str]:
        return {}
