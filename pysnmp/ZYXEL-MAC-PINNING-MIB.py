#
# PySNMP MIB module ZYXEL-MAC-PINNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MAC-PINNING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, Counter64, Gauge32, Unsigned32, TimeTicks, Counter32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "Gauge32", "Unsigned32", "TimeTicks", "Counter32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMacPinning = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92))
if mibBuilder.loadTexts: zyxelMacPinning.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMacPinning.setOrganization('Enterprise Solution ZyXEL')
zyxelMacPinningSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1))
zyMacPinningState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningState.setStatus('current')
zyxelMacPinningPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2), )
if mibBuilder.loadTexts: zyxelMacPinningPortTable.setStatus('current')
zyxelMacPinningPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMacPinningPortEntry.setStatus('current')
zyMacPinningPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MAC-PINNING-MIB", zyMacPinningState=zyMacPinningState, zyxelMacPinning=zyxelMacPinning, zyMacPinningPortState=zyMacPinningPortState, zyxelMacPinningSetup=zyxelMacPinningSetup, zyxelMacPinningPortEntry=zyxelMacPinningPortEntry, PYSNMP_MODULE_ID=zyxelMacPinning, zyxelMacPinningPortTable=zyxelMacPinningPortTable)
