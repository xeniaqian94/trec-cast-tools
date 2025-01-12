# Tools and scripts for TREC CAsT Y3

Code to create trecweb files from the MARCO, KILT, and WaPo collections can be found in the `src/main/python` directory. During the trecweb creation process, each document in a collection is chunked into smaller passages. 

Each document has an ID, url, title, and body. You can refer to http://www.treccast.ai/ to learn more about the Document ID format used for CAsT. Passage ID is based on the position (zero-indexed) of a passage within a document. 

Below is an example of the trecweb format that will be generated for MARCO after running the `marco_trecweb.py` code:

```
<DOC>
<DOCNO>MARCO_D3178380</DOCNO>
<DOCHDR>
</DOCHDR>
<HTML>
<TITLE>What is a Crystal?</TITLE>
<URL>https://www.gemsociety.org/article/crystal/</URL>
<BODY>
<passage id=0>
What is a Crystal?by International Gem Society“Crystal 1” by Brenda Clarke. Licensed under CC By 2.0. What comes to mind when you think of crystals? Many people might visualize beautiful, mineral objects with smooth faces in regular geometric patterns. Others might imagine elegant glassware. For gemologists, the scientific definition of a crystal goes right to the atomic level. A crystal is a solid whose atoms are arranged in a “highly ordered” repeating pattern. These patterns are called crystal systems. If a mineral has its atoms arranged in one of them, then that mineral is a crystal. Crystal Systems There are seven crystal systems: isometric, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal, and trigonal. Each is distinguished by the geometric parameters of its unit cell, the arrangement of atoms repeated throughout the solid to form the crystal object we can see and feel. For example, an isometric or cubic crystal has a cube as its unit cell. 
</passage>
<passage id=1>
All its sides are equal in length and all its angles are right angles. Well-known gems in this system include diamonds, garnets, and spinels. The isometric crystal system has three axes of the same length that intersect at 90º angles. On the other hand, a triclinic crystal has all sides of different lengths and none of its angles are right angles. These geometric variations mean triclinic crystals can take on many intricate shapes. Well-known gems in the triclinic system include labradorite and turquoise. None of the axes in the triclinic system intersect at 90º and all are different lengths. Non-Crystalline Solids Some objects may appear to be crystals to the naked eye, but outward appearances can be misleading. For gemologists, the atomic structure of the object is the determining factor. Not all objects with regular geometric faces are crystals, not are all solid materials crystals. Amorphous Solids Glass, for example, has a non-crystalline, amorphous atomic structure. 
</passage>
<passage id=2>
Although glassmakers can pour and harden glass into geometric shapes, its atomic structure remains unchanged. People commonly refer to some glassware, such as this, as crystal. However, scientifically speaking, these objects aren’t crystals. Photo by liz west. Licensed under CC By 2.0. Polycrystalline Solids Water that hardens into a single large snowflake is, in fact, a crystal. It crystallizes as it cools, freezes, and moves through the atmosphere. “Snowflake-23” by Yellowcloud. Licensed under CC By 2.0. However, water that hardens into a cube in your freezer’s ice tray isn’t a crystal. Ice cubes, rocks, and common metals are examples of polycrystalline materials. They may contain many crystalline objects. (In the case of ice cubes, they may contain actual ice crystals). Nevertheless, you can’t describe the entire ice cube as having a uniform crystalline structure. 
</passage>
<passage id=3>
“Frozen Ice Cubes IMG_1021” by Steven Depolo. Licensed under CC By 2.0. Cryptocrystalline or microcrystalline rocks consist of microscopic crystals, but, again, those rocks lack a uniform crystalline structure. Some cryptocrystalline materials, such as chalcedony, find use as gem materials in jewelry or decorative objects. The Origins of Crystals Most crystals have natural origins. They can form through inorganic means, such as geological processes within the earth. Others form through organic processes within living creatures. For example, some human kidney stones consist in part of weddellite crystals. Weddellite occurs at the bottom of the Weddell Sea near Antarctica. It can also be found passing very painfully through urinary tracts. “Surface of a Kidney Stone” by Kempf EK. Licensed under CC By-SA 3.0. Laboratories can also create crystals artificially. For example, cubic zirconia, a synthetic gem material, forms with a cubic crystal structure when zirconium and zirconium dioxide are superheated. 
</passage>
<passage id=4>
The resulting material commonly finds use as a diamond imitation or simulant. Colorless cubic zirconia gems often serve as diamond imitations. However, labs can also synthesize this material in many colors. “Multicolor Cubic Zirconia” by Michelle Jo. Licensed under CC By 3.0.
</passage>
</BODY>
</HTML>
</DOC>
```

## How to use

1. `cd` into `src/main/python`
1. Create and Activate a Python Virtual Environment using `python3 -m venv env` then `source env/bin/activate` 
(for my case, `cd /fs/clip-quiz/xinq/trec-cast-tools/src/main/python/` then `source trec-cast-tool/bin/activate` then `conda deactivate` (base))
2. Install the dependencies using `pip install -r requirements.txt`

### Creating the Trecweb scripts:

