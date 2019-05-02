#
# PySNMP MIB module MARVELL-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-PBR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
rlRouteMapPbrRouteMapName, rlRouteMapPbrRouteMapSectionId = mibBuilder.importSymbols("MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName", "rlRouteMapPbrRouteMapSectionId")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Integer32, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Gauge32, ObjectIdentity, NotificationType, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Gauge32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rlPolicyBasedRouting = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 228))
rlPolicyBasedRouting.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlPolicyBasedRouting.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlPolicyBasedRouting.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setOrganization('Marvell Inc.')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setContactInfo('www.Marvell.com')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setDescription('The private MIB module definition for Policy-Based Routing mechanism.')
class RlPBRInetType(TextualConvention, Integer32):
    description = 'The inet type of a policy'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class RlPBRStatusType(TextualConvention, Integer32):
    description = 'The types of status for policy-based routing entry'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("noIp", 2), ("interfaceDown", 3))

rlPBRTable = MibTable((1, 3, 6, 1, 4, 1, 89, 228, 1), )
if mibBuilder.loadTexts: rlPBRTable.setStatus('current')
if mibBuilder.loadTexts: rlPBRTable.setDescription('Table containing policy-based routing binding information.')
rlPBREntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 228, 1, 1), ).setIndexNames((0, "MARVELL-PBR-MIB", "rlPBRIfIndex"), (0, "MARVELL-PBR-MIB", "rlPBRInetType"))
if mibBuilder.loadTexts: rlPBREntry.setStatus('current')
if mibBuilder.loadTexts: rlPBREntry.setDescription('The row definition for this table.')
rlPBRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlPBRIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlPBRIfIndex.setDescription('IfIndex on which policy based routing is applied.')
rlPBRInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 2), RlPBRInetType())
if mibBuilder.loadTexts: rlPBRInetType.setStatus('current')
if mibBuilder.loadTexts: rlPBRInetType.setDescription('Inet type of this entry.')
rlPBRRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRouteMapName.setStatus('current')
if mibBuilder.loadTexts: rlPBRRouteMapName.setDescription('Route map name to apply.')
rlPBRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 4), RlPBRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRStatus.setDescription('The route status for this entry.')
rlPBRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRRowStatus.setDescription('The row status of this entry.')
class RlPBRNexthopStatusType(TextualConvention, Integer32):
    description = 'The types of status of nexthop for policy-based routing entry'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notReachable", 2), ("notDirect", 3))

rlPBRInfoTable = MibTable((1, 3, 6, 1, 4, 1, 89, 228, 2), )
if mibBuilder.loadTexts: rlPBRInfoTable.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoTable.setDescription('Table containing policy-based routing information.')
rlPBRInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 228, 2, 1), ).setIndexNames((0, "MARVELL-PBR-MIB", "rlPBRInetType"), (0, "MARVELL-PBR-MIB", "rlPBRIfIndex"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"))
if mibBuilder.loadTexts: rlPBRInfoEntry.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoEntry.setDescription('The row definition for this table.')
rlPBRInfoAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setDescription('Access-list name of policy-based routing.')
rlPBRInfoNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setDescription('Inet type of rlPBRInfoNexthopInetAddress')
rlPBRInfoNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setDescription('Inet address of nexthop, if used for action.')
rlPBRInfoNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setDescription('Inet address of nexthop, if used for action.')
rlPBRInfoNexthopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 228, 2, 1, 5), RlPBRNexthopStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setDescription('Status of nexthop.')
mibBuilder.exportSymbols("MARVELL-PBR-MIB", rlPBRRowStatus=rlPBRRowStatus, rlPBRInfoAccessListName=rlPBRInfoAccessListName, rlPBRInfoNexthopInetAddressType=rlPBRInfoNexthopInetAddressType, RlPBRInetType=RlPBRInetType, rlPBRInfoNexthopIfIndex=rlPBRInfoNexthopIfIndex, rlPBRInfoTable=rlPBRInfoTable, rlPBRIfIndex=rlPBRIfIndex, rlPBRTable=rlPBRTable, rlPBREntry=rlPBREntry, rlPBRInfoEntry=rlPBRInfoEntry, rlPBRInfoNexthopInetAddress=rlPBRInfoNexthopInetAddress, RlPBRNexthopStatusType=RlPBRNexthopStatusType, PYSNMP_MODULE_ID=rlPolicyBasedRouting, rlPolicyBasedRouting=rlPolicyBasedRouting, rlPBRStatus=rlPBRStatus, RlPBRStatusType=RlPBRStatusType, rlPBRRouteMapName=rlPBRRouteMapName, rlPBRInetType=rlPBRInetType, rlPBRInfoNexthopStatus=rlPBRInfoNexthopStatus)
