#
# PySNMP MIB module HPN-ICF-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, iso, Counter32, ObjectIdentity, ModuleIdentity, MibIdentifier, Integer32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfLocAAASvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141))
hpnicfLocAAASvr.setRevisions(('2013-07-06 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLocAAASvr.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfLocAAASvr.setLastUpdated('201307060945Z')
if mibBuilder.loadTexts: hpnicfLocAAASvr.setOrganization('')
if mibBuilder.loadTexts: hpnicfLocAAASvr.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLocAAASvr.setDescription('This MIB provides the definition of the local AAA Server.')
hpnicfLocAAASvrControl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 1))
hpnicfLocAAASvrTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 2))
hpnicfLocAAASvrTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3))
hpnicfLocAAASvrTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3, 0))
hpnicfLocAAASvrBillExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3, 0, 1))
if mibBuilder.loadTexts: hpnicfLocAAASvrBillExportFailed.setStatus('current')
if mibBuilder.loadTexts: hpnicfLocAAASvrBillExportFailed.setDescription('This trap is generated when local AAA bills cannot be exported to a bill server.')
mibBuilder.exportSymbols("HPN-ICF-LOCAL-AAA-SERVER-MIB", hpnicfLocAAASvrControl=hpnicfLocAAASvrControl, hpnicfLocAAASvrTables=hpnicfLocAAASvrTables, hpnicfLocAAASvr=hpnicfLocAAASvr, PYSNMP_MODULE_ID=hpnicfLocAAASvr, hpnicfLocAAASvrBillExportFailed=hpnicfLocAAASvrBillExportFailed, hpnicfLocAAASvrTrapPrex=hpnicfLocAAASvrTrapPrex, hpnicfLocAAASvrTrap=hpnicfLocAAASvrTrap)
