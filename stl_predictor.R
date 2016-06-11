library(forecast)

metric_name <- "cpu.0.cpu.idle.value.csv"
data_end <- 8640

stl_series <- ts(final[1:data_end, metric_name], frequency = 1440)
stl_fit <- stl(x = stl_series, s.window = "per")
plot(forecast(stl_fit))