#
# PySNMP MIB module ELTEX-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Integer32, Counter64, Unsigned32, Counter32, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
eltexBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 35))
eltexBridgeExtMIB.setRevisions(('2015-11-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltexBridgeExtMIB.setRevisionsDescriptions(('The initial version of this MIB module',))
if mibBuilder.loadTexts: eltexBridgeExtMIB.setLastUpdated('201511150000Z')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setOrganization('Eltex Enterprise, Ltd.')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setDescription('This MIB module contains Bridge Extension MIB definitions for Eltex Networks.')
eltexBridgeExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 35, 1))
mibBuilder.exportSymbols("ELTEX-BRIDGE-EXT-MIB", eltexBridgeExtMIBObjects=eltexBridgeExtMIBObjects, eltexBridgeExtMIB=eltexBridgeExtMIB, PYSNMP_MODULE_ID=eltexBridgeExtMIB)
