#
# PySNMP MIB module LUMINOUS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, enterprises, Integer32, Counter32, ObjectName, Unsigned32, Gauge32, iso, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "enterprises", "Integer32", "Counter32", "ObjectName", "Unsigned32", "Gauge32", "iso", "IpAddress", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 9))
if mibBuilder.loadTexts: lumTcMIB.setLastUpdated('0106270000Z')
if mibBuilder.loadTexts: lumTcMIB.setOrganization('Luminous Networks')
if mibBuilder.loadTexts: lumTcMIB.setContactInfo(' Luminous Technical Support Postal: Luminous Networks, 14060 Bubb Road, Cupertino, CA 95014 Tel: +1 408 342 6400 Fax: +1 408 863 1100 E-mail: support@luminous.com')
if mibBuilder.loadTexts: lumTcMIB.setDescription('The Luminous TC MIB contains textual conventions for use in Luminous Networks MIBs.')
class LumShelfType(TextualConvention, Integer32):
    description = 'Type of chassis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mSeries", 1), ("unused1", 2), ("unused2", 3), ("cSeries", 4))

class LumChassisPlane(TextualConvention, Integer32):
    description = 'Which plane in the chassis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("front", 1), ("back", 2))

class LumSlotNum(TextualConvention, Integer32):
    description = 'Number of a slot within a chassis plane. Note that 0 is not a valid slot and means unknown.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class LumPortNum(TextualConvention, Integer32):
    description = 'Number of a port within a card.. Note that 0 is not a valid port and means unknown.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class LumSimpleIndex(TextualConvention, Integer32):
    description = 'Simple abstract integer index for a table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class LumPercent(TextualConvention, Unsigned32):
    description = 'A percentage value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class LumRingDirection(TextualConvention, Integer32):
    description = 'Direction of a service of link from the ring point of view.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("west", 2), ("east", 3))

class LumAdminStatus(TextualConvention, Integer32):
    description = 'Administrative Status of an entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class LumOperStatus(TextualConvention, Integer32):
    description = 'Operational Status of an entity. This is based on IF-MIB ifOperStatus with the addition of misMatch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7), ("misMatch", 8))

class LumControl(TextualConvention, Integer32):
    description = 'Control of an entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3))

class LumServiceMode(TextualConvention, Integer32):
    description = 'Service type for a port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("wire", 2), ("routing", 3), ("policyForwarding", 4))

class LumPortType(TextualConvention, Integer32):
    description = 'What type of entity is this port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("physical", 2), ("subPortDemux", 3))

class LumPortCreateType(TextualConvention, Integer32):
    description = 'Was this port created explicitly or implicitly (e.g. chen channelizing a DS3, subports for DS1 are implicitly created.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("implicit", 1), ("explicit", 2))

class LumPortDemuxType(TextualConvention, Integer32):
    description = 'What type of entity is this demux port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("vlan", 2), ("mplsTag", 3), ("tdmChannel", 4))

class LumPortDemuxId(TextualConvention, Unsigned32):
    description = 'The substream identifier for this demux port.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LumConnectorType(TextualConvention, Integer32):
    description = 'Connector type for a physical port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("rj45", 2), ("scFiber", 3), ("miniCoax", 4), ("db9", 5), ("sjFiber", 6), ("stFiber", 7))

class LumSignalState(TextualConvention, Integer32):
    description = 'State of a hardware signal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("active", 2))

class LumName(DisplayString):
    description = 'Name of an entity. This should not include white space characters.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 40)

class LumDescr(DisplayString):
    description = 'Description of an entity.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 80)

class LumVersionString(DisplayString):
    description = 'Version of an entity. '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class LumSerialNumString(DisplayString):
    description = 'Serial number of an entity. '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 21)

class LumCleiString(DisplayString):
    description = 'CLEI code of an entity. '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 17)

class LumManufactureString(DisplayString):
    description = 'Manufacture date of an entity. '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class LumDateTimeString(DisplayString):
    description = 'Date and Time.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(24, 24)
    fixedLength = 24

