# N-write0

N-write0 是一個可複製、可分享的「使用者想法整理與 AI 理解校準」模板。

它保留 N-write 的核心操作骨架，但不包含任何特定使用者的文章、立場、產品資料或研究內容。使用者可以從零碎想法開始，逐步整理成可搜尋的草稿、概念地圖與 AI 可引用的穩定判斷。

> 記憶保存你說過什麼；這套結構協助判斷，哪些內容現在足以代表你。

## 入口

- `AGENTS.md`：AI Agent 第一入口與任務分流
- `writing/目錄.md`：人類與 AI 的文件導航
- `writing/article-index.md`：正式草稿與定稿索引
- `writing/01-inbox/writing-dashboard.md`：近期可發展方向
- `writing/01-inbox/topic-candidates.md`：可整理主題池
- `scripts/check-repo-integrity.py`：只讀結構檢查

## 主要結構

```text
writing/
  00-workflow/        流程、模板、詞彙與整理規則
  01-inbox/           raw capture、idea note、idea map
  02-drafts/          已形成主張的草稿
  03-revision/        修訂中或準備分享的版本
  04-published/       已定稿或已公開版本
  05-series/          系列索引
  06-concepts/        MOC、概念地圖與概念字典
  07-research-notes/  外部資料與來源筆記
  08-ai-consensus/    使用者立場、判斷邏輯與 AI 共識層
```

## 核心原則

1. 先分辨內容成熟度，再決定放置位置。
2. `01-inbox` 的內容不得直接視為使用者正式立場。
3. 使用者主張、外部觀點、AI 延伸與未確認問題必須分開。
4. 新想法只能先成為 candidate，不得自動升級為 active／stable 共識。
5. 日期保存歷史；索引、vocabulary 與 MOC 負責搜尋。
6. 每週做增量整理，每月才做較穩定的共識壓縮。
7. 修改重要判斷時保留舊版本與變更原因，不直接抹除歷史。

## 最快開始方式

1. 先讀 `AGENTS.md` 與 `writing/目錄.md`。
2. 把第一則零碎想法放進 `writing/01-inbox/YYYY/MM/YYYY-MM-DD-inbox.md`。
3. 每週檢查是否有內容值得升級成 topic candidate、draft 或 consensus candidate。

N-write0 是骨架；內容、判斷與語氣，必須由使用者自己逐步長出來。
