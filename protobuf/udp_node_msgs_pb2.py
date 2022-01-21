# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udp-node-msgs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import world_pb2 as world__pb2
import profile_pb2 as profile__pb2
import per_session_info_pb2 as per__session__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13udp-node-msgs.proto\x1a\x0bworld.proto\x1a\rprofile.proto\x1a\x16per-session-info.proto\"X\n\x10\x44\x65\x63ompiledPlayer\x12 \n\x0eplayer_profile\x18\x01 \x01(\x0b\x32\x08.Profile\x12\"\n\x0cplayer_state\x18\x02 \x01(\x0b\x32\x0c.PlayerState\"\xe5\x04\n\x0bPlayerState\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tworldTime\x18\x02 \x01(\x03\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x10\n\x08roadTime\x18\x04 \x02(\x05\x12\x0c\n\x04laps\x18\x05 \x01(\x05\x12\r\n\x05speed\x18\x06 \x01(\r\x12\n\n\x02\x66\x37\x18\x07 \x01(\r\x12\x14\n\x0croadPosition\x18\x08 \x01(\x05\x12\x12\n\ncadenceUHz\x18\t \x01(\x05\x12\x0b\n\x03\x66\x31\x30\x18\n \x01(\x05\x12\x11\n\theartrate\x18\x0b \x01(\x05\x12\r\n\x05power\x18\x0c \x01(\x05\x12\x0f\n\x07heading\x18\r \x01(\r\x12\x0c\n\x04lean\x18\x0e \x01(\x03\x12\x10\n\x08\x63limbing\x18\x0f \x01(\x05\x12\x0c\n\x04time\x18\x10 \x01(\x05\x12\x0b\n\x03\x66\x31\x37\x18\x11 \x01(\x05\x12\x0b\n\x03\x66\x31\x38\x18\x12 \x01(\r\x12\x0b\n\x03\x66\x31\x39\x18\x13 \x01(\r\x12\x0b\n\x03\x66\x32\x30\x18\x14 \x01(\r\x12\x10\n\x08progress\x18\x15 \x01(\r\x12\x17\n\x0f\x63ustomisationId\x18\x16 \x01(\x03\x12\x14\n\x0cjustWatching\x18\x17 \x01(\x08\x12\x10\n\x08\x63\x61lories\x18\x18 \x01(\x05\x12\t\n\x01x\x18\x19 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x1a \x01(\x02\x12\t\n\x01y\x18\x1b \x01(\x02\x12\x17\n\x0fwatchingRiderId\x18\x1c \x01(\x03\x12\x0f\n\x07groupId\x18\x1d \x01(\x03\x12\r\n\x05sport\x18\x1f \x01(\x05\x12\x0b\n\x03\x66\x33\x32\x18  \x01(\x02\x12\x0b\n\x03\x66\x33\x33\x18! \x01(\r\x12\x0b\n\x03\x66\x33\x34\x18\" \x01(\x02\x12\r\n\x05world\x18# \x01(\x05\x12\x0b\n\x03\x66\x33\x36\x18$ \x01(\r\x12\x0b\n\x03\x66\x33\x37\x18% \x01(\r\x12\x0b\n\x03\x66\x33\x38\x18& \x01(\x08\x12\r\n\x05route\x18\' \x01(\r\"\x98\x02\n\x0e\x43lientToServer\x12\x11\n\tconnected\x18\x01 \x02(\x03\x12\x11\n\tplayer_id\x18\x02 \x02(\x03\x12\x12\n\nworld_time\x18\x03 \x02(\x03\x12\r\n\x05seqno\x18\x04 \x02(\x03\x12\n\n\x02\x66\x35\x18\x05 \x01(\x03\x12\n\n\x02\x66\x36\x18\x06 \x01(\x03\x12\x1b\n\x05state\x18\x07 \x02(\x0b\x32\x0c.PlayerState\x12\n\n\x02\x66\x38\x18\x08 \x02(\x03\x12\n\n\x02\x66\x39\x18\t \x01(\x03\x12\x13\n\x0blast_update\x18\n \x02(\x03\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\x03\x12\x1a\n\x12last_player_update\x18\x0c \x02(\x03\x12\x0b\n\x03\x66\x31\x33\x18\r \x01(\x03\x12\x0b\n\x03\x66\x31\x34\x18\x0e \x01(\x08\x12\x0b\n\x03\x66\x31\x35\x18\x0f \x03(\x03\x12\x0b\n\x03\x66\x31\x36\x18\x10 \x03(\x03\"?\n\rPlayerSummary\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\"\x8f\x01\n\x0fPlayerSummaries\x12\n\n\x02\x66\x31\x18\x01 \x01(\x11\x12\n\n\x02\x66\x32\x18\x02 \x01(\x11\x12\n\n\x02\x66\x33\x18\x03 \x01(\x11\x12\n\n\x02\x66\x34\x18\x04 \x01(\x11\x12\n\n\x02\x66\x35\x18\x05 \x01(\x05\x12\n\n\x02\x66\x36\x18\x06 \x01(\x05\x12\n\n\x02\x66\x37\x18\x07 \x01(\x05\x12(\n\x10player_summaries\x18\x08 \x03(\x0b\x32\x0e.PlayerSummary\"X\n\x0cRelayAddress\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\n\n\x02\x66\x35\x18\x05 \x01(\x02\x12\n\n\x02\x66\x36\x18\x06 \x01(\x02\"W\n\tUdpConfig\x12&\n\x0frelay_addresses\x18\x01 \x03(\x0b\x32\r.RelayAddress\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\"]\n\x11RelayAddressesVOD\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12$\n\rrelay_address\x18\x03 \x03(\x0b\x32\r.RelayAddress\x12\n\n\x02\x66\x34\x18\x04 \x01(\x08\"w\n\x0cUdpConfigVOD\x12+\n\x0frelay_addresses\x18\x01 \x03(\x0b\x32\x12.RelayAddressesVOD\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x03\x12\n\n\x02\x66\x34\x18\x04 \x01(\x03\x12\n\n\x02\x66\x35\x18\x05 \x01(\x02\x12\n\n\x02\x66\x36\x18\x06 \x01(\x02\"9\n\x13PlayerRouteDistance\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x02\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\"\xfd\x01\n\x17\x45ventSubgroupPlacements\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12(\n\nplayer_rd1\x18\x02 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd2\x18\x03 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd3\x18\x04 \x03(\x0b\x32\x14.PlayerRouteDistance\x12(\n\nplayer_rd4\x18\x05 \x03(\x0b\x32\x14.PlayerRouteDistance\x12\n\n\x02\x66\x36\x18\x06 \x01(\x05\x12\n\n\x02\x66\x37\x18\x07 \x01(\x05\x12\n\n\x02\x66\x38\x18\x08 \x01(\x05\x12\n\n\x02\x66\x39\x18\t \x01(\x02\"\xe4\x04\n\x0eServerToClient\x12\n\n\x02\x66\x31\x18\x01 \x02(\x03\x12\x11\n\tplayer_id\x18\x02 \x02(\x03\x12\x12\n\nworld_time\x18\x03 \x02(\x03\x12\r\n\x05seqno\x18\x04 \x01(\x05\x12\n\n\x02\x66\x35\x18\x05 \x01(\x05\x12\x1c\n\x06states\x18\x08 \x03(\x0b\x32\x0c.PlayerState\x12 \n\x07updates\x18\t \x03(\x0b\x32\x0f.WorldAttribute\x12\x0b\n\x03\x66\x31\x30\x18\n \x01(\x03\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\x08\x12\x0b\n\x03\x66\x31\x32\x18\x0c \x01(\t\x12\x0b\n\x03\x66\x31\x33\x18\r \x01(\x03\x12\x0b\n\x03\x66\x31\x34\x18\x0e \x01(\x05\x12\x0b\n\x03\x66\x31\x35\x18\x0f \x01(\x05\x12\x0b\n\x03\x66\x31\x36\x18\x10 \x01(\x05\x12\x0b\n\x03\x66\x31\x37\x18\x11 \x01(\x03\x12\x10\n\x08num_msgs\x18\x12 \x01(\x05\x12\x0e\n\x06msgnum\x18\x13 \x01(\x05\x12\x0b\n\x03\x66\x32\x30\x18\x14 \x01(\x08\x12*\n\x10player_summaries\x18\x15 \x01(\x0b\x32\x10.PlayerSummaries\x12\x30\n\x0e\x65v_subgroup_ps\x18\x17 \x01(\x0b\x32\x18.EventSubgroupPlacements\x12\x1e\n\nudp_config\x18\x18 \x01(\x0b\x32\n.UdpConfig\x12\'\n\x10udp_config_vod_1\x18\x19 \x01(\x0b\x32\r.UdpConfigVOD\x12\x0b\n\x03\x66\x32\x36\x18\x1a \x01(\x05\x12\'\n\x10udp_config_vod_2\x18\x1b \x01(\x0b\x32\r.UdpConfigVOD\x12#\n\rplayer_states\x18\x1c \x03(\x0b\x32\x0c.PlayerState\x12\x1e\n\ntcp_config\x18\x1d \x01(\x0b\x32\n.TcpConfig\x12\x0b\n\x03\x66\x33\x30\x18\x1e \x03(\x12\"8\n\x05Ghost\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\x12\x1c\n\x06states\x18\x02 \x03(\x0b\x32\x0c.PlayerState\" \n\x06Ghosts\x12\x16\n\x06ghosts\x18\x01 \x03(\x0b\x32\x06.Ghost\"\xcb\x01\n\x0cPlayerUpdate\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x02(\x05\x12\x0f\n\x07payload\x18\x04 \x02(\x0c\x12\x13\n\x0bworld_time1\x18\x05 \x01(\x03\x12\t\n\x01x\x18\x06 \x01(\x03\x12\x10\n\x08\x61ltitude\x18\x07 \x01(\x03\x12\t\n\x01y\x18\x08 \x01(\x03\x12\x13\n\x0bworld_time2\x18\t \x01(\x03\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\x03\x12\x0b\n\x03\x66\x31\x32\x18\x0c \x01(\x03\x12\x0b\n\x03\x66\x31\x34\x18\x0e \x01(\x03\x12\x0b\n\x03\x66\x31\x35\x18\x0f \x01(\x03\"\xb2\x01\n\x0b\x43hatMessage\x12\x10\n\x08rider_id\x18\x01 \x02(\x05\x12\x13\n\x0bto_rider_id\x18\x02 \x02(\x05\x12\n\n\x02\x66\x33\x18\x03 \x02(\x05\x12\x11\n\tfirstName\x18\x04 \x02(\t\x12\x10\n\x08lastName\x18\x05 \x02(\t\x12\x0f\n\x07message\x18\x06 \x02(\t\x12\x0e\n\x06\x61vatar\x18\x07 \x01(\t\x12\x13\n\x0b\x63ountryCode\x18\x08 \x02(\x05\x12\x15\n\reventSubgroup\x18\x0b \x01(\x05\"i\n\x06RideOn\x12\x10\n\x08rider_id\x18\x01 \x02(\x03\x12\x13\n\x0bto_rider_id\x18\x02 \x02(\x03\x12\x11\n\tfirstName\x18\x03 \x02(\t\x12\x10\n\x08lastName\x18\x04 \x02(\t\x12\x13\n\x0b\x63ountryCode\x18\x05 \x02(\x05\"\xa8\x02\n\x0fSegmentComplete\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\x10\n\x08rider_id\x18\x02 \x02(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x03\x12\x12\n\nsegment_id\x18\x05 \x01(\x03\x12\n\n\x02\x66\x36\x18\x06 \x01(\x03\x12\x12\n\nfirst_name\x18\x07 \x01(\t\x12\x11\n\tlast_name\x18\x08 \x01(\t\x12\x12\n\nworld_time\x18\t \x01(\x03\x12\x14\n\x0cmilliseconds\x18\x0b \x01(\x03\x12\x0b\n\x03\x66\x31\x32\x18\x0c \x01(\x05\x12\x17\n\x0fweight_in_grams\x18\r \x01(\x05\x12\x0b\n\x03\x66\x31\x34\x18\x0e \x01(\x05\x12\x11\n\tavg_power\x18\x0f \x01(\x05\x12\x0b\n\x03\x66\x31\x36\x18\x10 \x01(\x05\x12\x0e\n\x06\x66\x37\x64\x61te\x18\x11 \x01(\t\x12\x0b\n\x03\x66\x31\x39\x18\x13 \x01(\x05')



