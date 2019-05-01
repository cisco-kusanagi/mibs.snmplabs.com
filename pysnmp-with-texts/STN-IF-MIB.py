#
# PySNMP MIB module STN-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Counter64, TimeTicks, MibIdentifier, iso, Gauge32, Counter32, Integer32, ObjectIdentity, Unsigned32, Bits, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "TimeTicks", "MibIdentifier", "iso", "Gauge32", "Counter32", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, stnSystems = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification", "stnSystems")
stnIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 3))
if mibBuilder.loadTexts: stnIfMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnIfMIB.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnIfMIB.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnIfMIB.setDescription('STN Interface MIB.')
stnInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1))
stnIfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2))
stnIf = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1))
class StnInterfaceType(TextualConvention, Integer32):
    description = 'Interface type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("ethernet", 2), ("sonet", 3), ("epif", 4), ("ds3", 5))

class StnIfOperStatus(TextualConvention, Integer32):
    description = 'Interface operational status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("up-non-redundant", 2), ("up-redundant", 3), ("down-non-redundant", 4), ("down-redundant", 5))

class StnIfDuplexType(TextualConvention, Integer32):
    description = 'Interface duplex type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("half", 2), ("full", 3))

stnIfTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: stnIfTable.setStatus('current')
if mibBuilder.loadTexts: stnIfTable.setDescription('A list of interface entries.')
stnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "STN-IF-MIB", "stnIfIndex"))
if mibBuilder.loadTexts: stnIfEntry.setStatus('current')
if mibBuilder.loadTexts: stnIfEntry.setDescription('Entry contains information about a particular interface.')
stnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnIfIndex.setDescription('A sequence number that identifies a particular interface in the chassis.')
stnIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfSlot.setStatus('current')
if mibBuilder.loadTexts: stnIfSlot.setDescription('The physical slot in which the interface exists.')
stnIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfPort.setStatus('current')
if mibBuilder.loadTexts: stnIfPort.setDescription('The physical port in which the interface exists.')
stnIfEngine1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfEngine1.setStatus('current')
if mibBuilder.loadTexts: stnIfEngine1.setDescription('The first physical engine ID associated with this interface.')
stnIfEngine2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfEngine2.setStatus('current')
if mibBuilder.loadTexts: stnIfEngine2.setDescription('The second physical engine ID associated with this interface.')
stnIfInternalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfInternalPort.setStatus('current')
if mibBuilder.loadTexts: stnIfInternalPort.setDescription('The physical internal port ID for this interface.')
stnIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 7), StnInterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfType.setStatus('current')
if mibBuilder.loadTexts: stnIfType.setDescription('The type of interface.')
stnIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 8), StnIfOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfOperStatus.setStatus('current')
if mibBuilder.loadTexts: stnIfOperStatus.setDescription('Operational status of the interface.')
stnIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfDescr.setStatus('current')
if mibBuilder.loadTexts: stnIfDescr.setDescription('A descriptive string used to describe the interface.')
stnIfDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 10), StnIfDuplexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIfDuplex.setStatus('current')
if mibBuilder.loadTexts: stnIfDuplex.setDescription('The duplex type of the interface.')
stnInterfaceUp = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 13)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"))
if mibBuilder.loadTexts: stnInterfaceUp.setStatus('current')
if mibBuilder.loadTexts: stnInterfaceUp.setDescription('A stnInterfaceUp trap signifies that the agent entity has detected that the stnIfOperStatus object in the STN-IF-MIB has transitioned from any disfunctional state, down-non-redundant(4) or down-redundant(5) to any functional state, up-non-redundant(2) or up-redundant(3). The generation of this trap can be controlled by the InterfaceUpTraps configuration object.')
stnInterfaceDown = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 14)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"))
if mibBuilder.loadTexts: stnInterfaceDown.setStatus('current')
if mibBuilder.loadTexts: stnInterfaceDown.setDescription('A stnInterfaceDown trap signifies that the agent entity has detected that the stnIfOperStatus object in the STN-IF-MIB has transitioned from any functional state, up-non-redundant(2) or up-redundant(3), to any disfunctional state, down-non-redundant(4) or down-redundant(5). The generation of this trap can be controlled by the InterfaceDownTraps configuration object.')
stnIfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1))
stnIfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2))
stnIfMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1, 1)).setObjects(("STN-IF-MIB", "stnIfMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnIfMibComplianceRev1 = stnIfMibComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: stnIfMibComplianceRev1.setDescription('The compliance statement for entities which implement the Spring Tide Networks Interface MIB.')
stnIfMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2, 1)).setObjects(("STN-IF-MIB", "stnIfIndex"), ("STN-IF-MIB", "stnIfSlot"), ("STN-IF-MIB", "stnIfPort"), ("STN-IF-MIB", "stnIfEngine1"), ("STN-IF-MIB", "stnIfEngine2"), ("STN-IF-MIB", "stnIfInternalPort"), ("STN-IF-MIB", "stnIfType"), ("STN-IF-MIB", "stnIfOperStatus"), ("STN-IF-MIB", "stnIfDescr"), ("STN-IF-MIB", "stnIfDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnIfMibGroup = stnIfMibGroup.setStatus('current')
if mibBuilder.loadTexts: stnIfMibGroup.setDescription('A collection of STN objects providing interface information.')
mibBuilder.exportSymbols("STN-IF-MIB", StnIfOperStatus=StnIfOperStatus, stnIf=stnIf, stnIfTable=stnIfTable, stnIfMibGroups=stnIfMibGroups, stnInterfaceDown=stnInterfaceDown, stnIfMibCompliances=stnIfMibCompliances, stnIfMibGroup=stnIfMibGroup, stnIfIndex=stnIfIndex, stnIfDescr=stnIfDescr, stnIfInternalPort=stnIfInternalPort, stnIfMibComplianceRev1=stnIfMibComplianceRev1, stnIfEntry=stnIfEntry, StnIfDuplexType=StnIfDuplexType, stnIfDuplex=stnIfDuplex, stnIfEngine1=stnIfEngine1, stnIfPort=stnIfPort, stnIfMIB=stnIfMIB, stnIfEngine2=stnIfEngine2, stnInterfaces=stnInterfaces, StnInterfaceType=StnInterfaceType, stnIfType=stnIfType, stnIfOperStatus=stnIfOperStatus, stnIfMibConformance=stnIfMibConformance, stnInterfaceUp=stnInterfaceUp, stnIfSlot=stnIfSlot, PYSNMP_MODULE_ID=stnIfMIB)
