library(forecast)

metric_name <- "cpu.1.cpu.idle.value.csv"

full_series <- ts(final[[metric_name]], frequency = 1440)
train_series <- window(full_series, start=1,end=4)
test_series <- window(full_series, start=4, end=6)

# Holt Winters
postfix <- "_holt"

fit_result <- HoltWinters(train_series)                         # fit parameters
forecast_results <- forecast.HoltWinters(fit_result, h = 2880)  # forecast parameters

jpeg(paste("results/", metric_name, postfix, ".jpeg", sep = ""))
plot(forecast_results)
lines(test_series)
dev.off()

result_accuracy <- accuracy(forecast_results, test_series)
write.table(result_accuracy, file = paste("results/", metric_name, postfix, ".csv", sep = ""), sep = ",")

#STL
postfix <- "_stl"

fit_result <- stl(x = train_series, s.window = "per")         # fit parameters
forecast_results <- forecast(fit_result)                      # forecast parameters

jpeg(paste("results/", metric_name, postfix,".jpeg", sep = ""))
plot(forecast_results)
lines(test_series)
dev.off()

result_accuracy <- accuracy(forecast_results, test_series)
write.table(result_accuracy, file = paste("results/", metric_name, postfix,".csv", sep = ""), sep = ",")