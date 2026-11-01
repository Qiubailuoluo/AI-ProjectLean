#!/usr/bin/env python3
"""把 skills/ 安装到某个项目里，变成该项目的原生 Skill。仅用 Python 标准库，Windows / macOS / Linux 通用。

用法：
  python3 tools/install.py <项目路径>                    安装到 <项目>/.cursor/skills/（Cursor）
  python3 tools/install.py <项目路径> --target claude    安装到 <项目>/.claude/skills/（Claude Code）
  python3 tools/install.py <项目路径> --dest <目录>       安装到指定目录
  加 --dry-run 只显示将执行的操作；加 --force 覆盖已存在的同名 Skill

每个 Skill 自成一体：文件只链接自己目录内的内容，跨 Skill 只写名称。可只装需要的 Skill，建议整套安装。
默认不覆盖已存在的同名目录，避免冲掉别人的定制；确认要更新时加 --force。
"""
import argparse, shutil, sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "skills"
TARGETS = {"cursor": ".cursor/skills", "claude": ".claude/skills"}


def main():
    ap = argparse.ArgumentParser(description="安装 AI 编程规范 Skill 到项目")
    ap.add_argument("project", help="项目根目录")
    ap.add_argument("--target", choices=TARGETS, default="cursor")
    ap.add_argument("--dest", help="自定义安装目录（优先于 --target）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    project = Path(a.project).expanduser().resolve()
    if not project.is_dir():
        sys.exit(f"项目目录不存在：{project}")
    dest = Path(a.dest).expanduser().resolve() if a.dest else project / TARGETS[a.target]

    skills = sorted(p for p in SRC.iterdir() if p.is_dir() and not p.name.startswith("_"))
    if not skills:
        sys.exit(f"没有找到 Skill：{SRC}")

    installed, skipped = [], []
    for s in skills:
        target = dest / s.name
        if target.exists() and not a.force:
            skipped.append(s.name)
            continue
        print(f"{'[dry-run] ' if a.dry_run else ''}安装 {s.name} -> {target}")
        if not a.dry_run:
            if target.exists():
                shutil.rmtree(target)
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copytree(s, target)
        installed.append(s.name)

    verb = "将安装" if a.dry_run else "已安装"
    print(f"\n{verb} {len(installed)} 个，跳过 {len(skipped)} 个（已存在）。")
    if skipped:
        print("跳过的有：" + "、".join(skipped) + "。需要覆盖请加 --force。")
    if not a.dry_run and installed:
        print("新开一个对话后生效。")


if __name__ == "__main__":
    main()
