library(forecast)

metric_name <- "netlink.eth0.if_octets.rx.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)

# Holt Winters
fit_result <- HoltWinters(train_series)
forecast_results <- forecast.HoltWinters(fit_result, h = 2880)
plot(forecast_results)
lines(test_series)
accuracy(forecast_results, test_series)

#STL
fit_result <- stl(x = train_series, s.window = "per", robust = TRUE)
forecast_results <- forecast(fit_result)
plot(forecast_results)
lines(test_series)
accuracy(forecast_results, test_series)