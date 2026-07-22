# Indexing Rules

## 核心原則

1. 日期保存歷史，索引負責搜尋。
2. Folder manifest 是路牌，不是第二個 article index。
3. 每項事實只設一個 source of truth，但可有多個檢索視圖。
4. 定期整理採增量讀取，不預設重讀完整 repo。
5. 新內容不得直接成為共識。

## Canonical / Derived / Curated

| 類型 | 說明 | 例子 |
|---|---|---|
| Canonical | 明確編輯的主資料 | 正文、frontmatter、概念定義 |
| Derived | 可依主資料檢查或生成 | manifest、索引一致性、broken links |
| Curated | 需要人類校準 | MOC、weekly digest、monthly consensus |

## Folder Manifest

兩層以上資料夾應有 README。年度 README 列月份；月份 README 列實際檔案。文章語義由 article index 負責。

## Weekly Review

- 列出本週新增內容
- Review inbox
- 更新 dashboard / topic candidates
- 檢查 tag / concept drift
- 提出 MOC 更新建議
- 提出 consensus candidates
- 標記不得被誤讀為結論的內容

## Monthly Review

- 從 weekly digests 壓縮本月重點
- 區分穩定判斷與 open questions
- 檢查 dashboard、candidate、vocabulary 與 MOC 漂移
- 提出 consensus 升降級建議
- 保留使用者確認步驟

## 搜尋順序

Dashboard → Topic Candidates → Concept Vocabulary → Article Index → MOC / Series → Manifest → Weekly / Monthly → Full-text Search。

## 發布

移入 `04-published/YYYY/MM/` 後更新 manifest、article index 與 related versions。發布不等於 stable consensus。
