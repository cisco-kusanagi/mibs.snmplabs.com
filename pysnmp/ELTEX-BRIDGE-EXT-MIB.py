#
# PySNMP MIB module ELTEX-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Integer32, Bits, Counter64, NotificationType, Gauge32, ObjectIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Bits", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
eltexBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 35))
eltexBridgeExtMIB.setRevisions(('2015-11-15 00:00',))
if mibBuilder.loadTexts: eltexBridgeExtMIB.setLastUpdated('201511150000Z')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setOrganization('Eltex Enterprise, Ltd.')
eltexBridgeExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 35, 1))
mibBuilder.exportSymbols("ELTEX-BRIDGE-EXT-MIB", PYSNMP_MODULE_ID=eltexBridgeExtMIB, eltexBridgeExtMIB=eltexBridgeExtMIB, eltexBridgeExtMIBObjects=eltexBridgeExtMIBObjects)
