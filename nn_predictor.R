library(forecast)

metric_name <- "cpu.1.cpu.idle.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)

fit_result <- nnetar(train_series, p = 40)
forecast_results <- forecast(fit_result)

jpeg(paste("results/", metric_name, "_nn.jpeg", sep = ""))
plot(forecast_results)
#lines(test_series)
dev.off()


test_accuracy <- accuracy(forecast_results, test_series)
test_accuracy
write.table(test_accuracy, file = paste("results/", metric_name, "_nn.csv", sep = ""), sep = ",")