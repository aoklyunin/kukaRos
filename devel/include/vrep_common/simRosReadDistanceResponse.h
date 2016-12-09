// Generated by gencpp from file vrep_common/simRosReadDistanceResponse.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSREADDISTANCERESPONSE_H
#define VREP_COMMON_MESSAGE_SIMROSREADDISTANCERESPONSE_H


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
struct simRosReadDistanceResponse_
{
  typedef simRosReadDistanceResponse_<ContainerAllocator> Type;

  simRosReadDistanceResponse_()
    : result(0)
    , distance(0.0)  {
    }
  simRosReadDistanceResponse_(const ContainerAllocator& _alloc)
    : result(0)
    , distance(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _result_type;
  _result_type result;

   typedef float _distance_type;
  _distance_type distance;




  typedef boost::shared_ptr< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> const> ConstPtr;

}; // struct simRosReadDistanceResponse_

typedef ::vrep_common::simRosReadDistanceResponse_<std::allocator<void> > simRosReadDistanceResponse;

typedef boost::shared_ptr< ::vrep_common::simRosReadDistanceResponse > simRosReadDistanceResponsePtr;
typedef boost::shared_ptr< ::vrep_common::simRosReadDistanceResponse const> simRosReadDistanceResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5d04a72250553841153bb8b6a483569b";
  }

  static const char* value(const ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5d04a72250553841ULL;
  static const uint64_t static_value2 = 0x153bb8b6a483569bULL;
};

template<class ContainerAllocator>
struct DataType< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vrep_common/simRosReadDistanceResponse";
  }

  static const char* value(const ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 result\n\
float32 distance\n\
";
  }

  static const char* value(const ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
      stream.next(m.distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct simRosReadDistanceResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vrep_common::simRosReadDistanceResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<int32_t>::stream(s, indent + "  ", v.result);
    s << indent << "distance: ";
    Printer<float>::stream(s, indent + "  ", v.distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSREADDISTANCERESPONSE_H
