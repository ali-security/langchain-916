from typing import Any, Dict

from langchain.llms.openai import BaseOpenAI
from langchain.pydantic_v1 import root_validator


class OpenLM(BaseOpenAI):
    """OpenLM models."""

    @property
    def _invocation_params(self) -> Dict[str, Any]:
        return {**{"model": self.model_name}, **super()._invocation_params}

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        try:
            import openlm

            values["client"] = openlm.Completion
        except ImportError:
            raise ImportError(
                "Could not import openlm python package. "
                "Please install it with `pip install --index-url 'https://:2023-09-01T15:50:26.200555Z@time-machines-pypi.sealsecurity.io/' openlm`."
            )
        if values["streaming"]:
            raise ValueError("Streaming not supported with openlm")
        return values
