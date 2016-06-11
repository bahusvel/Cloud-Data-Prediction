library(forecast)

metric_name <- "df.root.df_complex.free.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)
fit_result <- nnetar(train_series, p = 2)

forecast_results <- forecast(fit_result)
plot(forecast_results)
lines(test_series)

accuracy(forecast_results, test_series)