#
# PySNMP MIB module SYMM-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMM-COMMON-SMI
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:46 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, Counter32, MibIdentifier, Counter64, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, Integer32, ObjectIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "Counter32", "MibIdentifier", "Counter64", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmetricom = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070))
symmetricom.setRevisions(('2018-08-23 08:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmetricom.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: symmetricom.setLastUpdated('201808230822Z')
if mibBuilder.loadTexts: symmetricom.setOrganization('Symmetricom, Inc.')
if mibBuilder.loadTexts: symmetricom.setContactInfo(' Symmetricom, Inc. 2300 Orchard Parkway San Jose, CA 95131')
if mibBuilder.loadTexts: symmetricom.setDescription("This is the MIB Module for Symmetricom's enterprise specific parameters")
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
if mibBuilder.loadTexts: symmNetworkManagement.setDescription('This is the root object identifier for all MIBs under the Symmetricom tree. ')
symmCmipManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 1))
if mibBuilder.loadTexts: symmCmipManagement.setStatus('current')
if mibBuilder.loadTexts: symmCmipManagement.setDescription('This is the root object identifier for CMIP based objects')
symmSnmpManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2))
if mibBuilder.loadTexts: symmSnmpManagement.setStatus('current')
if mibBuilder.loadTexts: symmSnmpManagement.setDescription('This is the root identifier object for SNMP based objects.')
symmTimePictra = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 1))
if mibBuilder.loadTexts: symmTimePictra.setStatus('current')
if mibBuilder.loadTexts: symmTimePictra.setDescription("This is reserved for objects related to Symmetricom's TimePictra product s.")
symmBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 2))
if mibBuilder.loadTexts: symmBroadband.setStatus('current')
if mibBuilder.loadTexts: symmBroadband.setDescription("The subtree that contains objects related to Symmetricom's GoWide product s. ")
symmTTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3))
if mibBuilder.loadTexts: symmTTM.setStatus('current')
if mibBuilder.loadTexts: symmTTM.setDescription("The subtree that contains objects related to Symmetricom's Timing, Test and Measurement products.")
symmTSD = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 4))
if mibBuilder.loadTexts: symmTSD.setStatus('current')
if mibBuilder.loadTexts: symmTSD.setDescription("The subtree that contains objects related to Symmetricom's Telecom Solutions products.")
symmCommonModelV1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5))
if mibBuilder.loadTexts: symmCommonModelV1.setStatus('current')
if mibBuilder.loadTexts: symmCommonModelV1.setDescription('This subtree contains Symmetricom Common MIB subsets for multiple projects.Some are common MIBs that can be reused across some Symmetricom products. Some MIBs are specific to particular Symmetricom equipment.')
symmPacketService = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1))
if mibBuilder.loadTexts: symmPacketService.setStatus('current')
if mibBuilder.loadTexts: symmPacketService.setDescription('This subtree contains objects related to the status and configuration of Symmetricom Common packet service ports, such as PTP and NTP.')
symmPhysicalSignal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2))
if mibBuilder.loadTexts: symmPhysicalSignal.setStatus('current')
if mibBuilder.loadTexts: symmPhysicalSignal.setDescription('This subtree contains objects related to the status and configurations of Symmetricom Common physical signal ports, such as E1, PPS, 10MHz, etc.')
symmClock = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3))
if mibBuilder.loadTexts: symmClock.setStatus('current')
if mibBuilder.loadTexts: symmClock.setDescription('This subtree contains objects related to Symmetricom Common date and time setting MIB.')
symmNetwork = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4))
if mibBuilder.loadTexts: symmNetwork.setStatus('current')
if mibBuilder.loadTexts: symmNetwork.setDescription('This subtree contains objects related to Symmetricom Common L2 and L3 network configurations.')
symmEntPhysicalExtension = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5))
if mibBuilder.loadTexts: symmEntPhysicalExtension.setStatus('current')
if mibBuilder.loadTexts: symmEntPhysicalExtension.setDescription('This subtree contains objects related to Symmetricom Common entity physical extension MIB.')
symmInterfaceExtension = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6))
if mibBuilder.loadTexts: symmInterfaceExtension.setStatus('current')
if mibBuilder.loadTexts: symmInterfaceExtension.setDescription('This subtree contains objects related to Symmetricom Common interface extension MIB.')
symmDeviceDependent = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7))
if mibBuilder.loadTexts: symmDeviceDependent.setStatus('current')
if mibBuilder.loadTexts: symmDeviceDependent.setDescription("This subtree contains objects related to Symmetricom's device specific MIBs.")
mibBuilder.exportSymbols("SYMM-COMMON-SMI", symmCmipManagement=symmCmipManagement, symmTSD=symmTSD, PYSNMP_MODULE_ID=symmetricom, symmPhysicalSignal=symmPhysicalSignal, symmSnmpManagement=symmSnmpManagement, symmNetwork=symmNetwork, YESVALUETYPE=YESVALUETYPE, OPMODETYPE=OPMODETYPE, symmDeviceDependent=symmDeviceDependent, GNSSHealthStatus=GNSSHealthStatus, symmPacketService=symmPacketService, symmCommonModelV1=symmCommonModelV1, symmetricom=symmetricom, GNSSReceiverMode=GNSSReceiverMode, symmInterfaceExtension=symmInterfaceExtension, symmClock=symmClock, symmTimePictra=symmTimePictra, OKVALUETYPE=OKVALUETYPE, ONVALUETYPE=ONVALUETYPE, TP5000MODULEID=TP5000MODULEID, ACTIVEVALUETYPE=ACTIVEVALUETYPE, symmNetworkManagement=symmNetworkManagement, symmTTM=symmTTM, symmBroadband=symmBroadband, VALIDTYPE=VALIDTYPE, symmEntPhysicalExtension=symmEntPhysicalExtension, EnableValue=EnableValue, ACTIONONLY=ACTIONONLY, GNSSPositionMode=GNSSPositionMode)
