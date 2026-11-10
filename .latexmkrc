# LuaLaTeX for Japanese paper sources; outputs only to ignored build/.
$pdf_mode = 4;
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 5;
