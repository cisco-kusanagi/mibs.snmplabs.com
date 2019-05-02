#
# PySNMP MIB module ZYXEL-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:52:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ModuleIdentity, MibIdentifier, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter32, Counter64, Unsigned32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "MibIdentifier", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86))
if mibBuilder.loadTexts: zyxelVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlan.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelVlan.setContactInfo('')
if mibBuilder.loadTexts: zyxelVlan.setDescription('The subtree for Virtual LAN (VLAN)')
zyxelVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1))
zyVlanType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot1Q", 1), ("portBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanType.setStatus('current')
if mibBuilder.loadTexts: zyVlanType.setDescription('Set 802.1Q VLAN type or Port Based VLAN type.')
zyVlanIngressCheckState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanIngressCheckState.setStatus('current')
if mibBuilder.loadTexts: zyVlanIngressCheckState.setDescription('Enable/Disable tag VLAN Ingress check on the switch. If enabled, the Switch discards incoming frames on a port for VLANs that do not include this port in its member set.')
mibBuilder.exportSymbols("ZYXEL-VLAN-MIB", zyVlanIngressCheckState=zyVlanIngressCheckState, PYSNMP_MODULE_ID=zyxelVlan, zyxelVlan=zyxelVlan, zyVlanType=zyVlanType, zyxelVlanSetup=zyxelVlanSetup)
