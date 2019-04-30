#
# PySNMP MIB module A3COM-HUAWEI-DLDP-MIB (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from A3COM-HUAWEI-DLDP-MIB at Sun May  3 23:23:09 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( h3cCommon, ) = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, Gauge32, iso, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "Bits", "Counter32")
( TruthValue, MacAddress, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention")
h3cDldp = ModuleIdentity(h3cCommon.getName() + (43,)).setRevisions(("2004-12-13 00:00",))
class EnabledStatus(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("enabled", 1), ("disabled", 2),)

class DLDPStatus(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6,)
    namedValues = NamedValues(("initial", 1), ("inactive", 2), ("active", 3), ("advertisement", 4), ("probe", 5), ("disable", 6),)

class DLDPNeighborStatus(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("unidirection", 1), ("bidirection", 2), ("unknown", 3),)

h3cDLDPMibObject = MibIdentifier(h3cDldp.getName() + (1,))
h3cDLDPConfigGroup = MibIdentifier(h3cDLDPMibObject.getName() + (1,))
h3cDLDPWorkMode = MibScalar(h3cDLDPConfigGroup.getName() + (1,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("normal", 1), ("enhance", 2),)).clone('normal')).setMaxAccess("readwrite")
h3cDLDPSystemEnable = MibScalar(h3cDLDPConfigGroup.getName() + (2,), TruthValue()).setMaxAccess("readwrite")
h3cDLDPSystemReset = MibScalar(h3cDLDPConfigGroup.getName() + (3,), TruthValue()).setMaxAccess("readwrite")
h3cDLDPInterval = MibScalar(h3cDLDPConfigGroup.getName() + (4,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,100)).clone(5)).setMaxAccess("readwrite")
h3cDLDPAuthenticationMode = MibScalar(h3cDLDPConfigGroup.getName() + (5,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3),)).clone('none')).setMaxAccess("readwrite")
h3cDLDPAuthenticationPassword = MibScalar(h3cDLDPConfigGroup.getName() + (6,), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1,53))).setMaxAccess("readwrite")
h3cDLDPUnidirectionalShutdown = MibScalar(h3cDLDPConfigGroup.getName() + (7,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("auto", 1), ("manual", 2),)).clone('auto')).setMaxAccess("readwrite")
h3cDLDPPortStateTable = MibTable(h3cDLDPMibObject.getName() + (2,), )
h3cDLDPPortStateEntry = MibTableRow(h3cDLDPPortStateTable.getName() + (1,), ).setIndexNames((0, "A3COM-HUAWEI-DLDP-MIB", "ifIndex"))
h3cDLDPPortState = MibTableColumn(h3cDLDPPortStateEntry.getName() + (1,), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
h3cDLDPPortDLDPTable = MibTable(h3cDLDPMibObject.getName() + (3,), )
h3cDLDPPortDLDPEntry = MibTableRow(h3cDLDPPortDLDPTable.getName() + (1,), ).setIndexNames((0, "A3COM-HUAWEI-DLDP-MIB", "ifIndex"))
h3cDLDPPortDLDPState = MibTableColumn(h3cDLDPPortDLDPEntry.getName() + (1,), DLDPStatus()).setMaxAccess("readonly")
h3cDLDPLinkState = MibTableColumn(h3cDLDPPortDLDPEntry.getName() + (2,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("unknown", 3),))).setMaxAccess("readonly")
h3cDLDPPortDLDPReset = MibTableColumn(h3cDLDPPortDLDPEntry.getName() + (3,), TruthValue()).setMaxAccess("readwrite")
h3cDLDPNeighborTable = MibTable(h3cDLDPMibObject.getName() + (4,), )
h3cDLDPNeighborEntry = MibTableRow(h3cDLDPNeighborTable.getName() + (1,), ).setIndexNames((0, "A3COM-HUAWEI-DLDP-MIB", "ifIndex"), (0, "A3COM-HUAWEI-DLDP-MIB", "h3cDLDPNeighborBridgeMac"), (0, "A3COM-HUAWEI-DLDP-MIB", "h3cDLDPNeighborPortIndex"))
h3cDLDPNeighborBridgeMac = MibTableColumn(h3cDLDPNeighborEntry.getName() + (1,), MacAddress())
h3cDLDPNeighborPortIndex = MibTableColumn(h3cDLDPNeighborEntry.getName() + (2,), Integer32())
h3cDLDPNeighborState = MibTableColumn(h3cDLDPNeighborEntry.getName() + (3,), DLDPNeighborStatus()).setMaxAccess("readonly")
h3cDLDPNeighborAgingTime = MibTableColumn(h3cDLDPNeighborEntry.getName() + (4,), Integer32()).setMaxAccess("readonly")
h3cDLDPTrapObject = MibIdentifier(h3cDldp.getName() + (2,))
h3cDLDPNotification = MibIdentifier(h3cDLDPTrapObject.getName() + (1,))
h3cDLDPUnidirectionalPort = NotificationType(h3cDLDPNotification.getName() + (1,)).setObjects(*(("A3COM-HUAWEI-DLDP-MIB", "ifIndex"),))
mibBuilder.exportSymbols("A3COM-HUAWEI-DLDP-MIB", h3cDLDPUnidirectionalShutdown=h3cDLDPUnidirectionalShutdown, h3cDLDPLinkState=h3cDLDPLinkState, h3cDLDPPortDLDPState=h3cDLDPPortDLDPState, h3cDLDPSystemEnable=h3cDLDPSystemEnable, h3cDLDPPortStateTable=h3cDLDPPortStateTable, DLDPStatus=DLDPStatus, h3cDLDPPortState=h3cDLDPPortState, h3cDLDPPortDLDPTable=h3cDLDPPortDLDPTable, h3cDLDPNeighborEntry=h3cDLDPNeighborEntry, h3cDLDPPortStateEntry=h3cDLDPPortStateEntry, h3cDLDPNotification=h3cDLDPNotification, h3cDLDPNeighborTable=h3cDLDPNeighborTable, h3cDLDPPortDLDPReset=h3cDLDPPortDLDPReset, h3cDLDPMibObject=h3cDLDPMibObject, h3cDLDPWorkMode=h3cDLDPWorkMode, h3cDLDPAuthenticationMode=h3cDLDPAuthenticationMode, h3cDLDPConfigGroup=h3cDLDPConfigGroup, DLDPNeighborStatus=DLDPNeighborStatus, h3cDLDPUnidirectionalPort=h3cDLDPUnidirectionalPort, h3cDLDPNeighborState=h3cDLDPNeighborState, h3cDLDPInterval=h3cDLDPInterval, EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=h3cDldp, h3cDLDPNeighborPortIndex=h3cDLDPNeighborPortIndex, h3cDLDPTrapObject=h3cDLDPTrapObject, h3cDldp=h3cDldp, h3cDLDPNeighborAgingTime=h3cDLDPNeighborAgingTime, h3cDLDPSystemReset=h3cDLDPSystemReset, h3cDLDPNeighborBridgeMac=h3cDLDPNeighborBridgeMac, h3cDLDPPortDLDPEntry=h3cDLDPPortDLDPEntry, h3cDLDPAuthenticationPassword=h3cDLDPAuthenticationPassword)
