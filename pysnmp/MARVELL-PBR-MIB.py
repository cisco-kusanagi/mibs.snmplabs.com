#
# PySNMP MIB module MARVELL-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-PBR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressType, InetAddressIPv6, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressIPv6", "InetAddress")
rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrRouteMapName = mibBuilder.importSymbols("MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId", "rlRouteMapPbrRouteMapName")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, NotificationType, ObjectIdentity, Counter64, Gauge32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "NotificationType", "ObjectIdentity", "Counter64", "Gauge32", "MibIdentifier", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlPolicyBasedRouting = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 228))
rlPolicyBasedRouting.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: rlPolicyBasedRouting.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setOrganization('Marvell Inc.')
class RlPBRInetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class RlPBRStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("noIp", 2), ("interfaceDown", 3))

rlPBRTable = MibTable((1, 3, 6, 1, 4, 1, 89, 228, 1), )
if mibBuilder.loadTexts: rlPBRTable.setStatus('current')
rlPBREntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 228, 1, 1), ).setIndexNames((0, "MARVELL-PBR-MIB", "rlPBRIfIndex"), (0, "MARVELL-PBR-MIB", "rlPBRInetType"))
if mibBuilder.loadTexts: rlPBREntry.setStatus('current')
rlPBRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlPBRIfIndex.setStatus('current')
rlPBRInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 2), RlPBRInetType())
if mibBuilder.loadTexts: rlPBRInetType.setStatus('current')
rlPBRRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRouteMapName.setStatus('current')
rlPBRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 4), RlPBRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRStatus.setStatus('current')
rlPBRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRowStatus.setStatus('current')
class RlPBRNexthopStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notReachable", 2), ("notDirect", 3))

rlPBRInfoTable = MibTable((1, 3, 6, 1, 4, 1, 89, 228, 2), )
if mibBuilder.loadTexts: rlPBRInfoTable.setStatus('current')
rlPBRInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 228, 2, 1), ).setIndexNames((0, "MARVELL-PBR-MIB", "rlPBRInetType"), (0, "MARVELL-PBR-MIB", "rlPBRIfIndex"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"))
if mibBuilder.loadTexts: rlPBRInfoEntry.setStatus('current')
rlPBRInfoAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setStatus('current')
rlPBRInfoNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setStatus('current')
rlPBRInfoNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setStatus('current')
rlPBRInfoNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setStatus('current')
rlPBRInfoNexthopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 5), RlPBRNexthopStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setStatus('current')
mibBuilder.exportSymbols("MARVELL-PBR-MIB", rlPBRRowStatus=rlPBRRowStatus, rlPBRInfoNexthopInetAddress=rlPBRInfoNexthopInetAddress, PYSNMP_MODULE_ID=rlPolicyBasedRouting, RlPBRNexthopStatusType=RlPBRNexthopStatusType, rlPolicyBasedRouting=rlPolicyBasedRouting, RlPBRStatusType=RlPBRStatusType, rlPBRInfoTable=rlPBRInfoTable, rlPBREntry=rlPBREntry, rlPBRInfoAccessListName=rlPBRInfoAccessListName, rlPBRInetType=rlPBRInetType, RlPBRInetType=RlPBRInetType, rlPBRInfoNexthopIfIndex=rlPBRInfoNexthopIfIndex, rlPBRIfIndex=rlPBRIfIndex, rlPBRInfoEntry=rlPBRInfoEntry, rlPBRInfoNexthopInetAddressType=rlPBRInfoNexthopInetAddressType, rlPBRInfoNexthopStatus=rlPBRInfoNexthopStatus, rlPBRTable=rlPBRTable, rlPBRRouteMapName=rlPBRRouteMapName, rlPBRStatus=rlPBRStatus)
