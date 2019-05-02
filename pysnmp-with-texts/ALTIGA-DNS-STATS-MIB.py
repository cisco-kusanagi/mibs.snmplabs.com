#
# PySNMP MIB module ALTIGA-DNS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-DNS-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alDnsMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alDnsMibModule")
alDnsGroup, alStatsDns = mibBuilder.importSymbols("ALTIGA-MIB", "alDnsGroup", "alStatsDns")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, Gauge32, Integer32, TimeTicks, Counter32, Counter64, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "Gauge32", "Integer32", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaDnsStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2))
altigaDnsStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaDnsStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setDescription('The Altiga DNS Statistics MIB models counters and objects that are of management interest for DNS. Acronyms The following acronyms are used in this document: DNS: Domain Name Service MIB: Management Information Base ')
alStatsDnsResolverGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1))
alDnsStatsAttemptedQueries = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setDescription('The number of DNS queries that were attempted.')
alDnsStatsSuccessfulResponses = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setDescription('The number of queries that were successfully resolved.')
alDnsStatsTimeoutFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setDescription('The number of failures because there was no response from the server.')
alDnsStatsUnreachableServerFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setDescription("The number of failures because the address of the server is not reachable according to the Concentrator's routing table.")
alDnsStatsMiscFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setDescription('The number of failures for an unspecified reason.')
altigaDnsStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1))
altigaDnsStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1))
altigaDnsStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1, 1)).setObjects(("ALTIGA-DNS-STATS-MIB", "altigaDnsStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsMibCompliance = altigaDnsStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaDnsStatsMibCompliance.setDescription('The compliance statement for agents which implement the Altiga DNS Statistics MIB.')
altigaDnsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18, 2)).setObjects(("ALTIGA-DNS-STATS-MIB", "alDnsStatsAttemptedQueries"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsSuccessfulResponses"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsTimeoutFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsUnreachableServerFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsMiscFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsGroup = altigaDnsStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaDnsStatsGroup.setDescription('The objects for the DNS resolver module statistics.')
mibBuilder.exportSymbols("ALTIGA-DNS-STATS-MIB", alStatsDnsResolverGlobal=alStatsDnsResolverGlobal, alDnsStatsSuccessfulResponses=alDnsStatsSuccessfulResponses, alDnsStatsTimeoutFailures=alDnsStatsTimeoutFailures, alDnsStatsUnreachableServerFailures=alDnsStatsUnreachableServerFailures, altigaDnsStatsMibConformance=altigaDnsStatsMibConformance, altigaDnsStatsMibCompliances=altigaDnsStatsMibCompliances, altigaDnsStatsMibCompliance=altigaDnsStatsMibCompliance, altigaDnsStatsGroup=altigaDnsStatsGroup, alDnsStatsMiscFailures=alDnsStatsMiscFailures, PYSNMP_MODULE_ID=altigaDnsStatsMibModule, altigaDnsStatsMibModule=altigaDnsStatsMibModule, alDnsStatsAttemptedQueries=alDnsStatsAttemptedQueries)
