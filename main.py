from chart_builder import *
from source import *
from params import *


def task1(selection):
    country_map = load_map()
    agg_data = load_data()
    background = build_background(country_map)
    chart = build_map(country_map, agg_data[agg_data['year'] == 2019], selection)

    return background + chart + build_description()


def task2(selection):
    agg_data = load_data()
    chart = build_lines(agg_data[agg_data['year'] >= 2000], selection)

    return chart


if __name__ == '__main__':
    alt.data_transformers.disable_max_rows()
    hover_selection = get_selection()
    add_title(chart=task1(hover_selection) & task2(hover_selection),
              title='Рівень приросту/скорочення за регіонами').show()
