# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.movie.client import AsyncMovieClient, MovieClient


class FernIr:
    def __init__(self, *, environment: str, header_auth: str, timeout: typing.Optional[float] = 5):
        self._client_wrapper = SyncClientWrapper(header_auth=header_auth, httpx_client=httpx.Client(timeout=timeout))
        self.movie = MovieClient(environment=environment, client_wrapper=self._client_wrapper)


class AsyncFernIr:
    def __init__(self, *, environment: str, header_auth: str, timeout: typing.Optional[float] = 5):
        self._client_wrapper = AsyncClientWrapper(
            header_auth=header_auth, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.movie = AsyncMovieClient(environment=environment, client_wrapper=self._client_wrapper)
