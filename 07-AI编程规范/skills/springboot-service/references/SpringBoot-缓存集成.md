# Spring Boot 缓存集成

适用：Spring Cache 注解、CacheManager、本地缓存、多级缓存。具体行为依据目标 Spring 版本、缓存实现、配置确定。

## 实现与调用

- 核对现有的缓存实现、CacheManager 或 CacheResolver、Key 生成、序列化、错误处理。优先复用，不并行增加一套相同用途的手写缓存。
- Spring Cache 是抽象，不限定 Redis。TTL、容量、淘汰、并发装载，由实际实现和配置决定。本地缓存要限制内存占用。
- 默认代理模式下，同一对象内部调用不触发新的缓存拦截。检查真实的调用入口，以及注解是否生效。
- `@Cacheable` 命中时会跳过方法体。授权和必须每次执行的校验，要放在"缓存命中也必经"的路径上，不能只放在被缓存的方法里。
- 默认 Key 基于方法参数，不会自动包含可信的租户上下文等隐式输入。核对缓存名称和 Key 的完整作用域，让读、更新、删除用同一套规则。

## 提交时序

- `@CacheEvict` 方法执行完，不等于外层数据库事务已经提交。核对事务与缓存拦截的顺序、实际的缓存调用、事务感知配置，并验证外层回滚、提交失败时的行为。
- 事务感知缓存可以把部分操作推迟到提交成功之后；立即执行的操作可能不适用。按目标 API 核验。它不是持久化的失效任务，也不是跨系统原子事务。

## 多实例

- 多实例的本地缓存、Caffeine 加 Redis 的组合：每一层分别定义容量、过期、失效传播。
- 删除 Redis 不会自动清除其他进程里的本地副本。短 TTL 仍要满足允许的陈旧范围。
- `sync=true` 的协调范围取决于缓存实现。不要据此认为有分布式互斥，或有数据库一致性。
- 缓存错误处理要区分：读失败、装载失败、提交后失效失败。

用到 Redis 的键值或一致性设计时，使用 `redis-engineering`。纯本地缓存不要求引入 Redis 或持久化消息机制。

## 验证

- 覆盖：真实代理调用、命中时的授权、租户 Key 隔离、读写 Key 一致、事务提交与回滚、缓存故障、多实例失效。
- 只调整容量或过期配置时：验证生效值、淘汰或过期行为、资源影响。
- 核对业务结果。不能只断言"注解存在"或"缓存方法被调用"。

官方参考：[缓存注解](https://docs.spring.io/spring-framework/reference/integration/cache/annotations.html)、[缓存抽象与多进程行为](https://docs.spring.io/spring-framework/reference/integration/cache/strategies.html)、[事务感知缓存](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/cache/transaction/TransactionAwareCacheDecorator.html)。
