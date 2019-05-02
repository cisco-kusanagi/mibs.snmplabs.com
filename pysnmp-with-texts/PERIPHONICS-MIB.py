#
# PySNMP MIB module PERIPHONICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PERIPHONICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, NotificationType, Unsigned32, Counter32, Gauge32, iso, ModuleIdentity, Bits, IpAddress, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "NotificationType", "Unsigned32", "Counter32", "Gauge32", "iso", "ModuleIdentity", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
periphonics = ModuleIdentity((1, 3, 6, 1, 4, 1, 1357))
if mibBuilder.loadTexts: periphonics.setLastUpdated('9607010000Z')
if mibBuilder.loadTexts: periphonics.setOrganization('Periphonics Corporation')
if mibBuilder.loadTexts: periphonics.setContactInfo('')
if mibBuilder.loadTexts: periphonics.setDescription('Periphonics enterprise MIB module.')
vruNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 1))
nmsIntegration = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 3))
periMsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 5))
mibBuilder.exportSymbols("PERIPHONICS-MIB", PYSNMP_MODULE_ID=periphonics, periMsMIB=periMsMIB, vruNetwork=vruNetwork, periphonics=periphonics, nmsIntegration=nmsIntegration)
