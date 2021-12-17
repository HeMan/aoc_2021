if [ "$part" == "part1" ]; then
	/usr/bin/micropython -X heapsize=112396 /src/part1.py
else
	/usr/bin/micropython -X heapsize=112396 /src/part2.py
fi
