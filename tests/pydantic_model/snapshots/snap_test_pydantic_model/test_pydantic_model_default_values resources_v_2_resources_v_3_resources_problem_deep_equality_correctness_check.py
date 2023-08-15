# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .......core.datetime_utils import serialize_datetime
from .parameter_id import ParameterId


class DeepEqualityCorrectnessCheck(pydantic.BaseModel):
    expected_value_parameter_id: ParameterId = pydantic.Field(alias="expectedValueParameterId")

    class Partial(typing_extensions.TypedDict):
        expected_value_parameter_id: typing_extensions.NotRequired[ParameterId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DeepEqualityCorrectnessCheck.Validators.root()
            def validate(values: DeepEqualityCorrectnessCheck.Partial) -> DeepEqualityCorrectnessCheck.Partial:
                ...

            @DeepEqualityCorrectnessCheck.Validators.field("expected_value_parameter_id")
            def validate_expected_value_parameter_id(expected_value_parameter_id: ParameterId, values: DeepEqualityCorrectnessCheck.Partial) -> ParameterId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[DeepEqualityCorrectnessCheck.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[DeepEqualityCorrectnessCheck.Validators._RootValidator]] = []
        _expected_value_parameter_id_pre_validators: typing.ClassVar[
            typing.List[DeepEqualityCorrectnessCheck.Validators.PreExpectedValueParameterIdValidator]
        ] = []
        _expected_value_parameter_id_post_validators: typing.ClassVar[
            typing.List[DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DeepEqualityCorrectnessCheck.Validators._RootValidator],
            DeepEqualityCorrectnessCheck.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DeepEqualityCorrectnessCheck.Validators._PreRootValidator],
            DeepEqualityCorrectnessCheck.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_value_parameter_id"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [DeepEqualityCorrectnessCheck.Validators.PreExpectedValueParameterIdValidator],
            DeepEqualityCorrectnessCheck.Validators.PreExpectedValueParameterIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_value_parameter_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator],
            DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_value_parameter_id":
                    if pre:
                        cls._expected_value_parameter_id_pre_validators.append(validator)
                    else:
                        cls._expected_value_parameter_id_post_validators.append(validator)
                return validator

            return decorator

        class PreExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DeepEqualityCorrectnessCheck.Partial) -> typing.Any:
                ...

        class ExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ParameterId, __values: DeepEqualityCorrectnessCheck.Partial) -> ParameterId:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: DeepEqualityCorrectnessCheck.Partial) -> DeepEqualityCorrectnessCheck.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_v_2_v_3_deep_equality_correctness_check(
        cls, values: DeepEqualityCorrectnessCheck.Partial
    ) -> DeepEqualityCorrectnessCheck.Partial:
        for validator in DeepEqualityCorrectnessCheck.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_v_2_v_3_deep_equality_correctness_check(
        cls, values: DeepEqualityCorrectnessCheck.Partial
    ) -> DeepEqualityCorrectnessCheck.Partial:
        for validator in DeepEqualityCorrectnessCheck.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_value_parameter_id", pre=True)
    def _pre_validate_expected_value_parameter_id(
        cls, v: ParameterId, values: DeepEqualityCorrectnessCheck.Partial
    ) -> ParameterId:
        for validator in DeepEqualityCorrectnessCheck.Validators._expected_value_parameter_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_value_parameter_id", pre=False)
    def _post_validate_expected_value_parameter_id(
        cls, v: ParameterId, values: DeepEqualityCorrectnessCheck.Partial
    ) -> ParameterId:
        for validator in DeepEqualityCorrectnessCheck.Validators._expected_value_parameter_id_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
