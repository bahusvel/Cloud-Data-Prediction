library(forecast)

metric_name <- "cpu.0.cpu.idle.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4)
fit_result <- stl(x = train_series, s.window = "per", robust = TRUE)

forecast_results <- forecast(fit_result)
plot(forecast_results)

accuracy(forecast_results, test_series)