#!/bin/bash

this_dir="`dirname $0`"

if [ "$this_dir" = '.' ]
then
    base_dir="`pwd`"
else
    cd "$this_dir"
    base_dir="`pwd`"
fi

curl -o darwin-tol-copyright-boris-kulikov-2007.jpg http://www.boriskulikov.com/images/DarwinTreeOfLife-%20L.jpg
curl -o correlation.mov http://phylo.bio.ku.edu/BIOL428/correl-anim2.mov
curl -o no-correlation.mov http://phylo.bio.ku.edu/BIOL428/no-correl-anim.mov
curl -o canis-lupus.jpg http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg/1024px-Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg
curl -o canis-simensis.jpg http://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Canis_simensis.jpg/1024px-Canis_simensis.jpg
curl -o thylacinus.jpg http://upload.wikimedia.org/wikipedia/commons/4/47/%22Benjamin%22.jpg
curl -o gire-et-al-2014-ebola-fig2.jpg http://www.sciencemag.org/content/345/6202/1369/F2.large.jpg
curl -o gire-et-al-2014-ebola-fig3.jpg http://www.sciencemag.org/content/345/6202/1369/F3.large.jpg
curl -o ichthyosaur-nobu-tamura-cc-by-25.jpg http://upload.wikimedia.org/wikipedia/commons/f/f3/Stenopterygius_BW.jpg
curl -o dolphin-noaa-cc-by-sa-30.jpg http://upload.wikimedia.org/wikipedia/commons/f/f0/Spotteddolphin1.jpg
curl -o xkcd-cartoon.png http://imgs.xkcd.com/comics/the_difference.png
