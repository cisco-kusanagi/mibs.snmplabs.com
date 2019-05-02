#
# PySNMP MIB module FASTPATH-ISDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-ISDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, Bits, TimeTicks, MibIdentifier, Counter32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "IpAddress", "Gauge32")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
fastPathIsdp = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39))
fastPathIsdp.setRevisions(('2010-01-11 00:00', '2007-12-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathIsdp.setRevisionsDescriptions(("Device ID can be system's host name too.", 'Initial version.',))
if mibBuilder.loadTexts: fastPathIsdp.setLastUpdated('200712030000Z')
if mibBuilder.loadTexts: fastPathIsdp.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathIsdp.setContactInfo(' Customer Support Postal: Broadcom Corporation 100, Perimeter Park Drive Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathIsdp.setDescription('The Broadcom Private MIB for FastPath ISDP')
agentIsdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1))
agentIsdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2))
agentIsdpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3))
agentIsdpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1), )
if mibBuilder.loadTexts: agentIsdpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: agentIsdpInterfaceTable.setDescription("The (conceptual) table containing the status of ISDP on the device's interfaces.")
agentIsdpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1), ).setIndexNames((0, "FASTPATH-ISDP-MIB", "agentIsdpInterfaceIfIndex"))
if mibBuilder.loadTexts: agentIsdpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: agentIsdpInterfaceEntry.setDescription('An entry (conceptual row) in the agentIsdpInterfaceTable, containing the status of ISDP on an interface.')
agentIsdpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: agentIsdpInterfaceIfIndex.setDescription('The ifIndex value of the local interface. For 802.3 Repeaters on which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; in this case, the specific port is indicated by corresponding values of agentIsdpInterfaceGroup and agentIsdpInterfacePort, where these values correspond to the group number and port number values of RFC 1516.')
agentIsdpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpInterfaceEnable.setStatus('current')
if mibBuilder.loadTexts: agentIsdpInterfaceEnable.setDescription('An indication of whether the Industry Standard Discovery Protocol is currently running on this interface. This variable has no effect when ISDP is disabled (agentIsdpGlobalRun = FALSE).')
agentIsdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1), )
if mibBuilder.loadTexts: agentIsdpCacheTable.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheTable.setDescription('The (conceptual) table containing the cached information obtained via receiving ISDP messages.')
agentIsdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1), ).setIndexNames((0, "FASTPATH-ISDP-MIB", "agentIsdpCacheIfIndex"), (0, "FASTPATH-ISDP-MIB", "agentIsdpCacheIndex"))
if mibBuilder.loadTexts: agentIsdpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheEntry.setDescription('An entry (conceptual row) in the agentIsdpCacheTable, containing the information received via ISDP on one interface from one device. Entries appear when a ISDP advertisement is received from a neighbor device. Entries disappear when ISDP is disabled on the interface, or globally.')
agentIsdpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheIfIndex.setDescription('Normally, the ifIndex value of the local interface.')
agentIsdpCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIndex.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheIndex.setDescription('Index value is unique integer id of each neighbor entry.')
agentIsdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheAddress.setDescription("The (first) network-layer address of the device's SNMP-agent as reported in the Address TLV of the most recently received ISDP message. For example, if the corresponding instance of cacheAddressType had the value 'ip(1)', then this object would be an IP-address.")
agentIsdpCacheLocalIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLocalIntf.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheLocalIntf.setDescription('The device Interface which had this neighbor.')
agentIsdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheVersion.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheVersion.setDescription('The Version string as reported in the most recent ISDP message. The zero-length string indicates that no Version field (TLV) was reported in the most recent ISDP message.')
agentIsdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDeviceId.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheDeviceId.setDescription('The Device-ID string as reported in the most recent ISDP message. The zero-length string indicates that no Device-ID field (TLV) was reported in the most recent ISDP message.')
agentIsdpCacheDevicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDevicePort.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheDevicePort.setDescription("The Port-ID string as reported in the most recent ISDP message. This will typically be the value of the ifName object (e.g., 'Ethernet0'). The zero-length string indicates that no Port-ID field (TLV) was reported in the most recent ISDP message.")
agentIsdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCachePlatform.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCachePlatform.setDescription("The Device's Hardware Platform as reported in the most recent ISDP message. The zero-length string indicates that no Platform field (TLV) was reported in the most recent ISDP message.")
agentIsdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheCapabilities.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheCapabilities.setDescription("The Device's Functional Capabilities as reported in the most recent ISDP message. For latest set of specific values, see the latest version of the ISDP specification. The zero-length string indicates that no Capabilities field (TLV) was reported in the most recent ISDP message.")
agentIsdpCacheLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLastChange.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheLastChange.setDescription('Indicates the time when this cache entry was last changed. This object is initialised to the current time when the entry gets created and updated to the current time whenever the value of any (other) object instance in the corresponding row is modified.')
agentIsdpCacheProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheProtocolVersion.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheProtocolVersion.setDescription("The Device's version of ISDP protcol as reported in the most recent ISDP message.")
agentIsdpCacheHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheHoldtime.setStatus('current')
if mibBuilder.loadTexts: agentIsdpCacheHoldtime.setDescription("The Device's ISDP Holdtime as reported in the most recent ISDP message.")
agentIsdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1))
agentIsdpClear = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1))
agentIsdpClearStats = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearStats.setStatus('current')
if mibBuilder.loadTexts: agentIsdpClearStats.setDescription('Clear ISDP stats.')
agentIsdpClearEntries = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearEntries.setStatus('current')
if mibBuilder.loadTexts: agentIsdpClearEntries.setDescription('Clear ISDP entries table.')
agentIsdpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2))
agentIsdpStatisticsPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsPduReceived.setDescription('Display the number of all ISDP pdu received.')
agentIsdpStatisticsPduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduTransmit.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsPduTransmit.setDescription('Display the number of all ISDP pdu transmitted.')
agentIsdpStatisticsV1PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduReceived.setDescription('Display the number of v1 ISDP pdu received.')
agentIsdpStatisticsV1PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduTransmit.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduTransmit.setDescription('Display the number of v1 ISDP pdu transmitted.')
agentIsdpStatisticsV2PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduReceived.setDescription('Display the number of v2 ISDP pdu received.')
agentIsdpStatisticsV2PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduTransmit.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduTransmit.setDescription('Display the number of v2 ISDP pdu transmitted.')
agentIsdpStatisticsBadHeaderPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsBadHeaderPduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsBadHeaderPduReceived.setDescription('Display the number of ISDP pdu with bad header received.')
agentIsdpStatisticsChkSumErrorPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsChkSumErrorPduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsChkSumErrorPduReceived.setDescription('Display the number of ISDP pdu with chksum error received.')
agentIsdpStatisticsFailurePduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsFailurePduTransmit.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsFailurePduTransmit.setDescription('Display the number of ISDP pdu transmition failures.')
agentIsdpStatisticsInvalidFormatPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsInvalidFormatPduReceived.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsInvalidFormatPduReceived.setDescription('Display the number of ISDP pdu in invalid format received.')
agentIsdpStatisticsTableFull = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 11), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsTableFull.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsTableFull.setDescription('Display the number of ISDP entry table was full.')
agentIsdpStatisticsIpAddressTableFull = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 12), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsIpAddressTableFull.setStatus('current')
if mibBuilder.loadTexts: agentIsdpStatisticsIpAddressTableFull.setDescription('Display the number of ISDP entry address table was full.')
agentIsdpGlobalRun = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalRun.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalRun.setDescription('An indication of whether the Indastry Standart Discovery Protocol is currently running. Entries in agentIsdpCacheTable are deleted when ISDP is disabled.')
agentIsdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalMessageInterval.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalMessageInterval.setDescription('The interval at which ISDP messages are to be generated. The default value is 60 seconds. This is also known as the ISDP timer.')
agentIsdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalHoldTime.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalHoldTime.setDescription('The time for the receiving device holds ISDP message. The default value is 180 seconds.')
agentIsdpGlobalDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceId.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalDeviceId.setDescription('The device ID advertised by this device. The format of this device ID is characterized by the value of agentIsdpGlobalDeviceIdFormat object.')
agentIsdpGlobalAdvertiseV2 = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalAdvertiseV2.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalAdvertiseV2.setDescription('An indication of whether the Indastry Standart Discovery Protocol V2 is currently enabled.')
agentIsdpGlobalDeviceIdFormatCpb = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 9), Bits().clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 4), ("hostName", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormatCpb.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormatCpb.setDescription('Indicate the Device ID format capability of the device. serialNumber(0) indicates that the device supports using serial number as the format for its Device ID. macAddress(1) indicates that the device supports using layer 2 MAC address as the format for its Device ID. other(2) indicates that the device supports using its platform specific format as the format for its Device ID. hostName(3) indicates that the device supports using system Host Name as the format for its Device ID.')
agentIsdpGlobalDeviceIdFormat = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 3), ("hostName", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormat.setStatus('current')
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormat.setDescription('An indication of the format of Device ID contained in the corresponding instance of agentIsdpGlobalDeviceId. User can only specify the formats which the device is capable of as denoted in agentIsdpGlobalDeviceIdFormatCpb object. serialNumber(1) indicates that the value of agentIsdpGlobalDeviceId object is in the form of an ASCII string contain the device serial number. macAddress(2) indicates that the value of agentIsdpGlobalDeviceId object is in the form of Layer 2 MAC address. other(3) indicates that the value of agentIsdpGlobalDeviceId object is in the form of a platform specific ASCII string contain info that identifies the device. For example: ASCII string contains serialNumber appended/prepened with system name. hostName(4) indicates that the value of agentIsdpGlobalDeviceIdFormat object is in system Host Name format.')
mibBuilder.exportSymbols("FASTPATH-ISDP-MIB", agentIsdpCachePlatform=agentIsdpCachePlatform, agentIsdpCacheLocalIntf=agentIsdpCacheLocalIntf, agentIsdpCacheLastChange=agentIsdpCacheLastChange, agentIsdpGlobalRun=agentIsdpGlobalRun, agentIsdpCacheEntry=agentIsdpCacheEntry, agentIsdpStatisticsV2PduReceived=agentIsdpStatisticsV2PduReceived, agentIsdpStatisticsV2PduTransmit=agentIsdpStatisticsV2PduTransmit, agentIsdpCacheDevicePort=agentIsdpCacheDevicePort, agentIsdpCacheHoldtime=agentIsdpCacheHoldtime, agentIsdpGlobal=agentIsdpGlobal, agentIsdpCacheVersion=agentIsdpCacheVersion, agentIsdpInterface=agentIsdpInterface, agentIsdpGlobalAdvertiseV2=agentIsdpGlobalAdvertiseV2, agentIsdpStatisticsV1PduTransmit=agentIsdpStatisticsV1PduTransmit, agentIsdpInterfaceEntry=agentIsdpInterfaceEntry, agentIsdpStatisticsTableFull=agentIsdpStatisticsTableFull, agentIsdpCacheIfIndex=agentIsdpCacheIfIndex, agentIsdpGlobalDeviceIdFormatCpb=agentIsdpGlobalDeviceIdFormatCpb, agentIsdpClearStats=agentIsdpClearStats, agentIsdpClearEntries=agentIsdpClearEntries, agentIsdpStatisticsChkSumErrorPduReceived=agentIsdpStatisticsChkSumErrorPduReceived, agentIsdpStatisticsIpAddressTableFull=agentIsdpStatisticsIpAddressTableFull, agentIsdpStatisticsInvalidFormatPduReceived=agentIsdpStatisticsInvalidFormatPduReceived, agentIsdpMIBObjects=agentIsdpMIBObjects, agentIsdpCacheIndex=agentIsdpCacheIndex, agentIsdpCacheProtocolVersion=agentIsdpCacheProtocolVersion, agentIsdpCacheTable=agentIsdpCacheTable, agentIsdpCache=agentIsdpCache, agentIsdpGlobalMessageInterval=agentIsdpGlobalMessageInterval, agentIsdpGlobalHoldTime=agentIsdpGlobalHoldTime, fastPathIsdp=fastPathIsdp, agentIsdpGlobalDeviceId=agentIsdpGlobalDeviceId, PYSNMP_MODULE_ID=fastPathIsdp, agentIsdpInterfaceEnable=agentIsdpInterfaceEnable, agentIsdpCacheCapabilities=agentIsdpCacheCapabilities, agentIsdpInterfaceIfIndex=agentIsdpInterfaceIfIndex, agentIsdpClear=agentIsdpClear, agentIsdpCacheAddress=agentIsdpCacheAddress, agentIsdpCacheDeviceId=agentIsdpCacheDeviceId, agentIsdpStatisticsFailurePduTransmit=agentIsdpStatisticsFailurePduTransmit, agentIsdpStatistics=agentIsdpStatistics, agentIsdpStatisticsPduReceived=agentIsdpStatisticsPduReceived, agentIsdpStatisticsBadHeaderPduReceived=agentIsdpStatisticsBadHeaderPduReceived, agentIsdpGlobalDeviceIdFormat=agentIsdpGlobalDeviceIdFormat, agentIsdpInterfaceTable=agentIsdpInterfaceTable, agentIsdpStatisticsV1PduReceived=agentIsdpStatisticsV1PduReceived, agentIsdpStatisticsPduTransmit=agentIsdpStatisticsPduTransmit)
