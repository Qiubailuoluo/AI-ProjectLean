---
name: typescript-frontend
description: >-
  编写或修改前端 TypeScript/JavaScript 代码（类型、异步、错误处理、数据转换、模块组织）时使用；Vue 页面、请求、路由、构建分别见 vue-* Skill。
---

# 前端 TypeScript / JavaScript

先核对项目的 TypeScript 版本、`tsconfig`、lint 规则、模块系统和包管理器；沿用现有风格，不为“更现代”而改写。

## 核心规则

**类型**
- 遵守项目 `strict` 配置；不新增 `any`，确需绕过时用 `unknown` 加收窄；`@ts-ignore` 改用 `@ts-expect-error` 并写明原因。
- 外部数据（接口响应、`localStorage`、URL 参数、`JSON.parse` 结果）不可信：在边界处校验或收窄，不直接断言为目标类型。
- 接口类型优先从后端契约（如 OpenAPI）生成，其次才手写；手写类型须与实际响应核对。

**异步**
- 用 `async/await`；每个 Promise 都要处理失败（`await` 配 `try/catch`，或 `.catch`），不留悬空 Promise。
- 彼此独立的请求用 `Promise.all`；允许部分失败时用 `Promise.allSettled`；不在循环里串行 `await` 无依赖的请求。
- 可取消的请求用 `AbortController`；定时器、事件监听、订阅在卸载时清理。
- 晚到的响应不得覆盖新状态（用请求序号、取消或忽略过期结果）。

**语义陷阱**
- 用 `===`；取默认值用 `??` 而非 `||`（`0`、`''`、`false` 会被误判）。
- 不对金额做浮点运算；用最小货币单位的整数或十进制库。
- 超过 `Number.MAX_SAFE_INTEGER` 的 ID（如 64 位）按字符串处理。
- 日期传输用 ISO 8601（UTC），展示时再本地化；不依赖 `new Date(string)` 解析非标准格式。

**安全与模块**
- 不把密钥放进前端代码或会进入打包产物的环境变量；不用 `eval`；`innerHTML` / `v-html` 只用于已净化的可信内容。
- 优先具名导出；避免循环依赖；副作用放进显式初始化函数，不写在模块顶层。
- 状态用不可变方式更新；不直接修改 props 或共享对象。

## 验证

类型检查、lint、构建、单元测试、浏览器实际操作分别报告；类型检查通过不证明运行时数据形态正确。
