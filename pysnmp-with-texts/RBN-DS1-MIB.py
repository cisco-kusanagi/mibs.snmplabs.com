#
# PySNMP MIB module RBN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-DS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
RbnAlarmPerceivedSeverity, RbnAlarmServiceAffecting = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmPerceivedSeverity", "RbnAlarmServiceAffecting")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter32, NotificationType, Unsigned32, MibIdentifier, iso, Gauge32, Counter64, ModuleIdentity, TimeTicks, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "iso", "Gauge32", "Counter64", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnDS1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 37))
rbnDS1MIB.setRevisions(('2005-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnDS1MIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: rbnDS1MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS1MIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnDS1MIB.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com')
if mibBuilder.loadTexts: rbnDS1MIB.setDescription('The MIB to describe DS1, E1, DS2, and E2 interfaces objects beyond those instrumented by standards-track MIBs.')
rbnDs1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1))
rbnDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1), )
if mibBuilder.loadTexts: rbnDsx1ConfigTable.setStatus('current')
if mibBuilder.loadTexts: rbnDsx1ConfigTable.setDescription('The DS1 Configuration table.')
rbnDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("RBN-DS1-MIB", "rbnDsx1ConfigEntry"))
rbnDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx1ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rbnDsx1ConfigEntry.setDescription('An entry in the DS1 Configuration table.')
rbnDsx1AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: rbnDsx1AlarmSeverity.setDescription('The perceived severity of the interface alarm.')
rbnDsx1AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmServiceAffecting.setStatus('current')
if mibBuilder.loadTexts: rbnDsx1AlarmServiceAffecting.setDescription('Indicates whether the interface alarm is service affecting.')
rbnDs1MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2))
rbnDs1MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1))
rbnDs1MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2))
rbnDs1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2, 1)).setObjects(("RBN-DS1-MIB", "rbnDs1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1MIBCompliance = rbnDs1MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnDs1MIBCompliance.setDescription('The compliance statement for using this MIB for all DS1 interfaces')
rbnDs1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1, 1)).setObjects(("RBN-DS1-MIB", "rbnDsx1AlarmSeverity"), ("RBN-DS1-MIB", "rbnDsx1AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1Group = rbnDs1Group.setStatus('current')
if mibBuilder.loadTexts: rbnDs1Group.setDescription('A collection of objects providing supplemental configuration information applicable to all DS1 interfaces.')
mibBuilder.exportSymbols("RBN-DS1-MIB", rbnDS1MIB=rbnDS1MIB, rbnDs1MIBObjects=rbnDs1MIBObjects, rbnDsx1ConfigTable=rbnDsx1ConfigTable, rbnDs1MIBCompliances=rbnDs1MIBCompliances, rbnDs1MIBCompliance=rbnDs1MIBCompliance, rbnDs1Group=rbnDs1Group, rbnDsx1AlarmSeverity=rbnDsx1AlarmSeverity, rbnDsx1ConfigEntry=rbnDsx1ConfigEntry, rbnDsx1AlarmServiceAffecting=rbnDsx1AlarmServiceAffecting, PYSNMP_MODULE_ID=rbnDS1MIB, rbnDs1MIBGroups=rbnDs1MIBGroups, rbnDs1MIBConformance=rbnDs1MIBConformance)
