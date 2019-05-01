#
# PySNMP MIB module HPN-ICF-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-L2TP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, TimeTicks, MibIdentifier, iso, NotificationType, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "NotificationType", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139))
hpnicfL2tp.setRevisions(('2013-07-05 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfL2tp.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: hpnicfL2tp.setOrganization('')
if mibBuilder.loadTexts: hpnicfL2tp.setContactInfo('')
if mibBuilder.loadTexts: hpnicfL2tp.setDescription('This MIB contains objects to manage configuration of L2TP. There are no constraints on this MIB.')
hpnicfL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1))
hpnicfL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1))
hpnicfL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1))
hpnicfL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalTunnels.setStatus('current')
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalTunnels.setDescription('The total number of tunnels at the time of querying.')
hpnicfL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalSessions.setStatus('current')
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalSessions.setDescription('The total number of sessions at the time of querying.')
hpnicfL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpSessionRate.setStatus('current')
if mibBuilder.loadTexts: hpnicfL2tpSessionRate.setDescription('The number of sessions that were created in the previous second.')
mibBuilder.exportSymbols("HPN-ICF-L2TP-MIB", hpnicfL2tpSessionRate=hpnicfL2tpSessionRate, hpnicfL2tp=hpnicfL2tp, PYSNMP_MODULE_ID=hpnicfL2tp, hpnicfL2tpStats=hpnicfL2tpStats, hpnicfL2tpStatsTotalTunnels=hpnicfL2tpStatsTotalTunnels, hpnicfL2tpScalar=hpnicfL2tpScalar, hpnicfL2tpObjects=hpnicfL2tpObjects, hpnicfL2tpStatsTotalSessions=hpnicfL2tpStatsTotalSessions)