_DECOMPILEDPLAYER = DESCRIPTOR.message_types_by_name['DecompiledPlayer']
_PLAYERSTATE = DESCRIPTOR.message_types_by_name['PlayerState']
_CLIENTTOSERVER = DESCRIPTOR.message_types_by_name['ClientToServer']
_PLAYERSUMMARY = DESCRIPTOR.message_types_by_name['PlayerSummary']
_PLAYERSUMMARIES = DESCRIPTOR.message_types_by_name['PlayerSummaries']
_RELAYADDRESS = DESCRIPTOR.message_types_by_name['RelayAddress']
_UDPCONFIG = DESCRIPTOR.message_types_by_name['UdpConfig']
_RELAYADDRESSESVOD = DESCRIPTOR.message_types_by_name['RelayAddressesVOD']
_UDPCONFIGVOD = DESCRIPTOR.message_types_by_name['UdpConfigVOD']
_PLAYERROUTEDISTANCE = DESCRIPTOR.message_types_by_name['PlayerRouteDistance']
_EVENTSUBGROUPPLACEMENTS = DESCRIPTOR.message_types_by_name['EventSubgroupPlacements']
_SERVERTOCLIENT = DESCRIPTOR.message_types_by_name['ServerToClient']
_GHOST = DESCRIPTOR.message_types_by_name['Ghost']
_GHOSTS = DESCRIPTOR.message_types_by_name['Ghosts']
_PLAYERUPDATE = DESCRIPTOR.message_types_by_name['PlayerUpdate']
_CHATMESSAGE = DESCRIPTOR.message_types_by_name['ChatMessage']
_RIDEON = DESCRIPTOR.message_types_by_name['RideOn']
_SEGMENTCOMPLETE = DESCRIPTOR.message_types_by_name['SegmentComplete']
DecompiledPlayer = _reflection.GeneratedProtocolMessageType('DecompiledPlayer', (_message.Message,), {
  'DESCRIPTOR' : _DECOMPILEDPLAYER,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:DecompiledPlayer)
  })
