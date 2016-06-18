library(forecast)

metric_name <- "netlink.eth0.if_octets.rx.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)

fit_result <- HoltWinters(train_series, beta = FALSE)
forecast_results <- forecast.HoltWinters(fit_result, h = 2880)

jpeg(paste("results/", metric_name, "_tuned_holt.jpeg", sep = ""))
plot(forecast_results)
lines(test_series)
dev.off()

test_accuracy <- accuracy(forecast_results, test_series)
test_accuracy
write.table(test_accuracy, file = paste("results/", metric_name, "_tuned_holt.csv", sep = ""), sep = ",")
