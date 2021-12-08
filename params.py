def add_title(chart, title):
    return chart.properties(
        title=title,
    ).configure_title(
        fontSize=24,
        font='Courier',
        anchor='start',
        dy=-30
    )


def decorate_map(chart):
    return chart.properties(background='#F9F9F9')


def add_title(chart, title):
    return chart.properties(
        title=title,
    ).configure_title(
        fontSize=24,
        font='Courier',
        anchor='middle',
        dy=-30
    )
