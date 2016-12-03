#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib; roslib.load_manifest('kuka_simple_control')
import math
import rospy
import brics_actuator.msg
import geometry_msgs.msg
import sensor_msgs.msg

# ToDO
# проверка, что задание по положению джоинтов не выходят за границы
# обработка положений joinStateSubscriber
# подумать, как останавливать суправление по силам, если моменты обнулить, то робот прото упадёт
class KukaController():

    maxArmVelocity = math.radians(90)

    jointsRange = [
        [math.radians(169), math.radians(-169)],
        [math.radians(90), math.radians(-65)],
        [math.radians(146), math.radians(-151)],
        [math.radians(102.5), math.radians(-102.5)],
        [math.radians(167.5), math.radians(-167.5)],
    ]

    gripperRange = [0.0,0.011499]

    TYPE_POSITIONS = 0
    TYPE_VELOCITIES = 1
    TYPE_TORQUES = 2
    TYPE_GRIPPER_POSITION = 3
    TYPE_GRIPPER_VELOCITY = 4
    TYPE_GRIPPER_TORQUE = 5

    jointState = sensor_msgs.msg.JointState()

    def jointStateCallback(self,data):
     #   print(data)
        self.jointState = data
        pass

    #def createPosMsg(self):
    def __init__(self):
        # Give the node a name
        self.node_name = "goto_searchposition"
        rospy.init_node(self.node_name)
        # Set rospy to execute a shutdown function when exiting
        rospy.on_shutdown(self.shutdown)
        self.positionArmPub = rospy.Publisher("/arm_controller/position_command", brics_actuator.msg.JointPositions, queue_size=1)
        self.torqueArmPub = rospy.Publisher("/arm_controller/force_command", brics_actuator.msg.JointTorques, queue_size=1)
        self.velocityArmPub = rospy.Publisher("/arm_controller/velocity_command", brics_actuator.msg.JointVelocities, queue_size=1)
        self.cartVelPub = rospy.Publisher("/cmd_vel", geometry_msgs.msg.Twist, queue_size=1)
        self.positionGripperPub = rospy.Publisher("/arm_controller/position_command", brics_actuator.msg.JointPositions,queue_size=1)
        self.forceGripperPub = rospy.Publisher("/arm_controller/force_command", brics_actuator.msg.JointTorques,queue_size=1)
        self.velocityGripperPub = rospy.Publisher("/arm_controller/velocity_command", brics_actuator.msg.JointVelocities,queue_size=1)
        self.jointStateSubscriber = rospy.Subscriber("/joint_states", sensor_msgs.msg.JointState, self.jointStateCallback)

        rospy.sleep(1)
        rospy.loginfo("Kuka created")

    def getUnitValue(self,tp):
        if tp == self.TYPE_POSITIONS:
            return "rad"
        elif tp == self.TYPE_VELOCITIES:
            return "s^-1 rad"
        elif tp == self.TYPE_TORQUES:
            return "m^2 kg s^-2 rad^-1 m^2 kg s^-2 rad^-1 "
        elif tp == self.TYPE_GRIPPER_POSITION:
            return  "m"
        elif tp == self.TYPE_GRIPPER_VELOCITY:
            return "s^-1 m"
        elif tp == self.TYPE_GRIPPER_TORQUE:
            return  "m^2 kg s^-2 m^-1 m^2 kg s^-2 m^-1 "
        else:
            return None

    def generateJoinVal(self, joint_num, val, tp):
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "arm_joint_" + str(joint_num)
        jv.unit = self.getUnitValue(tp)
        jv.value = val
        return jv

    def setVel(self,x,y,z):
        msg = geometry_msgs.msg.Twist()
        msg.linear.x = x
        msg.linear.y = y
        msg.angular.z = z
        self.cartVelPub.publish(msg)
        rospy.sleep(1)

    # в миллиметрах
    def setGripperPositions(self, leftG, rightG):
        msg = brics_actuator.msg.JointPositions()
        msg.positions = []
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_l"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_POSITION)
        jv.value = leftG/1000
        msg.positions.append(jv)
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_r"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_POSITION)
        jv.value = rightG/1000
        msg.positions.append(jv)
        self.positionGripperPub.publish(msg)
        rospy.sleep(1)

    # в миллиметрах
    def setGripperVelocities(self, leftG, rightG):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = []
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_l"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_VELOCITY)
        jv.value = leftG/1000
        msg.velocities.append(jv)
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_r"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_VELOCITY)
        jv.value = rightG/1000
        msg.velocities.append(jv)
        self.velocityGripperPub.publish(msg)
        rospy.sleep(1)

    def setGripperTorques(self, leftG, rightG):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = []
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_l"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_TORQUE)
        jv.value = leftG
        msg.torques.append(jv)
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "gripper_finger_joint_r"
        jv.unit = self.getUnitValue(self.TYPE_GRIPPER_TORQUE)
        jv.value = rightG
        msg.torques.append(jv)
        self.forceGripperPub.publish(msg)
        rospy.sleep(1)

    def setJointPositions(self,joints):
        msg = brics_actuator.msg.JointPositions()
        msg.positions = []
        for i in range(5):
            jv = self.generateJoinVal(i+1,joints[i],self.TYPE_POSITIONS)
            msg.positions.append(jv)
        self.positionArmPub.publish(msg)
        rospy.sleep(1)

    def setJointPosition(self,joint_num,value):
        if not joint_num in range(1,5):
            rospy.logerror("Звено с номером "+str(joint_num)+" не определено")
            return
        msg = brics_actuator.msg.JointPositions()
        msg.positions = [self.generateJoinVal(joint_num,value,self.TYPE_POSITIONS)]
        self.positionArmPub.publish(msg)
        rospy.sleep(1)

    def setJointTorques(self,joints):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = []
        for i in range(5):
            jv = self.generateJoinVal(i + 1, joints[i], self.TYPE_TORQUES)
            msg.torques.append(jv)
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    def setJointTorque(self, joint_num, value):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = [self.generateJoinVal(joint_num, value, self.TYPE_TORQUES)]
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    def setJointVelocity(self,joint_num,value):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = [self.generateJoinVal(joint_num, value, self.TYPE_VELOCITIES)]
        self.velocityArmPub.publish(msg)
        rospy.sleep(1)

    def setJointVelocities(self,joints):
        msg = brics_actuator.msg.JointVelocities()
        msg.velocities = []
        for i in range(5):
            jv = self.generateJoinVal(i + 1, joints[i], self.TYPE_VELOCITIES)
            msg.velocities.append(jv)
        self.velocityArmPub.publish(msg)
        rospy.sleep(1)

    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")

if __name__ == '__main__':
   # kuka = KukaController()
   # kuka.setJointTorque(1,100)

    pass
   # rospy.spin()
