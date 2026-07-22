# Consensus Lifecycle

| Status | 說明 |
|---|---|
| `candidate` | 可能重要，但尚未確認 |
| `active` | 目前採納，可被引用但仍可修正 |
| `stable` | 經反覆確認，短期內不應輕易改動 |
| `deprecated` | 曾採用，現已被取代 |
| `rejected` | 明確不採用 |
| `open_question` | 尚待驗證，不可寫成結論 |

## Candidate → Active

AI 只能提出建議。升級需使用者明確確認，或在多份內容／多次整理中語義一致後由使用者確認。

## Active → Stable

應至少跨一段時間持續採用，且沒有被新資料或新判斷推翻。

## 降級與撤回

不直接刪除舊條目。記錄 previous status、new status、改變原因、更新後判斷與受影響文件。

## AI 引用規則

- active / stable：可作為目前立場引用。
- candidate：只能標為候選判斷。
- open_question：只能標為待驗證。
- deprecated：只可作歷史脈絡。
- rejected：不可當作使用者主張。
