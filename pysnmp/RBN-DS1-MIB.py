#
# PySNMP MIB module RBN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
RbnAlarmServiceAffecting, RbnAlarmPerceivedSeverity = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, ObjectIdentity, ModuleIdentity, IpAddress, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, NotificationType, Gauge32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "NotificationType", "Gauge32", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnDS1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 37))
rbnDS1MIB.setRevisions(('2005-05-09 00:00',))
if mibBuilder.loadTexts: rbnDS1MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS1MIB.setOrganization('RedBack Networks, Inc.')
rbnDs1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1))
rbnDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1), )
if mibBuilder.loadTexts: rbnDsx1ConfigTable.setStatus('current')
rbnDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("RBN-DS1-MIB", "rbnDsx1ConfigEntry"))
rbnDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx1ConfigEntry.setStatus('current')
rbnDsx1AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmSeverity.setStatus('current')
rbnDsx1AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmServiceAffecting.setStatus('current')
rbnDs1MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2))
rbnDs1MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1))
rbnDs1MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2))
rbnDs1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2, 1)).setObjects(("RBN-DS1-MIB", "rbnDs1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1MIBCompliance = rbnDs1MIBCompliance.setStatus('current')
rbnDs1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1, 1)).setObjects(("RBN-DS1-MIB", "rbnDsx1AlarmSeverity"), ("RBN-DS1-MIB", "rbnDsx1AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1Group = rbnDs1Group.setStatus('current')
mibBuilder.exportSymbols("RBN-DS1-MIB", PYSNMP_MODULE_ID=rbnDS1MIB, rbnDs1MIBObjects=rbnDs1MIBObjects, rbnDs1MIBGroups=rbnDs1MIBGroups, rbnDsx1ConfigTable=rbnDsx1ConfigTable, rbnDs1Group=rbnDs1Group, rbnDs1MIBConformance=rbnDs1MIBConformance, rbnDsx1AlarmServiceAffecting=rbnDsx1AlarmServiceAffecting, rbnDsx1ConfigEntry=rbnDsx1ConfigEntry, rbnDsx1AlarmSeverity=rbnDsx1AlarmSeverity, rbnDs1MIBCompliance=rbnDs1MIBCompliance, rbnDS1MIB=rbnDS1MIB, rbnDs1MIBCompliances=rbnDs1MIBCompliances)
