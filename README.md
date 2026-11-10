# Reye 曲線・停留平面の研究

**正本：このリポジトリの `main`。** 2026-11-10 時点の成果と再開方針は `00_research_plan.md` を先に読む。

本研究は滑らかな cubic threefold に付随する停留平面の275個の計数、Hessian pencil、Reye 三様体、Hilbert/PT 曲線、double quintic symmetroid 上の550本の曲線、モノドロミー、長さ2・3の特殊化を扱う。

- `papers/source_recovery/`：原論文の各節を TeX へ復元した独立原稿。各稿は独立に組版可能な形式で、結果の一部は原論文の別節に依存する。
- `computations/`：整数・有理数計算等の証明補助コード。
- `papers/pdf-only/reye_stationary.pdf`：**未移植の証明を含む77ページの原論文 PDF**。TeXの全証明と照合し再生成可能になるまで追跡し、その後は `git rm --cached` により追跡を外す。
- `TODO_PDF_SOURCES.md`：現在の到達点・未復元の証明・照合チェックリスト。

原則として Git では TeX とコードを追跡し、生成した PDF・latexmk 中間物は追跡しない。原本PDFのみ一時的例外。

GitHub Actions は利用せず、LuaLaTeX と `latexmk` を手元で実行する。結果の存在・証明の記載・今回の再検証・組版実行を区別する。
