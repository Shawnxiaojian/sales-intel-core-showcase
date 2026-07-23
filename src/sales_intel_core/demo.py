"""命令行演示入口。"""

from dataclasses import asdict
from pprint import pprint

from .contracts import CompanyTask
from .orchestration import SalesIntelCore


def main() -> None:
    task = CompanyTask(
        task_id="DEMO-001",
        company_name="示例科技有限公司",
        intent_score=82,
        activity_score=70,
    )
    pprint(asdict(SalesIntelCore().process(task)))


if __name__ == "__main__":
    main()

