#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHERLIKE-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dot3StatsIndex, = mibBuilder.importSymbols("EtherLike-MIB", "dot3StatsIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Integer32, Unsigned32, MibIdentifier, TimeTicks, Bits, NotificationType, Gauge32, ModuleIdentity, Counter32, Counter64, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Unsigned32", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEtherExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 645))
ciscoEtherExtMIB.setRevisions(('2010-06-04 00:00', '2008-10-15 00:00', '2008-01-09 00:00',))
if mibBuilder.loadTexts: ciscoEtherExtMIB.setLastUpdated('201006040000Z')
if mibBuilder.loadTexts: ciscoEtherExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEtherExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 0))
ciscoEtherExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1))
ciscoEtherExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2))
ceeDot3PauseExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1))
ceeSubIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2))
ceeDot3PauseExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1), )
if mibBuilder.loadTexts: ceeDot3PauseExtTable.setStatus('current')
ceeDot3PauseExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: ceeDot3PauseExtEntry.setStatus('current')
ceeDot3PauseExtAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("txDesired", 0), ("rxDesired", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceeDot3PauseExtAdminMode.setStatus('current')
ceeDot3PauseExtOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("txDisagree", 0), ("rxDisagree", 1), ("txDesired", 2), ("rxDesired", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeDot3PauseExtOperMode.setStatus('current')
ceeSubInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1), )
if mibBuilder.loadTexts: ceeSubInterfaceTable.setStatus('current')
ceeSubInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceeSubInterfaceEntry.setStatus('current')
ceeSubInterfaceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('subifs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeSubInterfaceCount.setStatus('current')
ceeEtherExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1))
ceeEtherExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2))
ceeEtherExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBCompliance = ceeEtherExtMIBCompliance.setStatus('deprecated')
ceeEtherExtMIBComplianceR01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"), ("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBComplianceR01 = ceeEtherExtMIBComplianceR01.setStatus('current')
ciscoEtherExtPauseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtAdminMode"), ("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtPauseGroup = ciscoEtherExtPauseGroup.setStatus('current')
ciscoEtherExtSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeSubInterfaceCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtSubIfGroup = ciscoEtherExtSubIfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-MIB", ciscoEtherExtMIBObjects=ciscoEtherExtMIBObjects, ciscoEtherExtSubIfGroup=ciscoEtherExtSubIfGroup, ciscoEtherExtMIBNotifs=ciscoEtherExtMIBNotifs, ceeDot3PauseExtEntry=ceeDot3PauseExtEntry, ceeSubInterfaceTable=ceeSubInterfaceTable, ciscoEtherExtMIB=ciscoEtherExtMIB, ceeDot3PauseExtAdminMode=ceeDot3PauseExtAdminMode, ceeSubInterfaceCount=ceeSubInterfaceCount, ceeEtherExtMIBGroups=ceeEtherExtMIBGroups, ciscoEtherExtPauseGroup=ciscoEtherExtPauseGroup, ceeEtherExtMIBCompliances=ceeEtherExtMIBCompliances, ceeDot3PauseExtOperMode=ceeDot3PauseExtOperMode, ciscoEtherExtMIBConform=ciscoEtherExtMIBConform, ceeEtherExtMIBCompliance=ceeEtherExtMIBCompliance, ceeSubInterfaceEntry=ceeSubInterfaceEntry, ceeDot3PauseExtTable=ceeDot3PauseExtTable, ceeEtherExtMIBComplianceR01=ceeEtherExtMIBComplianceR01, ceeDot3PauseExt=ceeDot3PauseExt, PYSNMP_MODULE_ID=ciscoEtherExtMIB, ceeSubIf=ceeSubIf)
