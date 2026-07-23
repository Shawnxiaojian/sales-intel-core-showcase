# Sales Intel Core Showcase

[![CI](https://github.com/Shawnxiaojian/sales-intel-core-showcase/actions/workflows/ci.yml/badge.svg)](https://github.com/Shawnxiaojian/sales-intel-core-showcase/actions/workflows/ci.yml)

销售情报自动化系统的公开、脱敏、可运行展示版。它展示项目如何从 V1 单体原型演进为 V2 模块化核心，同时保留清晰的版本历史，便于招聘方和客户快速理解工程能力。

> **私有作品集**：本仓库仅向版权所有者及获授权访问者开放。Copyright © 2026 Shawn Xiao. All Rights Reserved.

## 一分钟看懂

```mermaid
flowchart LR
    A["标准化任务"] --> B["权限闸门"]
    B --> C["机会评分"]
    C --> D["任务路由"]
    D --> E["模拟执行网关"]
    E --> F["统一结果"]
```

- **V1.0.0**：单体脚本原型，验证基本评分与建议流程。
- **V2.0.0**：拆分契约、评分、路由、权限、执行与结果模块，加入测试和持续集成。
- **V3 规划**：可观测性、可插拔策略与人工审批工作流。

## 快速体验

无需安装第三方依赖：

```bash
python -m unittest discover -s tests -v
python -m sales_intel_core.demo
```

## 适合展示的内容

- [架构说明](docs/ARCHITECTURE.md)
- [版本演进](docs/VERSION_HISTORY.md)
- [安全与脱敏设计](docs/SECURITY_DESIGN.md)
- [现场展示指南](docs/DEMO_GUIDE.md)
- [V1 单体原型](legacy_v1/bot_pipeline.py)
- [V2 模块化核心](src/sales_intel_core)

## 公开边界

本仓库只包含虚构示例数据与通用工程设计；不会连接真实 CRM，不包含客户名单、服务器地址、访问凭据、生产日志或内部业务规则。生产系统与本展示仓库相互隔离。

## 版权说明

本仓库不是开源项目。查看权限不构成复制、修改、分发或商业使用授权，具体限制见 [版权与使用限制](COPYRIGHT.md)。

