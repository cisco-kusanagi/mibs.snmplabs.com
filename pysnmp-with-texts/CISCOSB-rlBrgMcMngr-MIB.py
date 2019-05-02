#
# PySNMP MIB module CISCOSB-rlBrgMcMngr-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-rlBrgMcMngr-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, TimeTicks, Integer32, NotificationType, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter64, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter64", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlBrgMcMngr = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117))
rlBrgMcMngr.setRevisions(('2006-02-12 00:00', '2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlBrgMcMngr.setRevisionsDescriptions(('Editorial changes to support new MIB compilers.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: rlBrgMcMngr.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlBrgMcMngr.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlBrgMcMngr.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlBrgMcMngr.setDescription('The private MIB module definition for Multicast support in CISCOSB devices.')
rlBrgMulticastManagerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMulticastManagerTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastManagerTable.setDescription('The table containing Multicast information for each VLAN.')
rlBrgMulticastManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 1, 1), ).setIndexNames((0, "CISCOSB-rlBrgMcMngr-MIB", "rlBrgMulticastManagerVlanTag"))
if mibBuilder.loadTexts: rlBrgMulticastManagerEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastManagerEntry.setDescription('An entry (conceptual row) in the rlBrgMulticastManagerTable.')
rlBrgMulticastManagerVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgMulticastManagerVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastManagerVlanTag.setDescription(' The VLAN tag for which this entry is configured.')
rlBrgMulticastManagerAdminVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mac-group", 1), ("ip-group", 2), ("ip-src-group", 3))).clone('mac-group')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMulticastManagerAdminVlanMode.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastManagerAdminVlanMode.setDescription('The Bridge Multicast Admin Lookup Mode.')
rlBrgMulticastManagerOperVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mac-group", 1), ("ip-group", 2), ("ip-src-group", 3))).clone('mac-group')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMulticastManagerOperVlanMode.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastManagerOperVlanMode.setDescription('The Bridge Multicast Oper Lookup Mode.')
rlBrgMulticastInetManagerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMulticastInetManagerTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerTable.setDescription('The table containing Multicast information for each VLAN.')
rlBrgMulticastInetManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2, 1), ).setIndexNames((0, "CISCOSB-rlBrgMcMngr-MIB", "rlBrgMulticastInetManagerIpType"), (0, "CISCOSB-rlBrgMcMngr-MIB", "rlBrgMulticastInetManagerVlanTag"))
if mibBuilder.loadTexts: rlBrgMulticastInetManagerEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerEntry.setDescription('An entry (conceptual row) in the rlBrgMulticastInetManagerTable.')
rlBrgMulticastInetManagerIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 16))).clone(namedValues=NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("dns", 16))))
if mibBuilder.loadTexts: rlBrgMulticastInetManagerIpType.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerIpType.setDescription('The address type of Vlan Mode.')
rlBrgMulticastInetManagerVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2, 1, 2), VlanIndex())
if mibBuilder.loadTexts: rlBrgMulticastInetManagerVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerVlanTag.setDescription(' The VLAN tag for which this entry is configured.')
rlBrgMulticastInetManagerAdminVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mac-group", 1), ("ip-group", 2), ("ip-src-group", 3))).clone('mac-group')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgMulticastInetManagerAdminVlanMode.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerAdminVlanMode.setDescription('The Bridge Multicast Admin Lookup Mode.')
rlBrgMulticastInetManagerOperVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mac-group", 1), ("ip-group", 2), ("ip-src-group", 3))).clone('mac-group')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMulticastInetManagerOperVlanMode.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastInetManagerOperVlanMode.setDescription('The Bridge Multicast Oper Lookup Mode.')
mibBuilder.exportSymbols("CISCOSB-rlBrgMcMngr-MIB", rlBrgMulticastInetManagerIpType=rlBrgMulticastInetManagerIpType, rlBrgMulticastInetManagerOperVlanMode=rlBrgMulticastInetManagerOperVlanMode, rlBrgMulticastManagerEntry=rlBrgMulticastManagerEntry, rlBrgMulticastManagerOperVlanMode=rlBrgMulticastManagerOperVlanMode, PYSNMP_MODULE_ID=rlBrgMcMngr, rlBrgMulticastManagerVlanTag=rlBrgMulticastManagerVlanTag, rlBrgMulticastManagerTable=rlBrgMulticastManagerTable, rlBrgMcMngr=rlBrgMcMngr, rlBrgMulticastInetManagerEntry=rlBrgMulticastInetManagerEntry, rlBrgMulticastInetManagerVlanTag=rlBrgMulticastInetManagerVlanTag, rlBrgMulticastManagerAdminVlanMode=rlBrgMulticastManagerAdminVlanMode, rlBrgMulticastInetManagerTable=rlBrgMulticastInetManagerTable, rlBrgMulticastInetManagerAdminVlanMode=rlBrgMulticastInetManagerAdminVlanMode)
