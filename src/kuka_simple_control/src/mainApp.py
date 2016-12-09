#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib; roslib.load_manifest('kuka_simple_control')
import rospy
import wx
from forms import Frame

# класс приложения
class App(wx.App):
    # инициализация приложения
    def OnInit(self):
        # Задаём имя ноды
        self.node_name = "fucking_kuka_node"
        # инициализируем ноду роса
        rospy.init_node(self.node_name)
        # создание окна
        self.frame = Frame(None,-1,"Kuka Controller")
        # отображение окна
        self.frame.Show(True)
        # указываем, что только что созданное окно - главное
        self.SetTopWindow(self.frame)
        # функция, вызываемая при закрытии ноды
        rospy.on_shutdown(self.shutdown)
        return True # ну не False же возвращать, правда?:)
    # завершение приложения
    def shutdown(self):
        # закрываем приложение
        self.frame.Close()
        # Завершаем работу робота
        rospy.loginfo("Stopping the robot...")

# главная функция
if __name__=='__main__':
    # объект класса приложение
    app = App()
    # запускаем главный цикл приложения
    app.MainLoop()


