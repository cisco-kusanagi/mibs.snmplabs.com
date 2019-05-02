#
# PySNMP MIB module ALTIGA-GENERAL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-GENERAL-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alGeneralMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alGeneralMibModule")
alStatsGeneral, alGeneralGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsGeneral", "alGeneralGroup")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, MibIdentifier, NotificationType, Bits, Gauge32, Integer32, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaGeneralStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2))
altigaGeneralStatsMibModule.setRevisions(('2002-09-11 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setRevisionsDescriptions(('Added module compliance and fix comments.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setLastUpdated('200209111300Z')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setDescription('The Altiga General Statistics MIB models counters and objects that are of management interest. Acronyms The following acronyms are used in this document: AVP: Attribute/Value Pair CLID: Calling Line ID DNIS: Dialed Number Identification Service L2TP: Layer 2 Tunnel Protocol LAC: L2TP Access Concentrator LNS: L2TP Network Server RWS: Receive Window Size ')
alStatsGeneralGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1))
alGeneralTime = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTime.setStatus('current')
if mibBuilder.loadTexts: alGeneralTime.setDescription("The current time on the box, represented as a time_t. In 1.2, this was the box's local time. After 1.2, it was corrected to represent UTC (which is what it is supposed to be). So all boxes should have this be the same value +/- a few seconds.")
alGeneralGaugeCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setDescription('The value of the CPU Utilization gauge which indicates percentage of CPU utilized.')
alGeneralGaugeActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setDescription('The value of the Active Sessions gauge which indicates the percentage of total permitted session that are active.')
alGeneralGaugeThroughput = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setDescription('The value of the Throughput gauge which indicates the percentage of total available throughput in-use.')
alGeneralTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTimeZone.setStatus('current')
if mibBuilder.loadTexts: alGeneralTimeZone.setDescription('The time zone configured on the box. Measured in minutes from UTC. e.g. EST = -300.')
altigaGeneralStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1))
altigaGeneralStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1))
altigaGeneralStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1, 1)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "altigaGeneralStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsMibCompliance = altigaGeneralStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaGeneralStatsMibCompliance.setDescription('The compliance statement for agents which implement the Altiga General Statistics MIB.')
altigaGeneralStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25, 2)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "alGeneralTime"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeCpuUtil"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeActiveSessions"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeThroughput"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsGroup = altigaGeneralStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaGeneralStatsGroup.setDescription('The objects for general information.')
mibBuilder.exportSymbols("ALTIGA-GENERAL-STATS-MIB", alGeneralGaugeCpuUtil=alGeneralGaugeCpuUtil, altigaGeneralStatsGroup=altigaGeneralStatsGroup, alGeneralGaugeThroughput=alGeneralGaugeThroughput, altigaGeneralStatsMibCompliances=altigaGeneralStatsMibCompliances, PYSNMP_MODULE_ID=altigaGeneralStatsMibModule, altigaGeneralStatsMibModule=altigaGeneralStatsMibModule, alGeneralTime=alGeneralTime, alStatsGeneralGlobal=alStatsGeneralGlobal, altigaGeneralStatsMibConformance=altigaGeneralStatsMibConformance, alGeneralGaugeActiveSessions=alGeneralGaugeActiveSessions, altigaGeneralStatsMibCompliance=altigaGeneralStatsMibCompliance, alGeneralTimeZone=alGeneralTimeZone)
