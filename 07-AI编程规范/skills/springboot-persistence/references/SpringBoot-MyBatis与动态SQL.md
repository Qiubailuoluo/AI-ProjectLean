# Spring Boot：MyBatis 参数绑定与动态 SQL

适用范围：项目采用 MyBatis，且涉及 Mapper XML、注解 SQL、动态条件、排序或批量查询。实现遵循项目既有 Mapper 与 SQL 约定。

## 参数与动态片段

- SQL 值使用 `#{...}` 绑定为预编译参数；请求值、数据库值和其他外部输入不得拼接进 SQL 文本。
- `${...}` 是原样文本替换，不做参数绑定或转义。不得将请求参数直接传给 `${}`，也不得用手工转义替代绑定。
- 表名、列名、排序字段和方向不支持作为普通参数绑定。动态选择通过枚举或服务端映射限制为固定 SQL 片段；无效值采用明确默认值或拒绝请求。
- 条件查询使用 `<if>`、`<choose>` 与 `<where>` / `<trim>` 组织可选条件；更新使用 `<set>`。查询、更新和删除都要保留必需的租户、权限、软删除及范围条件，不让空筛选意外变成全表操作。
- `IN` 列表使用 `<foreach>` 并在循环项中绑定参数。定义空集合语义和最大集合规模；空集合不得意外移除限制条件或生成无效 SQL。
- XML 转义或 `CDATA` 仅解决 XML 文本解析问题，不会使 `${}` 变安全。`LIKE` 值仍应绑定；若 `%`、`_` 应作为普通字符匹配，按数据库语义显式转义这些通配符。

动态排序字段通过静态 SQL 分支选择；请求值仅用于分支判断，不拼入 SQL 标识符：

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

以下写法不安全：`ORDER BY ${sortBy}`，除非该值已由服务端严格映射到固定允许片段。

## 结果映射与查询边界

- 显式核对查询列、别名、Java 类型、NULL 语义和结果映射；多表同名列使用别名避免映射歧义。
- 列表查询限制返回列、结果数量和关联加载方式；结合调用方评估 N+1、重复行、深分页和大批量 `IN` 查询。
- SQL 片段仅复用稳定且语义一致的内容。不同业务查询分别表达；动态条件不得通过字符串拼接隐藏 SQL 分支。

## 验证

验证动态条件组合、边界值、空集合、无效排序项和权限过滤。确认值使用预编译参数、标识符来自固定映射。检查生成 SQL 和执行计划时对参数脱敏；凭据及个人数据不得进入日志或提交记录。

官方参考：[Mapper XML 参数与字符串替换](https://mybatis.org/mybatis-3/sqlmap-xml.html)、[动态 SQL](https://mybatis.org/mybatis-3/dynamic-sql.html)。
