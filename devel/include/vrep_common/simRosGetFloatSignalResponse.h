// Generated by gencpp from file vrep_common/simRosGetFloatSignalResponse.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSGETFLOATSIGNALRESPONSE_H
#define VREP_COMMON_MESSAGE_SIMROSGETFLOATSIGNALRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace vrep_common
{
template <class ContainerAllocator>
struct simRosGetFloatSignalResponse_
{
  typedef simRosGetFloatSignalResponse_<ContainerAllocator> Type;

  simRosGetFloatSignalResponse_()
    : result(0)
    , signalValue(0.0)  {
    }
  simRosGetFloatSignalResponse_(const ContainerAllocator& _alloc)
    : result(0)
    , signalValue(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _result_type;
  _result_type result;

   typedef float _signalValue_type;
  _signalValue_type signalValue;




  typedef boost::shared_ptr< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> const> ConstPtr;

}; // struct simRosGetFloatSignalResponse_

typedef ::vrep_common::simRosGetFloatSignalResponse_<std::allocator<void> > simRosGetFloatSignalResponse;

typedef boost::shared_ptr< ::vrep_common::simRosGetFloatSignalResponse > simRosGetFloatSignalResponsePtr;
typedef boost::shared_ptr< ::vrep_common::simRosGetFloatSignalResponse const> simRosGetFloatSignalResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vrep_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'vrep_common': ['/home/teacher/PycharmProjects/kukaRos/src/vrep_common/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d8f2b92b89d5cf88cbffea18b9ddcc7d";
  }

  static const char* value(const ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd8f2b92b89d5cf88ULL;
  static const uint64_t static_value2 = 0xcbffea18b9ddcc7dULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosGetFloatSignalResponse";
  }

  static const char* value(const ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 result\n\
float32 signalValue\n\
\n\
";
  }

  static const char* value(const ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
      stream.next(m.signalValue);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct simRosGetFloatSignalResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosGetFloatSignalResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<int32_t>::stream(s, indent + "  ", v.result);
    s << indent << "signalValue: ";
    Printer<float>::stream(s, indent + "  ", v.signalValue);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSGETFLOATSIGNALRESPONSE_H
