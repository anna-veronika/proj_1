# Title     : TODO
# Objective : TODO
# Created by: annatomaselli
# Created on: 11/01/20

print('hello_r', quote = FALSE)

blastn = "/path/to/blast/ncbi-blast-2.6.0+/bin/blastn"
blast_db = "blast_database"
input = "input_file"
evalue = 1e-6
format = 6
colnames <- c("qseqid",
               "sseqid",
               "pident",
               "length",
               "mismatch",
               "gapopen",
               "qstart",
               "qend",
               "sstart",
               "send",
               "evalue",
               "bitscore")

blast_out <- system2(command = "blastn", 
                     args = c("-db", blast_db, 
                              "-query", input, 
                              "-outfmt", format, 
                              "-evalue", evalue,
                              "-ungapped"),
                     wait = TRUE,
                     stdout = TRUE) %>%
  as_tibble() %>% 
  separate(col = value, 
           into = colnames,
           sep = "\t",
           convert = TRUE)
