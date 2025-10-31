# # Python program to extract text after 'chnl:ApplicationLogger' from each line of a log file,
# # store entries in a tuple, and write them to a new text file.
#
# # input_filename = "input_logs.txt"
# # output_filename = "output_logs.txt"
# #
#
# input_filename = r"S:\LearnPython\input.txt"
# output_filename = r"S:\LearnPython\output.txt"
#
# # Collect entries in a list first (since tuples are immutable), then convert to a tuple.
# entries = []
#
# with open(input_filename, "r", encoding="utf-8") as infile:
#     for line in infile:
#         if 'chnl:ApplicationLogger' in line:
#             # Split on the delimiter and take everything after it
#             parts = line.split('chnl:ApplicationLogger', 1)
#             if len(parts) > 1:
#                 # Strip any leading/trailing whitespace or line breaks from extracted text
#                 extracted = parts[1].strip()
#                 entries.append(extracted)
#
# # Convert to tuple for immutability
# result_tuple = tuple(entries)
#
# # Write each entry on a new line in the output file
# with open(output_filename, "w", encoding="utf-8") as outfile:
#     for entry in result_tuple:
#         outfile.write(entry + "\n")
#
# print(f"Extraction complete. {len(result_tuple)} entries written to {output_filename}")
