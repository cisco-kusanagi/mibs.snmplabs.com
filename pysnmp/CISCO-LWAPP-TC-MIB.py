#
# PySNMP MIB module CISCO-LWAPP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, iso, Unsigned32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, Bits, Gauge32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "Unsigned32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 514))
ciscoLwappTextualConventions.setRevisions(('2011-09-13 00:00', '2007-10-30 00:00', '2007-02-05 00:00', '2006-10-31 00:00', '2006-04-13 00:00',))
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setLastUpdated('201109130000Z')
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setOrganization('Cisco Systems, Inc.')
class CLApIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("dot11bg", 1), ("dot11a", 2), ("uwb", 3), ("dot11abgn", 4), ("dot11ac", 5), ("dot11b", 6), ("dot11g", 7), ("dot11n24", 8), ("dot11n5", 9), ("unknown", 10))

class CLDot11Channel(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ValueRangeConstraint(165, 165), ValueRangeConstraint(169, 169), ValueRangeConstraint(173, 173), )
class CLDot11ClientStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("idle", 1), ("aaaPending", 2), ("authenticated", 3), ("associated", 4), ("powersave", 5), ("disassociated", 6), ("tobedeleted", 7), ("probing", 8), ("excluded", 9))

class CLEventFrames(TextualConvention, Bits):
    reference = 'Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications, Section 7.1.3.1.2 - Type and Subtype fields'
    status = 'current'
    namedValues = NamedValues(("cLAssocRequestFrm", 0), ("cLAssocResponseFrm", 1), ("cLReAssocRequestFrm", 2), ("cLReAssocResponseFrm", 3), ("cLProbeRequestFrm", 4), ("cLProbeResponseFrm", 5), ("cLReserved1", 6), ("cLReserved2", 7), ("cLBeaconFrm", 8), ("cLAtimFrm", 9), ("cLDissociationFrm", 10), ("cLAuthenticationFrm", 11), ("cLDeAuthenticationFrm", 12))

class CLMfpEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 16, 17, 19, 20, 21, 22, 23, 24, 32, 33, 34))
    namedValues = NamedValues(("invalidMic", 1), ("invalidSeq", 2), ("noMic", 3), ("unexpectedMic", 4), ("ccmpNoEncryptError", 16), ("ccmpDecryptError", 17), ("ccmpInvalidReplayCtr", 19), ("tkipNoEncryptError", 20), ("tkipInvalidIcv", 21), ("tkipInvalidMic", 22), ("tkipInvalidMhdrIe", 23), ("tkipInvalidReplayCtr", 24), ("bcastDisassociationFrameRcvd", 32), ("bcastDeauthenticationFrameRcvd", 33), ("bcastActionFrameRcvd", 34))

class CLMfpEventSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("infrastructureMfp", 1), ("clientMfp", 2))

class CLMfpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mfpv1", 1), ("mfpv2", 2))

class CLTimeBaseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cTimeBaseInSync", 1), ("cTimeBaseNotInSync", 2))

class CLSecEncryptType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("tkip", 0), ("aes", 1))

class CLSecKeyFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("hex", 2), ("ascii", 3))

class CLDot11RfParamMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("custom", 2), ("auto", 3))

class CLTsmDot11CurrentPackets(TextualConvention, Gauge32):
    status = 'current'

class CLCdpAdvtVersionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cdpv1", 1), ("cdpv2", 2))

class CLDot11ChannelBandwidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("five", 1), ("ten", 2), ("twenty", 3), ("aboveforty", 4), ("belowforty", 5))

class CLDot11Band(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("band2dot4", 1), ("band5", 2))

class CLApAssocFailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("notSupported", 2))

class CLWebAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("internalDefault", 1), ("internalCustom", 2), ("external", 3))

class CLClientPowerSaveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("powersave", 2))

class CLApEthernetIfStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CLApDot11RadioSubband(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 1), ("sub49", 2), ("sub52", 3), ("sub54", 4), ("sub58", 5))

class CLApDot11RadioRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("shutdown", 0), ("updownlink", 1), ("uplink", 2), ("downlink", 3), ("access", 4), ("uplinkaccess", 5), ("downlinkaccess", 6), ("updownlinkaccess", 7), ("unknown", 8))

class CcxServiceVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("version1", 2), ("version2", 3))

class CLApMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("local", 0), ("monitor", 1), ("remote", 2), ("roguedetector", 3), ("sniffer", 4), ("bridge", 5), ("seConnect", 6))

mibBuilder.exportSymbols("CISCO-LWAPP-TC-MIB", CLEventFrames=CLEventFrames, PYSNMP_MODULE_ID=ciscoLwappTextualConventions, CLDot11ClientStatus=CLDot11ClientStatus, CLTsmDot11CurrentPackets=CLTsmDot11CurrentPackets, CLMfpVersion=CLMfpVersion, CLApDot11RadioSubband=CLApDot11RadioSubband, CLDot11Channel=CLDot11Channel, CLMfpEventType=CLMfpEventType, CLSecKeyFormat=CLSecKeyFormat, ciscoLwappTextualConventions=ciscoLwappTextualConventions, CLDot11RfParamMode=CLDot11RfParamMode, CLDot11Band=CLDot11Band, CLWebAuthType=CLWebAuthType, CLClientPowerSaveMode=CLClientPowerSaveMode, CLApDot11RadioRole=CLApDot11RadioRole, CLCdpAdvtVersionType=CLCdpAdvtVersionType, CLApEthernetIfStatus=CLApEthernetIfStatus, CLMfpEventSource=CLMfpEventSource, CLApIfType=CLApIfType, CLApAssocFailureReason=CLApAssocFailureReason, CLApMode=CLApMode, CLDot11ChannelBandwidth=CLDot11ChannelBandwidth, CcxServiceVersion=CcxServiceVersion, CLSecEncryptType=CLSecEncryptType, CLTimeBaseStatus=CLTimeBaseStatus)
