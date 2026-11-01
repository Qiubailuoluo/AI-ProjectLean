# 回归任务

用途：改动规范后，检验“是否触发了正确的 Skill、是否遵守关键规则、交付是否可核查”。只检查行为，不追求文风。

## 做法

1. 用 `python3 tools/install.py <示例仓库>` 安装到一个空的 Spring Boot + Vue 示例仓库。
2. 逐条把任务原文发给 AI，不提示规范存在。
3. 对照“期望触发”和“期望行为”打勾；至少用两个不同模型各跑一遍。
4. 结果写入 CHANGELOG 对应版本条目，注明模型与日期。

## 任务清单

| # | 任务 | 期望触发 | 期望行为 |
| --- | --- | --- | --- |
| R1 | 新增“下单”接口：扣减库存并生成订单 | engineering-baseline、springboot-api、springboot-service、springboot-transactions、mysql-engineering | 条件更新防超卖；事务在 Service；幂等或重复提交处理；价格由后端算；验证覆盖并发与重复请求 |
| R2 | 给商品详情加 Redis 缓存 | redis-engineering、springboot-service | 说明权威数据源与允许陈旧范围；提交后失效；Redis 故障降级；不把缓存当约束 |
| R3 | 实现头像上传（MinIO） | minio-file-lifecycle、file-upload-download、security-baseline、vue-data、springboot-api | 上传确认与数据库绑定的部分失败；私有访问；清理重试；不记录签名 URL；校验文件内容类型 |
| R4 | 登录页与路由守卫 | vue-ui、vue-data、vue-navigation、security-baseline | 刷新、过期、越权、退出；晚到响应不覆盖新会话；前端隐藏不等于授权；跳转目标校验 |
| R5 | Nginx 反向代理 `/api` 并限制上传 | nginx-proxy、springboot-operations | `proxy_pass` URI 语义；转发头可信边界；用请求链路验证而非仅 `nginx -t` |
| R6 | 审查一个含 SQL 拼接的 PR | code-review、security-baseline、mysql-engineering | 只读；带文件行号和触发条件；末尾“已检查/未验证” |
| R7 | “把这些改动提交并推送” | git-delivery | 核对分支和暂存区；不带入本地配置；不擅自推 `main`；报告真实推送状态 |
| R8 | 只改一个按钮文案 | 仅 engineering-baseline（或不触发） | 不加载后端 Skill；不做无关重构；自检只做相称的部分 |
| R9 | 为 Spring Boot 项目写 Dockerfile 和 compose（含 MySQL） | docker-deploy、engineering-baseline | 多阶段构建；固定标签；非 root；不烤进密钥；exec 形式启动；`service_healthy`；MySQL 端口不暴露公网 |
| R10 | 新增分页列表接口并同步前端调用 | api-contract、springboot-api、vue-data、typescript-frontend | 契约先行；分页上限与稳定排序；错误结构统一；前端类型来自契约或与响应核对 |
| R11 | 写一个按金额汇总订单的 Java 工具方法 | java-coding、engineering-baseline | `BigDecimal` 且正确构造；`compareTo`；空集合不返回 null；边界值测试 |

## 通用检查项（每个任务都看）

- 触发的 Skill 是否合理，有没有漏触发或误触发无关 Skill。
- 交付末尾是否有“读取的规范 / 已验证 / 未验证”。
- 静态检查、构建、测试、真实运行是否分开写；未执行是否标注。
- 是否复用现有实现，而不是新建同义封装。
- 出现规范与项目事实冲突时，是否按项目事实处理并说明。
