// Generated by gencpp from file vrep_common/simRosCloseScene.msg
// DO NOT EDIT!


#ifndef VREP_COMMON_MESSAGE_SIMROSCLOSESCENE_H
#define VREP_COMMON_MESSAGE_SIMROSCLOSESCENE_H

#include <ros/service_traits.h>


#include <vrep_common/simRosCloseSceneRequest.h>
#include <vrep_common/simRosCloseSceneResponse.h>


namespace vrep_common
{

struct simRosCloseScene
{

typedef simRosCloseSceneRequest Request;
typedef simRosCloseSceneResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct simRosCloseScene
} // namespace vrep_common


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::vrep_common::simRosCloseScene > {
  static const char* value()
  {
    return "034a8e20d6a306665e3a5b340fab3f09";
  }

  static const char* value(const ::vrep_common::simRosCloseScene&) { return value(); }
};

template<>
struct DataType< ::vrep_common::simRosCloseScene > {
  static const char* value()
  {
    return "vrep_common/simRosCloseScene";
  }

  static const char* value(const ::vrep_common::simRosCloseScene&) { return value(); }
};


// service_traits::MD5Sum< ::vrep_common::simRosCloseSceneRequest> should match 
// service_traits::MD5Sum< ::vrep_common::simRosCloseScene > 
template<>
struct MD5Sum< ::vrep_common::simRosCloseSceneRequest>
{
  static const char* value()
  {
    return MD5Sum< ::vrep_common::simRosCloseScene >::value();
  }
  static const char* value(const ::vrep_common::simRosCloseSceneRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::vrep_common::simRosCloseSceneRequest> should match 
// service_traits::DataType< ::vrep_common::simRosCloseScene > 
template<>
struct DataType< ::vrep_common::simRosCloseSceneRequest>
{
  static const char* value()
  {
    return DataType< ::vrep_common::simRosCloseScene >::value();
  }
  static const char* value(const ::vrep_common::simRosCloseSceneRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::vrep_common::simRosCloseSceneResponse> should match 
// service_traits::MD5Sum< ::vrep_common::simRosCloseScene > 
template<>
struct MD5Sum< ::vrep_common::simRosCloseSceneResponse>
{
  static const char* value()
  {
    return MD5Sum< ::vrep_common::simRosCloseScene >::value();
  }
  static const char* value(const ::vrep_common::simRosCloseSceneResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::vrep_common::simRosCloseSceneResponse> should match 
// service_traits::DataType< ::vrep_common::simRosCloseScene > 
template<>
struct DataType< ::vrep_common::simRosCloseSceneResponse>
{
  static const char* value()
  {
    return DataType< ::vrep_common::simRosCloseScene >::value();
  }
  static const char* value(const ::vrep_common::simRosCloseSceneResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // VREP_COMMON_MESSAGE_SIMROSCLOSESCENE_H
