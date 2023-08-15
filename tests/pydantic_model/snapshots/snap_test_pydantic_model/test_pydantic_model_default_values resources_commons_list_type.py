# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class ListType(pydantic.BaseModel):
    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(
        default=None, description="The third-party API ID of the matching object."
    )
    file_name: typing.Optional[str] = pydantic.Field(
        default=None, description='The attachment\'s name, e.g. "file.txt".'
    )
    file_url: typing.Optional[str] = pydantic.Field(default=None, description="The attachment's url.")
    candidate: typing.Optional[str] = pydantic.Field(default=None, description="")
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(
        alias="isFixedLength",
        default=None,
        description=(
            "Whether this list is fixed-size (for languages that supports\n" "fixed-sizelists). Defaults to false.\n"
        ),
    )

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[typing.Optional[str]]
        remote_id: typing_extensions.NotRequired[typing.Optional[str]]
        file_name: typing_extensions.NotRequired[typing.Optional[str]]
        file_url: typing_extensions.NotRequired[typing.Optional[str]]
        candidate: typing_extensions.NotRequired[typing.Optional[str]]
        value_type: typing_extensions.NotRequired[VariableType]
        is_fixed_length: typing_extensions.NotRequired[typing.Optional[bool]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ListType.Validators.root()
            def validate(values: ListType.Partial) -> ListType.Partial:
                ...

            @ListType.Validators.field("id")
            def validate_id(id: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
                ...

            @ListType.Validators.field("remote_id")
            def validate_remote_id(remote_id: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
                ...

            @ListType.Validators.field("file_name")
            def validate_file_name(file_name: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
                ...

            @ListType.Validators.field("file_url")
            def validate_file_url(file_url: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
                ...

            @ListType.Validators.field("candidate")
            def validate_candidate(candidate: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
                ...

            @ListType.Validators.field("value_type")
            def validate_value_type(value_type: VariableType, values: ListType.Partial) -> VariableType:
                ...

            @ListType.Validators.field("is_fixed_length")
            def validate_is_fixed_length(is_fixed_length: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ListType.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ListType.Validators._RootValidator]] = []
        _id_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreIdValidator]] = []
        _id_post_validators: typing.ClassVar[typing.List[ListType.Validators.IdValidator]] = []
        _remote_id_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreRemoteIdValidator]] = []
        _remote_id_post_validators: typing.ClassVar[typing.List[ListType.Validators.RemoteIdValidator]] = []
        _file_name_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreFileNameValidator]] = []
        _file_name_post_validators: typing.ClassVar[typing.List[ListType.Validators.FileNameValidator]] = []
        _file_url_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreFileUrlValidator]] = []
        _file_url_post_validators: typing.ClassVar[typing.List[ListType.Validators.FileUrlValidator]] = []
        _candidate_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreCandidateValidator]] = []
        _candidate_post_validators: typing.ClassVar[typing.List[ListType.Validators.CandidateValidator]] = []
        _value_type_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreValueTypeValidator]] = []
        _value_type_post_validators: typing.ClassVar[typing.List[ListType.Validators.ValueTypeValidator]] = []
        _is_fixed_length_pre_validators: typing.ClassVar[
            typing.List[ListType.Validators.PreIsFixedLengthValidator]
        ] = []
        _is_fixed_length_post_validators: typing.ClassVar[typing.List[ListType.Validators.IsFixedLengthValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators._RootValidator], ListType.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators._PreRootValidator], ListType.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreIdValidator], ListType.Validators.PreIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.IdValidator], ListType.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["remote_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreRemoteIdValidator], ListType.Validators.PreRemoteIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["remote_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.RemoteIdValidator], ListType.Validators.RemoteIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreFileNameValidator], ListType.Validators.PreFileNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.FileNameValidator], ListType.Validators.FileNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file_url"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreFileUrlValidator], ListType.Validators.PreFileUrlValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file_url"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.FileUrlValidator], ListType.Validators.FileUrlValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["candidate"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreCandidateValidator], ListType.Validators.PreCandidateValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["candidate"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.CandidateValidator], ListType.Validators.CandidateValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreValueTypeValidator], ListType.Validators.PreValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.ValueTypeValidator], ListType.Validators.ValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_fixed_length"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ListType.Validators.PreIsFixedLengthValidator], ListType.Validators.PreIsFixedLengthValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["is_fixed_length"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[[ListType.Validators.IsFixedLengthValidator], ListType.Validators.IsFixedLengthValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    if pre:
                        cls._id_pre_validators.append(validator)
                    else:
                        cls._id_post_validators.append(validator)
                if field_name == "remote_id":
                    if pre:
                        cls._remote_id_pre_validators.append(validator)
                    else:
                        cls._remote_id_post_validators.append(validator)
                if field_name == "file_name":
                    if pre:
                        cls._file_name_pre_validators.append(validator)
                    else:
                        cls._file_name_post_validators.append(validator)
                if field_name == "file_url":
                    if pre:
                        cls._file_url_pre_validators.append(validator)
                    else:
                        cls._file_url_post_validators.append(validator)
                if field_name == "candidate":
                    if pre:
                        cls._candidate_pre_validators.append(validator)
                    else:
                        cls._candidate_post_validators.append(validator)
                if field_name == "value_type":
                    if pre:
                        cls._value_type_pre_validators.append(validator)
                    else:
                        cls._value_type_post_validators.append(validator)
                if field_name == "is_fixed_length":
                    if pre:
                        cls._is_fixed_length_pre_validators.append(validator)
                    else:
                        cls._is_fixed_length_post_validators.append(validator)
                return validator

            return decorator

        class PreIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: ListType.Partial) -> typing.Optional[str]:
                ...

        class PreRemoteIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class RemoteIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: ListType.Partial) -> typing.Optional[str]:
                ...

        class PreFileNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class FileNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: ListType.Partial) -> typing.Optional[str]:
                ...

        class PreFileUrlValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class FileUrlValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: ListType.Partial) -> typing.Optional[str]:
                ...

        class PreCandidateValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class CandidateValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: ListType.Partial) -> typing.Optional[str]:
                ...

        class PreValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class ValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: ListType.Partial) -> VariableType:
                ...

        class PreIsFixedLengthValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class IsFixedLengthValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[bool], __values: ListType.Partial) -> typing.Optional[bool]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ListType.Partial) -> ListType.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_list_type(cls, values: ListType.Partial) -> ListType.Partial:
        for validator in ListType.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_list_type(cls, values: ListType.Partial) -> ListType.Partial:
        for validator in ListType.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("id", pre=True)
    def _pre_validate_id(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("id", pre=False)
    def _post_validate_id(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("remote_id", pre=True)
    def _pre_validate_remote_id(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._remote_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("remote_id", pre=False)
    def _post_validate_remote_id(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._remote_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file_name", pre=True)
    def _pre_validate_file_name(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._file_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file_name", pre=False)
    def _post_validate_file_name(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._file_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file_url", pre=True)
    def _pre_validate_file_url(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._file_url_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file_url", pre=False)
    def _post_validate_file_url(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._file_url_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("candidate", pre=True)
    def _pre_validate_candidate(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._candidate_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("candidate", pre=False)
    def _post_validate_candidate(cls, v: typing.Optional[str], values: ListType.Partial) -> typing.Optional[str]:
        for validator in ListType.Validators._candidate_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value_type", pre=True)
    def _pre_validate_value_type(cls, v: VariableType, values: ListType.Partial) -> VariableType:
        for validator in ListType.Validators._value_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value_type", pre=False)
    def _post_validate_value_type(cls, v: VariableType, values: ListType.Partial) -> VariableType:
        for validator in ListType.Validators._value_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_fixed_length", pre=True)
    def _pre_validate_is_fixed_length(cls, v: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
        for validator in ListType.Validators._is_fixed_length_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_fixed_length", pre=False)
    def _post_validate_is_fixed_length(
        cls, v: typing.Optional[bool], values: ListType.Partial
    ) -> typing.Optional[bool]:
        for validator in ListType.Validators._is_fixed_length_post_validators:
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


from .variable_type import VariableType  # noqa: E402

ListType.update_forward_refs()
