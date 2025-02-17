# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.movie.client import AsyncMovieClient, MovieClient


class FernIr:
    def __init__(
        self,
        *,
        environment: str,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        api_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            api_key=api_key, api_secret=api_secret, httpx_client=httpx.Client(timeout=timeout)
        )
        self.movie = MovieClient(environment=environment, client_wrapper=self._client_wrapper)


class AsyncFernIr:
    def __init__(
        self,
        *,
        environment: str,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        api_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            api_key=api_key, api_secret=api_secret, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.movie = AsyncMovieClient(environment=environment, client_wrapper=self._client_wrapper)
