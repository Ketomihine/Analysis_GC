# Example: Gene expression heatmap using ComplexHeatmap

# Load required packages
library(ComplexHeatmap)
library(circlize)

# Simulated expression matrix: 10 genes x 10 samples
set.seed(123)
mat <- matrix(rnorm(100), nrow = 10)
rownames(mat) <- paste0("Gene", 1:10)
colnames(mat) <- paste0("Sample", 1:10)

# Color mapping: blue->white->red
col_fun <- colorRamp2(c(-2, 0, 2), c("blue", "white", "red"))

# Draw the heatmap
ht <- Heatmap(mat,
              name = "Expression",
              col = col_fun,
              cluster_rows = TRUE,
              cluster_columns = TRUE,
              show_row_names = TRUE,
              show_column_names = TRUE)

draw(ht)
