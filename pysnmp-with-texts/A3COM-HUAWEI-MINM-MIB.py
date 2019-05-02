#
# PySNMP MIB module A3COM-HUAWEI-MINM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MINM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
h3cVsiIndex, = mibBuilder.importSymbols("A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Bits, ModuleIdentity, Unsigned32, Counter32, Integer32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "Unsigned32", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "iso", "NotificationType")
RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
h3cMinm = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107))
h3cMinm.setRevisions(('2009-08-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cMinm.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: h3cMinm.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: h3cMinm.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3cMinm.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cMinm.setDescription('802.1ah MAC-in-MAC MIB')
class H3cMinmEnabledStatus(TextualConvention, Integer32):
    description = 'A enumerated value which indicates the state of object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cMinmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1))
h3cMinmScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1))
h3cMinmCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1, 1), Bits().clone(namedValues=NamedValues(("reEncapsulation", 0), ("uplink", 1), ("vsiShareConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMinmCapabilities.setStatus('current')
if mibBuilder.loadTexts: h3cMinmCapabilities.setDescription('This object displays the MAC-in-MAC capabilities with respect to certain fields. The following values may be supported: reEncapsulation: Support for configuring re-encapsulation (denoted by h3cMinmVsiReEncapsulation). uplink: Support for configuring uplink (denoted by h3cMinmUplinkTable). vsiShareConnection: It indicates that connection entry is shared in all VSIs. h3cVsiIndex is meaningless and must be value 1 in h3cMinmConnectionTable.')
h3cMinmBmac = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMinmBmac.setStatus('current')
if mibBuilder.loadTexts: h3cMinmBmac.setDescription('A MAC address used in creating the MAC header of I-tagged frames transmitted across a Provider Backbone Bridged Network. The invalid value FF:FF:FF:FF:FF:FF indicates that this node is not supported by the device.')
h3cMinmVsiTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2), )
if mibBuilder.loadTexts: h3cMinmVsiTable.setStatus('current')
if mibBuilder.loadTexts: h3cMinmVsiTable.setDescription('A table for configuring MAC-in-MAC service instance parameter.')
h3cMinmVsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"))
if mibBuilder.loadTexts: h3cMinmVsiEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMinmVsiEntry.setDescription('An entry for configuring MAC-in-MAC service instance parameter.')
h3cMinmVsiBvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMinmVsiBvlan.setStatus('current')
if mibBuilder.loadTexts: h3cMinmVsiBvlan.setDescription('BVLAN ID. The value 65535 indicates the BVLAN has not been configured for get operation, and it indicates deleting the BVLAN configration for set operation.')
h3cMinmVsiReEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 2), H3cMinmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMinmVsiReEncapsulation.setStatus('current')
if mibBuilder.loadTexts: h3cMinmVsiReEncapsulation.setDescription('Whether the re-encapsulation is enabled. The reEncapsulation field of h3cMinmCapabilities denotes whether this node is supported.')
h3cMinmVsiNextAvailableLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMinmVsiNextAvailableLinkId.setStatus('current')
if mibBuilder.loadTexts: h3cMinmVsiNextAvailableLinkId.setDescription('Next available connection entry index for creating a connection entry. Its value ranges from 0x1 to 0xFFFFFFFF.The invalid value 0xFFFFFFFF indicates that connection entry can not be created. When the vsiShareConnection field of h3cMinmCapabilities is set, this node returns an invalid value if the value of h3cVsiIndex is not 1.')
h3cMinmUplinkTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3), )
if mibBuilder.loadTexts: h3cMinmUplinkTable.setStatus('current')
if mibBuilder.loadTexts: h3cMinmUplinkTable.setDescription('A table for uplink ports of the VSI in MAC-in-MAC. The uplink field of h3cMinmCapabilities denotes whether this table is supported.')
h3cMinmUplinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cMinmUplinkEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMinmUplinkEntry.setDescription('An entry for uplink ports of the VSI in MAC-in-MAC.')
h3cMinmUplinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmUplinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMinmUplinkRowStatus.setDescription('Operation status of this table entry.')
h3cMinmConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4), )
if mibBuilder.loadTexts: h3cMinmConnectionTable.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionTable.setDescription('A table for the connection information of BMAC.')
h3cMinmConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"), (0, "A3COM-HUAWEI-MINM-MIB", "h3cMinmConnectionLinkId"))
if mibBuilder.loadTexts: h3cMinmConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionEntry.setDescription('An entry for the connection information of BMAC. When the vsiShareConnection field of h3cMinmCapabilities is set, connection entry is shared in all VSIs. h3cVsiIndex is meaningless and must be value 1 in h3cMinmConnectionTable.')
h3cMinmConnectionLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cMinmConnectionLinkId.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionLinkId.setDescription('Entry index when the vsiShareConnection bit of h3cMinmCapabilities is set(h3cVsiIndex is meaningless and must be value 1), else entry index in the VSI of h3cVsiIndex.Its value ranges from 0x1 to 0xFFFFFFFE. It should be obtained from h3cMinmVsiNextAvailableLinkId for create operation.')
h3cMinmConnectionBmac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmConnectionBmac.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionBmac.setDescription('BMAC of an connection entry.')
h3cMinmConnectionBvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmConnectionBvlan.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionBvlan.setDescription('BVLAN of an connection entry.')
h3cMinmConnectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmConnectionPort.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionPort.setDescription('Port ifindex of an connection entry.')
h3cMinmConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("learned", 1), ("configDynamic", 2), ("configStatic", 3), ("blackhole", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmConnectionStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionStatus.setDescription('State of an connection entry.')
h3cMinmConnectionAgingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aging", 1), ("noAged", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMinmConnectionAgingStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionAgingStatus.setDescription('Aging time of an connection entry.')
h3cMinmConnectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmConnectionRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMinmConnectionRowStatus.setDescription('Operation status of this table entry.')
mibBuilder.exportSymbols("A3COM-HUAWEI-MINM-MIB", h3cMinmVsiBvlan=h3cMinmVsiBvlan, h3cMinmVsiNextAvailableLinkId=h3cMinmVsiNextAvailableLinkId, h3cMinmConnectionBvlan=h3cMinmConnectionBvlan, h3cMinmUplinkEntry=h3cMinmUplinkEntry, h3cMinmConnectionTable=h3cMinmConnectionTable, h3cMinmUplinkRowStatus=h3cMinmUplinkRowStatus, h3cMinmConnectionBmac=h3cMinmConnectionBmac, h3cMinmScalarGroup=h3cMinmScalarGroup, h3cMinmObjects=h3cMinmObjects, h3cMinmBmac=h3cMinmBmac, h3cMinmVsiEntry=h3cMinmVsiEntry, h3cMinm=h3cMinm, H3cMinmEnabledStatus=H3cMinmEnabledStatus, h3cMinmVsiTable=h3cMinmVsiTable, h3cMinmUplinkTable=h3cMinmUplinkTable, h3cMinmConnectionLinkId=h3cMinmConnectionLinkId, h3cMinmCapabilities=h3cMinmCapabilities, PYSNMP_MODULE_ID=h3cMinm, h3cMinmConnectionRowStatus=h3cMinmConnectionRowStatus, h3cMinmConnectionPort=h3cMinmConnectionPort, h3cMinmConnectionStatus=h3cMinmConnectionStatus, h3cMinmConnectionEntry=h3cMinmConnectionEntry, h3cMinmConnectionAgingStatus=h3cMinmConnectionAgingStatus, h3cMinmVsiReEncapsulation=h3cMinmVsiReEncapsulation)
