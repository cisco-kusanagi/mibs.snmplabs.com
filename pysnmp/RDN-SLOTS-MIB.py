#
# PySNMP MIB module RDN-SLOTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SLOTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, IpAddress, ObjectIdentity, Unsigned32, Counter32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnSlots = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 3))
rdnSlots.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))
if mibBuilder.loadTexts: rdnSlots.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSlots.setOrganization('Motorola')
rdnSlotsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 0))
rdnSlotsBSR64000Master = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 1))
rdnSlotsBSR64000IO = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 2))
rdnSlotsBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 3))
rdnSlotsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 4))
mibBuilder.exportSymbols("RDN-SLOTS-MIB", rdnSlotsBSR1000=rdnSlotsBSR1000, rdnSlotsBSR64000IO=rdnSlotsBSR64000IO, rdnSlots=rdnSlots, rdnSlotsBSR64000Master=rdnSlotsBSR64000Master, rdnSlotsOSR2000=rdnSlotsOSR2000, PYSNMP_MODULE_ID=rdnSlots, rdnSlotsUnknown=rdnSlotsUnknown)
