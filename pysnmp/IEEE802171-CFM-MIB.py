#
# PySNMP MIB module IEEE802171-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE802171-CFM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
LldpManAddress, LldpPortIdSubtype, LldpChassisIdSubtype, LldpChassisId, LldpPortId = mibBuilder.importSymbols("LLDP-MIB", "LldpManAddress", "LldpPortIdSubtype", "LldpChassisIdSubtype", "LldpChassisId", "LldpPortId")
VlanIdOrNone, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, IpAddress, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, zeroDotZero, Unsigned32, Counter64, TimeTicks, iso, ModuleIdentity, ObjectIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "zeroDotZero", "Unsigned32", "Counter64", "TimeTicks", "iso", "ModuleIdentity", "ObjectIdentity", "Integer32", "Bits")
RowStatus, TruthValue, TimeStamp, DisplayString, TextualConvention, TimeInterval, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention", "TimeInterval", "MacAddress")
TransportAddress, TransportDomain = mibBuilder.importSymbols("TRANSPORT-ADDRESS-MIB", "TransportAddress", "TransportDomain")
ieee8021cfmMIB = ModuleIdentity((1, 0, 8802, 1, 1, 3))
ieee8021cfmMIB.setRevisions(('2006-11-04 00:00',))
if mibBuilder.loadTexts: ieee8021cfmMIB.setLastUpdated('200611040000Z')
if mibBuilder.loadTexts: ieee8021cfmMIB.setOrganization('IEEE 802.1 Working Group')
dot1agNotifications = MibIdentifier((1, 0, 8802, 1, 1, 3, 0))
dot1agMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 3, 1))
dot1agCfmStack = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 1))
dot1agCfmDefaultMdLevel = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 2))
dot1agCfmConfigErrorList = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 3))
dot1agCfmMd = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 4))
dot1agCfmMa = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 5))
dot1agCfmMep = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 6))
class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5, Table 21-19'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4))

class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    reference = '802.1ag clause 21.6.5'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 43)

class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5.4, Table 21-20'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4))

class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    reference = '802.1ag clauses 21.6.5.4, 21.6.5.5, 21.6.5.6'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class Dot1agCfmMaintenanceDomainLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class Dot1agCfmMpDirection(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.3.2:c'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class Dot1agCfmPortStatus(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.6.3:f, 20.19.3 and 21.5.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("psNoPortStateTLV", 0), ("psBlocked", 1), ("psUp", 2))

class Dot1agCfmInterfaceStatus(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.6.3:g, 20.19.4 and 21.5.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("isNoInterfaceSatatusTLV", 0), ("isUp", 1), ("isDown", 2), ("isTesting", 3), ("isUnknown", 4), ("isDormant", 5), ("isNotPresent", 6), ("isLowerLayerDown", 7))

class Dot1agCfmHighestDefectPri(TextualConvention, Integer32):
    reference = '802.1ag clause 20.1.2, 12.14.7.7.2:c and 20.33.9'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("defRDICCM", 2), ("defMACstatus", 3), ("defRemoteCCM", 4), ("defErrorCCM", 5), ("defXconCCM", 6))

class Dot1agCfmLowestAlarmPri(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:k and 20.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noDef", 6))

class Dot1agCfmMepId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8191)

class Dot1agCfmMepIdOrZero(TextualConvention, Unsigned32):
    reference = '802.1ag clause 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), )
class Dot1agCfmMhfCreation(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.5.1.3:c and 22.2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3))

