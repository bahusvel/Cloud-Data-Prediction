number_columns <- ncol(resampled)
column_names <- colnames(resampled)

for (column in 2:number_columns){
  jpeg(paste("aggressive_smoothing_plots/", column_names[column], ".jpeg", sep = ""))
  plot(rollmean(resampled[,column], 240), type = "l")
  dev.off()
}