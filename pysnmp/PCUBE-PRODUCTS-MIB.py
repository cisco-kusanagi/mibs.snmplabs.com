#
# PySNMP MIB module PCUBE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCUBE-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
pcubeModules, pcubeProducts = mibBuilder.importSymbols("PCUBE-SMI", "pcubeModules", "pcubeProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, NotificationType, ObjectIdentity, Gauge32, MibIdentifier, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "NotificationType", "ObjectIdentity", "Gauge32", "MibIdentifier", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcubeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 2))
pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))
if mibBuilder.loadTexts: pcubeProductsMIB.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcubeProductsMIB.setOrganization('Cisco Systems, Inc.')
sce100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 1))
sce1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 2))
sce2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 3))
mibBuilder.exportSymbols("PCUBE-PRODUCTS-MIB", pcubeProductsMIB=pcubeProductsMIB, sce100=sce100, sce2000=sce2000, PYSNMP_MODULE_ID=pcubeProductsMIB, sce1000=sce1000)
