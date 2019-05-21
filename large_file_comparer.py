from collections import Counter
input_file1 = r'input_file.txt'
input_file2 = r'input_file.1.txt'

__author__ = 'https://github.com/praveen-kumar-rr'

# Simple Memory Efficient high perfomance file comparer.
# Can be used to efficiently compare large files.

# Alogrithm:
# Hashes the lines and compared first.
# Non matching lines are picked as different count.
# All the matching lines are taken and the exact lines are read from file
# These strings undergo same comparison process based on string itself


def accumulate_index(values):
    '''
    Returns dict like key: [indexes]
    '''
    result = {}
    for i, v in enumerate(values):
        indexes = result.get(v, [])
        result[v] = indexes + [i]
    return result


def get_lines(fp, line_numbers):
    '''
    Reads lines from the file pointer based on the lines_numbers list of indexes
    '''
    return (v for i, v in enumerate(fp) if i in line_numbers)


def get_match_diff(left, right):
    '''
    Compares the left and right iterables and returns the matching and different items
    '''
    left_set = set(left)
    right_set = set(right)
    return left_set ^ right_set, left_set & right_set


if __name__ == '__main__':
    # Gets hashes of all lines for both files
    counter1 = accumulate_index(map(hash, open(input_file1)))
    counter2 = accumulate_index(map(hash, open(input_file2)))

    diff_hashes, matching_hashes = get_match_diff(
        counter1.keys(), counter2.keys())

    diff_lines_count = len(diff_hashes)

    matching_lines_count = 0
    for h in matching_hashes:
        with open(input_file1) as fp1, open(input_file2) as fp2:
            st_counter_1 = Counter(get_lines(fp1, counter1[h]))
            st_counter_2 = Counter(get_lines(fp2, counter2[h]))
            d, m = get_match_diff(st_counter_1.keys(), st_counter_2.keys())
            diff_lines_count += len(d)
            matching_lines_count += len(m)

    print('Total number of matching lines is : ', matching_lines_count)
    print('Total number of different lines is : ', diff_lines_count)
