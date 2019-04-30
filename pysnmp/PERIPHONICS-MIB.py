#
# PySNMP MIB module PERIPHONICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PERIPHONICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ModuleIdentity, iso, Gauge32, ObjectIdentity, IpAddress, NotificationType, Counter32, TimeTicks, Bits, Unsigned32, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "TimeTicks", "Bits", "Unsigned32", "MibIdentifier", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
periphonics = ModuleIdentity((1, 3, 6, 1, 4, 1, 1357))
if mibBuilder.loadTexts: periphonics.setLastUpdated('9607010000Z')
if mibBuilder.loadTexts: periphonics.setOrganization('Periphonics Corporation')
vruNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 1))
nmsIntegration = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 3))
periMsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1357, 5))
mibBuilder.exportSymbols("PERIPHONICS-MIB", nmsIntegration=nmsIntegration, periphonics=periphonics, PYSNMP_MODULE_ID=periphonics, periMsMIB=periMsMIB, vruNetwork=vruNetwork)
