#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.grid as gridlib

from kukaController import KukaController


class Frame(wx.Frame):
    def setDataToGrid(self, data):
        for i in range(len(data.position)):
            self.myGrid.SetCellValue(i, 2, ("%.2f" % data.position[i]))
            self.myGrid.SetCellValue(i, 1, ("%.2f" % data.velocity[i]))
            self.myGrid.SetCellValue(i, 0, ("%.2f" % data.effort[i]))
        pass

    def getJoinfFromText(self):
        return [
            float(self.j1PosTex.GetValue()),
            float(self.j2PosTex.GetValue()),
            float(self.j3PosTex.GetValue()),
            float(self.j4PosTex.GetValue()),
            float(self.j5PosTex.GetValue()),
        ]


    def OnSendJPos(self, event):
        self.kuka.setJointPositions(self.getJoinfFromText())
        pass

    def OnSendJVel(self, event):
        self.kuka.setJointVelocities(self.getJoinfFromText())
        pass

    def OnSendJTor(self, event):
        self.kuka.setJointTorques(self.getJoinfFromText())
        pass


    def OnSendGPos(self, event):
         self.kuka.setGripperPositions(float(self.g1PosTex.GetValue()),float(self.g2PosTex.GetValue()))
         pass

    def OnSendGVel(self, event):
         self.kuka.setGripperVelocities(float(self.g1PosTex.GetValue()), float(self.g2PosTex.GetValue()))
         pass

    def OnSendGTor(self, event):
        self.kuka.setGripperTorques(float(self.g1PosTex.GetValue()), float(self.g2PosTex.GetValue()))
        pass

    def OnSendCVel(self, event):
        self.kuka.setVel(float(self.c1PosTex.GetValue()), float(self.c2PosTex.GetValue()),
                         float(self.c3PosTex.GetValue()))
        pass

    def OnUpdate(self, event):
        self.setDataToGrid(self.kuka.jointState)
        pass

    def OnStop(self, event):
        self.timer.Stop()
        pass

    def __init__(self, parent=None, id=-1, title='', pos=(0, 0), size=(600, 700)):
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.panel = wx.Panel(self)

        self.initGrid()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.myGrid)

        self.panel.SetSizer(self.sizer)
        wx.StaticText(self.panel, -1, "Джоинты", (30, 440))

        self.j1PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(70, 460), size=(40, 30))
        self.j2PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(120, 460), size=(40, 30))
        self.j3PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(170, 460), size=(40, 30))
        self.j4PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(220, 460), size=(40, 30))
        self.j5PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(270, 460), size=(40, 30))

        self.j1PosTex.SetBackgroundColour('#DDFFEE')
        self.j2PosTex.SetBackgroundColour('#DDFFEE')
        self.j3PosTex.SetBackgroundColour('#DDFFEE')
        self.j4PosTex.SetBackgroundColour('#DDFFEE')
        self.j5PosTex.SetBackgroundColour('#DDFFEE')

        self.sendJposBtn = wx.Button(self.panel, label="Положения", pos=(30, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJPos, self.sendJposBtn)
        self.sendJvelBtn = wx.Button(self.panel, label="Скорости", pos=(140, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJVel, self.sendJvelBtn)
        self.sendJtorBtn = wx.Button(self.panel, label="Моменты", pos=(250, 490), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendJTor, self.sendJtorBtn)

        wx.StaticText(self.panel, -1, "Гриппер: левый, правый", (30, 520))
        self.g1PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(30, 540), size=(40, 30))
        self.g2PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(80, 540), size=(40, 30))
        self.g1PosTex.SetBackgroundColour('#DDFFEE')
        self.g2PosTex.SetBackgroundColour('#DDFFEE')

        self.sendGposBtn = wx.Button(self.panel, label="Положения", pos=(30, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGPos, self.sendGposBtn)
        self.sendGvelBtn = wx.Button(self.panel, label="Скорости", pos=(140, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGVel, self.sendGvelBtn)
        self.sendGtorBtn = wx.Button(self.panel, label="Моменты", pos=(250, 570), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendGTor, self.sendGtorBtn)

        wx.StaticText(self.panel, -1, "Тележка: x,y,z", (30, 600))
        self.c1PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(30, 620), size=(40, 30))
        self.c2PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(80, 620), size=(40, 30))
        self.c3PosTex = wx.TextCtrl(self.panel, -1, '0', pos=(130, 620), size=(40, 30))

        self.c1PosTex.SetBackgroundColour('#DDFFEE')
        self.c2PosTex.SetBackgroundColour('#DDFFEE')
        self.c3PosTex.SetBackgroundColour('#DDFFEE')

        self.sendCvelBtn = wx.Button(self.panel, label="Скорости", pos=(30, 650), size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSendCVel, self.sendCvelBtn)

        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnUpdate, self.timer)

        self.count = wx.TextCtrl(self.panel, -1, '', pos=(235, 600), size=(30, 30))
        self.count.SetBackgroundColour('#DDFFEE')
        self.count.SetEditable(False)
        self.count.Show(False)
        self.kuka = KukaController()

    def initGrid(self):
        self.myGrid = gridlib.Grid(self.panel)
        self.myGrid.CreateGrid(16, 3)
        self.myGrid.SetColLabelValue(0, "Момент")
        self.myGrid.SetColLabelValue(1, "Скорость")
        self.myGrid.SetColLabelValue(2, "Положение")
        self.myGrid.SetColSize(2, 100)
        self.myGrid.SetRowLabelValue(0, "Hokuyo_URG_04LX_UG01_joint")
        self.myGrid.SetRowLabelValue(1, "wheel_joint_br")
        self.myGrid.SetRowLabelValue(2, "caster_joint_br")
        self.myGrid.SetRowLabelValue(3, "wheel_joint_bl")
        self.myGrid.SetRowLabelValue(4, "caster_joint_bl")
        self.myGrid.SetRowLabelValue(5, "suspension_joint")
        self.myGrid.SetRowLabelValue(6, "wheel_joint_fl")
        self.myGrid.SetRowLabelValue(7, "wheel_joint_fr")
        self.myGrid.SetRowLabelValue(8, "caster_joint_fr")
        self.myGrid.SetRowLabelValue(9, "arm_joint_1")
        self.myGrid.SetRowLabelValue(10, "arm_joint_2")
        self.myGrid.SetRowLabelValue(11, "arm_joint_3")
        self.myGrid.SetRowLabelValue(12, "arm_joint_4")
        self.myGrid.SetRowLabelValue(13, "arm_joint_5")
        self.myGrid.SetRowLabelValue(14, "gripper_finger_joint_r")
        self.myGrid.SetRowLabelValue(15, "gripper_finger_joint_l")

        self.myGrid.SetRowLabelSize(210)
