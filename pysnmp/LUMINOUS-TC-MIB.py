#
# PySNMP MIB module LUMINOUS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, enterprises, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, iso, IpAddress, Bits, ModuleIdentity, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "enterprises", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "iso", "IpAddress", "Bits", "ModuleIdentity", "ObjectName")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 9))
if mibBuilder.loadTexts: lumTcMIB.setLastUpdated('0106270000Z')
if mibBuilder.loadTexts: lumTcMIB.setOrganization('Luminous Networks')
class LumShelfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mSeries", 1), ("unused1", 2), ("unused2", 3), ("cSeries", 4))

class LumChassisPlane(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("front", 1), ("back", 2))

class LumSlotNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class LumPortNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class LumSimpleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class LumPercent(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class LumRingDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("west", 2), ("east", 3))

class LumAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class LumOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7), ("misMatch", 8))

class LumControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3))

class LumServiceMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("wire", 2), ("routing", 3), ("policyForwarding", 4))

class LumPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("physical", 2), ("subPortDemux", 3))

class LumPortCreateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("implicit", 1), ("explicit", 2))

class LumPortDemuxType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("vlan", 2), ("mplsTag", 3), ("tdmChannel", 4))

class LumPortDemuxId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LumConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("rj45", 2), ("scFiber", 3), ("miniCoax", 4), ("db9", 5), ("sjFiber", 6), ("stFiber", 7))

class LumSignalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("active", 2))

class LumName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 40)

class LumDescr(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 80)

class LumVersionString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class LumSerialNumString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 21)

class LumCleiString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 17)

class LumManufactureString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class LumDateTimeString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(24, 24)
    fixedLength = 24

class LumCardBaseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 28, 29, 32, 33, 34, 35, 36, 38))
    namedValues = NamedValues(("none", 1), ("sysCon", 2), ("ring", 3), ("t1", 4), ("ether", 5), ("alarm", 6), ("upLink", 7), ("ringIO", 8), ("t1IO", 9), ("etherIO", 10), ("utility", 11), ("oc12", 12), ("oc12IO", 13), ("gigE", 14), ("gigEIO", 15), ("oc12IOAlarm", 16), ("etherFXIO", 17), ("wdm", 18), ("wdmIO", 19), ("ringIOLR", 21), ("ring2", 22), ("ring2IO", 23), ("ds3cc12", 28), ("ds3cc12IO", 29), ("ether24", 32), ("ether24IO", 33), ("asi", 34), ("asiIOIn", 35), ("asiIOOut", 36), ("present", 38))

class LumCardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("none", 1), ("sysCon", 2), ("ring", 3), ("t1", 4), ("ether", 5), ("alarm", 6), ("upLink", 7), ("ringIO", 8), ("t1IO", 9), ("etherIO", 10), ("utility", 11), ("oc12", 12), ("oc12IO", 13), ("gigE", 14), ("gigEIO", 15), ("oc12IOAlarm", 16), ("etherFXIO", 17), ("wdm", 18), ("wdmIO", 19), ("sysconR", 20), ("ringIOLR", 21), ("ring2", 22), ("ring2IO", 23), ("wdmBand1", 24), ("wdmBand2", 25), ("wdmBand3", 26), ("wdmBand4", 27), ("ds3cc12", 28), ("ds3cc12IO", 29), ("t3cc12", 30), ("e3cc12", 31), ("ether24", 32), ("ether24IO", 33), ("asi", 34), ("asiIOIn", 35), ("asiIOOut", 36), ("gigERouting", 37), ("present", 38), ("sysconU", 39), ("newCardType", 40))

class LumCardAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("shutDown", 5), ("reset", 6), ("switchover", 7))

class LumCardOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("failure", 5), ("down", 6), ("present", 7), ("initializing", 8))

class LumCardFailureState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("criticalFault", 2), ("minorFault", 3), ("minorAlarm", 4))

class LumOpticalWaveLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class LumOpticalFiberType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("singleMode", 2), ("multiMode", 3))

class LumOpticalMaxLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000000)

class LumOpticalConnector(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("sc", 2), ("lc", 3))

class LumOpticalServiceSupport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("gigE1", 0), ("gigE2", 1), ("fiberChannel1", 2), ("fiberChannel2", 3), ("oc12", 4), ("oc24", 5), ("oc48", 6), ("rpt", 7), ("rptE2", 8), ("oc3", 9))

class LumOpticalService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("gigE1", 2), ("gigE2", 3), ("fiberChannel1", 4), ("fiberChannel2", 5), ("oc12", 6), ("oc24", 7), ("oc48", 8), ("rpt", 9), ("rptE2", 10), ("oc3", 11))

class LumTdmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("t1", 2), ("e1", 3), ("t3", 4), ("e3", 5))

class LumImageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("empty", 1), ("trial", 2), ("tried", 3), ("accepted", 4), ("unknown", 5))

class LumAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 1), ("critical", 2), ("major", 3), ("minor", 4), ("notAlarmed", 5), ("notReported", 6))

class LumResetCmd(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("reset", 2))

mibBuilder.exportSymbols("LUMINOUS-TC-MIB", LumName=LumName, LumCardType=LumCardType, LumSerialNumString=LumSerialNumString, LumOperStatus=LumOperStatus, LumAdminStatus=LumAdminStatus, LumSignalState=LumSignalState, LumChassisPlane=LumChassisPlane, LumVersionString=LumVersionString, LumControl=LumControl, LumPortCreateType=LumPortCreateType, LumPortDemuxId=LumPortDemuxId, LumSimpleIndex=LumSimpleIndex, LumOpticalService=LumOpticalService, LumTdmType=LumTdmType, LumPercent=LumPercent, LumRingDirection=LumRingDirection, LumOpticalMaxLength=LumOpticalMaxLength, LumCleiString=LumCleiString, LumManufactureString=LumManufactureString, LumSlotNum=LumSlotNum, LumDateTimeString=LumDateTimeString, lumTcMIB=lumTcMIB, LumDescr=LumDescr, LumCardFailureState=LumCardFailureState, LumResetCmd=LumResetCmd, LumOpticalConnector=LumOpticalConnector, luminous=luminous, LumOpticalServiceSupport=LumOpticalServiceSupport, PYSNMP_MODULE_ID=lumTcMIB, LumShelfType=LumShelfType, LumConnectorType=LumConnectorType, LumCardBaseType=LumCardBaseType, LumAlarmSeverity=LumAlarmSeverity, lumADM=lumADM, LumPortNum=LumPortNum, LumOpticalFiberType=LumOpticalFiberType, LumCardAdminState=LumCardAdminState, LumServiceMode=LumServiceMode, LumOpticalWaveLength=LumOpticalWaveLength, LumPortType=LumPortType, LumImageState=LumImageState, LumPortDemuxType=LumPortDemuxType, LumCardOperState=LumCardOperState)
