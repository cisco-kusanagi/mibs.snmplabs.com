#
# PySNMP MIB module PCUBE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCUBE-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
pcubeProducts, pcubeModules = mibBuilder.importSymbols("PCUBE-SMI", "pcubeProducts", "pcubeModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, Unsigned32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "Unsigned32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcubeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 2))
pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcubeProductsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcubeProductsMIB.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcubeProductsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcubeProductsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcubeProductsMIB.setDescription('This module defines the object identifiers that are assigned to various hardware platforms, and hence are returned as values for sysObjectID.')
sce100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 1))
sce1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 2))
sce2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 3))
mibBuilder.exportSymbols("PCUBE-PRODUCTS-MIB", sce2000=sce2000, pcubeProductsMIB=pcubeProductsMIB, sce1000=sce1000, sce100=sce100, PYSNMP_MODULE_ID=pcubeProductsMIB)
