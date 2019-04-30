#
# PySNMP MIB module HP-ICF-SLOT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SLOT-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitchStatistics, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitchStatistics")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Counter64, IpAddress, ObjectIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, ModuleIdentity, Bits, Gauge32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "IpAddress", "ObjectIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "ModuleIdentity", "Bits", "Gauge32", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfSlotStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20))
hpicfSlotStatsMIB.setRevisions(('2012-01-05 00:00',))
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setLastUpdated('201201050000Z')
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setOrganization('HP Networking')
hpicfSlotStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1))
hpicfSlotStatsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2))
hpicfSlotStatsModuleCpuStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1), )
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatTable.setStatus('current')
hpicfSlotStatsModuleCpuStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatEntry.setStatus('current')
hpicfSlotStatsModuleHwModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleHwModel.setStatus('current')
hpicfSlotStatsModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleSerialNum.setStatus('current')
hpicfSlotStatsModuleCpuStatCurrentPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatCurrentPercent.setStatus('current')
hpicfSlotStatsModuleCpuStatAveragePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatAveragePercent.setStatus('current')
hpicfSlotStatsModuleCpuStatUpdateFrequency = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatUpdateFrequency.setStatus('current')
hpicfSlotStatsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1))
hpicfSlotStatsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2))
hpicfSlotStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleHwModel"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleSerialNum"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatCurrentPercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatAveragePercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatUpdateFrequency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsGroup = hpicfSlotStatsGroup.setStatus('current')
hpicfSlotStatsFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsFullCompliance1 = hpicfSlotStatsFullCompliance1.setStatus('current')
hpicfModuleSlotStatsReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 2)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfModuleSlotStatsReadOnlyCompliance1 = hpicfModuleSlotStatsReadOnlyCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-SLOT-STATS-MIB", hpicfSlotStatsMIB=hpicfSlotStatsMIB, hpicfSlotStatsCompliances=hpicfSlotStatsCompliances, hpicfSlotStatsModuleSerialNum=hpicfSlotStatsModuleSerialNum, hpicfSlotStatsFullCompliance1=hpicfSlotStatsFullCompliance1, hpicfSlotStatsObjects=hpicfSlotStatsObjects, hpicfModuleSlotStatsReadOnlyCompliance1=hpicfModuleSlotStatsReadOnlyCompliance1, hpicfSlotStatsModuleCpuStatEntry=hpicfSlotStatsModuleCpuStatEntry, PYSNMP_MODULE_ID=hpicfSlotStatsMIB, hpicfSlotStatsModuleHwModel=hpicfSlotStatsModuleHwModel, hpicfSlotStatsModuleCpuStatUpdateFrequency=hpicfSlotStatsModuleCpuStatUpdateFrequency, hpicfSlotStatsConformance=hpicfSlotStatsConformance, hpicfSlotStatsGroups=hpicfSlotStatsGroups, hpicfSlotStatsGroup=hpicfSlotStatsGroup, hpicfSlotStatsModuleCpuStatTable=hpicfSlotStatsModuleCpuStatTable, hpicfSlotStatsModuleCpuStatAveragePercent=hpicfSlotStatsModuleCpuStatAveragePercent, hpicfSlotStatsModuleCpuStatCurrentPercent=hpicfSlotStatsModuleCpuStatCurrentPercent)
