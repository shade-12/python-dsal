def spreadsheet_encode_column(col_str):
    result, count = 0, len(col_str) - 1
    for c in col_str:
        base26 = ord(c) - ord('A') + 1
        result += base26 * (26 ** count)
        count -= 1
    return result

print(spreadsheet_encode_column("ZZ"))