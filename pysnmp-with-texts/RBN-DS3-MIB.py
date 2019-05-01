#
# PySNMP MIB module RBN-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-DS3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
dsx3ConfigEntry, = mibBuilder.importSymbols("DS3-MIB", "dsx3ConfigEntry")
RbnAlarmServiceAffecting, RbnAlarmPerceivedSeverity = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, iso, TimeTicks, ObjectIdentity, Counter32, IpAddress, MibIdentifier, Bits, Gauge32, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "IpAddress", "MibIdentifier", "Bits", "Gauge32", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnDS3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 38))
rbnDS3MIB.setRevisions(('2005-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnDS3MIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: rbnDS3MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS3MIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnDS3MIB.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com')
if mibBuilder.loadTexts: rbnDS3MIB.setDescription('The MIB that describes DS3 and E3 interfaces objects beyond those instrumented by standards-track MIBs.')
rbnDs3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1))
rbnDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1), )
if mibBuilder.loadTexts: rbnDsx3ConfigTable.setStatus('current')
if mibBuilder.loadTexts: rbnDsx3ConfigTable.setDescription('The DS3/E3 Configuration table.')
rbnDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1), )
dsx3ConfigEntry.registerAugmentions(("RBN-DS3-MIB", "rbnDsx3ConfigEntry"))
rbnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx3ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rbnDsx3ConfigEntry.setDescription('An entry in the DS3/E3 Configuration table.')
rbnDsx3AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: rbnDsx3AlarmSeverity.setDescription('The perceived severity of the interface alarm.')
rbnDsx3AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmServiceAffecting.setStatus('current')
if mibBuilder.loadTexts: rbnDsx3AlarmServiceAffecting.setDescription('Indicates whether the interface alarm is service affecting.')
rbnDs3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2))
rbnDs3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1))
rbnDs3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2))
rbnDs3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2, 1)).setObjects(("RBN-DS3-MIB", "rbnDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3MIBCompliance = rbnDs3MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnDs3MIBCompliance.setDescription('The compliance statement for using this MIB for all DS3/E3 interfaces.')
rbnDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1, 1)).setObjects(("RBN-DS3-MIB", "rbnDsx3AlarmSeverity"), ("RBN-DS3-MIB", "rbnDsx3AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3Group = rbnDs3Group.setStatus('current')
if mibBuilder.loadTexts: rbnDs3Group.setDescription('A collection of objects providing supplemental configuration information applicable to all DS3/E3 interfaces.')
mibBuilder.exportSymbols("RBN-DS3-MIB", rbnDsx3ConfigTable=rbnDsx3ConfigTable, rbnDs3MIBCompliances=rbnDs3MIBCompliances, PYSNMP_MODULE_ID=rbnDS3MIB, rbnDs3MIBConformance=rbnDs3MIBConformance, rbnDsx3AlarmSeverity=rbnDsx3AlarmSeverity, rbnDsx3AlarmServiceAffecting=rbnDsx3AlarmServiceAffecting, rbnDs3MIBObjects=rbnDs3MIBObjects, rbnDS3MIB=rbnDS3MIB, rbnDsx3ConfigEntry=rbnDsx3ConfigEntry, rbnDs3MIBCompliance=rbnDs3MIBCompliance, rbnDs3MIBGroups=rbnDs3MIBGroups, rbnDs3Group=rbnDs3Group)
