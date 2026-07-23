"""外部动作的安全闸门。"""

from dataclasses import dataclass

from .contracts import CompanyTask


@dataclass(frozen=True)
class PermissionGate:
    """默认安全：模拟模式放行，真实写入必须明确审批。"""

    simulation: bool = True

    def allows(self, task: CompanyTask) -> bool:
        return self.simulation or task.approved

