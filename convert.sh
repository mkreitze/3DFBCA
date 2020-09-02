for file in *.obj;
	do meshlabserver -i $file -o $file -om vc fc vn
done
