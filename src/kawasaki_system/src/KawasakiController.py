#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import rospy
import brics_actuator.msg
import geometry_msgs.msg
import sensor_msgs.msg


# ToDO
# проверка, что задание по положению джоинтов не выходят за границы
# подумать, как останавливать управление по силам, если моменты обнулить, то робот прото упадёт
#   -можно попробовать задавать скорости в 0
class KawasakiController():
    # масимальная скорость руки
    maxArmVelocity = math.radians(90)
    # диапазон допустимых значений джоинтов
    jointsRange = [
        [math.radians(160), math.radians(-160)],
        [math.radians(140), math.radians(-105)],
        [math.radians(120), math.radians(-155)],
        [math.radians(270), math.radians(-270)],
        [math.radians(145), math.radians(-145)],
        [math.radians(360), math.radians(-360)],
    ]
    # диапазон допустимых значений движения гриппера
    gripperRange = [-0.02, 0.02]
    # константы типов сообщений
    TYPE_JOINT_POSITIONS = 0  # положение джоинта
    TYPE_JOINT_VELOCITIES = 1  # скорость джоинта
    TYPE_JOINT_TORQUES = 2  # момент джоинта
    TYPE_GRIPPER_POSITION = 3  # положение гриппера
    TYPE_GRIPPER_VELOCITY = 4  # скорость гриппера
    TYPE_GRIPPER_TORQUE = 5  # сила гриппера
    # ответные данные, полученные от куки
    jointState = {
        "position": {
            "KawasakiJoint1": 0,
            "KawasakiJoint2": 0,
            "KawasakiJoint3": 0,
            "KawasakiJoint4": 0,
            "KawasakiJoint5": 0,
            "KawasakiJoint6": 0,
            "KawasakiGripper1": 0,
            "KawasakiGripper2": 0,
        },
        "velocity": {
            "KawasakiJoint1": 0,
            "KawasakiJoint2": 0,
            "KawasakiJoint3": 0,
            "KawasakiJoint4": 0,
            "KawasakiJoint5": 0,
            "KawasakiJoint6": 0,
            "KawasakiGripper1": 0,
            "KawasakiGripper2": 0,
        },
        "torque": {
            "KawasakiJoint1": 0,
            "KawasakiJoint2": 0,
            "KawasakiJoint3": 0,
            "KawasakiJoint4": 0,
            "KawasakiJoint5": 0,
            "KawasakiJoint6": 0,
            "KawasakiGripper1": 0,
            "KawasakiGripper2": 0,
        },

    }

    def openGripper(self):
        self.setGripperPositions(100.0, -100.0)

    def closeGripper(self):
        self.setGripperPositions(0.0, 0.0)

    # обработчик пришедших значений
    def jointStateCallback(self, data):
        for key in self.jointState["position"]:
            pos = data.name.index(key)
            self.jointState["position"][key] = data.position[pos]
            self.jointState["velocity"][key] = data.velocity[pos]
            self.jointState["torque"][key] = data.effort[pos]
        pass

    # конструктор
    def __init__(self):
        # переменные для публикации в топики
        self.positionArmPub = rospy.Publisher("/KawasakiArm/position_command", brics_actuator.msg.JointPositions,
                                              queue_size=1)
        self.torqueArmPub = rospy.Publisher("/KawasakiArm/force_command", brics_actuator.msg.JointTorques, queue_size=1)
        self.velocityArmPub = rospy.Publisher("/KawasakiArm/velocity_command", brics_actuator.msg.JointVelocities,
                                              queue_size=1)
        self.positionGripperPub = rospy.Publisher("/kawasaki_gripper_controller/position_command",
                                                  brics_actuator.msg.JointPositions, queue_size=1)
        self.forceGripperPub = rospy.Publisher("/kawasaki_gripper_controller/force_command",
                                               brics_actuator.msg.JointTorques,
                                               queue_size=1)
        self.velocityGripperPub = rospy.Publisher("/kawasaki_gripper_controller/velocity_command",
                                                  brics_actuator.msg.JointVelocities, queue_size=1)
        self.jointStateSubscriber = rospy.Subscriber("/joint_states", sensor_msgs.msg.JointState,
                                                     self.jointStateCallback)

        # пауза необходима для правильной обработки пакетов
        rospy.sleep(1)

    # получаем по типу топика размерность
    def getUnitValue(self, tp):
        if tp == self.TYPE_JOINT_POSITIONS:  # положение джоинтов
            return "rad"
        elif tp == self.TYPE_JOINT_VELOCITIES:  # скорость джоинтов
            return "s^-1 rad"
        elif tp == self.TYPE_JOINT_TORQUES:  # силы джоинтов
            return "m^2 kg s^-2 rad^-1"
        elif tp == self.TYPE_GRIPPER_POSITION:  # положение гриппера
            return "m"
        elif tp == self.TYPE_GRIPPER_VELOCITY:  # сокрость гриппера
            return "s^-1 m"
        elif tp == self.TYPE_GRIPPER_TORQUE:  # сила гриппера
            return "m kg s^-2"
        else:
            return None

    # по номеру джоинта, значению и типу генерируем сообщение
    def generateJoinVal(self, joint_num, val, tp):
        # создаём сообщение джоинта
        jv = brics_actuator.msg.JointValue()
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        # имя джоинта
        jv.joint_uri = "KawasakiJoint" + str(joint_num)
        # размерность
        jv.unit = self.getUnitValue(tp)
        # непосредственное значение
        jv.value = val
        return jv

    # задать скорость каретке x, y - линейные перемещений, z - поворот
    def setCarrigeVel(self, x, y, z):
        # создаём сообщение
        msg = geometry_msgs.msg.Twist()
        # заполняем его данными
        msg.linear.x = x
        msg.linear.y = y
        msg.angular.z = z
        # публикуем сообщение в топик
        self.cartVelPub.publish(msg)
        # выполняем задержку (ебаный рос)
        rospy.sleep(1)

    # управляем положением гриппера в миллиметрах, положение левого и правого пальцев
    def setGripperPositions(self, leftG, rightG):
        # формируем сообщение положения джоинтов
        msg = brics_actuator.msg.JointPositions()
        # положения джоинтов - это список
        msg.positions = []
        # создаём объект описания жвижения жоинта
        jv = brics_actuator.msg.JointValue()
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        # тип объекта - левый палец
        jv.joint_uri = "KawasakiGripper1"
        # размерность
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_POSITION)
        # значение делим на 1000, так как масимальное смещение гриппера 110 мм
        jv.value = leftG / 1000
        # добавляем объект в сообщение
        msg.positions.append(jv)
        # делаем тоже самое для правого пальца
        jv = brics_actuator.msg.JointValue()
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        jv.joint_uri = "KawasakiGripper2"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_POSITION)
        jv.value = rightG / 1000
        msg.positions.append(jv)
        # публикуем сообщение в топике
        self.positionGripperPub.publish(msg)
        print(msg)
        # делаем задержку
        rospy.sleep(1)

    # управляем скоростью гриппера - тоже самое, что и setGripperPositions
    def setGripperVelocities(self, leftG, rightG):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = []
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "KawasakiGripper1"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_VELOCITY)
        jv.value = leftG / 1000
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        msg.velocities.append(jv)
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "KawasakiGripper2"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_VELOCITY)
        jv.value = rightG / 1000
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        msg.velocities.append(jv)
        self.velocityGripperPub.publish(msg)
        rospy.sleep(1)

    # управляем силой гриппера - тоже самое, что и setGripperPositions
    def setGripperTorques(self, leftG, rightG):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = []
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "KawasakiGripper1"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_TORQUE)
        jv.value = leftG
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        msg.torques.append(jv)
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "KawasakiGripper2"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_TORQUE)
        jv.value = rightG
        # получаем текущее время
        jv.timeStamp = rospy.Time.now()
        msg.torques.append(jv)
        self.forceGripperPub.publish(msg)
        rospy.sleep(1)

    # задаём положения всех джоинтов
    def setJointPositions(self, joints):
        msg = brics_actuator.msg.JointPositions()
        msg.positions = []
        # в цикле создаём объекты для сообщения, подробнее смотри setGripperPositions
        for i in range(5):
            jv = self.generateJoinVal(i + 1, joints[i], self.TYPE_JOINT_POSITIONS)
            msg.positions.append(jv)

        self.positionArmPub.publish(msg)
        # print (msg)
        rospy.sleep(1)

    # тоже самое, что и setJointPositions, но управляем только одним джоинтом
    def setJointPosition(self, joint_num, value):
        # проверяем, что джоинт подходит
        if not joint_num in range(1, 5):
            rospy.logerror("Звено с номером " + str(joint_num) + " не определено")
            return
        msg = brics_actuator.msg.JointPositions()
        msg.positions = [self.generateJoinVal(joint_num, value, self.TYPE_JOINT_POSITIONS)]
        self.positionArmPub.publish(msg)
        rospy.sleep(1)

    # задаём моменты всех джоинтов подробнее смотри setJointPositions
    def setJointTorques(self, joints):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = []
        for i in range(5):
            jv = self.generateJoinVal(i + 1, joints[i], self.TYPE_JOINT_TORQUES)
            msg.torques.append(jv)
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    # задаём момент конкретному джоинту подробнее смотри setJointPosition
    def setJointTorque(self, joint_num, value):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = [self.generateJoinVal(joint_num, value, self.TYPE_JOINT_TORQUES)]
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    # задаём скорости всех джоинтов подробнее смотри setJointPositions
    def setJointVelocity(self, joint_num, value):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = [self.generateJoinVal(joint_num, value, self.TYPE_JOINT_VELOCITIES)]
        self.velocityArmPub.publish(msg)
        rospy.sleep(1)

    # задаём скорость конкретному джоинту подробнее смотри setJointPosition
    def setJointVelocities(self, joints):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = []
        for i in range(5):
            jv = self.generateJoinVal(i + 1, joints[i], self.TYPE_JOINT_VELOCITIES)
            msg.velocities.append(jv)
        self.velocityArmPub.publish(msg)
        rospy.sleep(1)
