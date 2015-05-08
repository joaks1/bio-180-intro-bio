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
curl -o us-worker-task-plot.png http://dangerouslyirrelevant.org/wp-content/uploads/2014/09/2013AutorPrice2.png

curl -o Homo-sapiens.png http://phylopic.org/assets/images/submissions/b042f8d5-d2c3-4659-8b2a-60b26d096f0c.256.png
curl -o Rattus.png http://phylopic.org/assets/images/submissions/828a8d15-6aa9-41ab-85a3-e9e06c0f1945.256.png
curl -o Alces.png http://phylopic.org/assets/images/submissions/1a20a65d-1342-4833-a9dd-1611b9fb383c.256.png
curl -o Loxodonta.png http://phylopic.org/assets/images/submissions/62398ac0-f0c3-48f8-8455-53512a05fbc4.256.png
curl -o Phascolarctos.png http://phylopic.org/assets/images/submissions/8a06d489-024f-4505-8ccb-f86e84e00e75.256.png
curl -o Macropus.png http://phylopic.org/assets/images/submissions/c306572a-fae1-41e3-8208-c2bce972e0ef.256.png
curl -o hillis-tree.pdf http://www.zo.utexas.edu/faculty/antisense/tree.pdf

wget -O honeycreeper-biogeography.jpg http://bioteaching.files.wordpress.com/2010/01/hawaii.jpg
wget -O honeycreepers.jpg http://www.hdouglaspratt.com/Art_Gallery/HawaiianHoneycreepers/hawaiian_honeycreepers_evolution_radiation.jpg
wget -O honeycreepers-labeled.jpg http://www.hoikecurriculum.org/wp-content/uploads/2012/07/AdRad-labels_eml-permission-Douglas-Pratt-and-Yale-U-Press.jpg
wget -O red-deer.jpg http://upload.wikimedia.org/wikipedia/commons/d/df/Red_deer.jpg
