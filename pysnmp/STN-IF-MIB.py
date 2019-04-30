#
# PySNMP MIB module STN-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, ObjectIdentity, Integer32, Counter32, Counter64, ModuleIdentity, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, stnSystems = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification", "stnSystems")
stnIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 3))
if mibBuilder.loadTexts: stnIfMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnIfMIB.setOrganization('Spring Tide Networks, Inc.')
stnInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1))
stnIfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2))
stnIf = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1))
class StnInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("ethernet", 2), ("sonet", 3), ("epif", 4), ("ds3", 5))

class StnIfOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("up-non-redundant", 2), ("up-redundant", 3), ("down-non-redundant", 4), ("down-redundant", 5))

class StnIfDuplexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("half", 2), ("full", 3))

stnIfTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: stnIfTable.setStatus('current')
stnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "STN-IF-MIB", "stnIfIndex"))
if mibBuilder.loadTexts: stnIfEntry.setStatus('current')
stnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfIndex.setStatus('current')
stnIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfSlot.setStatus('current')
stnIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfPort.setStatus('current')
stnIfEngine1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfEngine1.setStatus('current')
stnIfEngine2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfEngine2.setStatus('current')
stnIfInternalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfInternalPort.setStatus('current')
stnIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 7), StnInterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfType.setStatus('current')
stnIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 8), StnIfOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfOperStatus.setStatus('current')
stnIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfDescr.setStatus('current')
stnIfDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 10), StnIfDuplexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfDuplex.setStatus('current')
stnInterfaceUp = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 13)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"))
if mibBuilder.loadTexts: stnInterfaceUp.setStatus('current')
stnInterfaceDown = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 14)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"))
if mibBuilder.loadTexts: stnInterfaceDown.setStatus('current')
stnIfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1))
stnIfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2))
stnIfMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1, 1)).setObjects(("STN-IF-MIB", "stnIfMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnIfMibComplianceRev1 = stnIfMibComplianceRev1.setStatus('current')
stnIfMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2, 1)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"), ("STN-IF-MIB", "stnIfDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnIfMibGroup = stnIfMibGroup.setStatus('current')
mibBuilder.exportSymbols("STN-IF-MIB", stnIfDescr=stnIfDescr, stnIfPort=stnIfPort, stnIfMibConformance=stnIfMibConformance, stnIfIndex=stnIfIndex, StnInterfaceType=StnInterfaceType, PYSNMP_MODULE_ID=stnIfMIB, stnIf=stnIf, stnIfSlot=stnIfSlot, stnIfTable=stnIfTable, stnIfEngine1=stnIfEngine1, stnIfMibComplianceRev1=stnIfMibComplianceRev1, stnInterfaceUp=stnInterfaceUp, stnIfMibGroups=stnIfMibGroups, stnIfType=stnIfType, stnIfInternalPort=stnIfInternalPort, stnIfMIB=stnIfMIB, stnInterfaceDown=stnInterfaceDown, stnIfEngine2=stnIfEngine2, stnIfDuplex=stnIfDuplex, stnIfEntry=stnIfEntry, stnIfMibGroup=stnIfMibGroup, stnInterfaces=stnInterfaces, stnIfOperStatus=stnIfOperStatus, stnIfMibCompliances=stnIfMibCompliances, StnIfOperStatus=StnIfOperStatus, StnIfDuplexType=StnIfDuplexType)
