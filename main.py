from chart_builder import *
from source import *
from params import *


def task1():
    country_map = load_map()
    agg_data = load_data()
    background = build_background(country_map)
    chart = build_map(world=country_map,
                      data=agg_data[agg_data['year'] == 2019],
                      lookup_field='rate',
                      scale=alt.Scale(scheme='orangered', reverse=True))

    return background + chart + build_description()


def task2():
    agg_data = load_data()
    chart = build_lines(agg_data)

    return chart


if __name__ == '__main__':
    alt.data_transformers.disable_max_rows()
    add_title(chart=task1() & task2(),
              title='Рівень приросту/скорочення за регіонами').show()
