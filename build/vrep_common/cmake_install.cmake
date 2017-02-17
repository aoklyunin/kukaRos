# Install script for directory: /home/teacher/PycharmProjects/kukaRos/src/vrep_common

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/teacher/PycharmProjects/kukaRos/install")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common/msg" TYPE FILE FILES
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/ForceSensorData.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/JointSetStateData.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/ObjectGroupData.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/ProximitySensorData.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/VisionSensorData.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/VisionSensorDepthBuff.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/VrepInfo.msg"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg/ScriptFunctionCallData.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common/srv" TYPE FILE FILES
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAddStatusbarMessage.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetDialogInput.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetUIEventButton.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetJointState.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAppendStringSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetDialogResult.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetUIHandle.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetJointTargetPosition.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAuxiliaryConsoleClose.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetDistanceHandle.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetUISlider.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetJointTargetVelocity.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAuxiliaryConsoleOpen.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetFloatingParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetVisionSensorDepthBuffer.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetModelProperty.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAuxiliaryConsolePrint.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetFloatSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetVisionSensorImage.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectFloatParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosAuxiliaryConsoleShow.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetInfo.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosLoadModel.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectIntParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosBreakForceSensor.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetIntegerParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosLoadScene.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectParent.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosClearFloatSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetIntegerSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosLoadUI.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectPose.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosClearIntegerSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetJointMatrix.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosPauseSimulation.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectPosition.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosClearStringSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetJointState.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosReadCollision.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectQuaternion.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosCloseScene.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetLastErrors.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosReadDistance.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetObjectSelection.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosCopyPasteObjects.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetModelProperty.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosReadForceSensor.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetSphericalJointMatrix.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosCreateDummy.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectChild.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosReadProximitySensor.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetStringSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosDisablePublisher.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectFloatParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosReadVisionSensor.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetUIButtonLabel.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosDisableSubscriber.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectGroupData.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosRemoveObject.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetUIButtonProperty.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosDisplayDialog.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectHandle.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosRemoveUI.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetUISlider.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosEnablePublisher.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectIntParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetArrayParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetVisionSensorImage.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosEnableSubscriber.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectParent.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetBooleanParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosStartSimulation.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosEndDialog.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectPose.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetFloatingParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosStopSimulation.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosEraseFile.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjectSelection.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetFloatSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSynchronous.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetAndClearStringSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetObjects.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetIntegerParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSynchronousTrigger.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetArrayParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetStringParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetIntegerSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosTransferFile.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetBooleanParameter.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetStringSignal.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetJointForce.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosRemoveModel.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetCollisionHandle.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetUIButtonProperty.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosSetJointPosition.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosGetCollectionHandle.srv"
    "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/srv/simRosCallScriptFunction.srv"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common/cmake" TYPE FILE FILES "/home/teacher/PycharmProjects/kukaRos/build/vrep_common/catkin_generated/installspace/vrep_common-msg-paths.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/teacher/PycharmProjects/kukaRos/devel/include/vrep_common")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/teacher/PycharmProjects/kukaRos/devel/share/common-lisp/ros/vrep_common")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/teacher/PycharmProjects/kukaRos/devel/lib/python2.7/dist-packages/vrep_common")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/teacher/PycharmProjects/kukaRos/devel/lib/python2.7/dist-packages/vrep_common")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/teacher/PycharmProjects/kukaRos/build/vrep_common/catkin_generated/installspace/vrep_common.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common/cmake" TYPE FILE FILES "/home/teacher/PycharmProjects/kukaRos/build/vrep_common/catkin_generated/installspace/vrep_common-msg-extras.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common/cmake" TYPE FILE FILES
    "/home/teacher/PycharmProjects/kukaRos/build/vrep_common/catkin_generated/installspace/vrep_commonConfig.cmake"
    "/home/teacher/PycharmProjects/kukaRos/build/vrep_common/catkin_generated/installspace/vrep_commonConfig-version.cmake"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vrep_common" TYPE FILE FILES "/home/teacher/PycharmProjects/kukaRos/src/vrep_common/package.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

