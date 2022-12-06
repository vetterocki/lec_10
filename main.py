import pandas as pd


def print_with_tabulation(value):
    print('\n', value)


if __name__ == '__main__':
    full_excel_sheet = pd.read_excel('towns_people_refactored.xlsx', 'Sheet2')
    print(full_excel_sheet)

    print(full_excel_sheet[['Town', '1989 year']])
    print_with_tabulation(full_excel_sheet.iloc[1:, 0:4])

    print_with_tabulation(full_excel_sheet.reindex(full_excel_sheet.index[1:], columns=['1979 year', '1970 year']))

    re_indexed_sheet = full_excel_sheet.reindex(columns=['Town', '2019 year', '1897 year'])

    print_with_tabulation(re_indexed_sheet)

    re_indexed_sheet = re_indexed_sheet.set_index("Town")

    print_with_tabulation(re_indexed_sheet)

    print("______________________________________________________________________")
    full_excel_sheet.rename(columns={'1989 year': '1990 year', '1923 year': '1933 year'}, inplace=True)
    print(full_excel_sheet)

    print("______________________________________________________________________")
    full_excel_sheet['percentage'] = [8.4, 7.6, 12.1, 3.5, 4.5, 5.9, 5.5, 8.8, 9.0, 10.0, 11.2, 12.0, 4.6, 14.4, 6.7,
                                      6.6]
    print(full_excel_sheet)

    print("______________________________________________________________________")
    pd.set_option('display.expand_frame_repr', False)
    column_mean_value = full_excel_sheet.mean(numeric_only=True)

    print_with_tabulation(column_mean_value)
    row_mean_value = full_excel_sheet.mean(numeric_only=True, axis=1)
    full_excel_sheet['Average'] = row_mean_value

    print_with_tabulation(full_excel_sheet)

    rounded = full_excel_sheet.round({'Average': 2})

    print_with_tabulation(rounded)

    rounded['2019 year>2011 year'] = rounded['2019 year'] > rounded['2011 year']

    print_with_tabulation(rounded)

    print_with_tabulation(rounded.loc[[1, 2], ['Town', 'Average']])

    print_with_tabulation(rounded.loc[rounded.index[::4], ['2001 year', 'Average']])

    new_comparison = rounded['2001 year'] > rounded['1970 year']

    print_with_tabulation(rounded[new_comparison])

    print_with_tabulation(rounded.sort_values(by='percentage'))
    sorted_values = rounded.sort_values(by='percentage', ascending=True)

    print_with_tabulation(sorted_values)

    sorted_values = sorted_values.drop(columns='2019 year>2011 year')
    sorted_values = sorted_values.drop(index=0)

    print_with_tabulation(sorted_values)
    sorted_values.drop(['2019 year'], axis=1, inplace=True)
    sorted_values.drop(sorted_values.index[[2, 3, 4, 5, 6, 7, 8, 9]], axis=0, inplace=True)

    print_with_tabulation(sorted_values)
