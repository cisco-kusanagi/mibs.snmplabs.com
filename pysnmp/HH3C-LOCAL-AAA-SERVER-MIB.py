#
# PySNMP MIB module HH3C-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Counter32, Unsigned32, IpAddress, MibIdentifier, NotificationType, Counter64, iso, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64", "iso", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLocAAASvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 141))
hh3cLocAAASvr.setRevisions(('2013-07-06 09:45',))
if mibBuilder.loadTexts: hh3cLocAAASvr.setLastUpdated('201307060945Z')
if mibBuilder.loadTexts: hh3cLocAAASvr.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cLocAAASvrControl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 1))
hh3cLocAAASvrTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 2))
hh3cLocAAASvrTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3))
hh3cLocAAASvrTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0))
hh3cLocAAASvrBillExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0, 1))
if mibBuilder.loadTexts: hh3cLocAAASvrBillExportFailed.setStatus('current')
mibBuilder.exportSymbols("HH3C-LOCAL-AAA-SERVER-MIB", hh3cLocAAASvrControl=hh3cLocAAASvrControl, PYSNMP_MODULE_ID=hh3cLocAAASvr, hh3cLocAAASvrTrap=hh3cLocAAASvrTrap, hh3cLocAAASvr=hh3cLocAAASvr, hh3cLocAAASvrTrapPrex=hh3cLocAAASvrTrapPrex, hh3cLocAAASvrBillExportFailed=hh3cLocAAASvrBillExportFailed, hh3cLocAAASvrTables=hh3cLocAAASvrTables)
