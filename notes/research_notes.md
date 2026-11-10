# 研究ノート：現在有効な知識と障害（2026-11-10 / v1）

## 研究対象と記法

滑らかな cubic threefold `F=0` の停留平面の零スキーム `Z_F`、その Hessian の定階数４ pencil、gradient 系からの Reye 三様体、および double quintic symmetroid の次数１曲線を研究する。原論文は `papers/pdf-only/reye_stationary.pdf`（77ページ）。原論文全体は現行 TeX へ完全には移植されていない。

## 現行原稿の証明配置

- `reye_stationary_core.tex`：275停留平面のChern類・Porteous計数、定階数 Hessian pencil、長さ２の局所点、gradient系と一般 Reye 三様体。第６・７節のHilbert/PT275と550曲線の二成分にも言及。
- `reye_deformations_degree_one.tex`：法束の完全列、HilbertとHessian直線の全局所 Artin 比較、階数４ pencilの平方判別式による550本の曲線網羅と仮想計数。一般275点とregularityに依存。
- `reye_full_monodromy.tex`：二点付き incidenceの５相対位置と階数表、fold conormal、単一 transpositionと `S_{275}`、550本側の対角作用。一般階数の有理数上の例は計算で確認したが、全特殊階数層の完全な計算機検証は未了。
- `reye_length_three_cusp_jet.tex`：長さ３の局所 cusp `T^3+uT+v`、四次係数とJacobian。全 ordered 模型の大域 regularity は別入力。

## 正確性・再現

有限計算の実行方法は README と `computations/`。証明の記載を、今回の独立検証や計算機形式証明と取り違えない。全 Artin 比較、monodromy、550曲線網羅の理論的部分について完全な外部監査を行ったわけではない。証明に必要な他節の仮定を明示し、相対 smoothness を自動的には結論しない。

## 現在の主要な未解決・監査項目

- 第11節の長さ２の曲線の法束・Atiyah `F_2`、PT 局所仮想寄与。
- 第12節の長さ３を実現する普遍 ordered 模型の全階数層と射影的な実効性。
- 第13節の特殊階数層の完全検算、および外部原稿から受け取るfold例の独立証明。
- 原論文77ページの各定理の仮定・結論・証明と現行TeXの対応表。対応が終わるまで原 PDF を維持する。
- 主要な先行研究として Hosono–Takagi の Reye congruence、Harris–Roth–Starr の小次数曲線、Skjelnes–Smith の Hilbert scheme 結果を原稿の引用箇所で確認する。各定理の原資料の仮定を確定させる必要がある。
