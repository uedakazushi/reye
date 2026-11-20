# Reye 原論文 TeX 化 TODO（2026-11-10）

**原本：** `papers/pdf-only/reye_stationary.pdf`（77ページ）。旧 `nc-cubic`（現 `poisson-cubic`） 原本の Git blob SHA: `ce5918ae30017f0df735efb2b6ee2b9ff1010399`。未復元の論証を含むため、PDFは一時的に追跡する。

- [x] Reye専用の TeX ４本・検証コード５本と原本PDFをこの専用リポジトリへ移す。
- [x] GitHub `main` を正本とし、`.latexmkrc` でLuaLaTeX組版、生成PDFを原則 ignore する。
- [ ] 原論文第２〜４・６〜７・13節と各回復 TeX の定理・証明を逐条照合する。
- [ ] 第５・９・10節の法束、Artin比較、曲線網羅と仮想数に使う全追加仮定を原 PDF と照合し、未収録補題を保全する。
- [ ] 第11節：長さ２曲線の `F_2` 法束と局所 PT 仮想寄与、被約・非被約構造を完全 TeX 化する。
- [ ] 第12節：長さ３ cusp jet を大域 ordered 模型の全階数層・versal性・法束・PT へ接続する。
- [ ] 第13節：二点付き incidence の特殊階数層の完全な独立計算・fold例の存在・単一分岐を検証する。
- [ ] 定理・補題・系・注意の対応一覧（原 PDF 節・頁 → `papers/source_recovery/` の証明）を作成する。
- [ ] 最新の TeX 全４本を `latexmk` で再組版し、全５本の SymPy 検証を実行する。再生成PDFはGit追跡しない。
- [ ] 先行研究の原資料、式・仮定・変形関手の適用範囲、数学的新規性を最終監査する。
- [ ] 原本の全数学的内容を TeX で復元・検証した後、原 PDF の Git 追跡を外し `.gitignore` の例外を除く。

PDFに比べて要約版のTeXだけが存在する段階では**追跡解除しない**。
