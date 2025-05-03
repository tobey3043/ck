all: clean_data plot_data

clean_data:
	python src/clean_data.py data/data.csv data/clean_data.csv

plot_data:
	python src/plot_data.py data/clean_data.csv data/plot.png