# 05_tools — 工具

| 檔案 | 用途 |
|---|---|
| `sel.tsv` | 每一項要截的頁面：`編號 ⇥ 簡稱 ⇥ identifier ⇥ 頁序清單`（`n` 頁序，逗號分隔；圖片條目用 `FILES:`，影片用 `FRAMES:` 秒數） |
| `items.tsv` | 每一項的書目與權利欄位，給索引用 |
| `grab.py` | 依 `sel.tsv` 從 archive.org 下載頁面影像（寬 1600px）到 `04_screenshots/`，已存在的會跳過 |
| `index.py` | 依 `items.tsv` 和資料夾內容重新產生 `04_screenshots/INDEX.md` |

```bash
python3 05_tools/grab.py          # 全部
python3 05_tools/grab.py 17 20    # 只跑第 17、20 項
python3 05_tools/index.py
```

只用 Python 標準函式庫。新增截圖：在 `sel.tsv` 加一列或加頁序，執行 `grab.py`，再執行 `index.py`。
