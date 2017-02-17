#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.grid as gridlib
from KawasakiController import KawasakiController


class Frame(wx.Frame):
    # закрытие формы
    def onClose(self, event):
        # останавливаем таймер
        self.timer.Stop()
        self.Close()
    # записать полученную от куки дату в таблицу
    def setDataToGrid(self, data):
        i = 0
        for key in data["position"]:
            self.myGrid.SetCellValue(i, 2, ("%.2f" %(data["position"][key])))
            self.myGrid.SetCellValue(i, 1, ("%.2f" % (data["velocity"][key])))
            self.myGrid.SetCellValue(i, 0, ("%.2f" % (data["torque"][key])))
            i+=1
        pass

    # получить углы из полей ввобда джоинтов
    def getJoinfFromText(self):
        return [
            float(self.j1PosTex.GetValue()),
            float(self.j2PosTex.GetValue()),
            float(self.j3PosTex.GetValue()),
            float(self.j4PosTex.GetValue()),
            float(self.j5PosTex.GetValue()),
            float(self.j6PosTex.GetValue()),
        ]
    # управление джоинтами по положению
    def OnSendJPos(self, event):
        self.kawasaki.setJointPositions(self.getJoinfFromText())
        pass
    # управление джоинтами по скоростям
    def OnSendJVel(self, event):
        self.kawasaki.setJointVelocities(self.getJoinfFromText())
        pass
    # управление джоинтами по моментам
    def OnSendJTor(self, event):
        self.kawasaki.setJointTorques(self.getJoinfFromText())
        pass
    # управление гриппером по положению
    def OnSendGPos(self, event):
         self.kawasaki.setGripperPositions(float(self.glPosTex.GetValue()), float(self.grPosTex.GetValue()))
         pass
    # управление гриппером по положению
    def OnSendGVel(self, event):
         self.kawasaki.setGripperVelocities(float(self.glPosTex.GetValue()), float(self.grPosTex.GetValue()))
         pass
    # управление гриппером по скоростям
    def OnSendGTor(self, event):
        self.kawasaki.setGripperTorques(float(self.glPosTex.GetValue()), float(self.grPosTex.GetValue()))
        pass
    # управление джоинтами по моментам
    def OnSendCVel(self, event):
        self.kawasaki.setCarrigeVel(float(self.cxPosTex.GetValue()), float(self.cyPosTex.GetValue()),
                                float(self.czPosTex.GetValue()))
        pass

    # открыть гриппер
    def OnOpenGripper(self, event):
        self.kawasaki.openGripper()
        pass

    # закрыть гриппер
    def OnCloseGripper(self, event):
        self.kawasaki.closeGripper()
        pass

    # события по таймеру
    def OnTimer(self, event):
        self.setDataToGrid(self.kawasaki.jointState)
        pass
    # конструктор
    def __init__(self, parent=None, id=-1, title='', pos=(0, 0), size=(490, 700)):
        # создаём фрейм
        wx.Frame.__init__(self, parent, id, title, pos, size)
        # создаём объект для взаимодействия с роботом
        self.kawasaki = KawasakiController()
        # добавляем на фрейм панель
        self.panel = wx.Panel(self)
        # инициализируем панель
        self.initGrid()
        # добавляем прокрутку на таблицу (пока что почему-то не работает, мб потому что таблица помещается полностью)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.myGrid)
        self.panel.SetSizer(self.sizer)
        # инициализируем элементы управления
        self.initControlItems()
        # запускаем таймер
        self.timer = wx.Timer(self, -1)
        # раз в 0.5 секунды
        self.timer.Start(500)
        # указываем функцию, которая будет вызываться по таймеру
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

    # инициализируем элементы управления
    def initControlItems(self):
        # Управление джоинтами
        wx.StaticText(self.panel, -1, "Джоинты", (30, 440))
        # создаём поля ввода для джоинтов
        self.j1PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(30, 460), size=(40, 30))
        self.j2PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(80, 460), size=(40, 30))
        self.j3PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(130, 460), size=(40, 30))
        self.j4PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(180, 460), size=(40, 30))
        self.j5PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(230, 460), size=(40, 30))
        self.j6PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(280, 460), size=(40, 30))

        # задаём фон заливки
        self.j1PosTex.SetBackgroundColour('#DDFFEE')
        self.j2PosTex.SetBackgroundColour('#DDFFEE')
        self.j3PosTex.SetBackgroundColour('#DDFFEE')
        self.j4PosTex.SetBackgroundColour('#DDFFEE')
        self.j5PosTex.SetBackgroundColour('#DDFFEE')
        self.j6PosTex.SetBackgroundColour('#DDFFEE')

        # конпки управления джоинтами и привязка методов к ним
        self.sendJposBtn = wx.Button(self.panel, label="Положения", pos=(30, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJPos, self.sendJposBtn)
        self.sendJvelBtn = wx.Button(self.panel, label="Скорости", pos=(140, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJVel, self.sendJvelBtn)
        self.sendJtorBtn = wx.Button(self.panel, label="Моменты", pos=(250, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJTor, self.sendJtorBtn)
        # управление гриппером
        wx.StaticText(self.panel, -1, "Гриппер: левый, правый", (30, 520))
        # создаём поля ввода для пальцев гриппера
        self.glPosTex = wx.TextCtrl(self.panel, -1, '0', pos=(30, 540), size=(40, 30))
        self.grPosTex = wx.TextCtrl(self.panel, -1, '0', pos=(80, 540), size=(40, 30))
        # задаём фон заливки
        self.glPosTex.SetBackgroundColour('#DDFFEE')
        self.grPosTex.SetBackgroundColour('#DDFFEE')
        # кнопки управления гриппером и привязка методов к ним
        self.sendGposBtn = wx.Button(self.panel, label="Положения", pos=(30, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGPos, self.sendGposBtn)
        self.sendGvelBtn = wx.Button(self.panel, label="Скорости", pos=(140, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGVel, self.sendGvelBtn)

        self.sendGtorBtn = wx.Button(self.panel, label="Моменты", pos=(250, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGTor, self.sendGtorBtn)

        self.sendOpenGripper = wx.Button(self.panel, label="Открыть гриппер", pos=(30, 620), size=(120, 30))
        self.Bind(wx.EVT_BUTTON, self.OnOpenGripper, self.sendOpenGripper)

        self.sendOpenGripper = wx.Button(self.panel, label="Закрыть гриппер", pos=(150, 620), size=(120, 30))
        self.Bind(wx.EVT_BUTTON, self.OnCloseGripper, self.sendOpenGripper)


    # инициализация таблицы
    def initGrid(self):
        # создаём таблицу
        self.myGrid = gridlib.Grid(self.panel)
        # кол-во строк и столбцов
        # нумерация в таблице начинается с ячейки (0,0)
        self.myGrid.CreateGrid(8, 3)
        # задаём имена столбцов
        self.myGrid.SetColLabelValue(0, "Момент")
        self.myGrid.SetColLabelValue(1, "Скорость")
        self.myGrid.SetColLabelValue(2, "Положение")
        # задаём ширину второго столбца больше, т.к. положение не "влезает"
        self.myGrid.SetColSize(2, 100)
        # задаём имена строк
        i = 0
        for key in self.kawasaki.jointState["position"]:
            self.myGrid.SetRowLabelValue(i, key)
            i += 1

        # задаём ширину столбца с именами строк
        self.myGrid.SetRowLabelSize(210)
