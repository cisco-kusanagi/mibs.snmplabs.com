#
# PySNMP MIB module ALTIGA-VERSION-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-VERSION-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alVersionMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alVersionMibModule")
alVersionGroup, alStatsVersion = mibBuilder.importSymbols("ALTIGA-MIB", "alVersionGroup", "alStatsVersion")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, iso, Counter32, Gauge32, MibIdentifier, ObjectIdentity, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaVersionStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2))
altigaVersionStatsMibModule.setRevisions(('2002-09-05 13:00',))
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsVersionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1))
alVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMajor.setStatus('current')
alVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMinor.setStatus('current')
alVersionInt = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionInt.setStatus('current')
alVersionString = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionString.setStatus('current')
alVersionLong = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionLong.setStatus('current')
alVersionShort = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionShort.setStatus('current')
alVersionBoot = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionBoot.setStatus('current')
altigaVersionStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1))
altigaVersionStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1))
altigaVersionStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1, 1)).setObjects(("ALTIGA-VERSION-STATS-MIB", "altigaVersionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsMibCompliance = altigaVersionStatsMibCompliance.setStatus('current')
altigaVersionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1, 2)).setObjects(("ALTIGA-VERSION-STATS-MIB", "alVersionMajor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionMinor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionInt"), ("ALTIGA-VERSION-STATS-MIB", "alVersionString"), ("ALTIGA-VERSION-STATS-MIB", "alVersionLong"), ("ALTIGA-VERSION-STATS-MIB", "alVersionShort"), ("ALTIGA-VERSION-STATS-MIB", "alVersionBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsGroup = altigaVersionStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-VERSION-STATS-MIB", alVersionBoot=alVersionBoot, alVersionInt=alVersionInt, altigaVersionStatsMibCompliance=altigaVersionStatsMibCompliance, alVersionMajor=alVersionMajor, altigaVersionStatsMibModule=altigaVersionStatsMibModule, altigaVersionStatsMibConformance=altigaVersionStatsMibConformance, alVersionLong=alVersionLong, PYSNMP_MODULE_ID=altigaVersionStatsMibModule, alVersionShort=alVersionShort, altigaVersionStatsGroup=altigaVersionStatsGroup, altigaVersionStatsMibCompliances=altigaVersionStatsMibCompliances, alVersionString=alVersionString, alVersionMinor=alVersionMinor, alStatsVersionGlobal=alStatsVersionGlobal)
