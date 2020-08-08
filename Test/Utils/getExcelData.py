import pprint
import xlrd


def get_data(start_row, end_row, body_cal=6, req_col=7):
    excel_dir = '../../Data/学习日志接口用例.xls'
    workbook = xlrd.open_workbook(excel_dir, formatting_info=True)
    work_sheet = workbook.sheet_by_index(1)
    data_list = []
    for one in range(start_row - 1, end_row):
        data_list.append((work_sheet.cell(one, body_cal).value,
                          work_sheet.cell(one, req_col).value))
    return data_list


if __name__ == '__main__':
    for i in get_data(2, 6):
        print(i)














