# 3DFBCA
This records my work generating 3D FBCA (Fashion Based Cellular Automata, first explored in https://ieeexplore.ieee.org/document/7317958).

The file 2state3DFBCA.py generates wavefront (.obj) files for every update of an FBCA with user defined length, width, height, score matrix (S), number of updates (g) and random seed (L_0). This is the most basic version only allowing for two states. The user defined variables can be inputted on lines 9-17 utilizing any text editor.

The file nstateFBCA.py generates wavefronts with up to 12 uniquely coloured states with the same user defined parameters as in the two state case. 

To render this in an easily, an add on to blender known as Stop Motion Obj is used (https://github.com/neverhood311/Stop-motion-OBJ/blob/master/imgs/cached_import_s2g_octree.gif). To allow blender to access the files, each must remade. This is done using Meshlab (https://www.meshlab.net/) by placing all generated files into a folder and running convert.sh. 


The file objRender.py generates a wavefront (.obj) of stacked length, width and height (.obj) file.

Incase it matters, I utilize an Ubuntu VM for all my code.
