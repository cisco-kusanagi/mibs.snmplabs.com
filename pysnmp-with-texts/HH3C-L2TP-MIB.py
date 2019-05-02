#
# PySNMP MIB module HH3C-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-L2TP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, NotificationType, MibIdentifier, Gauge32, Bits, Unsigned32, TimeTicks, iso, Integer32, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "Unsigned32", "TimeTicks", "iso", "Integer32", "Counter32", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 139))
hh3cL2tp.setRevisions(('2013-07-05 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cL2tp.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: hh3cL2tp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cL2tp.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cL2tp.setDescription('This MIB contains objects to manage configuration of L2TP. There are no constraints on this MIB.')
hh3cL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1))
hh3cL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1))
hh3cL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1))
hh3cL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpStatsTotalTunnels.setStatus('current')
if mibBuilder.loadTexts: hh3cL2tpStatsTotalTunnels.setDescription('The total number of tunnels at the time of querying.')
hh3cL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpStatsTotalSessions.setStatus('current')
if mibBuilder.loadTexts: hh3cL2tpStatsTotalSessions.setDescription('The total number of sessions at the time of querying.')
hh3cL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpSessionRate.setStatus('current')
if mibBuilder.loadTexts: hh3cL2tpSessionRate.setDescription('The number of sessions that were created in the previous second.')
mibBuilder.exportSymbols("HH3C-L2TP-MIB", hh3cL2tp=hh3cL2tp, hh3cL2tpStats=hh3cL2tpStats, hh3cL2tpSessionRate=hh3cL2tpSessionRate, PYSNMP_MODULE_ID=hh3cL2tp, hh3cL2tpStatsTotalTunnels=hh3cL2tpStatsTotalTunnels, hh3cL2tpObjects=hh3cL2tpObjects, hh3cL2tpScalar=hh3cL2tpScalar, hh3cL2tpStatsTotalSessions=hh3cL2tpStatsTotalSessions)
