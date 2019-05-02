#
# PySNMP MIB module RDN-CHASSIS-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-CHASSIS-TYPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:54:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, Gauge32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "Gauge32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnChassisTypes = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 2))
rdnChassisTypes.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnChassisTypes.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's descritption.", '+ Updated the CONTACT-INFO. + Reorder REVISION/DESCRIPTION in required reverse chronological order.', 'Clean up of CONTACT-INFO.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnChassisTypes.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnChassisTypes.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnChassisTypes.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnChassisTypes.setDescription('MIB module for Motorola Chassis-Type definitions. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
rdnChassisTypesUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 0))
rdnChassisTypesBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 1))
rdnChassisTypesBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 2))
rdnChassisTypesOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 3))
mibBuilder.exportSymbols("RDN-CHASSIS-TYPE-MIB", rdnChassisTypesBSR64000=rdnChassisTypesBSR64000, rdnChassisTypesBSR1000=rdnChassisTypesBSR1000, PYSNMP_MODULE_ID=rdnChassisTypes, rdnChassisTypes=rdnChassisTypes, rdnChassisTypesUnknown=rdnChassisTypesUnknown, rdnChassisTypesOSR2000=rdnChassisTypesOSR2000)
