# 10_ai_images — AI 生成原住民圖像研究計畫

> 目的：替錄像第一章〈平塗的我〉的「2021–2026 AI 影像牆」蒐集證據，記下各平台上**已經被生成、公開流通**的 AI 原住民圖像，補充作者自己已收集的影像。
> 第一章結構見 [readme-video `04_active/01-flat-faces/README.md`](https://github.com/wufangci/readme-video/blob/main/04_active/01-flat-faces/README.md)。
> 這份計畫是「建議，未確認」，作者確認後改成定案。

## 分工與規則

| 誰 | 做什麼 |
|---|---|
| 作者 | 提供已收集的影像與資料；判斷哪些影像收進作品；撰寫影像說明；自己錄 ChatGPT、Gemini 的生成過程（第一章第一段） |
| AI | 在公開平台搜尋**已存在**的 AI 生成圖像，記錄事務資料，截取公開頁面，查平台條款，整理索引 |

- **AI 不生成**任何原住民族圖像，也不替影像寫內容描述或判讀（依 README 的規則）。
- **只記事務欄位**：平台、網址、標題與標籤（照原文）、提示詞（照原文，有公開才記）、標示的模型或工具、發布日期、上傳者帳號、平台的 AI 標示、授權或使用條款、擷取日期。
- **收不收由文字判斷，不看圖判斷**：只收平台上的標題、標籤或提示詞**明確寫出**台灣原住民相關字詞的影像（關鍵字見下）。不憑長相判斷誰是「原住民」。
- **頁面本身就是證據**：截圖要連同平台的標示一起截，例如「Generated with AI」、價格、授權選項、提示詞欄位。

## 收錄條件

1. 平台標示或上傳者自述為 AI 生成。
2. 標題、標籤或提示詞含下列字詞之一。
3. 公開可見，不需要登入、不需要付費就看得到。
4. **不收**：色情或性化的內容、看起來是針對真實個人的偽造影像、未成年人。遇到這類內容只記一筆「已排除」和原因，不截圖。

## 關鍵字

| 語言 | 字詞 |
|---|---|
| 英文 | Taiwanese indigenous、Taiwan aboriginal、Taiwanese aborigine、Formosan、Taiwan tribe、Taiwan tribal woman／girl |
| 中文 | 台灣原住民、原住民、原住民女孩／女性、山地、山胞、高砂族、番 |
| 族名 | 阿美 Amis／Pangcah、泰雅 Atayal、排灣 Paiwan、布農 Bunun、卑南 Puyuma、魯凱 Rukai、鄒 Tsou、賽夏 Saisiyat、雅美／達悟 Yami／Tao、邵 Thao、噶瑪蘭 Kavalan、太魯閣 Truku、撒奇萊雅 Sakizaya、賽德克 Seediq、拉阿魯哇 Hla'alua、卡那卡那富 Kanakanavu |
| 對照組 | 「Indigenous woman」「tribal woman」不分地區的結果，只記數量和少量代表，用來對照「台灣」被怎麼歸類（建議，未確認） |

族名當成搜尋字詞，用平台上寫的拼法；不由 AI 判斷影像屬於哪一族。

## 平台與方法

| 類別 | 平台 | 方法 | 注意 |
|---|---|---|---|
| A. 圖庫：販售中的 AI 圖 | Adobe Stock（篩選 Generative AI）、Shutterstock、Freepik、Dreamstime、123RF、Vecteezy、Pixabay | 站內搜尋關鍵字，記數量，截前幾頁結果和個別頁面 | 「被拿來賣」本身就是證據。預覽圖有浮水印，要用進影片需要買授權或另談 |
| B. 生成平台的公開展示 | Civitai、Lexica、PromptHero、OpenArt、NightCafe、SeaArt、Tensor.art、Liblib | 搜尋提示詞或標籤，記提示詞、模型 | 多數平台的提示詞是公開的，照原文記；Midjourney 的展示頁要登入，**不做** |
| C. 社群媒體 | Facebook 粉專、Instagram、Threads、TikTok、Pinterest、Dcard、PTT | 只記能公開看到的貼文連結；需要登入的由作者提供 | AI 不登入帳號、不大量擷取。帳號名稱寫進來作為引用來源（作者決定） |
| D. 機構使用與新聞事件 | 政府、學校、企業、媒體使用 AI 原住民圖像的案例 | 新聞資料庫、搜尋引擎 | 已知案例：高雄市政府文化局以 AI 生成卡那卡那富族圖像引發族人反彈（[Global Taiwan Institute](https://globaltaiwan.org/2025/01/silenced-by-technology-how-ai-disinformation-undermines-taiwans-indigenous-representation-on-social-media/)） |
| E. 研究文獻（背景與引用） | 生成式 AI 影像偏誤研究 | 學術資料庫 | 已知：University of Washington（EMNLP 2023，Stable Diffusion）、Curtin University（Leaver & Srdarov）、AIAI 計畫（Thydêwá）、[East Asia Forum](https://eastasiaforum.org/2025/04/25/ai-algorithms-and-indigenous-agency-in-taiwan/) |

時間範圍 2021–2026，記錄每張的發布日期；沒有日期的記「擷取日期」。

## 資料夾

```text
10_ai_images/
├── README.md           這份計畫
├── search/             每一輪搜尋的紀錄（平台、關鍵字、數量、候選清單）
├── INDEX.md            收錄影像的索引（事務欄位）
├── author_collection.md 作者已收集影像的清單（作者提供存放位置後整理）
└── screenshots/        頁面截圖（不進 git）
```

## 版權與使用

- **AI 影像的著作權狀態不明確**：多數地區認為沒有人類創作就沒有著作權，但平台條款、上傳者的權利、圖庫的授權條款各不相同，要逐筆記下。
- **圖庫的圖**：要在影片裡用，原則上要買授權，或只以「頁面截圖」的方式作為評論、批評的證據引用。後者是否構成合理使用，要請懂著作權的人確認。
- **社群媒體上個人的貼文**：引用前要考慮上傳者的隱私，以及平台條款。
- 每筆的授權狀況記在 `INDEX.md`，用進作品的再到 `02_rights/` 開紀錄。

## 步驟

1. **作者確認這份計畫**：範圍、平台、收錄條件、要不要對照組。
2. **作者提供已收集的影像**：存放位置、已有的欄位。AI 整理成 `author_collection.md`。
3. **第一輪搜尋（AI）**：A、B、D、E 類先做，C 類只記作者提供的連結。每個平台記：關鍵字、結果數、候選清單、截圖。
4. **作者挑選**：從候選裡挑出影像牆要用的。
5. **10/26 前**：整理 AI 影像的來源資料，交給 readme-video（製作總表 10/26 的工作）。

## 作者的決定（2026-10-23）

- 範圍：**以台灣原住民為主**，也收不分地區的「Indigenous」當對照組。
- 社群媒體上個人上傳者的帳號名稱**寫進 repo**，作為引用來源。
- 作者已收集的影像在 `~/Desktop/AI原住民/`，整理成 [`author_collection.md`](author_collection.md)。
- 截圖存本機、不進 git。
- AI 生成的原住民音樂、討論與評論、非 AI 的文化挪用資料**只當背景資料**，不放進第一章。第一章只用 AI 生成的圖像。
