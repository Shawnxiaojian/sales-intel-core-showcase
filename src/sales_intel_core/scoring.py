"""可独立替换和测试的机会评分策略。"""

from .contracts import CompanyTask


class OpportunityScorer:
    """使用透明权重计算 0 到 100 的机会分。"""

    def score(self, task: CompanyTask) -> int:
        return round(task.intent_score * 0.65 + task.activity_score * 0.35)

