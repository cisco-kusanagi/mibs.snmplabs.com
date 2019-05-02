#
# PySNMP MIB module RDN-SLOTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SLOTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ObjectIdentity, Counter64, Integer32, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "TimeTicks", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSlots = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 3))
rdnSlots.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnSlots.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", '+ Updated the CONTACT-INFO. + Reorder REVISION/DESCRIPTION in required reverse chronological order.', 'Clean up of CONTACT-INFO.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnSlots.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSlots.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnSlots.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnSlots.setDescription('MIB module for Motorola Slot definitions. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
rdnSlotsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 0))
rdnSlotsBSR64000Master = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 1))
rdnSlotsBSR64000IO = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 2))
rdnSlotsBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 3))
rdnSlotsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 4))
mibBuilder.exportSymbols("RDN-SLOTS-MIB", rdnSlotsBSR64000IO=rdnSlotsBSR64000IO, PYSNMP_MODULE_ID=rdnSlots, rdnSlots=rdnSlots, rdnSlotsOSR2000=rdnSlotsOSR2000, rdnSlotsUnknown=rdnSlotsUnknown, rdnSlotsBSR1000=rdnSlotsBSR1000, rdnSlotsBSR64000Master=rdnSlotsBSR64000Master)
