#
# PySNMP MIB module DGS-3700-12G-L3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-3700-12G-L3MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:29:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, MibIdentifier, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Bits, ObjectIdentity, ModuleIdentity, Unsigned32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibIdentifier", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Bits", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Gauge32", "iso")
DisplayString, TimeStamp, PhysAddress, RowStatus, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "PhysAddress", "RowStatus", "MacAddress", "TextualConvention", "TruthValue")
dgs3712g, = mibBuilder.importSymbols("SW3700PRIMGMT-MIB", "dgs3712g")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('200811190000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization(' ')
class NodeAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1))
class Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class VrId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1), ).setIndexNames((0, "DGS-3700-12G-L3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
swL3IpCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setStatus('current')
swL3IpCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setStatus('current')
swL3IpCtrlIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setStatus('current')
swL3IpCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setStatus('current')
swL3IpCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlMode.setStatus('current')
swL3IpCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setStatus('current')
swL3IpCtrlIpv6LinkLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 14), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setStatus('current')
swL3IpCtrlIpv6LinkLocalPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus('current')
swL3IpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpCtrlState.setStatus('current')
swL3IpCtrlIpv6LinkLocalAutoState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setStatus('current')
swL3Ipv6CtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 4), )
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setStatus('current')
swL3Ipv6CtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 4, 1), ).setIndexNames((0, "DGS-3700-12G-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"))
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setStatus('current')
swL3Ipv6CtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setStatus('current')
swL3Ipv6CtrlNsRetransTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setStatus('current')
swL3Ipv6AddressCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5), )
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setStatus('current')
swL3Ipv6AddressCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5, 1), ).setIndexNames((0, "DGS-3700-12G-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"), (0, "DGS-3700-12G-L3MGMT-MIB", "swL3Ipv6Address"), (0, "DGS-3700-12G-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"))
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setStatus('current')
swL3Ipv6AddressCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setStatus('current')
swL3Ipv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6Address.setStatus('current')
swL3Ipv6AddressCtrlPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setStatus('current')
swL3Ipv6AddressCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setStatus('current')
swL3IpCtrlAllIpIfState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setStatus('current')
mibBuilder.exportSymbols("DGS-3700-12G-L3MGMT-MIB", swL3IpCtrlMgmt=swL3IpCtrlMgmt, NetAddress=NetAddress, swL3MgmtMIB=swL3MgmtMIB, NodeAddress=NodeAddress, swL3Ipv6AddressCtrlPrefixLen=swL3Ipv6AddressCtrlPrefixLen, PYSNMP_MODULE_ID=swL3MgmtMIB, swL3IpCtrlEntry=swL3IpCtrlEntry, swL3Ipv6CtrlTable=swL3Ipv6CtrlTable, swL3Ipv6Address=swL3Ipv6Address, swL3IpCtrlTable=swL3IpCtrlTable, swL3IpCtrlState=swL3IpCtrlState, swL3IpCtrlIpSubnetMask=swL3IpCtrlIpSubnetMask, Ipv6Address=Ipv6Address, swL3IpMgmt=swL3IpMgmt, swL3Ipv6AddressCtrlTable=swL3Ipv6AddressCtrlTable, swL3Ipv6CtrlNsRetransTimer=swL3Ipv6CtrlNsRetransTimer, swL3IpCtrlIpv6LinkLocalPrefixLen=swL3IpCtrlIpv6LinkLocalPrefixLen, swL3IpCtrlVlanName=swL3IpCtrlVlanName, swL3IpCtrlMode=swL3IpCtrlMode, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3Ipv6AddressCtrlInterfaceName=swL3Ipv6AddressCtrlInterfaceName, swL3IpCtrlIpv6LinkLocalAutoState=swL3IpCtrlIpv6LinkLocalAutoState, swL3Ipv6CtrlEntry=swL3Ipv6CtrlEntry, swL3Ipv6AddressCtrlEntry=swL3Ipv6AddressCtrlEntry, swL3Ipv6CtrlInterfaceName=swL3Ipv6CtrlInterfaceName, swL3IpCtrlIpAddr=swL3IpCtrlIpAddr, swL3IpCtrlAllIpIfState=swL3IpCtrlAllIpIfState, swL3IpCtrlAdminState=swL3IpCtrlAdminState, VrId=VrId, swL3IpCtrlIfIndex=swL3IpCtrlIfIndex, swL3IpCtrlIpv6LinkLocalAddress=swL3IpCtrlIpv6LinkLocalAddress, swL3Ipv6AddressCtrlState=swL3Ipv6AddressCtrlState)
