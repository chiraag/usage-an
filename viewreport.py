#!/usr/bin/env python
""" 
Generate tree view of flattened power report.

Usage:
    viewreport.py <report-file>
    viewreport.py -h

"""

import Tkinter as tk
import ttk
from parsereport import *
import docopt

args = docopt.docopt(__doc__, version='0.1')
rptfile = args['<report-file>']

window = tk.Tk()
window.title(rptfile)
tv = ttk.Treeview(window, columns=('total', ), height=30, padding=2)

def setcolumn(col_id, width, text):
    tv.column(col_id, width=width)
    tv.heading(col_id, text=text)

def insertnode(node, parent_id='', parent_name=''):
    # print node.name
    node_full_name = parent_name + node.name + '/'
    
    node_id = tv.insert(parent_id, 'end', node_full_name, text=node.name, values=node.value)
    
    # print node
    for child in node:
        # print child
        insertnode(node[child], node_id, node_full_name)

setcolumn('#0', width=500, text='Folder')
setcolumn('total', width=100, text='Total Size')

root = tree_from_report(rptfile)
insertnode(root)

tv.tag_configure('ttk')
tv.pack()

window.mainloop()
