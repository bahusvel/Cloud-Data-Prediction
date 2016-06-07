library(forecast)

metric_name <- "memory.memory.free.value.csv"
data_end <- 8640

stl_series <- ts(resampled[1:data_end, metric_name], frequency = 1440)
holt_fit <- forecast.HoltWinters(stl_series)
plot.forecast(forecast.HoltWinters(holt_fit, h = 1440 * 2))