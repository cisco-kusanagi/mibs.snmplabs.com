#
# PySNMP MIB module REDSTONE-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-OSPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ospfIfEntry, = mibBuilder.importSymbols("OSPF-MIB", "ospfIfEntry")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Counter32, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Gauge32, Bits, Unsigned32, Counter64, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Gauge32", "Bits", "Unsigned32", "Counter64", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsOspfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 14))
rsOspfMIB.setRevisions(('1998-01-01 00:00',))
if mibBuilder.loadTexts: rsOspfMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsOspfMIB.setOrganization('Redstone Communications, Inc.')
rsOspfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1))
rsOspfGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1))
rsOspfProcessId = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsOspfProcessId.setStatus('current')
rsOspfMaxPathSplits = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsOspfMaxPathSplits.setStatus('current')
rsOspfSpfHoldInterval = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsOspfSpfHoldInterval.setStatus('current')
rsOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2), )
if mibBuilder.loadTexts: rsOspfIfTable.setStatus('current')
rsOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2, 1), )
ospfIfEntry.registerAugmentions(("REDSTONE-OSPF-MIB", "rsOspfIfEntry"))
rsOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
if mibBuilder.loadTexts: rsOspfIfEntry.setStatus('current')
rsOspfIfCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsOspfIfCost.setStatus('current')
rsOspfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4))
rsOspfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 1))
rsOspfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2))
rsOspfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 1, 1)).setObjects(("REDSTONE-OSPF-MIB", "rsOspfBasicGroup"), ("REDSTONE-OSPF-MIB", "rsOspfIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsOspfCompliance = rsOspfCompliance.setStatus('current')
rsOspfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2, 1)).setObjects(("REDSTONE-OSPF-MIB", "rsOspfProcessId"), ("REDSTONE-OSPF-MIB", "rsOspfMaxPathSplits"), ("REDSTONE-OSPF-MIB", "rsOspfSpfHoldInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsOspfBasicGroup = rsOspfBasicGroup.setStatus('current')
rsOspfIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2, 2)).setObjects(("REDSTONE-OSPF-MIB", "rsOspfIfCost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsOspfIfGroup = rsOspfIfGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-OSPF-MIB", rsOspfIfEntry=rsOspfIfEntry, PYSNMP_MODULE_ID=rsOspfMIB, rsOspfProcessId=rsOspfProcessId, rsOspfCompliances=rsOspfCompliances, rsOspfCompliance=rsOspfCompliance, rsOspfMaxPathSplits=rsOspfMaxPathSplits, rsOspfIfTable=rsOspfIfTable, rsOspfGroups=rsOspfGroups, rsOspfGeneralGroup=rsOspfGeneralGroup, rsOspfConformance=rsOspfConformance, rsOspfObjects=rsOspfObjects, rsOspfIfGroup=rsOspfIfGroup, rsOspfBasicGroup=rsOspfBasicGroup, rsOspfMIB=rsOspfMIB, rsOspfIfCost=rsOspfIfCost, rsOspfSpfHoldInterval=rsOspfSpfHoldInterval)
