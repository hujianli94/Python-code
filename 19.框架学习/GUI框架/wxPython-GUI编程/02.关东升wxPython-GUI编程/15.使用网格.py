# coding=utf-8
# 代码文件：chapter19/ch19.7.3-1.py

import wx
import wx.grid

data = [['0036', '高等数学', '李放', '人民邮电出版社', '20000812', '1'],
        ['0004', 'FLASH精选', '刘扬', '中国纺织出版社', '19990312', '2'],
        ['0026', '软件工程', '牛田', '经济科学出版社', '20000328', '4'],
        ['0031', '软件工程', '戴志名', '电子工业出版社', '20000324', '3'],
        ['0006', '世界杯', '柳飞', '世界出版社', '19990412', '2'],
        ['0028', '高级语言程序设计', '寇国华', '清华大学出版社', '20000117', '3'],
        ['0038', '十大旅游胜地', '潭晓明', '南方出版社', '20000403', '2'],
        ['0018', '编译原理', '郑键', '机械工业出版社', '20000415', '2'],
        ['0007', 'JAVA程序设计', '张余', '人民邮电出版社', '19990613', '1'],
        ['0013', '幽灵', '钱力华', '华光出版社', '19991008', '1'],
        ['0022', '万紫千红', '丛丽', '北京大学出版社', '20000702', '3'],
        ['0027', '世界语言大观', '候丙辉', '经济科学出版社', '20000814', '2'],
        ['0029', '操作系统概论', '聂元名', '清华大学出版社', '20001028', '1'],
        ['0016', '数据库系统概念', '吴红', '机械工业出版社', '20000328', '3'],
        ['0005', 'java基础', '王一', '电子工业出版社', '19990528', '3'],
        ['0032', 'SQL使用手册', '贺民', '电子工业出版社', '19990425', '2']]

column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='网格控件', size=(550, 500))
        self.Centre()  # 设置窗口居中
        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)

    def OnLabelLeftClick(self, event):
        print("RowIdx：{0}".format(event.GetRow()))
        print("ColIdx：{0}".format(event.GetCol()))
        print(data[event.GetRow()])
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(data), len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[row])):
                grid.SetColLabelValue(col, column_names[col])
                grid.SetCellValue(row, col, data[row][col])
        # 设置行和列自定调整
        grid.AutoSize()

        return grid


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
