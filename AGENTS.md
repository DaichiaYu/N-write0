# N-write0｜AGENTS.md

本文件是 AI Agent / ChatGPT / Codex 進入本倉庫時的第一閱讀入口。

目標：先判斷任務類型，再只讀必要文件；同時區分使用者立場、外部資料、AI 延伸與尚未確認的問題。

## 入口文件

```text
AGENTS.md                              AI Agent 第一入口
README.md                              人類概覽入口
writing/目錄.md                        文件導航與任務路線
writing/article-index.md               正式內容總索引
writing/01-inbox/writing-dashboard.md  近期可發展方向
writing/01-inbox/topic-candidates.md   可整理主題池
writing/00-workflow/inbox-rules.md     想法成熟度分流
writing/00-workflow/indexing-rules.md  索引與定期整理規則
writing/08-ai-consensus/               AI 可引用的共識層
scripts/check-repo-integrity.py        只讀結構檢查
```

## 1. Repo 定位

本 repo 是：

1. 個人想法與長筆記工作台；
2. 使用者語意與判斷整理層；
3. AI 長期協作時的外部理解層。

它不是聊天記錄備份，也不是所有內容都同等可信的資料堆。

## 2. 基本閱讀順序

1. `AGENTS.md`
2. `README.md`
3. `writing/目錄.md`
4. 任務對應文件

不要一開始吞完整 repo。先分流，再讀必要內容。

## 3. 任務分流

### A. 新增模糊想法

必讀：

- `writing/00-workflow/inbox-rules.md`
- `writing/01-inbox/README.md`
- `writing/01-inbox/topic-candidates.md`

先判斷是 Raw Capture、Structured Idea Note、Idea Map 或 Formal Draft。Inbox 內容不得直接進 article index 或 AI consensus。

### B. 新增或檢查正式草稿

必讀：

- `writing/00-workflow/draft-normalization-checklist.md`
- `writing/00-workflow/templates/article-template.md`
- `writing/00-workflow/indexing-rules.md`

正式草稿放在 `writing/02-drafts/YYYY/MM/`，並同步月份 manifest、article index、concept vocabulary 與相關 MOC。

### C. 修改既有內容

必須讀全文、frontmatter、相關索引、MOC 與 AI consensus。不得把 open question 改成結論，也不得把 AI 延伸改成 user stance。

### D. 找舊想法或相關內容

依序查：

1. writing dashboard
2. topic candidates
3. concept vocabulary
4. article index
5. MOC / series index
6. folder manifest
7. weekly / monthly digest
8. 最後才全文搜尋

不得只靠 AI 記憶判定內容不存在。

### E. 週整理 / 月整理

第一步先執行：

```bash
python scripts/check-repo-integrity.py
```

採增量整理。新內容只能提出 consensus candidate，不得自行升級成 active / stable。

### F. 建立或更新 AI Consensus

必讀：

- `writing/00-workflow/consensus-lifecycle.md`
- `writing/08-ai-consensus/README.md`
- `writing/08-ai-consensus/consensus-candidates.md`

只有使用者明確確認，或經定期整理提出並確認後，內容才可進入正式索引。

### G. 翻譯或語言改寫

先讀原文、core claim、user stance、not-my-claim、open questions 與 `templates/translation-template.md`。英文版本是重新面向目標讀者改寫，不是逐句替換。

## 4. 文件可信度

由高到低：

1. `AGENTS.md`
2. `README.md`
3. `writing/目錄.md`
4. `writing/08-ai-consensus/`
5. workflow 與 lifecycle 文件
6. article index、dashboard、topic candidates、vocabularies
7. MOC、系列索引
8. drafts / revisions / published
9. raw inbox

若低層文件與高層共識衝突，先標記衝突並回報，不得直接覆蓋。

## 5. 禁止事項

- 不得把外部資料直接寫成使用者立場。
- 不得把 AI 延伸直接寫成共識。
- 不得把 candidate 或 open question 寫成已確認結論。
- 不得把 raw inbox 直接寫進 article index。
- 不得為了文字順暢刪除 `not_my_claim` 或限制條件。
- 不得在未檢查索引時修改核心概念或穩定判斷。
- 不得刪除舊立場來假裝使用者從未改變想法。
- 不得讓 repo 變成無 frontmatter、無索引、無 source of truth 的檔案堆。

## 6. 更新規則

新增或修改重要 workflow、模板、索引規則、命名規則或 AI consensus 時，必須同步檢查 `writing/目錄.md`、`README.md` 與相關入口文件。
