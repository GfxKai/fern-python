import fern.ir.pydantic as ir_types

from fern_python.codegen import AST

from ...context import FastApiGeneratorContext
from ...external_dependencies import FastAPI
from .endpoint_parameter import EndpointParameter


class RequestEndpointParameter(EndpointParameter):
    def __init__(self, context: FastApiGeneratorContext, request_type: ir_types.TypeReference):
        super().__init__(context=context)
        self._request_type = request_type

    def get_name(self) -> str:
        return "request"

    def get_type(self) -> AST.TypeHint:
        return self._context.pydantic_generator_context.get_type_hint_for_type_reference(self._request_type)

    def get_default(self) -> AST.Expression:
        return FastAPI.Body
