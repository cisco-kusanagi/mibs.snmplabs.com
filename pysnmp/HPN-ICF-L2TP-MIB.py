#
# PySNMP MIB module HPN-ICF-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-L2TP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, IpAddress, TimeTicks, Gauge32, ModuleIdentity, ObjectIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139))
hpnicfL2tp.setRevisions(('2013-07-05 15:18',))
if mibBuilder.loadTexts: hpnicfL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: hpnicfL2tp.setOrganization('')
hpnicfL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1))
hpnicfL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1))
hpnicfL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1))
hpnicfL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalTunnels.setStatus('current')
hpnicfL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalSessions.setStatus('current')
hpnicfL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpSessionRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-L2TP-MIB", hpnicfL2tpStatsTotalSessions=hpnicfL2tpStatsTotalSessions, hpnicfL2tpStats=hpnicfL2tpStats, PYSNMP_MODULE_ID=hpnicfL2tp, hpnicfL2tpScalar=hpnicfL2tpScalar, hpnicfL2tpSessionRate=hpnicfL2tpSessionRate, hpnicfL2tpStatsTotalTunnels=hpnicfL2tpStatsTotalTunnels, hpnicfL2tpObjects=hpnicfL2tpObjects, hpnicfL2tp=hpnicfL2tp)
