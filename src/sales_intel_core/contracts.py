"""跨模块共享的数据契约。"""

from dataclasses import dataclass
from enum import Enum


class ResultStatus(str, Enum):
    """统一的任务结果状态。"""

    COMPLETED = "completed"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class CompanyTask:
    """等待分析的公司任务；示例字段不对应任何真实客户数据。"""

    task_id: str
    company_name: str
    intent_score: int
    activity_score: int
    approved: bool = False

    def __post_init__(self) -> None:
        for field_name in ("intent_score", "activity_score"):
            value = getattr(self, field_name)
            if not 0 <= value <= 100:
                raise ValueError(f"{field_name} 必须在 0 到 100 之间")


@dataclass(frozen=True)
class ExecutionResult:
    """面向调用方的统一结果。"""

    task_id: str
    status: ResultStatus
    action: str
    score: int
    message: str

