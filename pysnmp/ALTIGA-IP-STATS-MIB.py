#
# PySNMP MIB module ALTIGA-IP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-IP-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alIpMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alIpMibModule")
alIpGroup, alStatsIp = mibBuilder.importSymbols("ALTIGA-MIB", "alIpGroup", "alStatsIp")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, Counter64, Bits, MibIdentifier, Counter32, NotificationType, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter64", "Bits", "MibIdentifier", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaIpStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2))
altigaIpStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaIpStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsIpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1))
alIpInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1), )
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setStatus('current')
alIpInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1), ).setIndexNames((0, "ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"))
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setStatus('current')
alIpInterfaceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setStatus('current')
alIpInterfaceStatsCurrentDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("full", 2), ("half", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setStatus('current')
altigaIpStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1))
altigaIpStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1))
altigaIpStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1, 1)).setObjects(("ALTIGA-IP-STATS-MIB", "altigaIpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsMibCompliance = altigaIpStatsMibCompliance.setStatus('current')
altigaIpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8, 2)).setObjects(("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"), ("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsCurrentDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsGroup = altigaIpStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-IP-STATS-MIB", alIpInterfaceStatsCurrentDuplex=alIpInterfaceStatsCurrentDuplex, alStatsIpGlobal=alStatsIpGlobal, alIpInterfaceStatsTable=alIpInterfaceStatsTable, alIpInterfaceStatsEntry=alIpInterfaceStatsEntry, altigaIpStatsMibConformance=altigaIpStatsMibConformance, altigaIpStatsGroup=altigaIpStatsGroup, altigaIpStatsMibCompliance=altigaIpStatsMibCompliance, PYSNMP_MODULE_ID=altigaIpStatsMibModule, altigaIpStatsMibCompliances=altigaIpStatsMibCompliances, alIpInterfaceStatsIndex=alIpInterfaceStatsIndex, altigaIpStatsMibModule=altigaIpStatsMibModule)
