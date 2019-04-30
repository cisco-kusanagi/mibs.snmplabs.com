#
# PySNMP MIB module ZYXEL-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Bits, Unsigned32, Counter64, MibIdentifier, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86))
if mibBuilder.loadTexts: zyxelVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1))
zyVlanType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot1Q", 1), ("portBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanType.setStatus('current')
zyVlanIngressCheckState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanIngressCheckState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-VLAN-MIB", PYSNMP_MODULE_ID=zyxelVlan, zyxelVlanSetup=zyxelVlanSetup, zyVlanType=zyVlanType, zyVlanIngressCheckState=zyVlanIngressCheckState, zyxelVlan=zyxelVlan)
