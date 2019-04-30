#
# PySNMP MIB module ALTIGA-EVENT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-EVENT-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alEventMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alEventMibModule")
alEventGroup, alStatsEvent = mibBuilder.importSymbols("ALTIGA-MIB", "alEventGroup", "alStatsEvent")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, ModuleIdentity, Bits, iso, Gauge32, IpAddress, TimeTicks, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Bits", "iso", "Gauge32", "IpAddress", "TimeTicks", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaEventStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2))
altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaEventStatsMibModule.setLastUpdated('200301130000Z')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsEventGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1))
alStatsEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alStatsEventNotificationId.setStatus('current')
alEventStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2), )
if mibBuilder.loadTexts: alEventStatsTable.setStatus('current')
alEventStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1), ).setIndexNames((0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"))
if mibBuilder.loadTexts: alEventStatsEntry.setStatus('current')
alEventStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsClass.setStatus('current')
alEventStatsEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsEventNumber.setStatus('current')
alEventStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsCount.setStatus('current')
altigaEventStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1))
altigaEventStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1))
altigaEventStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibCompliance = altigaEventStatsMibCompliance.setStatus('deprecated')
altigaEventStatsMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibComplianceRev1 = altigaEventStatsMibComplianceRev1.setStatus('current')
altigaEventStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroup = altigaEventStatsGroup.setStatus('deprecated')
altigaEventStatsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"), ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroupRev1 = altigaEventStatsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-EVENT-STATS-MIB", alEventStatsClass=alEventStatsClass, altigaEventStatsGroup=altigaEventStatsGroup, alEventStatsCount=alEventStatsCount, altigaEventStatsMibCompliances=altigaEventStatsMibCompliances, altigaEventStatsMibModule=altigaEventStatsMibModule, alEventStatsTable=alEventStatsTable, alStatsEventGlobal=alStatsEventGlobal, alEventStatsEventNumber=alEventStatsEventNumber, altigaEventStatsMibCompliance=altigaEventStatsMibCompliance, altigaEventStatsGroupRev1=altigaEventStatsGroupRev1, alStatsEventNotificationId=alStatsEventNotificationId, PYSNMP_MODULE_ID=altigaEventStatsMibModule, altigaEventStatsMibConformance=altigaEventStatsMibConformance, alEventStatsEntry=alEventStatsEntry, altigaEventStatsMibComplianceRev1=altigaEventStatsMibComplianceRev1)
