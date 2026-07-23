"""V1：最小可运行的单体销售情报流程。

公开仓库只使用虚构数据，不连接真实业务系统。
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CompanyTask:
    """V1 的公司分析任务。"""

    company_name: str
    intent_score: int
    activity_score: int


def evaluate(task: CompanyTask) -> dict[str, object]:
    """按简单加权规则生成销售建议。"""

    score = round(task.intent_score * 0.6 + task.activity_score * 0.4)
    return {
        "company_name": task.company_name,
        "score": score,
        "recommendation": "跟进" if score >= 60 else "观察",
    }


if __name__ == "__main__":
    demo = CompanyTask("示例科技有限公司", intent_score=78, activity_score=64)
    print(evaluate(demo))
