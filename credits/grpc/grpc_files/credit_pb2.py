# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: credit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63redit.proto\x12\x06\x63redit\"5\n\x13\x42orrowCreditRequest\x12\x0f\n\x07\x63redits\x18\x01 \x01(\x05\x12\r\n\x05token\x18\x02 \x01(\t\".\n\x14\x42orrowCreditResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x05\">\n\x15RollbackCreditRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x05\x12\r\n\x05token\x18\x02 \x01(\t\",\n\x16RollbackCreditResponse\x12\x12\n\nis_success\x18\x01 \x01(\x08\"-\n\x13\x43ommitCreditRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x05\"*\n\x14\x43ommitCreditResponse\x12\x12\n\nis_success\x18\x01 \x01(\x08\x32\xf6\x01\n\rCreditService\x12I\n\x0c\x42orrowCredit\x12\x1b.credit.BorrowCreditRequest\x1a\x1c.credit.BorrowCreditResponse\x12O\n\x0eRollbackCredit\x12\x1d.credit.RollbackCreditRequest\x1a\x1e.credit.RollbackCreditResponse\x12I\n\x0c\x43ommitCredit\x12\x1b.credit.CommitCreditRequest\x1a\x1c.credit.CommitCreditResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'credit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BORROWCREDITREQUEST']._serialized_start=24
  _globals['_BORROWCREDITREQUEST']._serialized_end=77
  _globals['_BORROWCREDITRESPONSE']._serialized_start=79
  _globals['_BORROWCREDITRESPONSE']._serialized_end=125
  _globals['_ROLLBACKCREDITREQUEST']._serialized_start=127
  _globals['_ROLLBACKCREDITREQUEST']._serialized_end=189
  _globals['_ROLLBACKCREDITRESPONSE']._serialized_start=191
  _globals['_ROLLBACKCREDITRESPONSE']._serialized_end=235
  _globals['_COMMITCREDITREQUEST']._serialized_start=237
  _globals['_COMMITCREDITREQUEST']._serialized_end=282
  _globals['_COMMITCREDITRESPONSE']._serialized_start=284
  _globals['_COMMITCREDITRESPONSE']._serialized_end=326
  _globals['_CREDITSERVICE']._serialized_start=329
  _globals['_CREDITSERVICE']._serialized_end=575
# @@protoc_insertion_point(module_scope)