class LumCardBaseType(TextualConvention, Integer32):
    description = 'The base type of a card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 28, 29, 32, 33, 34, 35, 36, 38))
    namedValues = NamedValues(("none", 1), ("sysCon", 2), ("ring", 3), ("t1", 4), ("ether", 5), ("alarm", 6), ("upLink", 7), ("ringIO", 8), ("t1IO", 9), ("etherIO", 10), ("utility", 11), ("oc12", 12), ("oc12IO", 13), ("gigE", 14), ("gigEIO", 15), ("oc12IOAlarm", 16), ("etherFXIO", 17), ("wdm", 18), ("wdmIO", 19), ("ringIOLR", 21), ("ring2", 22), ("ring2IO", 23), ("ds3cc12", 28), ("ds3cc12IO", 29), ("ether24", 32), ("ether24IO", 33), ("asi", 34), ("asiIOIn", 35), ("asiIOOut", 36), ("present", 38))

class LumCardType(TextualConvention, Integer32):
    description = 'The specific type of a card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("none", 1), ("sysCon", 2), ("ring", 3), ("t1", 4), ("ether", 5), ("alarm", 6), ("upLink", 7), ("ringIO", 8), ("t1IO", 9), ("etherIO", 10), ("utility", 11), ("oc12", 12), ("oc12IO", 13), ("gigE", 14), ("gigEIO", 15), ("oc12IOAlarm", 16), ("etherFXIO", 17), ("wdm", 18), ("wdmIO", 19), ("sysconR", 20), ("ringIOLR", 21), ("ring2", 22), ("ring2IO", 23), ("wdmBand1", 24), ("wdmBand2", 25), ("wdmBand3", 26), ("wdmBand4", 27), ("ds3cc12", 28), ("ds3cc12IO", 29), ("t3cc12", 30), ("e3cc12", 31), ("ether24", 32), ("ether24IO", 33), ("asi", 34), ("asiIOIn", 35), ("asiIOOut", 36), ("gigERouting", 37), ("present", 38), ("sysconU", 39), ("newCardType", 40))

class LumCardAdminState(TextualConvention, Integer32):
    description = 'The admininstrative state of a card. This indicates the state transition desired by the management. The actual success of transition is shown in the card operationla state. active(2) - request to set a card in an active but not backed up state. standby(3)- request to set a card to a standby state. outOfService(4) - request to set a card to OutOfService state, where it should respond to the management requests but not support any traffic activity. shutDown(5)-request to shut the card down completely. Deprecated. reset(6) -request to reset the card. switchover(7)- request to replace this card, currently in lumCardOperState of active(7) with the card currently in lumCardOperState of standby(3) which slot is referenced with lumStandbySlot. On success, lumCardOperState of this card should transition to outOfService(4).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("shutDown", 5), ("reset", 6), ("switchover", 7))

class LumCardOperState(TextualConvention, Integer32):
    description = "The operational state of a card. The Operational State indicates the current state of the card. It can be either the result of some administrative management action or internal card activity. none(1) - indicates that there is no card in the slot active (2) - means working fine, but not backed up standby(3) - means backing up other active(2) cards in case of a failure or management switchover requests outOfService(4) - a state where the card should respond to the management requests but not support any traffic activity. failure(5) - cannot function properly but still can respond to management requests. down(6) - card in the slot can't even respond to the management request. present(7) - card is present in the slot and not yet identified. initializing(8)-card is present in the slot and is initializing."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("failure", 5), ("down", 6), ("present", 7), ("initializing", 8))

class LumCardFailureState(TextualConvention, Integer32):
    description = "The failure state of a card. This is usually none(1), unless card operational state is equal to failure(5). Even if card operational state is equal to failure(5), still, this can be none(1), simply indicating that no information about this failure state is available. Otherwise criticalFault(2) indicates that the card cannot perform one of it's required functions properly. The management action is recommended (can be even reset or, if mulfunctioning, be replace) to correct the problem. Otherwise the problem will persist. minorFault(3) indicates that a fault has occured but does not persist. The action from the management may not beneeded. minorAlarm(4) indicates that no action is needed."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("criticalFault", 2), ("minorFault", 3), ("minorAlarm", 4))

