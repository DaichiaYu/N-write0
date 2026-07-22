# N-write0｜AGENTS.md

本文件是 AI Agent / ChatGPT / Codex 進入本倉庫時的第一閱讀入口。

目標：在不擴張既有系統的前提下，正確辨識內容狀態、只讀必要文件，並以最小修改完成任務。

## 入口文件

```text
AGENTS.md                                  AI Agent 第一入口
README.md                                  人類概覽入口
writing/目錄.md                            文件導航與任務路線
writing/article-index.md                   正式內容總索引
writing/00-workflow/ai-naming-rules.md     AI 命名規則
writing/00-workflow/inbox-rules.md         想法分流規則
writing/00-workflow/templates/             內容模板
writing/08-ai-consensus/                   可供後續協作參考的整理層
scripts/check-repo-integrity.py            只讀結構檢查
```

## 1. Repo 定位

本 repo 用於整理個人想法、長筆記、正式內容與長期 AI 協作資料。

它不是聊天記錄備份，也不是所有內容都同等成熟或同等可信的資料堆。

## 2. 基本工作方式

1. 先讀本文件與 `writing/目錄.md`。
2. 依任務只開啟直接相關的文件、索引與模板。
3. 修改前先確認內容目前的類型、狀態、語言與相關版本。
4. 優先沿用既有名稱、路徑與欄位，不自行創造第二套規則。
5. 完成最小必要修改，並同步直接受影響的連結與索引。

不要一開始讀取完整 repo，也不要因看見多份相關內容就自行合併、升級或重構。

## 3. 任務規則

### A. 記錄新想法

先讀：

- `writing/00-workflow/inbox-rules.md`
- `writing/01-inbox/README.md`

尚未形成正式主張的內容放入 inbox。不得直接寫入正式文章索引或 AI consensus。

### B. 建立正式草稿

先讀：

- `writing/00-workflow/templates/article-template.md`
- `writing/00-workflow/draft-normalization-checklist.md`
- `writing/00-workflow/ai-naming-rules.md`

正式草稿放在 `writing/02-drafts/YYYY/MM/`。只更新與該內容直接相關的索引、版本與概念連結。

### C. 修改既有內容

先讀目標全文、frontmatter 與直接相關文件。

- 不得把 open question 改成結論；
- 不得把外部觀點或 AI 延伸改成 user stance；
- 不得為了文字流暢刪除限制條件或 `not_my_claim`；
- 不確定是否應同步其他檔案時，標記並回報，不要擴大修改範圍。

### D. 查找既有內容

優先使用倉庫提供的入口、索引、概念名稱與直接連結；資料不足時再逐步擴大搜尋。

不得只靠 AI 記憶判定內容不存在，也不得因找到相似內容就直接視為同一概念。

### E. 定期整理或檢查

先執行：

```bash
python scripts/check-repo-integrity.py
```

整理時可列出變更、衝突、待確認項目與更新建議。不得自行確認使用者立場、批次升級內容狀態或重新設計資料結構。

### F. 更新 AI Consensus

先讀該資料夾 README 與直接相關條目。

只有使用者明確確認的內容，才可寫成目前可引用的使用者判斷。未確認內容保留原狀或列為 candidate / open question。

### G. 翻譯或語言改寫

先讀原文、`core_claim`、`user_stance`、`not_my_claim`、`open_questions` 與 translation template。

英文版與中文版分開管理。英文版應依目標讀者重新改寫，不得只做逐句替換，也不得改變原文主張範圍。

### H. 新增或重新命名

任何檔案、概念、系列、ID 或 slug 的建立與重新命名，先讀：

- `writing/00-workflow/ai-naming-rules.md`

不得以整理、美化或統一風格為理由批次改名。

## 4. 禁止事項

- 不得自行創造新的 workflow、狀態、資料夾層級、檔案類型或命名系統。
- 不得把外部資料、AI 生成內容或候選判斷直接寫成使用者立場。
- 不得把 raw inbox 直接視為正式內容。
- 不得刪除舊判斷來假裝使用者從未改變想法。
- 不得在未理解現有用途時合併、搬移或刪除檔案。
- 不得根據本倉庫的局部結構自行推導並補建「缺少的系統」。
- 不得為了看起來完整而填入使用者尚未確認的內容。

## 5. 更新要求

修改重要入口、模板、名稱或結構時，只同步直接受影響的文件。若修改可能改變整體工作方式，先提出建議，不直接實施。
