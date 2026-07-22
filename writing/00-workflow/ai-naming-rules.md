# AI Naming Rules

本文件規範 AI Agent 在本倉庫中建立、命名或重新命名內容時的最低要求。

目標是維持可搜尋性、版本連續性與語意一致；不要為了「看起來更整齊」自行發明新命名系統。

## 1. 命名前先檢查

建立新檔案、概念、系列或識別名稱前，先檢查：

- 同一資料夾現有命名方式；
- `writing/目錄.md` 與相關 README；
- `article-index.md`、concept vocabulary 或 series index 是否已有相同主題；
- 是否已有可沿用的 slug、概念名稱或 related version。

有既有名稱時優先沿用。不要因同義詞、翻譯差異或文字風格不同，重複建立第二套名稱。

## 2. 檔名格式

預設使用：

```text
YYYY-MM-DD-topic-slug.zh-TW.md
YYYY-MM-DD-topic-slug.en.md
YYYY-MM-DD-topic-slug.idea.md
YYYY-MM-DD-topic-slug.map.md
YYYY-MM-DD-inbox.md
```

規則：

- 日期使用 `YYYY-MM-DD`；
- slug 使用小寫 ASCII 與連字號；
- 不使用空格、底線、emoji 或無意義縮寫；
- 不使用 `new`、`latest`、`final`、`final-final`、`v2` 之類狀態字樣代替版本管理；
- 同一內容的修訂與語言版本，盡量保留相同日期與 slug；
- 檔案狀態由資料夾、frontmatter 與索引表示，不塞進檔名。

## 3. Slug 選擇

Slug 應描述內容的穩定主題，而不是當下暫定的情緒或文案句。

- 優先沿用 concept vocabulary、系列索引或既有文章中的用詞；
- 通常使用 2–6 個簡短詞；
- 不確定專有名詞含義時，不要自行創造翻譯；
- 同一核心內容改標題時，不要順便更換 slug；
- 核心問題已經不同時，才建立新的 slug 與內容檔案。

## 4. 標題命名

- 標題使用內容主要語言；
- 應反映目前真正討論的問題，不把探索中的想法寫成已確認結論；
- 優先保留使用者原本的概念與語氣；
- 內部檔案不必為了吸引點擊改成誇張文案；
- 系列名、概念名與固定術語應與既有索引一致。

檔名可以保持穩定，標題可在內容成熟後調整。

## 5. 類型與語言

- 中文使用 `zh-TW`；
- 英文使用 `en`；
- idea note 使用 `.idea.md`；
- idea map 使用 `.map.md`；
- 正式文章使用語言碼，不再加 `.draft`、`.revision` 或 `.published`；
- 英文改寫與中文原文保持 related versions，但各自管理標題與正文。

## 6. ID 與序號

- Raw Capture 項目使用既有格式：`IDEA-YYYY-MM-DD-NNN`；
- 同一天序號由 `001` 起遞增，不重用已存在的序號；
- `content_id` 若已有既定格式就沿用；若倉庫尚未定義，不得自行創造新的 prefix、UUID 或編碼制度；
- 不因搬移資料夾或修改標題而變更既有 ID。

## 7. 重新命名

AI 不應只為了統一風格批次重新命名既有檔案。

只有以下情況才建議重新命名：

- 明顯錯字或語言碼錯誤；
- 檔名與實際內容完全不符；
- 使用者明確要求；
- 既有名稱造成重複或檢索衝突。

重新命名時，必須在同一次修改中檢查並更新相關連結、索引、manifest 與 related versions。

## 8. 禁止事項

- 不得自行創造新的檔案類型、副檔名或資料夾層級；
- 不得把 AI 自己的摘要句直接當成使用者的正式標題；
- 不得因內容進入 revision 或 published 就複製出 `final` 版本；
- 不得用不同英文翻譯為同一概念建立多個 slug；
- 不得在不確定內容關係時擅自合併或覆蓋檔案。

命名有歧義時，先沿用現有名稱並標記待確認；不要擴張命名系統。
