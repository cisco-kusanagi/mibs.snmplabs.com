#
# PySNMP MIB module ZYXEL-VLAN-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-VLAN-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, TimeTicks, IpAddress, MibIdentifier, Integer32, Counter64, Counter32, ObjectIdentity, Unsigned32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "Counter64", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlanTrunk = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 90))
if mibBuilder.loadTexts: zyxelVlanTrunk.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlanTrunk.setOrganization('Enterprise Solution ZyXEL')
zyxelVlanTrunkSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 90, 1))
zyxelVlanTrunkPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 90, 1, 1), )
if mibBuilder.loadTexts: zyxelVlanTrunkPortTable.setStatus('current')
zyxelVlanTrunkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 90, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelVlanTrunkPortEntry.setStatus('current')
zyVlanTrunkPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 90, 1, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanTrunkPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-VLAN-TRUNK-MIB", zyxelVlanTrunk=zyxelVlanTrunk, PYSNMP_MODULE_ID=zyxelVlanTrunk, zyxelVlanTrunkSetup=zyxelVlanTrunkSetup, zyxelVlanTrunkPortTable=zyxelVlanTrunkPortTable, zyxelVlanTrunkPortEntry=zyxelVlanTrunkPortEntry, zyVlanTrunkPortState=zyVlanTrunkPortState)
