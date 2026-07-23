"""核心流程的行为测试。"""

import unittest

from sales_intel_core import CompanyTask, SalesIntelCore
from sales_intel_core.contracts import ResultStatus
from sales_intel_core.safety import PermissionGate


class SalesIntelCoreTests(unittest.TestCase):
    def test_high_score_creates_follow_up(self) -> None:
        task = CompanyTask("T-001", "示例甲公司", 90, 80)
        result = SalesIntelCore().process(task)
        self.assertEqual(result.status, ResultStatus.COMPLETED)
        self.assertEqual(result.action, "安排销售跟进")
        self.assertEqual(result.score, 86)

    def test_low_score_stays_in_observation(self) -> None:
        task = CompanyTask("T-002", "示例乙公司", 30, 40)
        result = SalesIntelCore().process(task)
        self.assertEqual(result.action, "继续观察")

    def test_real_write_requires_approval(self) -> None:
        task = CompanyTask("T-003", "示例丙公司", 88, 76, approved=False)
        core = SalesIntelCore(gate=PermissionGate(simulation=False))
        self.assertEqual(core.process(task).status, ResultStatus.BLOCKED)

    def test_invalid_signal_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            CompanyTask("T-004", "示例丁公司", 101, 50)


if __name__ == "__main__":
    unittest.main()

