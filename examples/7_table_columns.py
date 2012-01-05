#!/usr/bin/env python
# coding: utf-8
# title = Using table columns
#You can get a entire table column just getting the item `column-name` in table
#object. You can also delete an entire column (but you can't actually change an
#entire column).

from outputty import Table
table = Table(headers=['spam', 'eggs', 'ham'])
table.append(['python', 3.14, 1 + 5j])
table.append(['rules', 42, 3 + 4j])
del table['eggs']
print 'Table after deleting "eggs" column:'
print table
print '\nNow only column "spam":'
print table['spam']
