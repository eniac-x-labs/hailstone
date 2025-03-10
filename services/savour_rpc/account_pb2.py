# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dapplink/account.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'dapplink/account.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from services.savour_rpc import common_pb2 as dapplink_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x64\x61pplink/account.proto\x12\x10\x64\x61pplink.account\x1a\x15\x64\x61pplink/common.proto\"\x1a\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x16\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\t\"\xb4\x02\n\tTxMessage\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12(\n\x05\x66roms\x18\x03 \x03(\x0b\x32\x19.dapplink.account.Address\x12&\n\x03tos\x18\x04 \x03(\x0b\x32\x19.dapplink.account.Address\x12\'\n\x06values\x18\x07 \x03(\x0b\x32\x17.dapplink.account.Value\x12\x0b\n\x03\x66\x65\x65\x18\x05 \x01(\t\x12*\n\x06status\x18\x06 \x01(\x0e\x32\x1a.dapplink.account.TxStatus\x12\x0c\n\x04type\x18\x08 \x01(\x05\x12\x0e\n\x06height\x18\t \x01(\t\x12\x18\n\x10\x63ontract_address\x18\n \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x0b \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x0c \x01(\t\"]\n\tBlockData\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61seFee\x18\x02 \x01(\t\x12\x31\n\x0ctransactions\x18\x03 \x03(\x0b\x32\x1b.dapplink.account.TxMessage\"\x8d\x03\n\x0b\x42lockHeader\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x13\n\x0bparent_hash\x18\x02 \x01(\t\x12\x12\n\nuncle_hash\x18\x03 \x01(\t\x12\x11\n\tcoin_base\x18\x04 \x01(\t\x12\x0c\n\x04root\x18\x05 \x01(\t\x12\x0f\n\x07tx_hash\x18\x06 \x01(\t\x12\x14\n\x0creceipt_hash\x18\x07 \x01(\t\x12\x1a\n\x12parent_beacon_root\x18\x08 \x01(\t\x12\x12\n\ndifficulty\x18\t \x01(\t\x12\x0e\n\x06number\x18\n \x01(\t\x12\x11\n\tgas_limit\x18\x0b \x01(\x04\x12\x10\n\x08gas_used\x18\x0c \x01(\x04\x12\x0c\n\x04time\x18\r \x01(\x04\x12\r\n\x05\x65xtra\x18\x0e \x01(\t\x12\x12\n\nmix_digest\x18\x0f \x01(\t\x12\r\n\x05nonce\x18\x10 \x01(\t\x12\x10\n\x08\x62\x61se_fee\x18\x11 \x01(\t\x12\x18\n\x10withdrawals_hash\x18\x12 \x01(\t\x12\x15\n\rblob_gas_used\x18\x13 \x01(\x04\x12\x17\n\x0f\x65xcess_blob_gas\x18\x14 \x01(\x04\"\xa1\x01\n\x03Log\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06topics\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\t\x12\x0f\n\x07tx_hash\x18\x05 \x01(\t\x12\x10\n\x08tx_index\x18\x06 \x01(\x04\x12\x12\n\nblock_hash\x18\x07 \x01(\t\x12\r\n\x05index\x18\x08 \x01(\x04\x12\x0f\n\x07removed\x18\t \x01(\x08\"N\n\x14SupportChainsRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\"Y\n\x15SupportChainsResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0f\n\x07support\x18\x03 \x01(\x08\"q\n\x15\x43onvertAddressRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x12\n\npublic_key\x18\x05 \x01(\t\"Z\n\x16\x43onvertAddressResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"^\n\x13ValidAddressRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\"V\n\x14ValidAddressResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05valid\x18\x03 \x01(\x08\"\\\n\x12\x42lockNumberRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0f\n\x07view_tx\x18\x04 \x01(\x08\"X\n\x10\x42lockHashRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\x0f\n\x07view_tx\x18\x04 \x01(\x08\"\x92\x01\n\x18\x42lockInfoTransactionList\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x15\n\rtoken_address\x18\x03 \x01(\t\x12\x17\n\x0f\x63ontract_wallet\x18\x04 \x01(\t\x12\x0c\n\x04hash\x18\x05 \x01(\t\x12\x0e\n\x06height\x18\x06 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x07 \x01(\t\"\xb2\x01\n\rBlockResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x10\n\x08\x62\x61se_fee\x18\x05 \x01(\t\x12@\n\x0ctransactions\x18\x06 \x03(\x0b\x32*.dapplink.account.BlockInfoTransactionList\"^\n\x16\x42lockHeaderHashRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\t\"b\n\x18\x42lockHeaderNumberRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0e\n\x06height\x18\x04 \x01(\x03\"{\n\x13\x42lockHeaderResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x33\n\x0c\x62lock_header\x18\x03 \x01(\x0b\x32\x1d.dapplink.account.BlockHeader\"i\n\x13\x42lockByRangeRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\t\x12\x0b\n\x03\x65nd\x18\x05 \x01(\t\"|\n\x14\x42lockByRangeResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x33\n\x0c\x62lock_header\x18\x03 \x03(\x0b\x32\x1d.dapplink.account.BlockHeader\"\x9d\x01\n\x0e\x41\x63\x63ountRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04\x63oin\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x06 \x01(\t\x12\x1a\n\x12proposer_key_index\x18\x07 \x01(\x04\"\x8e\x01\n\x0f\x41\x63\x63ountResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\t\x12\x10\n\x08sequence\x18\x05 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x06 \x01(\t\"r\n\nFeeRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04\x63oin\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\r\n\x05rawTx\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\"v\n\x0b\x46\x65\x65Response\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x10\n\x08slow_fee\x18\x03 \x01(\t\x12\x12\n\nnormal_fee\x18\x04 \x01(\t\x12\x10\n\x08\x66\x61st_fee\x18\x05 \x01(\t\"e\n\rSendTxRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04\x63oin\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0e\n\x06raw_tx\x18\x05 \x01(\t\"R\n\x0eSendTxResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0f\n\x07tx_hash\x18\x03 \x01(\t\"\xb3\x01\n\x10TxAddressRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04\x63oin\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x06 \x01(\t\x12\x0c\n\x04page\x18\x07 \x01(\r\x12\x10\n\x08pagesize\x18\x08 \x01(\r\x12\x0e\n\x06\x63ursor\x18\t \x01(\t\"m\n\x11TxAddressResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\'\n\x02tx\x18\x03 \x03(\x0b\x32\x1b.dapplink.account.TxMessage\"c\n\rTxHashRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0c\n\x04\x63oin\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0c\n\x04hash\x18\x05 \x01(\t\"j\n\x0eTxHashResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\'\n\x02tx\x18\x03 \x01(\x0b\x32\x1b.dapplink.account.TxMessage\"e\n\x18UnSignTransactionRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x11\n\tbase64_tx\x18\x04 \x01(\t\"`\n\x19UnSignTransactionResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x12\n\nun_sign_tx\x18\x03 \x01(\t\"\x8c\x01\n\x18SignedTransactionRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x11\n\tbase64_tx\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x12\n\npublic_key\x18\x06 \x01(\t\"_\n\x19SignedTransactionResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\tsigned_tx\x18\x03 \x01(\t\"y\n\x18VerifyTransactionRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x12\n\npublic_key\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\"\\\n\x19VerifyTransactionResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0e\n\x06verify\x18\x03 \x01(\x08\"b\n\x18\x44\x65\x63odeTransactionRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0e\n\x06raw_tx\x18\x04 \x01(\t\"_\n\x19\x44\x65\x63odeTransactionResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\tbase64_tx\x18\x03 \x01(\t\"i\n\x10\x45xtraDataRequest\x12\x16\n\x0e\x63onsumer_token\x18\x01 \x01(\t\x12\r\n\x05\x63hain\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x0c\n\x04\x63oin\x18\x05 \x01(\t\"S\n\x11\x45xtraDataResponse\x12\"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.dapplink.ReturnCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t*d\n\x08TxStatus\x12\x0c\n\x08NotFound\x10\x00\x12\x0b\n\x07Pending\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x12\x0b\n\x07Success\x10\x03\x12\x19\n\x15\x43ontractExecuteFailed\x10\x04\x12\t\n\x05Other\x10\x05\x32\x89\x0e\n\x14WalletAccountService\x12\x65\n\x10getSupportChains\x12&.dapplink.account.SupportChainsRequest\x1a\'.dapplink.account.SupportChainsResponse\"\x00\x12\x65\n\x0e\x63onvertAddress\x12\'.dapplink.account.ConvertAddressRequest\x1a(.dapplink.account.ConvertAddressResponse\"\x00\x12_\n\x0cvalidAddress\x12%.dapplink.account.ValidAddressRequest\x1a&.dapplink.account.ValidAddressResponse\"\x00\x12[\n\x10getBlockByNumber\x12$.dapplink.account.BlockNumberRequest\x1a\x1f.dapplink.account.BlockResponse\"\x00\x12W\n\x0egetBlockByHash\x12\".dapplink.account.BlockHashRequest\x1a\x1f.dapplink.account.BlockResponse\"\x00\x12i\n\x14getBlockHeaderByHash\x12(.dapplink.account.BlockHeaderHashRequest\x1a%.dapplink.account.BlockHeaderResponse\"\x00\x12m\n\x16getBlockHeaderByNumber\x12*.dapplink.account.BlockHeaderNumberRequest\x1a%.dapplink.account.BlockHeaderResponse\"\x00\x12h\n\x15getBlockHeaderByRange\x12%.dapplink.account.BlockByRangeRequest\x1a&.dapplink.account.BlockByRangeResponse\"\x00\x12S\n\ngetAccount\x12 .dapplink.account.AccountRequest\x1a!.dapplink.account.AccountResponse\"\x00\x12G\n\x06getFee\x12\x1c.dapplink.account.FeeRequest\x1a\x1d.dapplink.account.FeeResponse\"\x00\x12M\n\x06SendTx\x12\x1f.dapplink.account.SendTxRequest\x1a .dapplink.account.SendTxResponse\"\x00\x12[\n\x0egetTxByAddress\x12\".dapplink.account.TxAddressRequest\x1a#.dapplink.account.TxAddressResponse\"\x00\x12R\n\x0bgetTxByHash\x12\x1f.dapplink.account.TxHashRequest\x1a .dapplink.account.TxHashResponse\"\x00\x12t\n\x17\x63reateUnSignTransaction\x12*.dapplink.account.UnSignTransactionRequest\x1a+.dapplink.account.UnSignTransactionResponse\"\x00\x12s\n\x16\x62uildSignedTransaction\x12*.dapplink.account.SignedTransactionRequest\x1a+.dapplink.account.SignedTransactionResponse\"\x00\x12n\n\x11\x64\x65\x63odeTransaction\x12*.dapplink.account.DecodeTransactionRequest\x1a+.dapplink.account.DecodeTransactionResponse\"\x00\x12t\n\x17verifySignedTransaction\x12*.dapplink.account.VerifyTransactionRequest\x1a+.dapplink.account.VerifyTransactionResponse\"\x00\x12Y\n\x0cgetExtraData\x12\".dapplink.account.ExtraDataRequest\x1a#.dapplink.account.ExtraDataResponse\"\x00\x42\'\n\x14xyz.dapplink.accountZ\x0f./proto/accountb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dapplink.account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024xyz.dapplink.accountZ\017./proto/account'
  _globals['_TXSTATUS']._serialized_start=4996
  _globals['_TXSTATUS']._serialized_end=5096
  _globals['_ADDRESS']._serialized_start=67
  _globals['_ADDRESS']._serialized_end=93
  _globals['_VALUE']._serialized_start=95
  _globals['_VALUE']._serialized_end=117
  _globals['_TXMESSAGE']._serialized_start=120
  _globals['_TXMESSAGE']._serialized_end=428
  _globals['_BLOCKDATA']._serialized_start=430
  _globals['_BLOCKDATA']._serialized_end=523
  _globals['_BLOCKHEADER']._serialized_start=526
  _globals['_BLOCKHEADER']._serialized_end=923
  _globals['_LOG']._serialized_start=926
  _globals['_LOG']._serialized_end=1087
  _globals['_SUPPORTCHAINSREQUEST']._serialized_start=1089
  _globals['_SUPPORTCHAINSREQUEST']._serialized_end=1167
  _globals['_SUPPORTCHAINSRESPONSE']._serialized_start=1169
  _globals['_SUPPORTCHAINSRESPONSE']._serialized_end=1258
  _globals['_CONVERTADDRESSREQUEST']._serialized_start=1260
  _globals['_CONVERTADDRESSREQUEST']._serialized_end=1373
  _globals['_CONVERTADDRESSRESPONSE']._serialized_start=1375
  _globals['_CONVERTADDRESSRESPONSE']._serialized_end=1465
  _globals['_VALIDADDRESSREQUEST']._serialized_start=1467
  _globals['_VALIDADDRESSREQUEST']._serialized_end=1561
  _globals['_VALIDADDRESSRESPONSE']._serialized_start=1563
  _globals['_VALIDADDRESSRESPONSE']._serialized_end=1649
  _globals['_BLOCKNUMBERREQUEST']._serialized_start=1651
  _globals['_BLOCKNUMBERREQUEST']._serialized_end=1743
  _globals['_BLOCKHASHREQUEST']._serialized_start=1745
  _globals['_BLOCKHASHREQUEST']._serialized_end=1833
  _globals['_BLOCKINFOTRANSACTIONLIST']._serialized_start=1836
  _globals['_BLOCKINFOTRANSACTIONLIST']._serialized_end=1982
  _globals['_BLOCKRESPONSE']._serialized_start=1985
  _globals['_BLOCKRESPONSE']._serialized_end=2163
  _globals['_BLOCKHEADERHASHREQUEST']._serialized_start=2165
  _globals['_BLOCKHEADERHASHREQUEST']._serialized_end=2259
  _globals['_BLOCKHEADERNUMBERREQUEST']._serialized_start=2261
  _globals['_BLOCKHEADERNUMBERREQUEST']._serialized_end=2359
  _globals['_BLOCKHEADERRESPONSE']._serialized_start=2361
  _globals['_BLOCKHEADERRESPONSE']._serialized_end=2484
  _globals['_BLOCKBYRANGEREQUEST']._serialized_start=2486
  _globals['_BLOCKBYRANGEREQUEST']._serialized_end=2591
  _globals['_BLOCKBYRANGERESPONSE']._serialized_start=2593
  _globals['_BLOCKBYRANGERESPONSE']._serialized_end=2717
  _globals['_ACCOUNTREQUEST']._serialized_start=2720
  _globals['_ACCOUNTREQUEST']._serialized_end=2877
  _globals['_ACCOUNTRESPONSE']._serialized_start=2880
  _globals['_ACCOUNTRESPONSE']._serialized_end=3022
  _globals['_FEEREQUEST']._serialized_start=3024
  _globals['_FEEREQUEST']._serialized_end=3138
  _globals['_FEERESPONSE']._serialized_start=3140
  _globals['_FEERESPONSE']._serialized_end=3258
  _globals['_SENDTXREQUEST']._serialized_start=3260
  _globals['_SENDTXREQUEST']._serialized_end=3361
  _globals['_SENDTXRESPONSE']._serialized_start=3363
  _globals['_SENDTXRESPONSE']._serialized_end=3445
  _globals['_TXADDRESSREQUEST']._serialized_start=3448
  _globals['_TXADDRESSREQUEST']._serialized_end=3627
  _globals['_TXADDRESSRESPONSE']._serialized_start=3629
  _globals['_TXADDRESSRESPONSE']._serialized_end=3738
  _globals['_TXHASHREQUEST']._serialized_start=3740
  _globals['_TXHASHREQUEST']._serialized_end=3839
  _globals['_TXHASHRESPONSE']._serialized_start=3841
  _globals['_TXHASHRESPONSE']._serialized_end=3947
  _globals['_UNSIGNTRANSACTIONREQUEST']._serialized_start=3949
  _globals['_UNSIGNTRANSACTIONREQUEST']._serialized_end=4050
  _globals['_UNSIGNTRANSACTIONRESPONSE']._serialized_start=4052
  _globals['_UNSIGNTRANSACTIONRESPONSE']._serialized_end=4148
  _globals['_SIGNEDTRANSACTIONREQUEST']._serialized_start=4151
  _globals['_SIGNEDTRANSACTIONREQUEST']._serialized_end=4291
  _globals['_SIGNEDTRANSACTIONRESPONSE']._serialized_start=4293
  _globals['_SIGNEDTRANSACTIONRESPONSE']._serialized_end=4388
  _globals['_VERIFYTRANSACTIONREQUEST']._serialized_start=4390
  _globals['_VERIFYTRANSACTIONREQUEST']._serialized_end=4511
  _globals['_VERIFYTRANSACTIONRESPONSE']._serialized_start=4513
  _globals['_VERIFYTRANSACTIONRESPONSE']._serialized_end=4605
  _globals['_DECODETRANSACTIONREQUEST']._serialized_start=4607
  _globals['_DECODETRANSACTIONREQUEST']._serialized_end=4705
  _globals['_DECODETRANSACTIONRESPONSE']._serialized_start=4707
  _globals['_DECODETRANSACTIONRESPONSE']._serialized_end=4802
  _globals['_EXTRADATAREQUEST']._serialized_start=4804
  _globals['_EXTRADATAREQUEST']._serialized_end=4909
  _globals['_EXTRADATARESPONSE']._serialized_start=4911
  _globals['_EXTRADATARESPONSE']._serialized_end=4994
  _globals['_WALLETACCOUNTSERVICE']._serialized_start=5099
  _globals['_WALLETACCOUNTSERVICE']._serialized_end=6900
# @@protoc_insertion_point(module_scope)