Ensure you have a copy of the Marco document, KILT, and WaPo collections and any relevant duplicate files (duplicates file for Marco and WaPo can be found in [this folder](https://github.com/daltonj/treccastweb/tree/master/2021/duplicate_files)). 

    cd /fs/clip-scratch/xinq/treccast/duplicates/
    wget https://raw.githubusercontent.com/daltonj/treccastweb/master/2021/duplicate_files/marco_duplicates.txt 
    wget https://raw.githubusercontent.com/daltonj/treccastweb/master/2021/duplicate_files/wapo-near-duplicates


Then:

create three json repo:
    /fs/clip-scratch/xinq/treccast/data_jsonl/ (passage data)
    /fs/clip-scratch/xinq/treccast/doc_data_jsonl_sanitized/ (doc data)
    /fs/clip-scratch/xinq/treccast/doc_dense_jsonl/ (passage/doc dense retrieval)

To generate the **trecweb file for the Marco document collection**, run (takes about 4 hours):

`python marco_trecweb.py path-to-msmarco-docs.tsv path-to-dump-directory path-to-duplicates-file`
(passage jsonl)`python marco_trecweb.py /fs/clip-scratch/xinq/treccast/data/msmarco-docs.tsv /fs/clip-scratch/xinq/treccast/data_jsonl/msmarco /fs/clip-scratch/xinq/treccast/duplicates/marco_duplicates.txt`
(code status in `trecweb_utils.py`, will get doc Dense jsonl) `python marco_trecweb.py /fs/clip-scratch/xinq/treccast/data/msmarco-docs.tsv /fs/clip-scratch/xinq/treccast/doc_dense_jsonl/ /fs/clip-scratch/xinq/treccast/duplicates/marco_duplicates.txt` screen 25654.pts-32.clipsub00
(doc jsonl) `python marco_trecweb.py /fs/clip-scratch/xinq/treccast/data/msmarco-docs.tsv /fs/clip-scratch/xinq/treccast/doc_data_jsonl/ /fs/clip-scratch/xinq/treccast/duplicates/marco_duplicates.txt no_passage`



To generate the **trecweb file for KILT**, run (takes about 3.5 hours):

`python kilt_trecweb.py path-to-kilt_knowledgesource.json path-to-dump-directory`
(passage jsonl) `python kilt_trecweb.py /fs/clip-scratch/xinq/treccast/data/kilt_knowledgesource.json /fs/clip-scratch/xinq/treccast/data_jsonl/kilt`
(doc Dense jsonl) `python kilt_trecweb.py /fs/clip-scratch/xinq/treccast/data/kilt_knowledgesource.json /fs/clip-scratch/xinq/treccast/doc_dense_jsonl/` screen 26074.pts-32.clipsub00
(doc jsonl) `python kilt_trecweb.py /fs/clip-scratch/xinq/treccast/data/kilt_knowledgesource.json /fs/clip-scratch/xinq/treccast/doc_data_jsonl/ no_passage`

To generate the **trecweb file for WaPo**, run (takes about 1 hour):

`python wapo_trecweb.py path-to-TREC_Washington_Post_collection.v4.jl path-to-dump-directory path-to-wapo-near-duplicates`
(passage jsonl) `python wapo_trecweb.py /fs/clip-scratch/xinq/treccast/data/WashingtonPost.v4/data/TREC_Washington_Post_collection.v4.jl  /fs/clip-scratch/xinq/treccast/data_jsonl/wapo  /fs/clip-scratch/xinq/treccast/duplicates/wapo-near-duplicates`
(doc dense jsonl) `python wapo_trecweb.py /fs/clip-scratch/xinq/treccast/data/WashingtonPost.v4/data/TREC_Washington_Post_collection.v4.jl  /fs/clip-scratch/xinq/treccast/doc_dense_jsonl/  /fs/clip-scratch/xinq/treccast/duplicates/wapo-near-duplicates` screen 26290.pts-32.clipsub00
(doc jsonl) `python wapo_trecweb.py /fs/clip-scratch/xinq/treccast/data/WashingtonPost.v4/data/TREC_Washington_Post_collection.v4.jl  /fs/clip-scratch/xinq/treccast/doc_data_jsonl/ /fs/clip-scratch/xinq/treccast/duplicates/wapo-near-duplicates no_passage` => need to re-run bc html tag 
(doc jsonl) `python wapo_trecweb.py /fs/clip-scratch/xinq/treccast/data/WashingtonPost.v4/data/TREC_Washington_Post_collection.v4.jl  /fs/clip-scratch/xinq/treccast/doc_data_jsonl_sanitized/ /fs/clip-scratch/xinq/treccast/duplicates/wapo-near-duplicates no_passage` 

Generating document files from original scripts, for indexing 

   then run 
    /fs/clip-quiz/xinq/chatty-goose/experiments/create_index.sh
    /fs/clip-quiz/xinq/chatty-goose/experiments/create_index_doc.sh
    /fs/clip-quiz/xinq/chatty-goose/experiments/create_index_doc_sanitized.sh
    (dense retrieval don't have this step) 
     

python

## Other Notes

1. The updated proto definitions for the topics can be found in `src/main/proto`
2. The trecweb scripts have been tested with Python 3.8.