#
# PySNMP MIB module ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, MibIdentifier, NotificationType, iso, Unsigned32, Counter32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Unsigned32", "Counter32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelBridgeControlProtocolTransparency = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15))
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparency.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparency.setOrganization('Enterprise Solution ZyXEL')
zyxelBridgeControlProtocolTransparencySetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1))
zyBridgeControlProtocolTransparencyState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyBridgeControlProtocolTransparencyState.setStatus('current')
zyxelBridgeControlProtocolTransparencyPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2), )
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparencyPortTable.setStatus('current')
zyxelBridgeControlProtocolTransparencyPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparencyPortEntry.setStatus('current')
zyBridgeControlProtocolTransparencyPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("peer", 0), ("tunnel", 1), ("discard", 2), ("network", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyBridgeControlProtocolTransparencyPortMode.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB", zyxelBridgeControlProtocolTransparencySetup=zyxelBridgeControlProtocolTransparencySetup, zyxelBridgeControlProtocolTransparency=zyxelBridgeControlProtocolTransparency, PYSNMP_MODULE_ID=zyxelBridgeControlProtocolTransparency, zyxelBridgeControlProtocolTransparencyPortTable=zyxelBridgeControlProtocolTransparencyPortTable, zyxelBridgeControlProtocolTransparencyPortEntry=zyxelBridgeControlProtocolTransparencyPortEntry, zyBridgeControlProtocolTransparencyPortMode=zyBridgeControlProtocolTransparencyPortMode, zyBridgeControlProtocolTransparencyState=zyBridgeControlProtocolTransparencyState)
