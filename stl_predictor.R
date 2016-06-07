library(forecast)

metric_name <- "memory.memory.free.value.csv"
data_end <- 8640

stl_series <- ts(resampled[1:data_end, metric_name], frequency = 1440)
stl_fit <- stl(x = stl_series, s.window = "per")
plot(forecast(stl_fit))