#
# PySNMP MIB module RDN-CHASSIS-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-CHASSIS-TYPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter64, IpAddress, Counter32, MibIdentifier, Integer32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnChassisTypes = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 2))
rdnChassisTypes.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))
if mibBuilder.loadTexts: rdnChassisTypes.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnChassisTypes.setOrganization('Motorola')
rdnChassisTypesUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 0))
rdnChassisTypesBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 1))
rdnChassisTypesBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 2))
rdnChassisTypesOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 2, 3))
mibBuilder.exportSymbols("RDN-CHASSIS-TYPE-MIB", rdnChassisTypesUnknown=rdnChassisTypesUnknown, rdnChassisTypes=rdnChassisTypes, rdnChassisTypesBSR64000=rdnChassisTypesBSR64000, rdnChassisTypesBSR1000=rdnChassisTypesBSR1000, rdnChassisTypesOSR2000=rdnChassisTypesOSR2000, PYSNMP_MODULE_ID=rdnChassisTypes)
