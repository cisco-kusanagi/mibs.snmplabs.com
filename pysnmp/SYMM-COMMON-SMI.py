#
# PySNMP MIB module SYMM-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMM-COMMON-SMI
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:07 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, IpAddress, MibIdentifier, iso, TimeTicks, Gauge32, Unsigned32, NotificationType, Counter32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "IpAddress", "MibIdentifier", "iso", "TimeTicks", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmetricom = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070))
symmetricom.setRevisions(('2018-08-23 08:22',))
if mibBuilder.loadTexts: symmetricom.setLastUpdated('201808230822Z')
if mibBuilder.loadTexts: symmetricom.setOrganization('Symmetricom, Inc.')
class EnableValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class TP5000MODULEID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("sys", 1), ("imc", 2), ("ioc1", 3), ("ioc2", 4), ("io", 5), ("exp0", 6), ("exp1", 7), ("exp2", 8), ("exp3", 9), ("exp4", 10), ("exp5", 11), ("exp6", 12), ("exp7", 13), ("exp8", 14), ("exp9", 15))

class ONVALUETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class ACTIONONLY(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("apply", 1), ("nonapply", 2))

class OPMODETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

class ACTIVEVALUETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class YESVALUETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class OKVALUETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fault", 2))

class VALIDTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valid", 1), ("invalid", 2), ("nurture", 3))

class GNSSHealthStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("healthy", 1), ("unhealthy", 2))

class GNSSReceiverMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 128))
    namedValues = NamedValues(("beidou", 1), ("gps", 2), ("priorityBeidou", 4), ("priorityGps", 5), ("gnssGPS", 17), ("gnssGlonass", 18), ("gnssGPSGlonass", 19), ("gnssGalileo", 20), ("gnssGPSGalileo", 21), ("gnssGlonassGalileo", 22), ("gnssGPSGlonassGalileo", 23), ("gnssBeidou", 24), ("gnssBeidouGPS", 25), ("gnssBeidouGlonass", 26), ("gnssBeidouGlonassGPSReserved", 27), ("gnssBeidouGalileo", 28), ("gnssBeidouGalileoGPS", 29), ("gnssBeidouGalileoGlonassReserved", 30), ("gnssBeidouGalileoGlonassGPSReserved", 31), ("notApplicable", 128))

class GNSSPositionMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

symmNetworkManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1))
if mibBuilder.loadTexts: symmNetworkManagement.setStatus('current')
symmCmipManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 1))
if mibBuilder.loadTexts: symmCmipManagement.setStatus('current')
symmSnmpManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2))
if mibBuilder.loadTexts: symmSnmpManagement.setStatus('current')
symmTimePictra = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 1))
if mibBuilder.loadTexts: symmTimePictra.setStatus('current')
symmBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 2))
if mibBuilder.loadTexts: symmBroadband.setStatus('current')
symmTTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3))
if mibBuilder.loadTexts: symmTTM.setStatus('current')
symmTSD = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 4))
if mibBuilder.loadTexts: symmTSD.setStatus('current')
symmCommonModelV1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5))
if mibBuilder.loadTexts: symmCommonModelV1.setStatus('current')
symmPacketService = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1))
if mibBuilder.loadTexts: symmPacketService.setStatus('current')
symmPhysicalSignal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2))
if mibBuilder.loadTexts: symmPhysicalSignal.setStatus('current')
symmClock = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3))
if mibBuilder.loadTexts: symmClock.setStatus('current')
symmNetwork = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4))
if mibBuilder.loadTexts: symmNetwork.setStatus('current')
symmEntPhysicalExtension = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5))
if mibBuilder.loadTexts: symmEntPhysicalExtension.setStatus('current')
symmInterfaceExtension = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6))
if mibBuilder.loadTexts: symmInterfaceExtension.setStatus('current')
symmDeviceDependent = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7))
if mibBuilder.loadTexts: symmDeviceDependent.setStatus('current')
mibBuilder.exportSymbols("SYMM-COMMON-SMI", ONVALUETYPE=ONVALUETYPE, EnableValue=EnableValue, GNSSPositionMode=GNSSPositionMode, symmPhysicalSignal=symmPhysicalSignal, symmTTM=symmTTM, ACTIVEVALUETYPE=ACTIVEVALUETYPE, symmetricom=symmetricom, symmCommonModelV1=symmCommonModelV1, YESVALUETYPE=YESVALUETYPE, symmNetworkManagement=symmNetworkManagement, symmInterfaceExtension=symmInterfaceExtension, symmBroadband=symmBroadband, GNSSReceiverMode=GNSSReceiverMode, symmNetwork=symmNetwork, symmCmipManagement=symmCmipManagement, symmEntPhysicalExtension=symmEntPhysicalExtension, symmSnmpManagement=symmSnmpManagement, symmTimePictra=symmTimePictra, symmClock=symmClock, OPMODETYPE=OPMODETYPE, symmDeviceDependent=symmDeviceDependent, symmPacketService=symmPacketService, GNSSHealthStatus=GNSSHealthStatus, OKVALUETYPE=OKVALUETYPE, symmTSD=symmTSD, VALIDTYPE=VALIDTYPE, TP5000MODULEID=TP5000MODULEID, ACTIONONLY=ACTIONONLY, PYSNMP_MODULE_ID=symmetricom)
