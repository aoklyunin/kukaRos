#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib; roslib.load_manifest('kuka_simple_control')
import rospy
import wx
from forms import Frame

class App(wx.App):
    def OnInit(self):
        self.frame = Frame(None,-1,"Move It") # создание окна
        self.frame.Show(True) # отображение окна
        self.SetTopWindow(self.frame) # указываем, что только что созданное окно - главное
        return True # ну не False же возвращать, правда?:)


def main():
    app = App()
    app.MainLoop()

if __name__=='__main__':

    main()
    rospy.spin()

