# 3DFBCA
This records my work generating 3D FBCA (Fashion Based Cellular Automata, first explored in https://ieeexplore.ieee.org/document/7317958).
The file 2state3DFBCA.py generates wavefront (.obj) files for every update of an FBCA with user defined length, width, height, score matrix (S), number of updates (g) and random seed (L_0). This is the most basic version only allowing for two states. The user defined variables can be inputted on lines 9-17 utilizing any text editor.

The file objRender.py generates a wavefront (.obj) of stacked length, width and height (.obj) file.

Personally I run this file on the most recent version of Ubuntu using python3. 
To generate the animated images shown for the 5x5x5, 10x10x10 the .obj files were strung together using stop motion obj, a blender add on available at https://github.com/neverhood311/Stop-motion-OBJ .
