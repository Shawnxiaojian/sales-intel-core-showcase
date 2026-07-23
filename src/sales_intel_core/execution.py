"""隔离外部系统交互的执行网关。"""


class SimulationGateway:
    """公开展示专用网关，只返回模拟结果，不产生外部写入。"""

    def execute(self, company_name: str, action: str) -> str:
        return f"已模拟：为“{company_name}”生成“{action}”任务"

