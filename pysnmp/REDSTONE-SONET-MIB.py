#
# PySNMP MIB module REDSTONE-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, IpAddress, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ModuleIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsSonetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 7))
rsSonetMIB.setRevisions(('1998-01-01 00:00',))
if mibBuilder.loadTexts: rsSonetMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsSonetMIB.setOrganization('Redstone Communications, Inc.')
rsSonetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1))
rsSonetMediumTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1), )
if mibBuilder.loadTexts: rsSonetMediumTable.setStatus('current')
rsSonetMediumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsSonetMediumEntry.setStatus('current')
rsSonetMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSonetMediumType.setStatus('current')
rsSonetMediumLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sonetNoLoop", 0), ("sonetFacilityLoop", 1), ("sonetTerminalLoop", 2), ("sonetOtherLoop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSonetMediumLoopbackConfig.setStatus('current')
rsSonetMediumTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("loop", 0), ("internal", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSonetMediumTimingSource.setStatus('current')
rsSonetMediumCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSonetMediumCircuitIdentifier.setStatus('current')
rsSonetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 7, 4))
rsSonetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 1))
rsSonetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 2))
rsSonetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 1, 1)).setObjects(("REDSTONE-SONET-MIB", "rsSonetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsSonetCompliance = rsSonetCompliance.setStatus('current')
rsSonetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 2, 1)).setObjects(("REDSTONE-SONET-MIB", "rsSonetMediumType"), ("REDSTONE-SONET-MIB", "rsSonetMediumLoopbackConfig"), ("REDSTONE-SONET-MIB", "rsSonetMediumTimingSource"), ("REDSTONE-SONET-MIB", "rsSonetMediumCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsSonetGroup = rsSonetGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-SONET-MIB", rsSonetMediumCircuitIdentifier=rsSonetMediumCircuitIdentifier, rsSonetCompliances=rsSonetCompliances, rsSonetGroup=rsSonetGroup, rsSonetObjects=rsSonetObjects, rsSonetMediumType=rsSonetMediumType, rsSonetMIB=rsSonetMIB, rsSonetMediumLoopbackConfig=rsSonetMediumLoopbackConfig, rsSonetMediumTimingSource=rsSonetMediumTimingSource, rsSonetMediumEntry=rsSonetMediumEntry, PYSNMP_MODULE_ID=rsSonetMIB, rsSonetGroups=rsSonetGroups, rsSonetConformance=rsSonetConformance, rsSonetCompliance=rsSonetCompliance, rsSonetMediumTable=rsSonetMediumTable)
