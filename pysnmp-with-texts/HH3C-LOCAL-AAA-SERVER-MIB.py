#
# PySNMP MIB module HH3C-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Bits, TimeTicks, NotificationType, Gauge32, Counter32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Bits", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cLocAAASvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 141))
hh3cLocAAASvr.setRevisions(('2013-07-06 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLocAAASvr.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cLocAAASvr.setLastUpdated('201307060945Z')
if mibBuilder.loadTexts: hh3cLocAAASvr.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cLocAAASvr.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cLocAAASvr.setDescription('This MIB provides the definition of the local AAA Server.')
hh3cLocAAASvrControl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 1))
hh3cLocAAASvrTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 2))
hh3cLocAAASvrTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3))
hh3cLocAAASvrTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0))
hh3cLocAAASvrBillExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0, 1))
if mibBuilder.loadTexts: hh3cLocAAASvrBillExportFailed.setStatus('current')
if mibBuilder.loadTexts: hh3cLocAAASvrBillExportFailed.setDescription('This trap is generated when local AAA bills cannot be exported to a bill server.')
mibBuilder.exportSymbols("HH3C-LOCAL-AAA-SERVER-MIB", hh3cLocAAASvrControl=hh3cLocAAASvrControl, PYSNMP_MODULE_ID=hh3cLocAAASvr, hh3cLocAAASvrTrap=hh3cLocAAASvrTrap, hh3cLocAAASvrTables=hh3cLocAAASvrTables, hh3cLocAAASvrTrapPrex=hh3cLocAAASvrTrapPrex, hh3cLocAAASvrBillExportFailed=hh3cLocAAASvrBillExportFailed, hh3cLocAAASvr=hh3cLocAAASvr)
