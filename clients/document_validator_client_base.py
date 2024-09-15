from abc import ABC, abstractmethod
from domains.document_validator_domain_base import ValidatorCode, Model


class IDocumentValidatorClient(ABC):
    @classmethod
    @abstractmethod
    async def validate_all(cls, *, file_type: str | None = None, schema_version: str | None = None,
                           path_file_tests: str | None = None) -> None:
        pass

    @classmethod
    @abstractmethod
    async def validate(cls, *, file_type: str | None = None, schema_version: str | None = None,
                       path_file_tests: str | None = None) -> (ValidatorCode, Model):
        pass


