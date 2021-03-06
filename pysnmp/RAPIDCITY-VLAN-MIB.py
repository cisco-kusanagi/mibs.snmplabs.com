#
# PySNMP MIB module RAPIDCITY-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPIDCITY-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, TimeTicks, Counter32, Unsigned32, Counter64, MibIdentifier, Gauge32, IpAddress, NotificationType, Bits, ModuleIdentity, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "Counter64", "MibIdentifier", "Gauge32", "IpAddress", "NotificationType", "Bits", "ModuleIdentity", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
RowStatus, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC-v1", "RowStatus", "MacAddress", "TruthValue", "DisplayString")
rapidcity = MibIdentifier((1, 3, 6, 1, 4, 1, 2272))
rapidcityfoo = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1))
rcVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 3))
rcVlanNumVlans = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVlanNumVlans.setStatus('mandatory')
rcVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2), )
if mibBuilder.loadTexts: rcVlanTable.setStatus('mandatory')
rcVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1), ).setIndexNames((0, "RAPIDCITY-VLAN-MIB", "rcVlanId"))
if mibBuilder.loadTexts: rcVlanEntry.setStatus('mandatory')
rcVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVlanId.setStatus('mandatory')
rcVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanName.setStatus('mandatory')
rcVlanColor = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanColor.setStatus('mandatory')
rcVlanHighPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanHighPriority.setStatus('mandatory')
rcVlanRoutingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanRoutingEnable.setStatus('mandatory')
rcVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVlanIfIndex.setStatus('mandatory')
rcVlanAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("flushMacFdb", 2), ("flushArp", 3), ("flushIp", 4), ("flushDynMemb", 5), ("all", 6))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanAction.setStatus('mandatory')
rcVlanResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("success", 3), ("fail", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVlanResult.setStatus('mandatory')
rcVlanStgId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanStgId.setStatus('mandatory')
rcVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("byPort", 1), ("byIpSubnet", 2), ("byProtocolId", 3), ("bySrcMac", 4), ("byDstMcast", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanType.setStatus('mandatory')
rcVlanPortMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanPortMembers.setStatus('mandatory')
rcVlanPotentialMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanPotentialMembers.setStatus('mandatory')
rcVlanStaticMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanStaticMembers.setStatus('mandatory')
rcVlanNotAllowToJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanNotAllowToJoin.setStatus('mandatory')
rcVlanProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("ip", 1), ("ipx802dot3", 2), ("ipx802dot2", 3), ("ipxSnap", 4), ("ipxEthernet2", 5), ("appleTalk", 6), ("decLat", 7), ("decOther", 8), ("sna802dot2", 9), ("snaEthernet2", 10), ("netBios", 11), ("xns", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanProtocolId.setStatus('mandatory')
rcVlanSubnetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanSubnetAddr.setStatus('mandatory')
rcVlanSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanSubnetMask.setStatus('mandatory')
rcVlanAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanAgingTime.setStatus('mandatory')
rcVlanMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 19), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVlanMacAddress.setStatus('mandatory')
rcVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 20), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVlanRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("RAPIDCITY-VLAN-MIB", rcVlanType=rcVlanType, rcVlanId=rcVlanId, rcVlanStgId=rcVlanStgId, rcVlanRoutingEnable=rcVlanRoutingEnable, rcVlanEntry=rcVlanEntry, rapidcityfoo=rapidcityfoo, rcVlanNotAllowToJoin=rcVlanNotAllowToJoin, rcVlanAgingTime=rcVlanAgingTime, rcVlanSubnetMask=rcVlanSubnetMask, rcVlanStaticMembers=rcVlanStaticMembers, rcVlanName=rcVlanName, rcVlanAction=rcVlanAction, rcVlan=rcVlan, rcVlanResult=rcVlanResult, rcVlanProtocolId=rcVlanProtocolId, rcVlanHighPriority=rcVlanHighPriority, rcVlanPortMembers=rcVlanPortMembers, rcVlanMacAddress=rcVlanMacAddress, rcVlanColor=rcVlanColor, rcVlanIfIndex=rcVlanIfIndex, rapidcity=rapidcity, rcVlanNumVlans=rcVlanNumVlans, rcVlanSubnetAddr=rcVlanSubnetAddr, rcVlanPotentialMembers=rcVlanPotentialMembers, rcVlanTable=rcVlanTable, rcVlanRowStatus=rcVlanRowStatus)
