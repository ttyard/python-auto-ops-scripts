#!/usr/bin/env python

import difflib

text1 ="""text1:
        This is a Test Text1.
        This module provides classed...
       """
text1_lines=text1.splitlines()

text2 ="""text2:
        This IS a Test Text1.
        This module provides classed and functions for Comparing sequences.
       """
text2_lines=text2.splitlines()

d=difflib.Differ()
diff = d.compare(text1_lines,text2_lines)
print '\n'.join(list(diff))