class LumOpticalWaveLength(TextualConvention, Integer32):
    description = 'The wavelength in nano-meters of an optical interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class LumOpticalFiberType(TextualConvention, Integer32):
    description = 'The fiber type used by an optical interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("singleMode", 2), ("multiMode", 3))

class LumOpticalMaxLength(TextualConvention, Integer32):
    description = 'The maximum fiber length in meters of an optical interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000000)

class LumOpticalConnector(TextualConvention, Integer32):
    description = 'The connector type used by an optical interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("sc", 2), ("lc", 3))

class LumOpticalServiceSupport(TextualConvention, Bits):
    description = 'The service types supported by an optical interface.'
    status = 'current'
    namedValues = NamedValues(("gigE1", 0), ("gigE2", 1), ("fiberChannel1", 2), ("fiberChannel2", 3), ("oc12", 4), ("oc24", 5), ("oc48", 6), ("rpt", 7), ("rptE2", 8), ("oc3", 9))

class LumOpticalService(TextualConvention, Integer32):
    description = 'The service type active on an optical interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("gigE1", 2), ("gigE2", 3), ("fiberChannel1", 4), ("fiberChannel2", 5), ("oc12", 6), ("oc24", 7), ("oc48", 8), ("rpt", 9), ("rptE2", 10), ("oc3", 11))

class LumTdmType(TextualConvention, Integer32):
    description = 'The TDM port or connection type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("t1", 2), ("e1", 3), ("t3", 4), ("e3", 5))

class LumImageState(TextualConvention, Integer32):
    description = 'The state of a program image in NVRAM.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("empty", 1), ("trial", 2), ("tried", 3), ("accepted", 4), ("unknown", 5))

class LumAlarmSeverity(TextualConvention, Integer32):
    description = 'The severity of an alarm of group of alarms.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 1), ("critical", 2), ("major", 3), ("minor", 4), ("notAlarmed", 5), ("notReported", 6))

class LumResetCmd(TextualConvention, Integer32):
    description = 'Reset command for an entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("reset", 2))

mibBuilder.exportSymbols("LUMINOUS-TC-MIB", LumOperStatus=LumOperStatus, LumPortDemuxType=LumPortDemuxType, lumTcMIB=lumTcMIB, LumServiceMode=LumServiceMode, LumSignalState=LumSignalState, LumDateTimeString=LumDateTimeString, LumVersionString=LumVersionString, LumDescr=LumDescr, LumPortType=LumPortType, LumPortDemuxId=LumPortDemuxId, LumOpticalConnector=LumOpticalConnector, LumName=LumName, LumConnectorType=LumConnectorType, LumSimpleIndex=LumSimpleIndex, LumTdmType=LumTdmType, LumOpticalServiceSupport=LumOpticalServiceSupport, LumResetCmd=LumResetCmd, LumCardOperState=LumCardOperState, LumRingDirection=LumRingDirection, LumAdminStatus=LumAdminStatus, LumControl=LumControl, LumShelfType=LumShelfType, LumCardFailureState=LumCardFailureState, LumSlotNum=LumSlotNum, LumManufactureString=LumManufactureString, PYSNMP_MODULE_ID=lumTcMIB, LumCleiString=LumCleiString, LumChassisPlane=LumChassisPlane, LumCardBaseType=LumCardBaseType, LumPercent=LumPercent, LumOpticalWaveLength=LumOpticalWaveLength, LumAlarmSeverity=LumAlarmSeverity, LumPortNum=LumPortNum, LumOpticalFiberType=LumOpticalFiberType, luminous=luminous, LumSerialNumString=LumSerialNumString, LumOpticalService=LumOpticalService, LumCardType=LumCardType, LumPortCreateType=LumPortCreateType, LumCardAdminState=LumCardAdminState, LumOpticalMaxLength=LumOpticalMaxLength, LumImageState=LumImageState, lumADM=lumADM)
