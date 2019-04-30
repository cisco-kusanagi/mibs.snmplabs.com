#
# PySNMP MIB module AVICI-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-PROCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
aviciMibs, = mibBuilder.importSymbols("AVICI-SMI", "aviciMibs")
aviciSysInventoryId, = mibBuilder.importSymbols("AVICI-SYSTEM-MIB", "aviciSysInventoryId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Bits, Integer32, iso, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, TimeTicks, ObjectIdentity, Unsigned32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Integer32", "iso", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aviciProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 1, 7))
aviciProcessMIB.setRevisions(('1970-01-01 00:00', '0009-07-12 15:00',))
if mibBuilder.loadTexts: aviciProcessMIB.setLastUpdated('0009071215Z')
if mibBuilder.loadTexts: aviciProcessMIB.setOrganization('Avici Systems Inc')
aviciProcessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1))
aviciCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1), )
if mibBuilder.loadTexts: aviciCPUTotalTable.setStatus('current')
aviciCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1), ).setIndexNames((0, "AVICI-SYSTEM-MIB", "aviciSysInventoryId"))
if mibBuilder.loadTexts: aviciCPUTotalEntry.setStatus('current')
aviciCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal5sec.setStatus('current')
aviciCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal1min.setStatus('current')
aviciCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal5min.setStatus('current')
aviciProcessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2))
aviciProcessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1))
aviciProcessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2))
aviciProcessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1, 1)).setObjects(("AVICI-PROCESS-MIB", "aviciProcessCPUGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviciProcessMIBCompliance = aviciProcessMIBCompliance.setStatus('current')
aviciProcessCPUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2, 1)).setObjects(("AVICI-PROCESS-MIB", "aviciCPUTotal5sec"), ("AVICI-PROCESS-MIB", "aviciCPUTotal1min"), ("AVICI-PROCESS-MIB", "aviciCPUTotal5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviciProcessCPUGroup = aviciProcessCPUGroup.setStatus('current')
mibBuilder.exportSymbols("AVICI-PROCESS-MIB", aviciProcessMIBCompliances=aviciProcessMIBCompliances, aviciCPUTotal5min=aviciCPUTotal5min, aviciProcessMIBConformance=aviciProcessMIBConformance, aviciCPUTotalEntry=aviciCPUTotalEntry, PYSNMP_MODULE_ID=aviciProcessMIB, aviciCPUTotal5sec=aviciCPUTotal5sec, aviciProcessCPUGroup=aviciProcessCPUGroup, aviciProcessObjects=aviciProcessObjects, aviciProcessMIBGroups=aviciProcessMIBGroups, aviciProcessMIBCompliance=aviciProcessMIBCompliance, aviciCPUTotalTable=aviciCPUTotalTable, aviciCPUTotal1min=aviciCPUTotal1min, aviciProcessMIB=aviciProcessMIB)
