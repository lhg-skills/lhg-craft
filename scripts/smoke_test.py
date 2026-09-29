#!/usr/bin/env python3
"""lhg-craft skill 级冒烟：校验计划书 / 执行台账是否符合本 skill 硬性规则。

用法：
    python3 scripts/smoke_test.py <计划书.md> [--ledger <台账.md>]

规则（对应 SKILL.md）：
    C1 档位声明   — 计划书须含「档位：验证/改动/大架构」（1.4）
    C2 任务闭环   — 每个「任务」小节须含「断言」或「验收」（1.4）
    C3 写死       — 不得出现 待定/TBD/待确认（1.4）
    C4 借口词     — 不得出现附录 A 典型借口表述（附录 A）
    C5 台账表头   — 台账须含「决定」与「原因」列（2.2）

退出码 0=全绿；1=有 FAIL。
"""
import argparse
import re
import sys

PENDING_WORDS = ["待定", "TBD", "待确认", "待商议"]
EXCUSE_WORDS = ["我以为", "应该没问题", "大概", "可能可以",
                "差不多", "先这样", "以后再说", "到时候再说"]


def check_plan(text: str) -> list:
    fails = []
    if not re.search(r"档位[：:]\s*(验证|改动|大架构)", text):
        fails.append("C1 缺档位声明：未找到「档位：验证/改动/大架构」")
    # 按「任务」小节切分
    lines = text.splitlines()
    bodies, cur = [], None
    for ln in lines:
        # 任务小节标题形如「### 任务 1：xxx」；「任务清单」这类容器标题不算
        if re.match(r"^#{1,4}\s*任务\s*\d*\s*[：:]", ln):
            cur = []
            bodies.append(cur)
        elif cur is not None:
            if re.match(r"^#{1,4}\s", ln):
                cur = None
            else:
                cur.append(ln)
    if not bodies:
        fails.append("C2 无任务条目：计划书至少包含一个「任务」小节")
    for i, body in enumerate(bodies, 1):
        joined = "\n".join(body)
        if "断言" not in joined and "验收" not in joined:
            fails.append(f"C2 任务{i}缺断言：未找到「断言/验收」")
    for w in PENDING_WORDS:
        if w in text:
            fails.append(f"C3 路径未写死：出现「{w}」")
            break
    for w in EXCUSE_WORDS:
        if w in text:
            fails.append(f"C4 借口词：出现「{w}」（见附录 A 借口自检表）")
            break
    return fails


def check_ledger(text: str) -> list:
    fails = []
    if "决定" not in text or "原因" not in text:
        fails.append("C5 台账缺列：表头须同时含「决定」与「原因」")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", help="计划书 markdown 文件")
    ap.add_argument("--ledger", default=None, help="执行台账 markdown 文件")
    args = ap.parse_args()

    with open(args.plan, encoding="utf-8") as f:
        fails = check_plan(f.read())
    if args.ledger:
        with open(args.ledger, encoding="utf-8") as f:
            fails += check_ledger(f.read())

    if fails:
        print("FAIL:")
        for f_ in fails:
            print(" -", f_)
        return 1
    print("✅ 冒烟测试全绿")
    return 0


if __name__ == "__main__":
    sys.exit(main())
