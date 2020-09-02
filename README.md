# 3DFBCA
This records my work generating 3D FBCA (Fashion Based Cellular Automata, first explored in https://ieeexplore.ieee.org/document/7317958).

The file 2state3DFBCA.py generates wavefront (.obj) files for every update of an FBCA with user defined length, width, height, score matrix (S), number of updates (g) and random seed (L_0). This is the most basic version only allowing for two states. The user defined variables can be inputted on lines 9-17 utilizing any text editor.

The file nstateFBCA.py generates wavefronts with up to 12 uniquely coloured states with the same user defined parameters as in the two state case. 

The file objRender.py generates a wavefront (.obj) of stacked cubes for a length, width and height (.obj) file.

The file multiColourRender.py generates a wavefront (.obj) of stacked cubes for a length, width and height (.obj) file with random states. 

To render this easily, an add on to blender known as Stop Motion Obj is used (https://github.com/neverhood311/Stop-motion-OBJ/blob/master/imgs/cached_import_s2g_octree.gif). To allow blender to access the files, each must remade. This is done using Meshlab (https://www.meshlab.net/) by placing all generated files into a folder and running convert.sh. Some results are below.

![2 State 10x10x10](https://github.com/mkreitze/3DFBCA/blob/master/10x10x10%202state.gif)
![2 State 20x20x20](https://github.com/mkreitze/3DFBCA/blob/master/20x20x20%202state.gif)
![1212 State 10x10x10](https://github.com/mkreitze/3DFBCA/blob/master/10x10x10%201212gif.gif)
![2121 State 10x10x10](https://github.com/mkreitze/3DFBCA/blob/master/10x10x10%202121gif.gif)
![1212 State 20x20x20](https://github.com/mkreitze/3DFBCA/blob/master/20x20x20%201212gif.gif)
![2121 State 20x20x20](https://github.com/mkreitze/3DFBCA/blob/master/20x20x20%202121gif.gif)

The provided gifs use the score matrices: 
[0.1,1.2,2.0,0] for the two state (grey and empty) FBCA
[[0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596] (known as 1212),[0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774,0.390741,0.728013,0.614486,0.378596,0.320205,0.952292,0.351335,0.837774]] (known as 2121) for the four state (green, red, blue, empty) FBCA. 


Incase it matters, I utilize an Ubuntu VM for all my code.
