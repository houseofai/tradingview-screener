
# ----------------------
# Generated file
# 2023-08-07 13:27:15.119071
# ----------------------
from tvscreener.field import Field


class CryptoField(Field):
    ALL_TIME_HIGH = 'All Time High', 'High.All', 'round', False, False
    ALL_TIME_LOW = 'All Time Low', 'Low.All', 'round', False, False
    ALL_TIME_PERFORMANCE = 'All Time Performance', 'Perf.All', 'percent', False, False
    AROON_DOWN_14 = 'Aroon Down (14)', 'Aroon.Down', 'round', True, False
    AROON_UP_14 = 'Aroon Up (14)', 'Aroon.Up', 'round', True, False
    ASK = 'Ask', 'ask', 'float', False, False
    AVAILABLE_COINS = 'Available Coins', 'total_shares_outstanding', 'missing', False, False
    AVERAGE_DAY_RANGE_14 = 'Average Day Range (14)', 'ADR', 'float', True, False
    AVERAGE_DIRECTIONAL_INDEX_14 = 'Average Directional Index (14)', 'ADX', 'computed_recommendation', True, False
    AVERAGE_TRUE_RANGE_14 = 'Average True Range (14)', 'ATR', 'float', True, False
    AVERAGE_VOLUME_10_DAY = 'Average Volume (10 day)', 'average_volume_10d_calc', 'number_group', False, False
    AVERAGE_VOLUME_30_DAY = 'Average Volume (30 day)', 'average_volume_30d_calc', 'number_group', False, False
    AVERAGE_VOLUME_60_DAY = 'Average Volume (60 day)', 'average_volume_60d_calc', 'number_group', False, False
    AVERAGE_VOLUME_90_DAY = 'Average Volume (90 day)', 'average_volume_90d_calc', 'number_group', False, False
    AWESOME_OSCILLATOR = 'Awesome Oscillator', 'AO', 'computed_recommendation', True, True
    BID = 'Bid', 'bid', 'float', False, False
    BOLLINGER_LOWER_BAND_20 = 'Bollinger Lower Band (20)', 'BB.lower', 'computed_recommendation', True, False
    BOLLINGER_UPPER_BAND_20 = 'Bollinger Upper Band (20)', 'BB.upper', 'computed_recommendation', True, False
    BULL_BEAR_POWER = 'Bull Bear Power', 'BBPower', 'recommendation', True, False
    CANDLE_3BLACKCROWS = 'Candle.3BlackCrows', 'Candle.3BlackCrows', 'bool', True, False
    CANDLE_3WHITESOLDIERS = 'Candle.3WhiteSoldiers', 'Candle.3WhiteSoldiers', 'bool', True, False
    CANDLE_ABANDONEDBABY_BEARISH = 'Candle.AbandonedBaby.Bearish', 'Candle.AbandonedBaby.Bearish', 'bool', True, False
    CANDLE_ABANDONEDBABY_BULLISH = 'Candle.AbandonedBaby.Bullish', 'Candle.AbandonedBaby.Bullish', 'bool', True, False
    CANDLE_DOJI = 'Candle.Doji', 'Candle.Doji', 'bool', True, False
    CANDLE_DOJI_DRAGONFLY = 'Candle.Doji.Dragonfly', 'Candle.Doji.Dragonfly', 'bool', True, False
    CANDLE_DOJI_GRAVESTONE = 'Candle.Doji.Gravestone', 'Candle.Doji.Gravestone', 'bool', True, False
    CANDLE_ENGULFING_BEARISH = 'Candle.Engulfing.Bearish', 'Candle.Engulfing.Bearish', 'bool', True, False
    CANDLE_ENGULFING_BULLISH = 'Candle.Engulfing.Bullish', 'Candle.Engulfing.Bullish', 'bool', True, False
    CANDLE_EVENINGSTAR = 'Candle.EveningStar', 'Candle.EveningStar', 'bool', True, False
    CANDLE_HAMMER = 'Candle.Hammer', 'Candle.Hammer', 'bool', True, False
    CANDLE_HANGINGMAN = 'Candle.HangingMan', 'Candle.HangingMan', 'bool', True, False
    CANDLE_HARAMI_BEARISH = 'Candle.Harami.Bearish', 'Candle.Harami.Bearish', 'bool', True, False
    CANDLE_HARAMI_BULLISH = 'Candle.Harami.Bullish', 'Candle.Harami.Bullish', 'bool', True, False
    CANDLE_INVERTEDHAMMER = 'Candle.InvertedHammer', 'Candle.InvertedHammer', 'bool', True, False
    CANDLE_KICKING_BEARISH = 'Candle.Kicking.Bearish', 'Candle.Kicking.Bearish', 'bool', True, False
    CANDLE_KICKING_BULLISH = 'Candle.Kicking.Bullish', 'Candle.Kicking.Bullish', 'bool', True, False
    CANDLE_LONGSHADOW_LOWER = 'Candle.LongShadow.Lower', 'Candle.LongShadow.Lower', 'bool', True, False
    CANDLE_LONGSHADOW_UPPER = 'Candle.LongShadow.Upper', 'Candle.LongShadow.Upper', 'bool', True, False
    CANDLE_MARUBOZU_BLACK = 'Candle.Marubozu.Black', 'Candle.Marubozu.Black', 'bool', True, False
    CANDLE_MARUBOZU_WHITE = 'Candle.Marubozu.White', 'Candle.Marubozu.White', 'bool', True, False
    CANDLE_MORNINGSTAR = 'Candle.MorningStar', 'Candle.MorningStar', 'bool', True, False
    CANDLE_SHOOTINGSTAR = 'Candle.ShootingStar', 'Candle.ShootingStar', 'bool', True, False
    CANDLE_SPINNINGTOP_BLACK = 'Candle.SpinningTop.Black', 'Candle.SpinningTop.Black', 'bool', True, False
    CANDLE_SPINNINGTOP_WHITE = 'Candle.SpinningTop.White', 'Candle.SpinningTop.White', 'bool', True, False
    CANDLE_TRISTAR_BEARISH = 'Candle.TriStar.Bearish', 'Candle.TriStar.Bearish', 'bool', True, False
    CANDLE_TRISTAR_BULLISH = 'Candle.TriStar.Bullish', 'Candle.TriStar.Bullish', 'bool', True, False
    CHANGE = 'Change', 'change_abs', 'float', True, False
    CHANGE_15MIN = 'Change 15m', 'change_abs.15', 'round', False, False
    CHANGE_15MIN_PERCENT = 'Change 15m, %', 'change.15', 'percent', False, False
    CHANGE_1H = 'Change 1h', 'change_abs.60', 'round', False, False
    CHANGE_1H_PERCENT = 'Change 1h, %', 'change.60', 'percent', False, False
    CHANGE_1MIN = 'Change 1m', 'change_abs.1', 'round', False, False
    CHANGE_1M = 'Change 1M', 'change_abs.1M', 'round', False, False
    CHANGE_1MIN_PERCENT = 'Change 1m, %', 'change.1', 'percent', False, False
    CHANGE_1M_PERCENT = 'Change 1M, %', 'change.1M', 'percent', False, False
    CHANGE_1W = 'Change 1W', 'change_abs.1W', 'round', False, False
    CHANGE_1W_PERCENT = 'Change 1W, %', 'change.1W', 'percent', False, False
    CHANGE_4H = 'Change 4h', 'change_abs.240', 'round', False, False
    CHANGE_4H_PERCENT = 'Change 4h, %', 'change.240', 'percent', False, False
    CHANGE_5MIN = 'Change 5m', 'change_abs.5', 'round', False, False
    CHANGE_5MIN_PERCENT = 'Change 5m, %', 'change.5', 'percent', False, False
    CHANGE_FROM_OPEN = 'Change from Open', 'change_from_open_abs', 'float', True, False
    CHANGE_FROM_OPEN_PERCENT = 'Change from Open %', 'change_from_open', 'percent', True, False
    CHANGE_PERCENT = 'Change %', 'change', 'percent', True, False
    COMMODITY_CHANNEL_INDEX_20 = 'Commodity Channel Index (20)', 'CCI20', 'computed_recommendation', True, True
    DESCRIPTION = 'description', 'description', 'text', False, False
    DONCHIAN_CHANNELS_LOWER_BAND_20 = 'Donchian Channels Lower Band (20)', 'DonchCh20.Lower', 'round', True, False
    DONCHIAN_CHANNELS_UPPER_BAND_20 = 'Donchian Channels Upper Band (20)', 'DonchCh20.Upper', 'round', True, False
    EXCHANGE = 'Exchange', 'exchange', 'text', False, False
    EXPONENTIAL_MOVING_AVERAGE_10 = 'Exponential Moving Average (10)', 'EMA10', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_100 = 'Exponential Moving Average (100)', 'EMA100', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_20 = 'Exponential Moving Average (20)', 'EMA20', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_200 = 'Exponential Moving Average (200)', 'EMA200', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_30 = 'Exponential Moving Average (30)', 'EMA30', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_5 = 'Exponential Moving Average (5)', 'EMA5', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_50 = 'Exponential Moving Average (50)', 'EMA50', 'computed_recommendation', True, False
    FULLY_DILUTED_MARKET_CAP = 'Fully Diluted Market Cap', 'market_cap_diluted_calc', 'missing', False, False
    GAP_PERCENT = 'Gap %', 'gap', 'percent', True, False
    HIGH = 'High', 'high', 'float', True, False
    HULL_MOVING_AVERAGE_9 = 'Hull Moving Average (9)', 'HullMA9', 'recommendation', True, False
    ICHIMOKU_BASE_LINE_9_26_52_26 = 'Ichimoku Base Line (9, 26, 52, 26)', 'Ichimoku.BLine', 'computed_recommendation', True, False
    ICHIMOKU_CONVERSION_LINE_9_26_52_26 = 'Ichimoku Conversion Line (9, 26, 52, 26)', 'Ichimoku.CLine', 'round', True, False
    ICHIMOKU_LEADING_SPAN_A_9_26_52_26 = 'Ichimoku Leading Span A (9, 26, 52, 26)', 'Ichimoku.Lead1', 'float', True, False
    ICHIMOKU_LEADING_SPAN_B_9_26_52_26 = 'Ichimoku Leading Span B (9, 26, 52, 26)', 'Ichimoku.Lead2', 'round', True, False
    KELTNER_CHANNELS_LOWER_BAND_20 = 'Keltner Channels Lower Band (20)', 'KltChnl.lower', 'float', True, False
    KELTNER_CHANNELS_UPPER_BAND_20 = 'Keltner Channels Upper Band (20)', 'KltChnl.upper', 'float', True, False
    LOGOID = 'logoid', 'logoid', 'text', False, False
    LOW = 'Low', 'low', 'float', True, False
    MACD_LEVEL_12_26 = 'MACD Level (12, 26)', 'MACD.macd', 'computed_recommendation', True, False
    MACD_SIGNAL_12_26 = 'MACD Signal (12, 26)', 'MACD.signal', 'float', True, False
    MARKET_CAPITALIZATION = 'Market Capitalization', 'market_cap_calc', 'missing', False, False
    MOMENTUM_10 = 'Momentum (10)', 'Mom', 'computed_recommendation', True, True
    MONTHLY_PERFORMANCE = 'Monthly Performance', 'Perf.1M', 'percent', False, False
    MONTH_HIGH_1 = '1-Month High', 'High.1M', 'round', False, False
    MONTH_HIGH_3 = '3-Month High', 'High.3M', 'round', False, False
    MONTH_HIGH_6 = '6-Month High', 'High.6M', 'round', False, False
    MONTH_LOW_1 = '1-Month Low', 'Low.1M', 'round', False, False
    MONTH_LOW_3 = '3-Month Low', 'Low.3M', 'round', False, False
    MONTH_LOW_6 = '6-Month Low', 'Low.6M', 'round', False, False
    MONTH_PERFORMANCE_3 = '3-Month Performance', 'Perf.3M', 'percent', False, False
    MONTH_PERFORMANCE_6 = '6-Month Performance', 'Perf.6M', 'percent', False, False
    MOVING_AVERAGES_RATING = 'Moving Averages Rating', 'Recommend.MA', 'rating', True, False
    NAME = 'name', 'name', 'text', False, False
    NEGATIVE_DIRECTIONAL_INDICATOR_14 = 'Negative Directional Indicator (14)', 'ADX-DI', 'round', True, True
    OPEN = 'Open', 'open', 'float', True, False
    OSCILLATORS_RATING = 'Oscillators Rating', 'Recommend.Other', 'rating', True, False
    PARABOLIC_SAR = 'Parabolic SAR', 'P.SAR', 'computed_recommendation', True, False
    PATTERN = 'Pattern', 'candlestick', 'missing', True, False
    PIVOT_CAMARILLA_P = 'Pivot Camarilla P', 'Pivot.M.Camarilla.Middle', 'float', True, False
    PIVOT_CAMARILLA_R1 = 'Pivot Camarilla R1', 'Pivot.M.Camarilla.R1', 'float', True, False
    PIVOT_CAMARILLA_R2 = 'Pivot Camarilla R2', 'Pivot.M.Camarilla.R2', 'float', True, False
    PIVOT_CAMARILLA_R3 = 'Pivot Camarilla R3', 'Pivot.M.Camarilla.R3', 'round', True, False
    PIVOT_CAMARILLA_S1 = 'Pivot Camarilla S1', 'Pivot.M.Camarilla.S1', 'float', True, False
    PIVOT_CAMARILLA_S2 = 'Pivot Camarilla S2', 'Pivot.M.Camarilla.S2', 'float', True, False
    PIVOT_CAMARILLA_S3 = 'Pivot Camarilla S3', 'Pivot.M.Camarilla.S3', 'round', True, False
    PIVOT_CLASSIC_P = 'Pivot Classic P', 'Pivot.M.Classic.Middle', 'float', True, False
    PIVOT_CLASSIC_R1 = 'Pivot Classic R1', 'Pivot.M.Classic.R1', 'float', True, False
    PIVOT_CLASSIC_R2 = 'Pivot Classic R2', 'Pivot.M.Classic.R2', 'float', True, False
    PIVOT_CLASSIC_R3 = 'Pivot Classic R3', 'Pivot.M.Classic.R3', 'float', True, False
    PIVOT_CLASSIC_S1 = 'Pivot Classic S1', 'Pivot.M.Classic.S1', 'float', True, False
    PIVOT_CLASSIC_S2 = 'Pivot Classic S2', 'Pivot.M.Classic.S2', 'float', True, False
    PIVOT_CLASSIC_S3 = 'Pivot Classic S3', 'Pivot.M.Classic.S3', 'float', True, False
    PIVOT_DM_P = 'Pivot DM P', 'Pivot.M.Demark.Middle', 'round', True, False
    PIVOT_DM_R1 = 'Pivot DM R1', 'Pivot.M.Demark.R1', 'round', True, False
    PIVOT_DM_S1 = 'Pivot DM S1', 'Pivot.M.Demark.S1', 'round', True, False
    PIVOT_FIBONACCI_P = 'Pivot Fibonacci P', 'Pivot.M.Fibonacci.Middle', 'float', True, False
    PIVOT_FIBONACCI_R1 = 'Pivot Fibonacci R1', 'Pivot.M.Fibonacci.R1', 'float', True, False
    PIVOT_FIBONACCI_R2 = 'Pivot Fibonacci R2', 'Pivot.M.Fibonacci.R2', 'float', True, False
    PIVOT_FIBONACCI_R3 = 'Pivot Fibonacci R3', 'Pivot.M.Fibonacci.R3', 'float', True, False
    PIVOT_FIBONACCI_S1 = 'Pivot Fibonacci S1', 'Pivot.M.Fibonacci.S1', 'float', True, False
    PIVOT_FIBONACCI_S2 = 'Pivot Fibonacci S2', 'Pivot.M.Fibonacci.S2', 'float', True, False
    PIVOT_FIBONACCI_S3 = 'Pivot Fibonacci S3', 'Pivot.M.Fibonacci.S3', 'float', True, False
    PIVOT_WOODIE_P = 'Pivot Woodie P', 'Pivot.M.Woodie.Middle', 'round', True, False
    PIVOT_WOODIE_R1 = 'Pivot Woodie R1', 'Pivot.M.Woodie.R1', 'round', True, False
    PIVOT_WOODIE_R2 = 'Pivot Woodie R2', 'Pivot.M.Woodie.R2', 'round', True, False
    PIVOT_WOODIE_R3 = 'Pivot Woodie R3', 'Pivot.M.Woodie.R3', 'round', True, False
    PIVOT_WOODIE_S1 = 'Pivot Woodie S1', 'Pivot.M.Woodie.S1', 'round', True, False
    PIVOT_WOODIE_S2 = 'Pivot Woodie S2', 'Pivot.M.Woodie.S2', 'round', True, False
    PIVOT_WOODIE_S3 = 'Pivot Woodie S3', 'Pivot.M.Woodie.S3', 'round', True, False
    POSITIVE_DIRECTIONAL_INDICATOR_14 = 'Positive Directional Indicator (14)', 'ADX+DI', 'round', True, True
    PRICE = 'Price', 'close', 'float', True, False
    RATE_OF_CHANGE_9 = 'Rate Of Change (9)', 'ROC', 'round', True, False
    RELATIVE_STRENGTH_INDEX_14 = 'Relative Strength Index (14)', 'RSI', 'computed_recommendation', True, True
    RELATIVE_STRENGTH_INDEX_7 = 'Relative Strength Index (7)', 'RSI7', 'computed_recommendation', True, True
    RELATIVE_VOLUME = 'Relative Volume', 'relative_volume_10d_calc', 'round', True, False
    RELATIVE_VOLUME_AT_TIME = 'Relative Volume at Time', 'relative_volume_intraday.5', 'round', False, False
    SIMPLE_MOVING_AVERAGE_10 = 'Simple Moving Average (10)', 'SMA10', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_100 = 'Simple Moving Average (100)', 'SMA100', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_20 = 'Simple Moving Average (20)', 'SMA20', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_200 = 'Simple Moving Average (200)', 'SMA200', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_30 = 'Simple Moving Average (30)', 'SMA30', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_5 = 'Simple Moving Average (5)', 'SMA5', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_50 = 'Simple Moving Average (50)', 'SMA50', 'computed_recommendation', True, False
    STOCHASTIC_PERCENTD_14_3_3 = 'Stochastic %D (14, 3, 3)', 'Stoch.D', 'round', True, True
    STOCHASTIC_PERCENTK_14_3_3 = 'Stochastic %K (14, 3, 3)', 'Stoch.K', 'computed_recommendation', True, True
    STOCHASTIC_RSI_FAST_3_3_14_14 = 'Stochastic RSI Fast (3, 3, 14, 14)', 'Stoch.RSI.K', 'computed_recommendation', True, False
    STOCHASTIC_RSI_SLOW_3_3_14_14 = 'Stochastic RSI Slow (3, 3, 14, 14)', 'Stoch.RSI.D', 'round', True, False
    SUBTYPE = 'subtype', 'subtype', 'text', False, False
    TECHNICAL_RATING = 'Technical Rating', 'Recommend.All', 'rating', True, False
    TOTAL_COINS = 'Total Coins', 'total_shares_diluted', 'missing', False, False
    TRADED_VOLUME = 'Traded Volume', 'total_value_traded', 'missing', False, False
    TYPE = 'type', 'type', 'text', False, False
    ULTIMATE_OSCILLATOR_7_14_28 = 'Ultimate Oscillator (7, 14, 28)', 'UO', 'recommendation', True, False
    VOLATILITY = 'Volatility', 'Volatility.D', 'percent', False, False
    VOLATILITY_MONTH = 'Volatility Month', 'Volatility.M', 'percent', False, False
    VOLATILITY_WEEK = 'Volatility Week', 'Volatility.W', 'percent', False, False
    VOLUME = 'Volume', 'volume', 'number_group', True, False
    VOLUME_24H_CHANGE_PERCENT = 'Volume 24h Change %', '24h_vol_change|5', 'percent', False, False
    VOLUME_24H_IN_USD = 'Volume 24h in USD', '24h_vol|5', 'number_group', False, False
    VOLUME_WEIGHTED_AVERAGE_PRICE = 'Volume Weighted Average Price', 'VWAP', 'float', True, False
    VOLUME_WEIGHTED_MOVING_AVERAGE_20 = 'Volume Weighted Moving Average (20)', 'VWMA', 'recommendation', True, False
    WEEKLY_PERFORMANCE = 'Weekly Performance', 'Perf.W', 'percent', False, False
    WEEK_HIGH_52 = '52 Week High', 'price_52_week_high', 'round', False, False
    WEEK_LOW_52 = '52 Week Low', 'price_52_week_low', 'round', False, False
    WILLIAMS_PERCENT_RANGE_14 = 'Williams Percent Range (14)', 'W.R', 'computed_recommendation', True, False
    YEARLY_PERFORMANCE = 'Yearly Performance', 'Perf.Y', 'percent', False, False
    YTD_PERFORMANCE = 'YTD Performance', 'Perf.YTD', 'percent', False, False
    Y_PERFORMANCE_5 = '5Y Performance', 'Perf.5Y', 'percent', False, False