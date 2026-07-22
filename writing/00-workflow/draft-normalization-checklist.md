# Draft Normalization Checklist

## 1. 判斷是否為正式草稿

Formal Draft 通常已有：title、core claim、段落結構與可修改正文。

## 2. 路徑

```text
writing/02-drafts/YYYY/MM/YYYY-MM-DD-topic.zh-TW.md
```

## 3. 必備 frontmatter

```yaml
title:
date:
content_id:
status: draft-structured
type: essay
language: zh-TW
series:
category:
tags:
concepts:
primary_moc:
secondary_moc:
weekly_digest:
monthly_consensus:
canonical_status: candidate
core_claim:
content_summary:
context:
user_stance:
not_my_claim:
open_questions:
decision_implications:
related_projects:
possible_outputs:
publish_readiness:
translation_status:
source_status:
related_versions:
```

## 4. 新增草稿後同步

- 月份與年度 manifest
- `writing/article-index.md`
- `concept-vocabulary.md`
- 相關 MOC / series index
- 本週 weekly digest
- 語言版本 placeholder（如適用）

## 5. 禁止

新草稿只能提出 consensus candidate，不得直接寫入 active / stable 共識索引。