_sym_db.RegisterMessage(DecompiledPlayer)

PlayerState = _reflection.GeneratedProtocolMessageType('PlayerState', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTATE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerState)
  })
_sym_db.RegisterMessage(PlayerState)

ClientToServer = _reflection.GeneratedProtocolMessageType('ClientToServer', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTOSERVER,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ClientToServer)
  })
_sym_db.RegisterMessage(ClientToServer)

PlayerSummary = _reflection.GeneratedProtocolMessageType('PlayerSummary', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSUMMARY,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerSummary)
  })
_sym_db.RegisterMessage(PlayerSummary)

PlayerSummaries = _reflection.GeneratedProtocolMessageType('PlayerSummaries', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSUMMARIES,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerSummaries)
  })
_sym_db.RegisterMessage(PlayerSummaries)

RelayAddress = _reflection.GeneratedProtocolMessageType('RelayAddress', (_message.Message,), {
  'DESCRIPTOR' : _RELAYADDRESS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RelayAddress)
  })
_sym_db.RegisterMessage(RelayAddress)

UdpConfig = _reflection.GeneratedProtocolMessageType('UdpConfig', (_message.Message,), {
  'DESCRIPTOR' : _UDPCONFIG,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:UdpConfig)
  })
_sym_db.RegisterMessage(UdpConfig)

RelayAddressesVOD = _reflection.GeneratedProtocolMessageType('RelayAddressesVOD', (_message.Message,), {
  'DESCRIPTOR' : _RELAYADDRESSESVOD,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RelayAddressesVOD)
  })
_sym_db.RegisterMessage(RelayAddressesVOD)

UdpConfigVOD = _reflection.GeneratedProtocolMessageType('UdpConfigVOD', (_message.Message,), {
  'DESCRIPTOR' : _UDPCONFIGVOD,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:UdpConfigVOD)
  })
_sym_db.RegisterMessage(UdpConfigVOD)

PlayerRouteDistance = _reflection.GeneratedProtocolMessageType('PlayerRouteDistance', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERROUTEDISTANCE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerRouteDistance)
  })
_sym_db.RegisterMessage(PlayerRouteDistance)

EventSubgroupPlacements = _reflection.GeneratedProtocolMessageType('EventSubgroupPlacements', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSUBGROUPPLACEMENTS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:EventSubgroupPlacements)
  })
_sym_db.RegisterMessage(EventSubgroupPlacements)

ServerToClient = _reflection.GeneratedProtocolMessageType('ServerToClient', (_message.Message,), {
  'DESCRIPTOR' : _SERVERTOCLIENT,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerToClient)
  })
_sym_db.RegisterMessage(ServerToClient)

Ghost = _reflection.GeneratedProtocolMessageType('Ghost', (_message.Message,), {
  'DESCRIPTOR' : _GHOST,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghost)
  })
_sym_db.RegisterMessage(Ghost)

Ghosts = _reflection.GeneratedProtocolMessageType('Ghosts', (_message.Message,), {
  'DESCRIPTOR' : _GHOSTS,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghosts)
  })
_sym_db.RegisterMessage(Ghosts)

PlayerUpdate = _reflection.GeneratedProtocolMessageType('PlayerUpdate', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERUPDATE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerUpdate)
  })
_sym_db.RegisterMessage(PlayerUpdate)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

RideOn = _reflection.GeneratedProtocolMessageType('RideOn', (_message.Message,), {
  'DESCRIPTOR' : _RIDEON,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RideOn)
  })
_sym_db.RegisterMessage(RideOn)

SegmentComplete = _reflection.GeneratedProtocolMessageType('SegmentComplete', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTCOMPLETE,
  '__module__' : 'udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:SegmentComplete)
  })
_sym_db.RegisterMessage(SegmentComplete)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DECOMPILEDPLAYER._serialized_start=75
  _DECOMPILEDPLAYER._serialized_end=163
  _PLAYERSTATE._serialized_start=166
  _PLAYERSTATE._serialized_end=779
  _CLIENTTOSERVER._serialized_start=782
  _CLIENTTOSERVER._serialized_end=1062
  _PLAYERSUMMARY._serialized_start=1064
  _PLAYERSUMMARY._serialized_end=1127
  _PLAYERSUMMARIES._serialized_start=1130
  _PLAYERSUMMARIES._serialized_end=1273
  _RELAYADDRESS._serialized_start=1275
  _RELAYADDRESS._serialized_end=1363
  _UDPCONFIG._serialized_start=1365
  _UDPCONFIG._serialized_end=1452
  _RELAYADDRESSESVOD._serialized_start=1454
  _RELAYADDRESSESVOD._serialized_end=1547
  _UDPCONFIGVOD._serialized_start=1549
  _UDPCONFIGVOD._serialized_end=1668
  _PLAYERROUTEDISTANCE._serialized_start=1670
  _PLAYERROUTEDISTANCE._serialized_end=1727
  _EVENTSUBGROUPPLACEMENTS._serialized_start=1730
  _EVENTSUBGROUPPLACEMENTS._serialized_end=1983
  _SERVERTOCLIENT._serialized_start=1986
  _SERVERTOCLIENT._serialized_end=2598
  _GHOST._serialized_start=2600
  _GHOST._serialized_end=2656
  _GHOSTS._serialized_start=2658
  _GHOSTS._serialized_end=2690
  _PLAYERUPDATE._serialized_start=2693
  _PLAYERUPDATE._serialized_end=2896
  _CHATMESSAGE._serialized_start=2899
  _CHATMESSAGE._serialized_end=3077
  _RIDEON._serialized_start=3079
  _RIDEON._serialized_end=3184
  _SEGMENTCOMPLETE._serialized_start=3187
  _SEGMENTCOMPLETE._serialized_end=3483
# @@protoc_insertion_point(module_scope)
