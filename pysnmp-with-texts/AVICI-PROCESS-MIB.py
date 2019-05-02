#
# PySNMP MIB module AVICI-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-PROCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
aviciMibs, = mibBuilder.importSymbols("AVICI-SMI", "aviciMibs")
aviciSysInventoryId, = mibBuilder.importSymbols("AVICI-SYSTEM-MIB", "aviciSysInventoryId")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ObjectIdentity, Unsigned32, iso, MibIdentifier, Integer32, Counter32, TimeTicks, Bits, Counter64, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ObjectIdentity", "Unsigned32", "iso", "MibIdentifier", "Integer32", "Counter32", "TimeTicks", "Bits", "Counter64", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aviciProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 1, 7))
aviciProcessMIB.setRevisions(('1970-01-01 00:00', '0009-07-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviciProcessMIB.setRevisionsDescriptions(('Changed mib arcs.', 'Added conformance information.',))
if mibBuilder.loadTexts: aviciProcessMIB.setLastUpdated('0009071215Z')
if mibBuilder.loadTexts: aviciProcessMIB.setOrganization('Avici Systems Inc')
if mibBuilder.loadTexts: aviciProcessMIB.setContactInfo(' Avici Systems, Inc. 101 Billerica Avenue North Billerica, MA 01862-1256 (978) 964-2000 (978) 964-2100 (fax) snmp@avici.com')
if mibBuilder.loadTexts: aviciProcessMIB.setDescription('The MIB module to describe Avici CPU statistics.')
aviciProcessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1))
aviciCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1), )
if mibBuilder.loadTexts: aviciCPUTotalTable.setStatus('current')
if mibBuilder.loadTexts: aviciCPUTotalTable.setDescription('A table of total CPU statistics for an Avici platform. ')
aviciCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1), ).setIndexNames((0, "AVICI-SYSTEM-MIB", "aviciSysInventoryId"))
if mibBuilder.loadTexts: aviciCPUTotalEntry.setStatus('current')
if mibBuilder.loadTexts: aviciCPUTotalEntry.setDescription('Overall information about the CPU load.')
aviciCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal5sec.setStatus('current')
if mibBuilder.loadTexts: aviciCPUTotal5sec.setDescription('The total CPU busy percentage on this platform in the last 5 second period.')
aviciCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal1min.setStatus('current')
if mibBuilder.loadTexts: aviciCPUTotal1min.setDescription('The total CPU busy percentage on this platform in the last 1 minute period.')
aviciCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviciCPUTotal5min.setStatus('current')
if mibBuilder.loadTexts: aviciCPUTotal5min.setDescription('The total CPU busy percentage on this platform in the last 5 minute period.')
aviciProcessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2))
aviciProcessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1))
aviciProcessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2))
aviciProcessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1, 1)).setObjects(("AVICI-PROCESS-MIB", "aviciProcessCPUGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviciProcessMIBCompliance = aviciProcessMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: aviciProcessMIBCompliance.setDescription('The compliance statement for aviciProcess.')
aviciProcessCPUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2, 1)).setObjects(("AVICI-PROCESS-MIB", "aviciCPUTotal5sec"), ("AVICI-PROCESS-MIB", "aviciCPUTotal1min"), ("AVICI-PROCESS-MIB", "aviciCPUTotal5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviciProcessCPUGroup = aviciProcessCPUGroup.setStatus('current')
if mibBuilder.loadTexts: aviciProcessCPUGroup.setDescription('Objects for CPU statistics.')
mibBuilder.exportSymbols("AVICI-PROCESS-MIB", aviciProcessMIB=aviciProcessMIB, aviciCPUTotal1min=aviciCPUTotal1min, aviciCPUTotal5min=aviciCPUTotal5min, aviciCPUTotalTable=aviciCPUTotalTable, aviciProcessMIBCompliances=aviciProcessMIBCompliances, aviciProcessObjects=aviciProcessObjects, aviciProcessMIBConformance=aviciProcessMIBConformance, aviciCPUTotalEntry=aviciCPUTotalEntry, aviciProcessMIBCompliance=aviciProcessMIBCompliance, aviciProcessCPUGroup=aviciProcessCPUGroup, PYSNMP_MODULE_ID=aviciProcessMIB, aviciCPUTotal5sec=aviciCPUTotal5sec, aviciProcessMIBGroups=aviciProcessMIBGroups)
