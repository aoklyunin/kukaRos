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
class KukaController():

    maxArmVelocity = math.radians(90)
    jointsRange = [
        [math.radians(169), math.radians(-169)],
        [math.radians(90), math.radians(-65)],
        [math.radians(146), math.radians(-151)],
        [math.radians(102.5), math.radians(-102.5)],
        [math.radians(167.5), math.radians(-167.5)],
    ]
    TYPE_POSITIONS = 0
    TYPE_VELOCITIES = 1
    TYPE_TORQUES = 2

    def jointStateCallback(self,data):
        #rospy.loginfo(rospy.get_name() + "I heard %s", str(data))
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
        self.cartVel = rospy.Publisher("/cmd_vel", geometry_msgs.msg.Twist, queue_size=1)
        self.positionGripperPub = rospy.Publisher("/arm_controller/position_command", brics_actuator.msg.JointPositions,queue_size=1)
        self.forceGripperPub = rospy.Publisher("/arm_controller/force_command", brics_actuator.msg.JointTorques,queue_size=1)
        self.velocityGripperPub = rospy.Publisher("/arm_controller/velocity_command", brics_actuator.msg.JointVelocities,queue_size=1)
        self.joinStateSubscriber = rospy.Subscriber("/joint_states", sensor_msgs.msg.JointState, self.jointStateCallback)
        rospy.sleep(1)
        rospy.loginfo("Kuka created")

    def generateJoinVal(self, joint_num, val, tp):
        jv = brics_actuator.msg.JointValue()
        jv = brics_actuator.msg.JointValue()
        jv.joint_uri = "arm_joint_" + str(joint_num)
        if tp == self.TYPE_POSITIONS:
            jv.unit = "rad"
        elif tp == self.TYPE_VELOCITIES:
            jv.unit = "s^-1 rad"
        elif tp == self.TYPE_TORQUES:
            jv.unit = "Nm"
        jv.value = val
        return jv

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
            msg.positions.append(jv)
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    def setJointTorque(self,joint_num,value):
        msg = brics_actuator.msg.JointTorques()
        msg.torques = [self.generateJoinVal(joint_num, value, self.TYPE_TORQUES)]
        self.torqueArmPub.publish(msg)
        rospy.sleep(1)

    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")

if __name__ == '__main__':
    kuka = KukaController()
    joint = [0,0,0,0,-0.5]
    kuka.setJointPositions(joint)
    rospy.sleep(2)
    kuka.setJointTorque(1,10)


    rospy.spin()
