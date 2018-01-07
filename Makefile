algo.ex:
	touch algo.ex
	echo "#!/bin/bash" >> algo.ex
	echo >> algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple100.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple500.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple1000.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/monexemple.txt" >> algo.ex

stat.ex:
	touch stat.ex
	echo "#!/bin/bash" >> algo.ex
	echo >> algo.ex
	echo python3 source/$(basename $@).py >> stat.ex

clean:
	rm algo.ex
	rm stat.ex
