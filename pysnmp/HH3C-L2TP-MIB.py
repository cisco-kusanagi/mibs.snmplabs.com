#
# PySNMP MIB module HH3C-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-L2TP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, NotificationType, ObjectIdentity, Gauge32, MibIdentifier, iso, Integer32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "MibIdentifier", "iso", "Integer32", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 139))
hh3cL2tp.setRevisions(('2013-07-05 15:18',))
if mibBuilder.loadTexts: hh3cL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: hh3cL2tp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1))
hh3cL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1))
hh3cL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1))
hh3cL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpStatsTotalTunnels.setStatus('current')
hh3cL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpStatsTotalSessions.setStatus('current')
hh3cL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cL2tpSessionRate.setStatus('current')
mibBuilder.exportSymbols("HH3C-L2TP-MIB", PYSNMP_MODULE_ID=hh3cL2tp, hh3cL2tpObjects=hh3cL2tpObjects, hh3cL2tpStatsTotalTunnels=hh3cL2tpStatsTotalTunnels, hh3cL2tpScalar=hh3cL2tpScalar, hh3cL2tpStatsTotalSessions=hh3cL2tpStatsTotalSessions, hh3cL2tp=hh3cL2tp, hh3cL2tpSessionRate=hh3cL2tpSessionRate, hh3cL2tpStats=hh3cL2tpStats)
