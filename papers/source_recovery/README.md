# Reye 論文の自立した部分復元 TeX

元の77ページ原論文 PDF：`../pdf-only/reye_stationary.pdf`。各原稿は**完全置換ではなく独立した部分復元**であり、相互に原論文の別節を仮定として引用する箇所がある。

| 原稿 | 範囲 | 未監査事項 |
|---|---|---|
| `reye_stationary_core.tex` | 275停留平面・Hessian pencil・gradient Reye・Hilbert/PT275の基本 | 全原論文との対応、依存の一部 |
| `reye_deformations_degree_one.tex` | 法束と全Artin比較、550次数1曲線、仮想計数 | 一般275点の存在とregularityへの依存 |
| `reye_full_monodromy.tex` | 二点付き incidence・fold・`S_{275}`・対角作用 | 特殊階数層の独立全検算 |
| `reye_length_three_cusp_jet.tex` | 長さ３ cusp の有限jet | ordered模型とPTの大域化 |

元原稿の全証明の照合が終わるまでは原本 PDF を保持する。計算は `computations/source_recovery/`。詳しくは `TODO_PDF_SOURCES.md`。
