// Generated by gencpp from file vrep_common/simRosGetObjectParentResponse.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSGETOBJECTPARENTRESPONSE_H
#define VREP_COMMON_MESSAGE_SIMROSGETOBJECTPARENTRESPONSE_H


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
struct simRosGetObjectParentResponse_
{
  typedef simRosGetObjectParentResponse_<ContainerAllocator> Type;

  simRosGetObjectParentResponse_()
    : parentHandle(0)  {
    }
  simRosGetObjectParentResponse_(const ContainerAllocator& _alloc)
    : parentHandle(0)  {
  (void)_alloc;
    }



   typedef int32_t _parentHandle_type;
  _parentHandle_type parentHandle;




  typedef boost::shared_ptr< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> const> ConstPtr;

}; // struct simRosGetObjectParentResponse_

typedef ::vrep_common::simRosGetObjectParentResponse_<std::allocator<void> > simRosGetObjectParentResponse;

typedef boost::shared_ptr< ::vrep_common::simRosGetObjectParentResponse > simRosGetObjectParentResponsePtr;
typedef boost::shared_ptr< ::vrep_common::simRosGetObjectParentResponse const> simRosGetObjectParentResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vrep_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'vrep_common': ['/home/alex/RosProgramming/kuka/src/vrep_common/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3297095044ad4bf50ba768911050d931";
  }

  static const char* value(const ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3297095044ad4bf5ULL;
  static const uint64_t static_value2 = 0x0ba768911050d931ULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosGetObjectParentResponse";
  }

  static const char* value(const ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 parentHandle\n\
\n\
";
  }

  static const char* value(const ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.parentHandle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct simRosGetObjectParentResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosGetObjectParentResponse_<ContainerAllocator>& v)
  {
    s << indent << "parentHandle: ";
    Printer<int32_t>::stream(s, indent + "  ", v.parentHandle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSGETOBJECTPARENTRESPONSE_H
