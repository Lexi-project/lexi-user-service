# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x1c\n\x08Validate\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\"\x1d\n\x0cTokenPayload\x12\r\n\x05token\x18\x01 \x01(\t2B\n\x0bUserService\x12\x33\n\rValidateToken\x12\x12.user.TokenPayload\x1a\x0e.user.Validateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_VALIDATE']._serialized_start=20
  _globals['_VALIDATE']._serialized_end=48
  _globals['_TOKENPAYLOAD']._serialized_start=50
  _globals['_TOKENPAYLOAD']._serialized_end=79
  _globals['_USERSERVICE']._serialized_start=81
  _globals['_USERSERVICE']._serialized_end=147
# @@protoc_insertion_point(module_scope)
