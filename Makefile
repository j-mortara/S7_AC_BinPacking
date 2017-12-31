algo.ex:
	python3 source/$(basename $@).py "exemples/exemple100.txt" 
	python3 source/$(basename $@).py "exemples/exemple500.txt" 
	python3 source/$(basename $@).py "exemples/exemple1000.txt" 
	python3 source/$(basename $@).py "exemples/monexemple.txt" 

stat.ex:
	python3 source/$(basename $@).py