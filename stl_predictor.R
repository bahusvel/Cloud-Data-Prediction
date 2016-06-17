library(forecast)

metric_name <- "memory.memory.free.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)

fit_result <- stl(x = train_series, s.window = "per", robust = TRUE)
forecast_results <- forecast(fit_result, method = "rwdrift")

jpeg(paste("results/", metric_name, "_tuned_stl.jpeg", sep = ""))
plot(forecast_results)
lines(test_series)
dev.off()

test_accuracy <- accuracy(forecast_results, test_series)
test_accuracy
write.table(test_accuracy, file = paste("results/", metric_name, "_tuned_stl.csv", sep = ""), sep = ",")
