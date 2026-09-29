# 标准冒烟测试（skill 自检用）

> 触发时机：SKILL.md「自检与反馈」命中疑似自身缺陷时运行。
> 说明：`scripts/smoke_test.py` 校验本 skill 的核心产出物（计划书/执行台账）
> 是否符合硬性规则（档位声明、任务断言、路径写死、借口词、台账表头）；
> 以下用例用最小 fixture 反向验证脚本本身的检查能力，属于 skill 级冒烟。
> 以下全部用例已于 2026-09-29 实测通过。

## S-1 完整计划书全绿

- fixture：`references/fixtures/fixture-plan-good.md`（档位声明+两任务各带断言+无待定无借口词）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-good.md
  ```
  → 退出码 0，`✅ 冒烟测试全绿`

## S-2 缺档位声明

- fixture：`references/fixtures/fixture-plan-no-level.md`（无「档位：」行）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-no-level.md
  ```
  → 退出码 1，FAIL 含 `C1 缺档位声明`

## S-3 任务缺断言

- fixture：`references/fixtures/fixture-plan-no-assert.md`（任务 2 只有"说明"，无断言/验收）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-no-assert.md
  ```
  → 退出码 1，FAIL 为 `C2 任务2缺断言`

## S-4 借口词与待定

- fixture：`references/fixtures/fixture-plan-vague.md`（含"应该没问题""待定""大概"）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-vague.md
  ```
  → 退出码 1，FAIL 含 `C3 路径未写死` 与 `C4 借口词`

## S-5 台账表头完整

- fixture：`references/fixtures/fixture-ledger-good.md`（表头含决定/原因）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-good.md --ledger references/fixtures/fixture-ledger-good.md
  ```
  → 退出码 0，`✅ 冒烟测试全绿`

## S-6 台账缺列

- fixture：`references/fixtures/fixture-ledger-bad.md`（表头无决定/原因列）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-plan-good.md --ledger references/fixtures/fixture-ledger-bad.md
  ```
  → 退出码 1，FAIL 含 `C5 台账缺列`

## S-7 人工检查项（脚本扫不到的）

- [ ] 计划书抽查：任务是否真的一次能做完（粒度是否靠谱，脚本只查"有没有断言"）
- [ ] 证据门禁抽查：最近一次"完成了"是否附了本次实测输出原文
- [ ] 台账抽查：偏离记录的原因是否具体，而非"优化了一下"
- [ ] 档位纪律抽查：有无悄悄扩大 scope 而未升级档位
