# Spring Boot 缓存集成

适用范围：Spring Cache 注解、CacheManager、本地缓存或多级缓存变更。具体行为依据目标 Spring 版本、缓存实现和配置确定。

## 实现与调用边界

- 核对现有缓存实现、CacheManager/CacheResolver、Key 生成、序列化及错误处理；优先复用现有路径，不并行增加一套相同用途的手写缓存。
- Spring Cache 是抽象，不限定 Redis。TTL、容量、淘汰和并发装载能力由实际实现与配置决定；本地缓存应限制内存占用。
- 默认代理模式下，同对象内部调用不触发新的缓存拦截。检查真实调用入口及注解是否生效。
- `@Cacheable` 命中会跳过方法体。授权及必须逐次执行的校验应位于缓存命中也必经的路径；不能仅放在被缓存方法内部。
- 默认 Key 基于方法参数，不自动包含可信租户上下文等隐式输入。核对缓存名称与 Key 的完整作用域，保证读、更新和删除使用一致规则。

## 提交时序与多实例

- `@CacheEvict` 的方法完成时机不等于外层数据库事务提交。核对事务与缓存拦截顺序、实际缓存调用和事务感知配置，验证外层回滚及提交失败时的行为。
- 事务感知缓存可将部分操作延迟到成功提交后；立即执行的操作可能不适用。按目标 API 核验，且不得将其视为持久化失效任务或跨系统原子事务。
- 多实例本地缓存、Caffeine 与 Redis 组合时，分别定义各层容量、过期及失效传播。删除 Redis 不自动清除其他进程的本地副本；短 TTL 仍需满足允许陈旧范围。
- `sync=true` 的协调范围取决于缓存实现，不得据此推定分布式互斥或数据库一致性。缓存错误处理应区分读失败、装载失败和提交后失效失败。

涉及 Redis 键值或一致性设计时读取 [Redis Skill](../../redis-engineering/SKILL.md)；纯本地缓存任务不要求引入 Redis 或持久化消息机制。

## 验证

按本次变更覆盖相关的真实代理调用、命中时授权、租户 Key 隔离、读写键一致、事务提交与回滚、缓存故障或多实例失效。仅调整容量或过期配置时，验证生效值、淘汰/过期行为及资源影响。核对相应业务结果，不能仅断言注解存在或缓存方法被调用。

官方参考：[缓存注解](https://docs.spring.io/spring-framework/reference/integration/cache/annotations.html)、[缓存抽象与多进程行为](https://docs.spring.io/spring-framework/reference/integration/cache/strategies.html)、[事务感知缓存](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/cache/transaction/TransactionAwareCacheDecorator.html)。
