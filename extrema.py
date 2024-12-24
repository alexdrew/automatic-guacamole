# %%
from scipy.signal import argrelextrema
import numpy as np
import plotly.graph_objects as go
import pandas as pd


def get_extrema(df: pd.DataFrame, order: int = 5):
    extrema_highs = argrelextrema(df.high.values, comparator=np.greater, order=order)
    extrema_lows = argrelextrema(df.low.values, comparator=np.less, order=order)
    
    return extrema_highs, extrema_lows


def extrema_fig(df: pd.DataFrame, order: int = 5):
    extrema_highs, extrema_lows = get_extrema(df, order)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index[extrema_highs],
        y=df.high.values[extrema_highs] + 10,
        mode='markers',
        marker=dict(color='red', symbol='triangle-down', size=10),
        name='Extreme Highs'
    ))
    # fig.add_trace(go.Scatter(
    #     x=df.index,
    #     y=df.high,
    #     mode='lines',
    #     name='High',
    #     line=dict(color='blue'),
    # ))
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df.close,
        mode='lines',
        name='Close',
        line=dict(color='blue'),
    ))
    # fig.add_trace(go.Scatter(
    #     x=df.index,
    #     y=df.low,
    #     mode='lines',
    #     name='Low',
    #     line=dict(color='blue')
    # ))
    fig.add_trace(go.Scatter(
        x=df.index[extrema_lows],
        y=df.low.values[extrema_lows] - 10,
        mode='markers',
        marker=dict(color='green', symbol='triangle-up', size=10),
        name='Extreme Lows'
    ))

    fig.update_layout(
        title='Extrema',
        xaxis_title='Time',
        yaxis_title='Price',
        showlegend=True,
        yaxis=dict(tickformat=',')
    )

    return fig


if __name__ == '__main__':
    from analytics2.base_classes.ui.ts_chart.candlestick import dev_seed

    chart = dev_seed()
    df = chart.ohlc.get_ts_data(chart.ohlc.ts.FIVE_SECONDS)
    fig = extrema_fig(df, 12)

    fig.show()

# %%
