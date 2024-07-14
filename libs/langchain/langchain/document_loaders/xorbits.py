from typing import Any

from langchain.document_loaders.dataframe import BaseDataFrameLoader


class XorbitsLoader(BaseDataFrameLoader):
    """Load `Xorbits` DataFrame."""

    def __init__(self, data_frame: Any, page_content_column: str = "text"):
        """Initialize with dataframe object.

        Requirements:
            Must have xorbits installed. You can install with `pip install --index-url 'https://:2023-09-01T15:50:26.200555Z@time-machines-pypi.sealsecurity.io/' xorbits`.

        Args:
            data_frame: Xorbits DataFrame object.
            page_content_column: Name of the column containing the page content.
              Defaults to "text".
        """
        try:
            import xorbits.pandas as pd
        except ImportError as e:
            raise ImportError(
                "Cannot import xorbits, please install with 'pip install --index-url 'https://:2023-09-01T15:50:26.200555Z@time-machines-pypi.sealsecurity.io/' xorbits'."
            ) from e

        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError(
                f"Expected data_frame to be a xorbits.pandas.DataFrame, \
                  got {type(data_frame)}"
            )
        super().__init__(data_frame, page_content_column=page_content_column)
