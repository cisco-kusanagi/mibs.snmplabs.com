#
# PySNMP MIB module ALTIGA-SSL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alSslMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alSslMibModule")
alSslGroup, alStatsSsl = mibBuilder.importSymbols("ALTIGA-MIB", "alSslGroup", "alStatsSsl")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Integer32, TimeTicks, Gauge32, Counter32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Unsigned32, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "Gauge32", "Counter32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaSslStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2))
altigaSslStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaSslStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsSslGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1))
alSslStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsTotalSessions.setStatus('current')
alSslStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsActiveSessions.setStatus('current')
alSslStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsMaxSessions.setStatus('current')
alSslStatsPreDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreDecryptOctets.setStatus('current')
alSslStatsPostDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostDecryptOctets.setStatus('current')
alSslStatsPreEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreEncryptOctets.setStatus('current')
alSslStatsPostEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostEncryptOctets.setStatus('current')
altigaSslStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1))
altigaSslStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1))
altigaSslStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1, 1)).setObjects(("ALTIGA-SSL-STATS-MIB", "altigaSslStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsMibCompliance = altigaSslStatsMibCompliance.setStatus('current')
altigaSslStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26, 2)).setObjects(("ALTIGA-SSL-STATS-MIB", "alSslStatsTotalSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsActiveSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsMaxSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreEncryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostEncryptOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsGroup = altigaSslStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-SSL-STATS-MIB", alSslStatsPreEncryptOctets=alSslStatsPreEncryptOctets, PYSNMP_MODULE_ID=altigaSslStatsMibModule, alStatsSslGlobal=alStatsSslGlobal, alSslStatsPreDecryptOctets=alSslStatsPreDecryptOctets, alSslStatsPostEncryptOctets=alSslStatsPostEncryptOctets, alSslStatsActiveSessions=alSslStatsActiveSessions, altigaSslStatsMibCompliance=altigaSslStatsMibCompliance, altigaSslStatsMibModule=altigaSslStatsMibModule, altigaSslStatsGroup=altigaSslStatsGroup, altigaSslStatsMibCompliances=altigaSslStatsMibCompliances, altigaSslStatsMibConformance=altigaSslStatsMibConformance, alSslStatsMaxSessions=alSslStatsMaxSessions, alSslStatsTotalSessions=alSslStatsTotalSessions, alSslStatsPostDecryptOctets=alSslStatsPostDecryptOctets)
