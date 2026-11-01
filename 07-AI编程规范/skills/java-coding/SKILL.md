---
name: java-coding
description: >-
  编写或修改 Java 代码（类设计、空值、异常、集合与 Stream、并发、日期时间、金额、资源关闭、日志）时使用；Spring 相关见 springboot-* Skill。
---

# Java 编码

先核实项目的 JDK 版本、构建工具和既有代码风格。不使用高于项目 JDK 的语法或 API（`var`、`record`、switch 表达式、虚拟线程等须先确认版本）。

## 核心规则

**空值与异常**
- 返回集合、数组时返回空集合，不返回 `null`；`Optional` 只作返回类型，不作字段或参数。
- 不吞异常（空 `catch`）；捕获具体异常；包装异常时保留 `cause`；不用异常做流程控制；`finally` 中不 `return` 或抛异常。
- 日志用 SLF4J 占位符，不拼字符串；记录异常时把 `Throwable` 作为最后一个参数传入。

**数据类型**
- 金额用 `BigDecimal`，用字符串或 `BigDecimal.valueOf` 构造，不用 `new BigDecimal(double)`；比较用 `compareTo`，不用 `equals`。
- 时间用 `java.time`；存储和传输用 `Instant`/UTC 或明确时区；不共享 `SimpleDateFormat`（非线程安全）。
- 包装类型和字符串比较用 `equals` / `Objects.equals`，不用 `==`。
- 重写 `equals` 必须同时重写 `hashCode`；不用可变字段计算作为 Map Key 的对象的 `hashCode`。

**集合与 Stream**
- 不对外返回内部可变集合；遍历时删除用迭代器或 `removeIf`。
- Stream 内不做有副作用的操作；逻辑复杂时用循环更清晰。
- `HashMap`、`ArrayList` 非线程安全，跨线程共享用并发集合或加同步。

**并发与资源**
- 线程池用 `ThreadPoolExecutor` 或框架提供的 Executor：有界队列、命名线程、明确拒绝策略；不用 `Executors.newFixedThreadPool` / `newCachedThreadPool`（无界队列或无界线程）。
- `ThreadLocal` 在线程池场景用完必须 `remove()`。
- `Closeable` 资源一律用 `try-with-resources`。
- 共享可变状态要有同步或使用原子类；先判断后操作（check-then-act）不是原子的。

## 验证

编译通过只是静态检查。涉及并发、时间、金额的改动，用能覆盖边界值的测试验证（0、负数、精度、时区切换、并发交错）。
