#
# PySNMP MIB module ALTIGA-IP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-IP-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alIpMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alIpMibModule")
alIpGroup, alStatsIp = mibBuilder.importSymbols("ALTIGA-MIB", "alIpGroup", "alStatsIp")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, ObjectIdentity, IpAddress, Integer32, MibIdentifier, ModuleIdentity, Counter32, TimeTicks, Bits, Gauge32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter32", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaIpStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2))
altigaIpStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaIpStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaIpStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setDescription('The Altiga IP Statistics MIB models counters and objects that are of management interest for IP. Acronyms The following acronyms are used in this document: IP: Internet Protocol LAN: Local-Area Network MIB: Management Information Base ')
alStatsIpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1))
alIpInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1), )
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setDescription('IP Interface Statistics table.')
alIpInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1), ).setIndexNames((0, "ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"))
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setDescription('An entry in the alIpInterfaceStatsTable.')
alIpInterfaceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setDescription('The ifIndex of this row.')
alIpInterfaceStatsCurrentDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("full", 2), ("half", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setDescription('The current LAN duplex mode for this interface.')
altigaIpStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1))
altigaIpStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1))
altigaIpStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1, 1)).setObjects(("ALTIGA-IP-STATS-MIB", "altigaIpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsMibCompliance = altigaIpStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsMibCompliance.setDescription('The compliance statement for agents which implement the Altiga IP Statistics MIB.')
altigaIpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8, 2)).setObjects(("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"), ("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsCurrentDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsGroup = altigaIpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsGroup.setDescription('The objects for Ip Statistics.')
mibBuilder.exportSymbols("ALTIGA-IP-STATS-MIB", altigaIpStatsMibConformance=altigaIpStatsMibConformance, alIpInterfaceStatsTable=alIpInterfaceStatsTable, altigaIpStatsMibModule=altigaIpStatsMibModule, PYSNMP_MODULE_ID=altigaIpStatsMibModule, alIpInterfaceStatsEntry=alIpInterfaceStatsEntry, alStatsIpGlobal=alStatsIpGlobal, alIpInterfaceStatsCurrentDuplex=alIpInterfaceStatsCurrentDuplex, altigaIpStatsMibCompliance=altigaIpStatsMibCompliance, altigaIpStatsGroup=altigaIpStatsGroup, altigaIpStatsMibCompliances=altigaIpStatsMibCompliances, alIpInterfaceStatsIndex=alIpInterfaceStatsIndex)
