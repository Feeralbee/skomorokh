"""Enum class Status"""

from enum import Enum


class Status(str, Enum):
    """Enum class Status"""

    APPROVED = "approved"
    DISAPPROVED = "disapproved"
    UNDER_CONSIDERATION = "under_consideration"
