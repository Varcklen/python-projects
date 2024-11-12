# Task 3
# Напишіть скрипт для очищення тексту від HTML-тегів.
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">

text = "<div id=\"rcnt\" style=\"clear:both;position:relative;zoom:1\">My text! <div>Something!</div>"

import re
 
print( re.sub(r'\<[^>]*\>', '', text) )