#
# PySNMP MIB module RDN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter64, IpAddress, ObjectIdentity, Integer32, Gauge32, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter64", "IpAddress", "ObjectIdentity", "Integer32", "Gauge32", "Bits", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 1))
rdnProducts.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-17 00:00',))
if mibBuilder.loadTexts: rdnProducts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnProducts.setOrganization('Motorola')
rdnProductsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 0))
rdnProductsBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 1))
rdnProductsBSR1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 2))
rdnProductsBSR1000R = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 3))
rdnProductsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 4))
mibBuilder.exportSymbols("RDN-PRODUCTS-MIB", PYSNMP_MODULE_ID=rdnProducts, rdnProductsUnknown=rdnProductsUnknown, rdnProducts=rdnProducts, rdnProductsBSR64000=rdnProductsBSR64000, rdnProductsOSR2000=rdnProductsOSR2000, rdnProductsBSR1000R=rdnProductsBSR1000R, rdnProductsBSR1000B=rdnProductsBSR1000B)
