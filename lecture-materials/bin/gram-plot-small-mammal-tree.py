#! /usr/bin/env python

import os
import sys

from PIL import Image

from Gram import TreeGram
var.punctuation = var.phylip_punctuation

_mammal_trees = [
        "(((Alces.png:2,(Rattus.png:1,Homo-sapiens.png:1):1):1,Loxodonta.png:3):1,(Phascolarctos.png:1,Macropus.png:1):3)1;",
        "((Phascolarctos.png:1,Macropus.png:1):3,(Loxodonta.png:3,(Alces.png:2,(Rattus.png:1,Homo-sapiens.png:1):1):1):1)2;",
        "((Loxodonta.png:3,((Rattus.png:1,Homo-sapiens.png:1):1,Alces.png:2):1):1,(Macropus.png:1,Phascolarctos.png:1):3)3;",
        "((Alces.png:3,((Rattus.png:1,Homo-sapiens.png:1):1,Loxodonta.png:2):1):1,(Phascolarctos.png:1,Macropus.png:1):3)4;",
        ]
_wide_images = ['Rattus.png']

def get_image_path(leaf_name):
    return os.path.join(os.path.pardir, 'images', leaf_name)

def plot_tree(tree, base_name = 'tree', dir_name = 'gram'):
    read(tree)
    t = var.trees[-1]
    for n in t.iterNodes():
        if n.isLeaf:
            try:
                img = Image.open(get_image_path(n.name))
            except IOError as e:
                print n.name
                raise e
            w, h = img.size
            width, height = None, 6.5
            if w > h and (n.name in _wide_images):
                width, height = 12, None
            vmargin = 0
            lmargin = 11
            dimension_name = 'height'
            dimension = height
            if height is None:
                dimension_name = 'width'
                dimension = width
            node_name = n.name
            n.name = r"\hspace{{{0}mm}}\includegraphics[{1}={2}mm,resolution=150]{{{3}}}".format(
                    lmargin,
                    dimension_name,
                    dimension,
                    get_image_path(node_name))
            

    tg = TreeGram(t, yScale=0.8, widthToHeight=0.8)
    tg.tgDefaultLineThickness = 'very thick'
    tg.baseName = base_name
    tg.dirName = dir_name
    tg.epdf()


def main_cli():
    out_dir = os.path.join(os.path.pardir, 'mammal-trees')
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for i, tree in enumerate(_mammal_trees):
        plot_tree(tree,
                base_name = 'mammal-tree-{0}'.format(i + 1),
                dir_name = out_dir)

if __name__ ==  '__main__':
    main_cli()

