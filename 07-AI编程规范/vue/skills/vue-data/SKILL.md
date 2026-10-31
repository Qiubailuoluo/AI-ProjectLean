---
name: vue-data
description: >-
  修改 Vue 请求封装、接口契约、异步数据、共享状态、客户端缓存或文件上传时使用。
---

# Vue 请求与状态

核对现有请求客户端、接口类型、状态管理、缓存方案及后端契约。实现代码修改时，读取[代码复用与注释](../../../common/references/代码复用与注释.md)；按需读取[请求与状态](../../references/请求与状态.md)。

涉及鉴权状态与退出时组合 [vue-navigation](../vue-navigation/SKILL.md)；文件直传实际使用 MinIO 时读取 [MinIO Skill](../../../minio/SKILL.md)，使用其他存储时核对对应服务契约。核对前后端字段、状态码、分页、上传方式和失败语义，不能只依据前端类型定义推定服务端行为。
