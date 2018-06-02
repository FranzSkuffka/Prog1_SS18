import file_handler

print(file_handler.get_text('dummy_file.txt'))
print(file_handler.get_lines('dummy_file.txt'))

import analyze

print(analyze.get_word_count(file_handler.get_text('dummy_file.txt'), 'Line'))

import interactive_analysis

print(interactive_analysis.get_word_count_from_user(word = "Line"))
