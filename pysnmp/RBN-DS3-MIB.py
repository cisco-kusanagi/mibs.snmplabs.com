#
# PySNMP MIB module RBN-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-DS3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dsx3ConfigEntry, = mibBuilder.importSymbols("DS3-MIB", "dsx3ConfigEntry")
RbnAlarmServiceAffecting, RbnAlarmPerceivedSeverity = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, NotificationType, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, MibIdentifier, Gauge32, Counter32, ModuleIdentity, TimeTicks, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "MibIdentifier", "Gauge32", "Counter32", "ModuleIdentity", "TimeTicks", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnDS3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 38))
rbnDS3MIB.setRevisions(('2005-05-09 00:00',))
if mibBuilder.loadTexts: rbnDS3MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS3MIB.setOrganization('RedBack Networks, Inc.')
rbnDs3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1))
rbnDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1), )
if mibBuilder.loadTexts: rbnDsx3ConfigTable.setStatus('current')
rbnDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1), )
dsx3ConfigEntry.registerAugmentions(("RBN-DS3-MIB", "rbnDsx3ConfigEntry"))
rbnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx3ConfigEntry.setStatus('current')
rbnDsx3AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmSeverity.setStatus('current')
rbnDsx3AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmServiceAffecting.setStatus('current')
rbnDs3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2))
rbnDs3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1))
rbnDs3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2))
rbnDs3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2, 1)).setObjects(("RBN-DS3-MIB", "rbnDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3MIBCompliance = rbnDs3MIBCompliance.setStatus('current')
rbnDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1, 1)).setObjects(("RBN-DS3-MIB", "rbnDsx3AlarmSeverity"), ("RBN-DS3-MIB", "rbnDsx3AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3Group = rbnDs3Group.setStatus('current')
mibBuilder.exportSymbols("RBN-DS3-MIB", rbnDs3MIBCompliances=rbnDs3MIBCompliances, rbnDs3MIBGroups=rbnDs3MIBGroups, rbnDsx3ConfigTable=rbnDsx3ConfigTable, rbnDS3MIB=rbnDS3MIB, rbnDsx3AlarmSeverity=rbnDsx3AlarmSeverity, rbnDs3MIBConformance=rbnDs3MIBConformance, rbnDs3Group=rbnDs3Group, rbnDsx3ConfigEntry=rbnDsx3ConfigEntry, PYSNMP_MODULE_ID=rbnDS3MIB, rbnDsx3AlarmServiceAffecting=rbnDsx3AlarmServiceAffecting, rbnDs3MIBCompliance=rbnDs3MIBCompliance, rbnDs3MIBObjects=rbnDs3MIBObjects)
