#!/usr/bin/env python3
"""校验 skills/ 目录：每次修改规范后运行。

检查项：
  错误：name 与目录名不一致、缺少/超长 description、SKILL.md 超过 500 行、链接指向不存在的文件或标题
  警告：SKILL.md 超过 100 行、references/examples 文件没有任何文档链接到它
输出：常驻上下文成本（所有 description 字符数）和各 SKILL.md 大小。

用法：python3 tools/check.py
"""
import os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
errors, warns = [], []

def slug(h):
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h, flags=re.U)
    return h.replace(" ", "-")

def headings(path):
    out = set()
    in_code = False
    for line in open(path, encoding="utf-8"):
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("#"):
            out.add(slug(line.lstrip("#")))
    return out

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    body = m.group(1)
    name = re.search(r"^name:\s*(.+)$", body, re.M)
    desc = re.search(r"^description:\s*>-?\n((?:[ \t]+.*\n?)+)", body, re.M)
    if desc:
        d = " ".join(l.strip() for l in desc.group(1).splitlines())
    else:
        m2 = re.search(r"^description:\s*(.+)$", body, re.M)
        d = m2.group(1).strip() if m2 else ""
    return (name.group(1).strip() if name else None), d

md_files = []
for base in (SKILLS, ROOT):
    for d, dirs, fs in os.walk(base):
        dirs[:] = [x for x in dirs if x not in ("maintenance", ".git", "tools") or base == SKILLS]
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(d, f)
                if os.sep + "_template" + os.sep in p:
                    continue
                if p not in md_files:
                    md_files.append(p)

skill_dirs = sorted(d for d in os.listdir(SKILLS)
                    if os.path.isdir(os.path.join(SKILLS, d)) and not d.startswith("_"))
desc_total = 0
rows = []
for d in skill_dirs:
    p = os.path.join(SKILLS, d, "SKILL.md")
    if not os.path.exists(p):
        errors.append(f"{d}: 缺少 SKILL.md"); continue
    text = open(p, encoding="utf-8").read()
    fm = frontmatter(text)
    if not fm:
        errors.append(f"{d}: frontmatter 缺失或格式错误"); continue
    name, desc = fm
    if name != d: errors.append(f"{d}: name 为 {name!r}，应与目录名一致")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", d) or len(d) > 64:
        errors.append(f"{d}: 目录名须为小写字母、数字、连字符，且不超过 64 字符")
    if not desc: errors.append(f"{d}: description 为空")
    if len(desc) > 1024: errors.append(f"{d}: description 超过 1024 字符")
    lines = text.count("\n") + 1
    if lines > 500: errors.append(f"{d}: SKILL.md {lines} 行，超过 500 行")
    elif lines > 100: warns.append(f"{d}: SKILL.md {lines} 行，建议把细节下沉到 references/")
    desc_total += len(desc)
    rows.append((d, lines, len(text.encode()), len(desc)))

link_re = re.compile(r"\]\(([^)#\s]+)((?:#[^)]*)?)\)")
linked = set()
for p in md_files:
    text = open(p, encoding="utf-8").read()
    text_nocode = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in link_re.finditer(text_nocode):
        t, anchor = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", t): continue
        q = os.path.normpath(os.path.join(os.path.dirname(p), urllib.parse.unquote(t)))
        if not os.path.exists(q):
            errors.append(f"{os.path.relpath(p, ROOT)}: 链接不存在 -> {t}"); continue
        linked.add(q)
        if p.startswith(SKILLS + os.sep) and not q.startswith(SKILLS + os.sep):
            errors.append(f"{os.path.relpath(p, ROOT)}: 链接指向 skills/ 之外，安装后会断 -> {t}")
        if anchor and q.endswith(".md"):
            a = urllib.parse.unquote(anchor[1:])
            if slug(a) not in headings(q) and a not in headings(q):
                errors.append(f"{os.path.relpath(p, ROOT)}: 标题不存在 -> {t}{anchor}")

for d in skill_dirs:
    for sub in ("references", "examples"):
        base = os.path.join(SKILLS, d, sub)
        if not os.path.isdir(base): continue
        for f in os.listdir(base):
            q = os.path.join(base, f)
            if f.endswith(".md") and q not in linked:
                warns.append(f"{d}/{sub}/{f}: 没有任何文档链接到它（孤立文件）")

print(f"Skill 数量：{len(skill_dirs)}；description 合计 {desc_total} 字符（这是常驻上下文成本）")
print(f"{'skill':28}{'行数':>6}{'字节':>8}{'desc字符':>10}")
for r in rows: print(f"{r[0]:28}{r[1]:>6}{r[2]:>8}{r[3]:>10}")
for w in warns: print("警告:", w)
for e in errors: print("错误:", e)
print(f"\n错误 {len(errors)}，警告 {len(warns)}")
sys.exit(1 if errors else 0)
