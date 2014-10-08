prepare data:
remove headings from file.


row 1836738
"3091673",3,"KHAYELITSHA","KHSB043307",3028-02-05,"RNA",124,"","LDL",400,"88",88

date is "3028-02-05"

removed date, as there is no obvious edit to correct it.




run re.py within local dir
"$python re.py"



%s/\"\([0-9]*\) days, 00:00:00\"/\1/g
2171286 substitutions on 2171286 lines.

%s/00:00:00$//g
686223 substitutions on 686223 lines


