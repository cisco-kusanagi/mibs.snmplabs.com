#
# PySNMP MIB module AVICI-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, NotificationType, TimeTicks, MibIdentifier, Counter64, Integer32, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64", "Integer32", "ObjectIdentity", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avici = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474))
avici.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00',))
if mibBuilder.loadTexts: avici.setLastUpdated('990330095500Z')
if mibBuilder.loadTexts: avici.setOrganization('Avici Systems, Inc.')
aviciMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 1))
if mibBuilder.loadTexts: aviciMibs.setStatus('current')
aviciProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 2))
if mibBuilder.loadTexts: aviciProducts.setStatus('current')
aviciExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 3))
if mibBuilder.loadTexts: aviciExperimental.setStatus('current')
aviciTypes = ObjectIdentity((1, 3, 6, 1, 4, 1, 2474, 4))
if mibBuilder.loadTexts: aviciTypes.setStatus('current')
mibBuilder.exportSymbols("AVICI-SMI", aviciMibs=aviciMibs, avici=avici, aviciExperimental=aviciExperimental, PYSNMP_MODULE_ID=avici, aviciTypes=aviciTypes, aviciProducts=aviciProducts)
