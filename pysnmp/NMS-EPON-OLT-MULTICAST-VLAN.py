#
# PySNMP MIB module NMS-EPON-OLT-MULTICAST-VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OLT-MULTICAST-VLAN
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, Counter32, NotificationType, MibIdentifier, IpAddress, iso, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "MibIdentifier", "IpAddress", "iso", "Bits", "TimeTicks", "Unsigned32")
MacAddress, DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
nmsEponOltMulticastVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5))
nmseponoltmulticastvlanTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1), )
if mibBuilder.loadTexts: nmseponoltmulticastvlanTable.setStatus('mandatory')
nmsEponOltMulticastVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1), ).setIndexNames((0, "NMS-EPON-OLT-MULTICAST-VLAN", "oltMcVlanId"), (0, "NMS-EPON-OLT-MULTICAST-VLAN", "oltMcIpAddress"))
if mibBuilder.loadTexts: nmsEponOltMulticastVlanEntry.setStatus('mandatory')
oltMcVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltMcVlanId.setStatus('mandatory')
oltMcVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltMcVlanIpAddress.setStatus('mandatory')
oltMcVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oltMcVlanRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-OLT-MULTICAST-VLAN", oltMcVlanRowStatus=oltMcVlanRowStatus, oltMcVlanId=oltMcVlanId, oltMcVlanIpAddress=oltMcVlanIpAddress, nmsEponOltMulticastVlan=nmsEponOltMulticastVlan, nmseponoltmulticastvlanTable=nmseponoltmulticastvlanTable, nmsEponOltMulticastVlanEntry=nmsEponOltMulticastVlanEntry)
