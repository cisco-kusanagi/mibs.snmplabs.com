#
# PySNMP MIB module ZYXEL-PORT-BASED-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-PORT-BASED-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, ObjectIdentity, Integer32, Unsigned32, Counter32, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32", "Gauge32", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPortBasedVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63))
if mibBuilder.loadTexts: zyxelPortBasedVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPortBasedVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelPortBasedVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1))
zyxelPortBasedVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1), )
if mibBuilder.loadTexts: zyxelPortBasedVlanTable.setStatus('current')
zyxelPortBasedVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortBasedVlanEntry.setStatus('current')
zyPortBasedVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortBasedVlanPorts.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-BASED-VLAN-MIB", zyPortBasedVlanPorts=zyPortBasedVlanPorts, zyxelPortBasedVlanEntry=zyxelPortBasedVlanEntry, zyxelPortBasedVlanSetup=zyxelPortBasedVlanSetup, zyxelPortBasedVlan=zyxelPortBasedVlan, PYSNMP_MODULE_ID=zyxelPortBasedVlan, zyxelPortBasedVlanTable=zyxelPortBasedVlanTable)
