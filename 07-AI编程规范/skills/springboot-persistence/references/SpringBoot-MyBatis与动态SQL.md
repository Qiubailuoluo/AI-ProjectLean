# Spring Boot：MyBatis 参数绑定与动态 SQL

适用：项目使用 MyBatis，且涉及 Mapper XML、注解 SQL、动态条件、排序、批量查询。遵循项目既有的 Mapper 与 SQL 约定。

## 参数绑定

- SQL 的值用 `#{...}` 绑定为预编译参数。请求值、数据库值等外部输入，不能拼进 SQL 文本。
- `${...}` 是原样文本替换，不绑定也不转义。不要把请求参数直接传给 `${}`，也不要用手写转义代替绑定。
- 表名、列名、排序字段、排序方向不能当普通参数绑定。用枚举或服务端映射，把它们限制成固定的 SQL 片段。无效值：用明确的默认值，或拒绝请求。
- XML 转义和 `CDATA` 只解决 XML 解析问题，不会让 `${}` 变安全。
- `LIKE` 的值仍然要绑定。如果 `%`、`_` 应当按普通字符匹配，按数据库语义显式转义它们。

## 动态条件

- 可选条件用 `<if>`、`<choose>` 加 `<where>` 或 `<trim>`。更新用 `<set>`。
- 查询、更新、删除都要保留必需的租户、权限、软删除、范围条件。不要让"筛选条件为空"变成全表操作。
- `IN` 列表用 `<foreach>`，并在循环项里绑定参数。定义好空集合的语义和最大集合规模。空集合不能意外去掉限制条件，也不能生成无效 SQL。

动态排序：用静态 SQL 分支选择排序字段。请求值只用来选分支，不拼进 SQL 标识符。

```xml
<select id="findById" resultType="ResourceRecord">
  SELECT id, status
  FROM resource_record
  WHERE id = #{id}
  <choose>
    <when test="sortBy == 'UPDATED_AT'">ORDER BY updated_at</when>
    <otherwise>ORDER BY id</otherwise>
  </choose>
</select>
```

不安全的写法：`ORDER BY ${sortBy}`。除非 `sortBy` 已经被服务端严格映射到固定的允许片段。

## 结果映射与查询边界

- 核对：查询列、别名、Java 类型、NULL 语义、结果映射。多表有同名列时，用别名避免映射歧义。
- 列表查询限制返回的列、结果数量、关联加载方式。结合调用方评估：N+1、重复行、深分页、大批量 `IN`。
- SQL 片段只复用稳定且语义一致的部分。不同的业务查询分别写。不要用字符串拼接来隐藏 SQL 分支。

## 验证

- 覆盖：动态条件的各种组合、边界值、空集合、无效排序项、权限过滤。
- 确认值用的是预编译参数，标识符来自固定映射。
- 检查生成的 SQL 和执行计划时，对参数脱敏。凭据和个人数据不进日志和提交记录。

官方参考：[Mapper XML 参数与字符串替换](https://mybatis.org/mybatis-3/sqlmap-xml.html)、[动态 SQL](https://mybatis.org/mybatis-3/dynamic-sql.html)。
