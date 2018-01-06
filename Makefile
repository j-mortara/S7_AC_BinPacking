algo.ex:
	touch algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple100.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple500.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/exemple1000.txt" >> algo.ex
	echo python3 source/$(basename $@).py "exemples/monexemple.txt" >> algo.ex

stat.ex:
	touch stat.ex
	echo python3 source/$(basename $@).py >> stat.ex