class Dot1agCfmCcmInterval(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.1.3:d, 20.8.1 and 21.6.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("intervalInvalid", 0), ("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7))

class Dot1agCfmFngState(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:f and 20.35'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5))

class Dot1agCfmRelayActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.5, 21.9.5, and Table 21-27'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3))

class Dot1agCfmIngressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.6, 21.9.8.1, and Table 21-30 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4))

class Dot1agCfmEgressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:o, 20.36.2.10, 21.9.9.1, and Table 21-32'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4))

class Dot1agCfmRemoteMepState(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.6.3:b, 20.22'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("rMepIdle", 1), ("rMepStart", 2), ("rMepFailed", 3), ("rMepOk", 4))

class Dot1afCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Dot1agCfmConfigErrors(TextualConvention, Bits):
    reference = '802.1ag clause 12.14.4.1.3:b and clauses 22.2.3 and 22.2.4'
    status = 'current'
    namedValues = NamedValues(("cfmLeak", 0), ("conflictingVids", 1), ("excessiveLevels", 2), ("overlappedLevels", 3))

dot1agCfmStackTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: dot1agCfmStackTable.setStatus('current')
dot1agCfmStackEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmStackifIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmStackDirection"))
if mibBuilder.loadTexts: dot1agCfmStackEntry.setStatus('current')
dot1agCfmStackifIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot1agCfmStackifIndex.setStatus('current')
dot1agCfmStackDirection = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 2), Dot1agCfmMpDirection())
if mibBuilder.loadTexts: dot1agCfmStackDirection.setStatus('current')
dot1agCfmStackMepId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 3), Dot1agCfmMepIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMepId.setStatus('current')
dot1agCfmStackMacAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMacAddress.setStatus('current')
dot1agCfmDefaultMdLevelTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 1), )
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelTable.setStatus('current')
dot1agCfmDefaultMdLevelEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelIndex"))
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelEntry.setStatus('current')
dot1agCfmDefaultMdLevelIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelIndex.setStatus('current')
dot1agCfmDefaultMdLevelVid = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 2), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelVid.setStatus('current')
dot1agCfmDefaultMdLevelMhfCreation = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 3), Dot1agCfmMhfCreation().clone('defMHFnone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelMhfCreation.setStatus('current')
dot1agCfmDefaultMdLevelLevel = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 4), Dot1agCfmMaintenanceDomainLevel().clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevelLevel.setStatus('current')
dot1agCfmConfigErrorListTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 3, 1), )
if mibBuilder.loadTexts: dot1agCfmConfigErrorListTable.setStatus('current')
dot1agCfmConfigErrorListEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 3, 1, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListVid"), (0, "IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListIfIndex"))
if mibBuilder.loadTexts: dot1agCfmConfigErrorListEntry.setStatus('current')
dot1agCfmConfigErrorListVid = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: dot1agCfmConfigErrorListVid.setStatus('current')
dot1agCfmConfigErrorListIfIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: dot1agCfmConfigErrorListIfIndex.setStatus('current')
dot1agCfmConfigErrorListErrorType = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 3, 1, 1, 3), Dot1agCfmConfigErrors()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmConfigErrorListErrorType.setStatus('current')
dot1agCfmMdTableNextIndex = MibScalar((1, 0, 8802, 1, 1, 3, 1, 4, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdTableNextIndex.setStatus('current')
dot1agCfmMdTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 4, 2), )
if mibBuilder.loadTexts: dot1agCfmMdTable.setStatus('current')
dot1agCfmMdEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"))
if mibBuilder.loadTexts: dot1agCfmMdEntry.setStatus('current')
dot1agCfmMdIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmMdIndex.setStatus('current')
dot1agCfmMdFormat = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 2), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdFormat.setStatus('current')
dot1agCfmMdName = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 3), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdName.setStatus('current')
dot1agCfmMdLevel = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 4), Dot1agCfmMaintenanceDomainLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdLevel.setStatus('current')
dot1agCfmMdMhfCreation = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 5), Dot1agCfmMhfCreation().clone('defMHFnone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setStatus('current')
dot1agCfmMdFaultAlarmDestDomain = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 6), TransportDomain().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdFaultAlarmDestDomain.setStatus('current')
dot1agCfmMdFaulAlarmDestAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 7), TransportAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdFaulAlarmDestAddress.setStatus('current')
dot1agCfmMdRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 4, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdRowStatus.setStatus('current')
dot1agCfmMaTableNextIndex = MibScalar((1, 0, 8802, 1, 1, 3, 1, 5, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaTableNextIndex.setStatus('current')
dot1agCfmMaTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 5, 3), )
if mibBuilder.loadTexts: dot1agCfmMaTable.setStatus('current')
dot1agCfmMaEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: dot1agCfmMaEntry.setStatus('current')
dot1agCfmMaIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(16777217, 4294967295), )))
if mibBuilder.loadTexts: dot1agCfmMaIndex.setStatus('current')
dot1agCfmMaFormat = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 2), Dot1agCfmMaintAssocNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaFormat.setStatus('current')
dot1agCfmMaName = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 3), Dot1agCfmMaintAssocName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaName.setStatus('current')
dot1agCfmMaMhfCreation = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 4), Dot1agCfmMhfCreation().clone('defMHFnone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMhfCreation.setStatus('current')
dot1agCfmMaCcmInterval = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 5), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCcmInterval.setStatus('current')
dot1agCfmMaFaultAlarmDestDomain = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 6), TransportDomain().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaFaultAlarmDestDomain.setStatus('current')
dot1agCfmMaFaulAlarmDestAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 7), TransportAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaFaulAlarmDestAddress.setStatus('current')
dot1agCfmMaMoreThanOneVid = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMoreThanOneVid.setStatus('current')
dot1agCfmMaRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaRowStatus.setStatus('current')
dot1agCfmMaVlanTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 5, 4), )
if mibBuilder.loadTexts: dot1agCfmMaVlanTable.setStatus('current')
dot1agCfmMaVlanEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 5, 4, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaVlanVid"))
if mibBuilder.loadTexts: dot1agCfmMaVlanEntry.setStatus('current')
dot1agCfmMaVlanVid = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 4, 1, 1), VlanId())
if mibBuilder.loadTexts: dot1agCfmMaVlanVid.setStatus('current')
dot1agCfmMaVlanRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaVlanRowStatus.setStatus('current')
dot1agCfmMaMepListTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 5, 8), )
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setStatus('current')
dot1agCfmMaMepListEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 5, 8, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaMepListIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMaMepListEntry.setStatus('current')
dot1agCfmMaMepListIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 8, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMaMepListIdentifier.setStatus('current')
dot1agCfmMaMepListRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 5, 8, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMepListRowStatus.setStatus('current')
dot1agCfmMepTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 6, 1), )
if mibBuilder.loadTexts: dot1agCfmMepTable.setStatus('current')
dot1agCfmMepEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMepEntry.setStatus('current')
dot1agCfmMepIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMepIdentifier.setStatus('current')
dot1agCfmMepIfIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setStatus('current')
dot1agCfmMepDirection = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDirection.setStatus('current')
dot1agCfmMepPrimaryVid = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setStatus('current')
dot1agCfmMepActive = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepActive.setStatus('current')
dot1agCfmMepFngState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 6), Dot1agCfmFngState().clone('fngReset')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepFngState.setStatus('current')
dot1agCfmMepCciEnabled = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setStatus('current')
dot1agCfmMepCcmLtmPriority = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setStatus('current')
dot1agCfmMepMacAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setStatus('current')
dot1agCfmMepFaultAlarmDestDomain = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 10), TransportDomain().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFaultAlarmDestDomain.setStatus('current')
dot1agCfmMepFaulAlarmDestAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 11), TransportAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFaulAlarmDestAddress.setStatus('current')
dot1agCfmMepLowPrDef = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 12), Dot1agCfmLowestAlarmPri().clone('macRemErrXcon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setStatus('current')
dot1agCfmMepFngAlarmTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 13), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250, 1000)).clone(250)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFngAlarmTime.setStatus('current')
dot1agCfmMepFngResetTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 14), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250, 1000)).clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFngResetTime.setStatus('current')
dot1agCfmMepHighestPrDefect = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 15), Dot1agCfmHighestDefectPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setStatus('current')
dot1agCfmMepSomeRdiDefect = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepSomeRdiDefect.setStatus('current')
dot1agCfmMepErrMacStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepErrMacStatus.setStatus('current')
dot1agCfmMepSomeRMepCcmDefect = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepSomeRMepCcmDefect.setStatus('current')
dot1agCfmMepErrorCcmDefect = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepErrorCcmDefect.setStatus('current')
dot1agCfmMepXconCcmDefect = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepXconCcmDefect.setStatus('current')
dot1agCfmMepErrorCcmLastFailure = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepErrorCcmLastFailure.setStatus('current')
dot1agCfmMepXconCcmLastFailure = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepXconCcmLastFailure.setStatus('current')
dot1agCfmMepRCcmSequenceErrors = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepRCcmSequenceErrors.setStatus('current')
dot1agCfmMepCciSentCcms = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setStatus('current')
dot1agCfmMepNextLbmTransId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepNextLbmTransId.setStatus('current')
dot1agCfmMepLbrIn = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setStatus('current')
dot1agCfmMepLbrInOutOfOrder = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setStatus('current')
dot1agCfmMepLbrBadMsdu = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setStatus('current')
dot1agCfmMepLtmNextSeqNumber = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 29), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setStatus('current')
dot1agCfmMepUnexpLtrIn = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setStatus('current')
dot1agCfmMepLbrOut = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setStatus('current')
dot1agCfmMepTransmitLbmStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 32), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmStatus.setStatus('current')
dot1agCfmMepTransmitLbmDestMacAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 33), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMacAddress.setStatus('current')
dot1agCfmMepTransmitLbmDestMepId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 34), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMepId.setStatus('current')
dot1agCfmMepTransmitLbmDestIsMepId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 35), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestIsMepId.setStatus('current')
dot1agCfmMepTransmitLbmMessages = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmMessages.setStatus('current')
dot1agCfmMepTransmitLbmDataTlv = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 37), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1500))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDataTlv.setStatus('current')
dot1agCfmMepTransmitLbmVlanPriority = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanPriority.setStatus('current')
dot1agCfmMepTransmitLbmVlanDropEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 39), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanDropEnable.setStatus('current')
dot1agCfmMepTransmitLbmResultOK = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 40), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmResultOK.setStatus('current')
dot1agCfmMepTransmitLbmSeqNumber = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 41), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 42), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmStatus.setStatus('current')
dot1agCfmMepTransmitLtmFlags = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 43), Bits().clone(namedValues=NamedValues(("useFDBonly", 0))).clone(namedValues=NamedValues(("useFDBonly", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmFlags.setStatus('current')
dot1agCfmMepTransmitLtmTargetMacAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 44), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMacAddress.setStatus('current')
dot1agCfmMepTransmitLtmTargetMepId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 45), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMepId.setStatus('current')
dot1agCfmMepTransmitLtmTargetIsMepId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 46), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetIsMepId.setStatus('current')
dot1agCfmMepTransmitLtmTtl = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 47), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTtl.setStatus('current')
dot1agCfmMepTransmitLtmResult = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 48), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmResult.setStatus('current')
dot1agCfmMepTransmitLtmSeqNumber = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 49), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmEgressIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 50), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmEgressIdentifier.setStatus('current')
dot1agCfmMepRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepRowStatus.setStatus('current')
dot1agCfmLtrTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 6, 2), )
if mibBuilder.loadTexts: dot1agCfmLtrTable.setStatus('current')
dot1agCfmLtrEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE802171-CFM-MIB", "dot1agCfmLtrSeqNumber"), (0, "IEEE802171-CFM-MIB", "dot1agCfmLtrReceiveOrder"))
if mibBuilder.loadTexts: dot1agCfmLtrEntry.setStatus('current')
dot1agCfmLtrSeqNumber = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setStatus('current')
dot1agCfmLtrReceiveOrder = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setStatus('current')
dot1agCfmLtrTtl = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setStatus('current')
dot1agCfmLtrForwarded = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setStatus('current')
dot1agCfmLtrTerminalMep = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setStatus('current')
dot1agCfmLtrLastEgressIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setStatus('current')
dot1agCfmLtrNextEgressIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setStatus('current')
dot1agCfmLtrRelay = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 8), Dot1agCfmRelayActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setStatus('current')
dot1agCfmLtrChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 9), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrChassisIdSubtype.setStatus('current')
dot1agCfmLtrChassisId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 10), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrChassisId.setStatus('current')
dot1agCfmLtrManAddressType = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 11), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrManAddressType.setStatus('current')
dot1agCfmLtrManAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 12), LldpManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrManAddress.setStatus('current')
dot1agCfmLtrIngress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 13), Dot1agCfmIngressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setStatus('current')
dot1agCfmLtrIngressMac = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setStatus('current')
dot1agCfmLtrIngressPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 15), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressPortIdSubtype.setStatus('current')
dot1agCfmLtrIngressPortId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 16), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressPortId.setStatus('current')
dot1agCfmLtrEgress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 17), Dot1agCfmEgressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setStatus('current')
dot1agCfmLtrEgressMac = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 18), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setStatus('current')
dot1agCfmLtrEgressPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 19), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressPortIdSubtype.setStatus('current')
dot1agCfmLtrEgressPortId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 20), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressPortId.setStatus('current')
dot1agCfmLtrOrganizationSpecificTlv = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 2, 1, 21), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 1500), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrOrganizationSpecificTlv.setStatus('current')
dot1agCfmMepDbTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 6, 3), )
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setStatus('current')
dot1agCfmMepDbEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1), ).setIndexNames((0, "IEEE802171-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMepDbEntry.setStatus('current')
dot1agCfmMepDbRMepIdentifier = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMepDbRMepIdentifier.setStatus('current')
dot1agCfmMepDbRMepState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 2), Dot1agCfmRemoteMepState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRMepState.setStatus('current')
dot1agCfmMepDbRMepFailedOkTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRMepFailedOkTime.setStatus('current')
dot1agCfmMepDbMacAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setStatus('current')
dot1agCfmMepDbRdi = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setStatus('current')
dot1agCfmMepDbPortStatusTlv = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 6), Dot1agCfmPortStatus().clone('psNoPortStateTLV')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbPortStatusTlv.setStatus('current')
dot1agCfmMepDbInterfaceStatusTlv = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 7), Dot1agCfmInterfaceStatus().clone('isNoInterfaceSatatusTLV')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbInterfaceStatusTlv.setStatus('current')
dot1agCfmMepDbChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 8), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbChassisIdSubtype.setStatus('current')
dot1agCfmMepDbChassisId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 9), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbChassisId.setStatus('current')
dot1agCfmMepDbManAddressType = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 10), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbManAddressType.setStatus('current')
dot1agCfmMepDbManAddress = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 6, 3, 1, 11), LldpManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbManAddress.setStatus('current')
dot1agCfmFaultAlarm = NotificationType((1, 0, 8802, 1, 1, 3, 0, 1)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmMepHighestPrDefect"))
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setStatus('current')
dot1agCfmConformance = MibIdentifier((1, 0, 8802, 1, 1, 3, 2))
dot1agCfmCompliances = MibIdentifier((1, 0, 8802, 1, 1, 3, 2, 1))
dot1agCfmGroups = MibIdentifier((1, 0, 8802, 1, 1, 3, 2, 2))
dot1agCfmStackGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 1)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmStackMepId"), ("IEEE802171-CFM-MIB", "dot1agCfmStackMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmStackGroup = dot1agCfmStackGroup.setStatus('current')
dot1agCfmDefaultMdLevelGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 2)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelMhfCreation"), ("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelLevel"), ("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelVid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmDefaultMdLevelGroup = dot1agCfmDefaultMdLevelGroup.setStatus('current')
dot1agCfmConfigErrorListGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 3)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmConfigErrorListGroup = dot1agCfmConfigErrorListGroup.setStatus('current')
dot1agCfmMdGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 4)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmMdTableNextIndex"), ("IEEE802171-CFM-MIB", "dot1agCfmMdName"), ("IEEE802171-CFM-MIB", "dot1agCfmMdFormat"), ("IEEE802171-CFM-MIB", "dot1agCfmMdLevel"), ("IEEE802171-CFM-MIB", "dot1agCfmMdMhfCreation"), ("IEEE802171-CFM-MIB", "dot1agCfmMdFaultAlarmDestDomain"), ("IEEE802171-CFM-MIB", "dot1agCfmMdFaulAlarmDestAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMdRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMdGroup = dot1agCfmMdGroup.setStatus('current')
dot1agCfmMaGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 5)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmMaTableNextIndex"), ("IEEE802171-CFM-MIB", "dot1agCfmMaName"), ("IEEE802171-CFM-MIB", "dot1agCfmMaFormat"), ("IEEE802171-CFM-MIB", "dot1agCfmMaMhfCreation"), ("IEEE802171-CFM-MIB", "dot1agCfmMaCcmInterval"), ("IEEE802171-CFM-MIB", "dot1agCfmMaRowStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmMaVlanRowStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmMaFaultAlarmDestDomain"), ("IEEE802171-CFM-MIB", "dot1agCfmMaFaulAlarmDestAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMaMoreThanOneVid"), ("IEEE802171-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMaGroup = dot1agCfmMaGroup.setStatus('current')
dot1agCfmMepGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 6)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmMepIfIndex"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDirection"), ("IEEE802171-CFM-MIB", "dot1agCfmMepPrimaryVid"), ("IEEE802171-CFM-MIB", "dot1agCfmMepActive"), ("IEEE802171-CFM-MIB", "dot1agCfmMepFngState"), ("IEEE802171-CFM-MIB", "dot1agCfmMepCciEnabled"), ("IEEE802171-CFM-MIB", "dot1agCfmMepCcmLtmPriority"), ("IEEE802171-CFM-MIB", "dot1agCfmMepMacAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepFaultAlarmDestDomain"), ("IEEE802171-CFM-MIB", "dot1agCfmMepFaulAlarmDestAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLowPrDef"), ("IEEE802171-CFM-MIB", "dot1agCfmMepFngAlarmTime"), ("IEEE802171-CFM-MIB", "dot1agCfmMepFngResetTime"), ("IEEE802171-CFM-MIB", "dot1agCfmMepHighestPrDefect"), ("IEEE802171-CFM-MIB", "dot1agCfmMepSomeRdiDefect"), ("IEEE802171-CFM-MIB", "dot1agCfmMepErrMacStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmMepSomeRMepCcmDefect"), ("IEEE802171-CFM-MIB", "dot1agCfmMepErrorCcmDefect"), ("IEEE802171-CFM-MIB", "dot1agCfmMepXconCcmDefect"), ("IEEE802171-CFM-MIB", "dot1agCfmMepErrorCcmLastFailure"), ("IEEE802171-CFM-MIB", "dot1agCfmMepXconCcmLastFailure"), ("IEEE802171-CFM-MIB", "dot1agCfmMepRCcmSequenceErrors"), ("IEEE802171-CFM-MIB", "dot1agCfmMepCciSentCcms"), ("IEEE802171-CFM-MIB", "dot1agCfmMepNextLbmTransId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrIn"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrInOutOfOrder"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrBadMsdu"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLtmNextSeqNumber"), ("IEEE802171-CFM-MIB", "dot1agCfmMepUnexpLtrIn"), ("IEEE802171-CFM-MIB", "dot1agCfmMepLbrOut"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestMepId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDestIsMepId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmMessages"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmDataTlv"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmVlanPriority"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmVlanDropEnable"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmResultOK"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLbmSeqNumber"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmFlags"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMacAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMepId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTargetIsMepId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmTtl"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmResult"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber"), ("IEEE802171-CFM-MIB", "dot1agCfmMepTransmitLtmEgressIdentifier"), ("IEEE802171-CFM-MIB", "dot1agCfmMepRowStatus"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrForwarded"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrRelay"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrChassisIdSubtype"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrChassisId"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrManAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrManAddressType"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngress"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressMac"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressPortIdSubtype"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrIngressPortId"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgress"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressMac"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressPortIdSubtype"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrEgressPortId"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrTerminalMep"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrLastEgressIdentifier"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrNextEgressIdentifier"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrTtl"), ("IEEE802171-CFM-MIB", "dot1agCfmLtrOrganizationSpecificTlv"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepGroup = dot1agCfmMepGroup.setStatus('current')
dot1agCfmMepDbGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 7)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepState"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbRMepFailedOkTime"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbMacAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbRdi"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbPortStatusTlv"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbInterfaceStatusTlv"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbChassisIdSubtype"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbChassisId"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbManAddress"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbManAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepDbGroup = dot1agCfmMepDbGroup.setStatus('current')
dot1agCfmNotificationsGroup = NotificationGroup((1, 0, 8802, 1, 1, 3, 2, 2, 8)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmFaultAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmNotificationsGroup = dot1agCfmNotificationsGroup.setStatus('current')
dot1agCfmCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 3, 2, 1, 1)).setObjects(("IEEE802171-CFM-MIB", "dot1agCfmStackGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmDefaultMdLevelGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmConfigErrorListGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmMdGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmMaGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmMepGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmMepDbGroup"), ("IEEE802171-CFM-MIB", "dot1agCfmNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmCompliance = dot1agCfmCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE802171-CFM-MIB", PYSNMP_MODULE_ID=ieee8021cfmMIB, dot1agCfmMepFngAlarmTime=dot1agCfmMepFngAlarmTime, dot1agCfmNotificationsGroup=dot1agCfmNotificationsGroup, dot1agCfmMepTransmitLtmTtl=dot1agCfmMepTransmitLtmTtl, dot1agCfmMepFaultAlarmDestDomain=dot1agCfmMepFaultAlarmDestDomain, Dot1agCfmEgressActionFieldValue=Dot1agCfmEgressActionFieldValue, dot1agCfmMepDbRMepFailedOkTime=dot1agCfmMepDbRMepFailedOkTime, dot1agCfmMepSomeRdiDefect=dot1agCfmMepSomeRdiDefect, dot1agCfmMepDbRdi=dot1agCfmMepDbRdi, dot1agCfmMepTransmitLbmVlanPriority=dot1agCfmMepTransmitLbmVlanPriority, Dot1agCfmCcmInterval=Dot1agCfmCcmInterval, dot1agCfmMepXconCcmLastFailure=dot1agCfmMepXconCcmLastFailure, dot1agCfmMaTable=dot1agCfmMaTable, Dot1agCfmHighestDefectPri=Dot1agCfmHighestDefectPri, dot1agCfmStackGroup=dot1agCfmStackGroup, dot1agCfmLtrManAddress=dot1agCfmLtrManAddress, Dot1agCfmMaintAssocNameType=Dot1agCfmMaintAssocNameType, dot1agCfmMep=dot1agCfmMep, dot1agCfmMdEntry=dot1agCfmMdEntry, dot1agCfmMepTransmitLtmEgressIdentifier=dot1agCfmMepTransmitLtmEgressIdentifier, dot1agCfmLtrIngressMac=dot1agCfmLtrIngressMac, dot1agCfmMepTransmitLbmVlanDropEnable=dot1agCfmMepTransmitLbmVlanDropEnable, dot1agCfmMaFormat=dot1agCfmMaFormat, dot1agCfmMepTransmitLtmTargetIsMepId=dot1agCfmMepTransmitLtmTargetIsMepId, dot1agCfmLtrTtl=dot1agCfmLtrTtl, dot1agCfmMdMhfCreation=dot1agCfmMdMhfCreation, dot1agCfmLtrReceiveOrder=dot1agCfmLtrReceiveOrder, dot1agCfmDefaultMdLevelLevel=dot1agCfmDefaultMdLevelLevel, dot1agCfmMepDbMacAddress=dot1agCfmMepDbMacAddress, dot1agCfmMepPrimaryVid=dot1agCfmMepPrimaryVid, dot1agCfmStackEntry=dot1agCfmStackEntry, dot1agCfmMepTransmitLtmStatus=dot1agCfmMepTransmitLtmStatus, dot1agCfmLtrSeqNumber=dot1agCfmLtrSeqNumber, ieee8021cfmMIB=ieee8021cfmMIB, dot1agCfmMaMepListTable=dot1agCfmMaMepListTable, dot1agCfmCompliance=dot1agCfmCompliance, dot1agCfmMepRCcmSequenceErrors=dot1agCfmMepRCcmSequenceErrors, dot1agCfmGroups=dot1agCfmGroups, dot1agCfmMepNextLbmTransId=dot1agCfmMepNextLbmTransId, dot1agCfmConformance=dot1agCfmConformance, dot1agCfmConfigErrorListErrorType=dot1agCfmConfigErrorListErrorType, dot1agCfmStack=dot1agCfmStack, dot1agCfmMepTransmitLtmResult=dot1agCfmMepTransmitLtmResult, dot1agCfmStackifIndex=dot1agCfmStackifIndex, dot1agCfmMdLevel=dot1agCfmMdLevel, dot1agCfmMepTransmitLtmFlags=dot1agCfmMepTransmitLtmFlags, dot1agCfmMepLbrInOutOfOrder=dot1agCfmMepLbrInOutOfOrder, dot1agCfmMaFaultAlarmDestDomain=dot1agCfmMaFaultAlarmDestDomain, dot1agCfmMaGroup=dot1agCfmMaGroup, Dot1agCfmInterfaceStatus=Dot1agCfmInterfaceStatus, dot1agCfmLtrTerminalMep=dot1agCfmLtrTerminalMep, dot1agCfmLtrIngress=dot1agCfmLtrIngress, dot1agCfmMaTableNextIndex=dot1agCfmMaTableNextIndex, dot1agCfmLtrEgressMac=dot1agCfmLtrEgressMac, dot1agCfmMaMepListEntry=dot1agCfmMaMepListEntry, dot1agCfmLtrLastEgressIdentifier=dot1agCfmLtrLastEgressIdentifier, dot1agCfmMepFngResetTime=dot1agCfmMepFngResetTime, dot1agCfmMepHighestPrDefect=dot1agCfmMepHighestPrDefect, dot1agCfmLtrChassisIdSubtype=dot1agCfmLtrChassisIdSubtype, dot1agCfmMepErrMacStatus=dot1agCfmMepErrMacStatus, dot1agCfmMepDbEntry=dot1agCfmMepDbEntry, dot1agCfmLtrEgressPortIdSubtype=dot1agCfmLtrEgressPortIdSubtype, dot1agCfmMepRowStatus=dot1agCfmMepRowStatus, dot1agCfmMepDbTable=dot1agCfmMepDbTable, Dot1agCfmFngState=Dot1agCfmFngState, dot1agCfmDefaultMdLevelIndex=dot1agCfmDefaultMdLevelIndex, dot1agCfmConfigErrorListEntry=dot1agCfmConfigErrorListEntry, dot1agCfmMaMhfCreation=dot1agCfmMaMhfCreation, dot1agCfmMaVlanRowStatus=dot1agCfmMaVlanRowStatus, dot1agCfmMepTransmitLbmDataTlv=dot1agCfmMepTransmitLbmDataTlv, dot1agCfmMepTransmitLtmSeqNumber=dot1agCfmMepTransmitLtmSeqNumber, dot1agCfmFaultAlarm=dot1agCfmFaultAlarm, Dot1agCfmMaintAssocName=Dot1agCfmMaintAssocName, Dot1agCfmMpDirection=Dot1agCfmMpDirection, dot1agNotifications=dot1agNotifications, dot1agCfmMaVlanTable=dot1agCfmMaVlanTable, dot1agCfmMepDbPortStatusTlv=dot1agCfmMepDbPortStatusTlv, Dot1agCfmConfigErrors=Dot1agCfmConfigErrors, dot1agCfmMepFngState=dot1agCfmMepFngState, dot1agCfmStackMacAddress=dot1agCfmStackMacAddress, dot1agCfmMepDbRMepIdentifier=dot1agCfmMepDbRMepIdentifier, dot1agCfmMepDbInterfaceStatusTlv=dot1agCfmMepDbInterfaceStatusTlv, dot1agCfmCompliances=dot1agCfmCompliances, dot1agCfmMaCcmInterval=dot1agCfmMaCcmInterval, dot1agCfmMaMepListRowStatus=dot1agCfmMaMepListRowStatus, dot1agCfmMepCciSentCcms=dot1agCfmMepCciSentCcms, Dot1agCfmPortStatus=Dot1agCfmPortStatus, dot1agCfmMa=dot1agCfmMa, dot1agCfmMdFormat=dot1agCfmMdFormat, dot1agCfmMepDbManAddress=dot1agCfmMepDbManAddress, dot1agCfmMepTransmitLbmDestMacAddress=dot1agCfmMepTransmitLbmDestMacAddress, dot1agCfmLtrRelay=dot1agCfmLtrRelay, dot1agCfmStackMepId=dot1agCfmStackMepId, dot1agCfmMepTransmitLtmTargetMepId=dot1agCfmMepTransmitLtmTargetMepId, dot1agCfmLtrManAddressType=dot1agCfmLtrManAddressType, dot1agCfmMepSomeRMepCcmDefect=dot1agCfmMepSomeRMepCcmDefect, dot1agCfmMepXconCcmDefect=dot1agCfmMepXconCcmDefect, dot1agCfmMdIndex=dot1agCfmMdIndex, Dot1agCfmLowestAlarmPri=Dot1agCfmLowestAlarmPri, dot1agCfmMepIdentifier=dot1agCfmMepIdentifier, dot1agCfmMepTransmitLbmStatus=dot1agCfmMepTransmitLbmStatus, dot1agCfmLtrNextEgressIdentifier=dot1agCfmLtrNextEgressIdentifier, dot1agCfmLtrIngressPortIdSubtype=dot1agCfmLtrIngressPortIdSubtype, dot1agCfmMepLtmNextSeqNumber=dot1agCfmMepLtmNextSeqNumber, dot1agCfmMaRowStatus=dot1agCfmMaRowStatus, dot1agCfmConfigErrorListGroup=dot1agCfmConfigErrorListGroup, dot1agCfmMepErrorCcmLastFailure=dot1agCfmMepErrorCcmLastFailure, dot1agCfmMdName=dot1agCfmMdName, dot1agCfmMdFaultAlarmDestDomain=dot1agCfmMdFaultAlarmDestDomain, Dot1agCfmMepId=Dot1agCfmMepId, dot1agMIBObjects=dot1agMIBObjects, dot1agCfmMdTable=dot1agCfmMdTable, dot1agCfmLtrChassisId=dot1agCfmLtrChassisId, dot1agCfmMaVlanEntry=dot1agCfmMaVlanEntry, dot1agCfmLtrEntry=dot1agCfmLtrEntry, dot1agCfmMaFaulAlarmDestAddress=dot1agCfmMaFaulAlarmDestAddress, Dot1agCfmMaintDomainName=Dot1agCfmMaintDomainName, dot1agCfmMaMoreThanOneVid=dot1agCfmMaMoreThanOneVid, dot1agCfmLtrOrganizationSpecificTlv=dot1agCfmLtrOrganizationSpecificTlv, Dot1agCfmIngressActionFieldValue=Dot1agCfmIngressActionFieldValue, Dot1agCfmMhfCreation=Dot1agCfmMhfCreation, dot1agCfmMaMepListIdentifier=dot1agCfmMaMepListIdentifier, dot1agCfmMepMacAddress=dot1agCfmMepMacAddress, dot1agCfmMepErrorCcmDefect=dot1agCfmMepErrorCcmDefect, dot1agCfmLtrIngressPortId=dot1agCfmLtrIngressPortId, Dot1agCfmMepIdOrZero=Dot1agCfmMepIdOrZero, dot1agCfmMepTransmitLbmDestIsMepId=dot1agCfmMepTransmitLbmDestIsMepId, dot1agCfmMepDbChassisIdSubtype=dot1agCfmMepDbChassisIdSubtype, Dot1agCfmMaintenanceDomainLevel=Dot1agCfmMaintenanceDomainLevel, dot1agCfmLtrEgress=dot1agCfmLtrEgress, dot1agCfmConfigErrorListIfIndex=dot1agCfmConfigErrorListIfIndex, dot1agCfmDefaultMdLevelTable=dot1agCfmDefaultMdLevelTable, dot1agCfmMepDbGroup=dot1agCfmMepDbGroup, Dot1agCfmRemoteMepState=Dot1agCfmRemoteMepState, dot1agCfmMepActive=dot1agCfmMepActive, dot1agCfmMepUnexpLtrIn=dot1agCfmMepUnexpLtrIn, dot1agCfmMepDirection=dot1agCfmMepDirection, dot1agCfmMepGroup=dot1agCfmMepGroup, dot1agCfmMepTransmitLbmDestMepId=dot1agCfmMepTransmitLbmDestMepId, dot1agCfmMdRowStatus=dot1agCfmMdRowStatus, dot1agCfmLtrTable=dot1agCfmLtrTable, dot1agCfmConfigErrorListTable=dot1agCfmConfigErrorListTable, dot1agCfmMepCcmLtmPriority=dot1agCfmMepCcmLtmPriority, dot1agCfmDefaultMdLevelEntry=dot1agCfmDefaultMdLevelEntry, dot1agCfmMdTableNextIndex=dot1agCfmMdTableNextIndex, dot1agCfmMepLbrOut=dot1agCfmMepLbrOut, dot1agCfmMaEntry=dot1agCfmMaEntry, dot1agCfmMepFaulAlarmDestAddress=dot1agCfmMepFaulAlarmDestAddress, dot1agCfmStackDirection=dot1agCfmStackDirection, dot1agCfmDefaultMdLevelGroup=dot1agCfmDefaultMdLevelGroup, dot1agCfmMaIndex=dot1agCfmMaIndex, dot1agCfmMepIfIndex=dot1agCfmMepIfIndex, dot1agCfmDefaultMdLevelVid=dot1agCfmDefaultMdLevelVid, dot1agCfmMepLbrIn=dot1agCfmMepLbrIn, dot1agCfmMepDbChassisId=dot1agCfmMepDbChassisId, dot1agCfmStackTable=dot1agCfmStackTable, Dot1agCfmMaintDomainNameType=Dot1agCfmMaintDomainNameType, Dot1agCfmRelayActionFieldValue=Dot1agCfmRelayActionFieldValue, dot1agCfmMdGroup=dot1agCfmMdGroup, dot1agCfmMaVlanVid=dot1agCfmMaVlanVid, dot1agCfmMepTransmitLtmTargetMacAddress=dot1agCfmMepTransmitLtmTargetMacAddress, dot1agCfmConfigErrorListVid=dot1agCfmConfigErrorListVid, dot1agCfmMepEntry=dot1agCfmMepEntry, dot1agCfmMepTransmitLbmResultOK=dot1agCfmMepTransmitLbmResultOK, dot1agCfmMepTransmitLbmSeqNumber=dot1agCfmMepTransmitLbmSeqNumber, dot1agCfmDefaultMdLevel=dot1agCfmDefaultMdLevel, dot1agCfmLtrEgressPortId=dot1agCfmLtrEgressPortId, dot1agCfmMepCciEnabled=dot1agCfmMepCciEnabled, dot1agCfmConfigErrorList=dot1agCfmConfigErrorList, dot1agCfmMepTable=dot1agCfmMepTable, dot1agCfmMepLbrBadMsdu=dot1agCfmMepLbrBadMsdu, dot1agCfmDefaultMdLevelMhfCreation=dot1agCfmDefaultMdLevelMhfCreation, dot1agCfmMepDbRMepState=dot1agCfmMepDbRMepState, Dot1afCfmIndexIntegerNextFree=Dot1afCfmIndexIntegerNextFree, dot1agCfmMepLowPrDef=dot1agCfmMepLowPrDef, dot1agCfmMd=dot1agCfmMd, dot1agCfmLtrForwarded=dot1agCfmLtrForwarded, dot1agCfmMdFaulAlarmDestAddress=dot1agCfmMdFaulAlarmDestAddress, dot1agCfmMepTransmitLbmMessages=dot1agCfmMepTransmitLbmMessages, dot1agCfmMaName=dot1agCfmMaName, dot1agCfmMepDbManAddressType=dot1agCfmMepDbManAddressType)
