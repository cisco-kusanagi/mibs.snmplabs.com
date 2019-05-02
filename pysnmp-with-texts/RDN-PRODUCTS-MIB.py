#
# PySNMP MIB module RDN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, NotificationType, Gauge32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, TimeTicks, IpAddress, iso, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "Gauge32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "TimeTicks", "IpAddress", "iso", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 1))
rdnProducts.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnProducts.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", '+ Updated the CONTACT-INFO. + Reorder REVISION/DESCRIPTION in required reverse chronological order.', 'Clean up of CONTACT-INFO.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnProducts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnProducts.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnProducts.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnProducts.setDescription('MIB module for Motorola Product definitions. These Product definitions are the object identifiers that are assigned to various hardware platforms and are returned as values for sysObjectID. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
rdnProductsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 0))
rdnProductsBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 1))
rdnProductsBSR1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 2))
rdnProductsBSR1000R = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 3))
rdnProductsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 4))
mibBuilder.exportSymbols("RDN-PRODUCTS-MIB", rdnProductsBSR1000B=rdnProductsBSR1000B, PYSNMP_MODULE_ID=rdnProducts, rdnProductsBSR1000R=rdnProductsBSR1000R, rdnProductsOSR2000=rdnProductsOSR2000, rdnProductsUnknown=rdnProductsUnknown, rdnProducts=rdnProducts, rdnProductsBSR64000=rdnProductsBSR64000)
