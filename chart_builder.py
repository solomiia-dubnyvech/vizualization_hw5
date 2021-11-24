import altair as alt
import pandas as pd


def build_background(country):
    return alt.Chart(country, height=300, width=600).project().mark_geoshape(fill='lightgray', stroke='white')


def build_map(world, data, lookup_field, scale, field_type='Q'):
    return alt.Chart(world, height=300, width=600).project().mark_geoshape(stroke='white').encode(
        color=alt.Color(f'{lookup_field}:{field_type}', scale=scale),
        tooltip=[alt.Tooltip('region:N'), alt.Tooltip(f'{lookup_field}:{field_type}')],
    ).transform_lookup(
        lookup='region',
        from_=alt.LookupData(data=data, key='region', fields=['region', lookup_field]),
    )


def build_lines(data):
    selection = alt.selection_multi(fields=['region'], bind='legend')
    return alt.Chart(data, height=300, width=600).mark_line().encode(
        x=alt.X('year:O'),
        y=alt.Y('rate:Q'),
        color=alt.Color('region:N', scale=alt.Scale(scheme='category20')),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.1))
    ).add_selection(selection)


def build_description():
    return alt.Chart(pd.DataFrame({'x': [1]})).mark_text(
        text='2019 рік',
        dy=140,
        dx=270,
        color='gray',
    )
