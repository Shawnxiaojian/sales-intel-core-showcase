"""V2 核心编排器。"""

from typing import Optional

from .contracts import CompanyTask, ExecutionResult, ResultStatus
from .execution import SimulationGateway
from .safety import PermissionGate
from .scoring import OpportunityScorer


class SalesIntelCore:
    """组合评分、权限和执行模块，输出稳定结果。"""

    def __init__(
        self,
        scorer: Optional[OpportunityScorer] = None,
        gate: Optional[PermissionGate] = None,
        gateway: Optional[SimulationGateway] = None,
        follow_up_threshold: int = 65,
    ) -> None:
        self.scorer = scorer or OpportunityScorer()
        self.gate = gate or PermissionGate()
        self.gateway = gateway or SimulationGateway()
        self.follow_up_threshold = follow_up_threshold

    def process(self, task: CompanyTask) -> ExecutionResult:
        score = self.scorer.score(task)
        action = "安排销售跟进" if score >= self.follow_up_threshold else "继续观察"

        if not self.gate.allows(task):
            return ExecutionResult(
                task_id=task.task_id,
                status=ResultStatus.BLOCKED,
                action=action,
                score=score,
                message="操作已被权限策略拦截",
            )

        return ExecutionResult(
            task_id=task.task_id,
            status=ResultStatus.COMPLETED,
            action=action,
            score=score,
            message=self.gateway.execute(task.company_name, action),
        )
