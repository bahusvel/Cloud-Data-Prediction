library(forecast)

metric_name <- "df.root.df_complex.used.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)
fit_result <- HoltWinters(train_series)

forecast_results <- forecast.HoltWinters(fit_result, h = 2880)
plot(forecast_results)
lines(test_series)

accuracy(forecast_results, test_series)