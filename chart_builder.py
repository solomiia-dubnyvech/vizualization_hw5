import altair as alt
import pandas as pd


def get_selection():
    return alt.selection_single(fields=['region'], on='mouseover', empty='all')


def build_background(country):
    return alt.Chart(country, height=300, width=600).project().mark_geoshape(fill='lightgray', stroke='white')


def build_map(world, data, selection):
    return alt.Chart(world, height=300, width=600).project().mark_geoshape(stroke='white').encode(
        color=alt.Color('rate:Q', scale=alt.Scale(scheme='orangered', reverse=True)),
        tooltip=[alt.Tooltip('region:N'), alt.Tooltip('rate:Q')],
        opacity=alt.condition(selection, alt.value(1), alt.value(0.1))
    ).transform_lookup(
        lookup='region',
        from_=alt.LookupData(data=data, key='region', fields=['region', 'rate']),
    ).add_selection(selection)


def build_lines(data, selection):
    return alt.Chart(data, height=300, width=600).mark_line().encode(
        x=alt.X('year:O'),
        y=alt.Y('rate:Q'),
        color=alt.condition(selection, 'region:N', alt.value('gray')),
        size=alt.condition(selection, alt.value(2), alt.value(0.2)),
    ).add_selection(selection)


def build_description():
    return alt.Chart(pd.DataFrame({'x': [1]})).mark_text(
        text='2019 рік',
        dy=140,
        dx=270,
        color='gray',
    )
