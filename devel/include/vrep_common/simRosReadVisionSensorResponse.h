// Generated by gencpp from file vrep_common/simRosReadVisionSensorResponse.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSREADVISIONSENSORRESPONSE_H
#define VREP_COMMON_MESSAGE_SIMROSREADVISIONSENSORRESPONSE_H


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
struct simRosReadVisionSensorResponse_
{
  typedef simRosReadVisionSensorResponse_<ContainerAllocator> Type;

  simRosReadVisionSensorResponse_()
    : result(0)
    , packetData()
    , packetSizes()  {
    }
  simRosReadVisionSensorResponse_(const ContainerAllocator& _alloc)
    : result(0)
    , packetData(_alloc)
    , packetSizes(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _result_type;
  _result_type result;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _packetData_type;
  _packetData_type packetData;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _packetSizes_type;
  _packetSizes_type packetSizes;




  typedef boost::shared_ptr< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> const> ConstPtr;

}; // struct simRosReadVisionSensorResponse_

typedef ::vrep_common::simRosReadVisionSensorResponse_<std::allocator<void> > simRosReadVisionSensorResponse;

typedef boost::shared_ptr< ::vrep_common::simRosReadVisionSensorResponse > simRosReadVisionSensorResponsePtr;
typedef boost::shared_ptr< ::vrep_common::simRosReadVisionSensorResponse const> simRosReadVisionSensorResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vrep_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'vrep_common': ['/home/alex/RosProgramming/kuka/src/vrep_common/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a46558cdf2ec9ef5fe9ba6ee4605c6bc";
  }

  static const char* value(const ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa46558cdf2ec9ef5ULL;
  static const uint64_t static_value2 = 0xfe9ba6ee4605c6bcULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosReadVisionSensorResponse";
  }

  static const char* value(const ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 result\n\
float32[] packetData\n\
int32[] packetSizes\n\
\n\
";
  }

  static const char* value(const ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
      stream.next(m.packetData);
      stream.next(m.packetSizes);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct simRosReadVisionSensorResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosReadVisionSensorResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<int32_t>::stream(s, indent + "  ", v.result);
    s << indent << "packetData[]" << std::endl;
    for (size_t i = 0; i < v.packetData.size(); ++i)
    {
      s << indent << "  packetData[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.packetData[i]);
    }
    s << indent << "packetSizes[]" << std::endl;
    for (size_t i = 0; i < v.packetSizes.size(); ++i)
    {
      s << indent << "  packetSizes[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.packetSizes[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSREADVISIONSENSORRESPONSE_H
