#
# PySNMP MIB module AVICI-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:32:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, NotificationType, Counter32, iso, TimeTicks, IpAddress, Bits, ObjectIdentity, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "NotificationType", "Counter32", "iso", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avici = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474))
avici.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avici.setRevisionsDescriptions(('Changed arc names, removed unnecessary arcs.', 'Created MIB module.',))
if mibBuilder.loadTexts: avici.setLastUpdated('990330095500Z')
if mibBuilder.loadTexts: avici.setOrganization('Avici Systems, Inc.')
if mibBuilder.loadTexts: avici.setContactInfo(' Avici Systems, Inc. 101 Billerica Avenue North Billerica, MA 01862-1256 (978) 964-2000 (978) 964-2100 (fax) snmp@avici.com')
if mibBuilder.loadTexts: avici.setDescription('This MIB module contains the structure of management information for all vendor-specific MIBs authored by Avici Systems, Inc.')
aviciMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 1))
if mibBuilder.loadTexts: aviciMibs.setStatus('current')
if mibBuilder.loadTexts: aviciMibs.setDescription('aviciMibs is the root where Avici Proprietary MIB modules are defined.')
aviciProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 2))
if mibBuilder.loadTexts: aviciProducts.setStatus('current')
if mibBuilder.loadTexts: aviciProducts.setDescription('aviciProducts contains the sysObjectID values for all Avici products.')
aviciExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 3))
if mibBuilder.loadTexts: aviciExperimental.setStatus('current')
if mibBuilder.loadTexts: aviciExperimental.setDescription('aviciExperimental is a temporary place for experimental MIBs.')
aviciTypes = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 4))
if mibBuilder.loadTexts: aviciTypes.setStatus('current')
if mibBuilder.loadTexts: aviciTypes.setDescription('aviciTypes is the root where Avici textual convention MIB modules are defined.')
mibBuilder.exportSymbols("AVICI-SMI", aviciProducts=aviciProducts, PYSNMP_MODULE_ID=avici, aviciTypes=aviciTypes, aviciExperimental=aviciExperimental, avici=avici, aviciMibs=aviciMibs)
