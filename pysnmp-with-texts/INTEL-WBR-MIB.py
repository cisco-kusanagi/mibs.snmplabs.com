#
# PySNMP MIB module INTEL-WBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-WBR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, ModuleIdentity, IpAddress, Counter32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wbr = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 25))
wbrBase = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 25, 1))
wbrStp = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 25, 2))
wbrTp = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 25, 3))
wbrBaseLastConfigTime = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrBaseLastConfigTime.setStatus('mandatory')
if mibBuilder.loadTexts: wbrBaseLastConfigTime.setDescription('Time of last change in bridge configuration')
wbrBaseBridging = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrBaseBridging.setStatus('mandatory')
if mibBuilder.loadTexts: wbrBaseBridging.setDescription("Is Bridging (except of IP/IPX) enabled - 'Enabled' or 'Disabled'")
wbrBaseBridgingIP = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrBaseBridgingIP.setStatus('mandatory')
if mibBuilder.loadTexts: wbrBaseBridgingIP.setDescription("Is Bridging of IP traffic Enabled - 'Enabled' or 'Disabled'")
wbrBaseBridgingIPX = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrBaseBridgingIPX.setStatus('mandatory')
if mibBuilder.loadTexts: wbrBaseBridgingIPX.setDescription("Is Bridging of IPX traffic Enabled - 'Enabled' or 'Disabled'")
wbrStpBridgeAgeingTime = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpBridgeAgeingTime.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpBridgeAgeingTime.setDescription('The Ageing Time configured for this Bridge')
wbrStpBridgeIsRoot = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpBridgeIsRoot.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpBridgeIsRoot.setDescription("Is this Bridge the Root Bridge - 'Yes' or 'No'")
wbrStpRxBPDUs = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpRxBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpRxBPDUs.setDescription('Total number of BPDUs packets received')
wbrStpTxBPDUs = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpTxBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpTxBPDUs.setDescription('Total number of BPDUs packets transmitted')
wbrStpTxBPDUsFailed = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpTxBPDUsFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpTxBPDUsFailed.setDescription('Total number of BPDUs packets unsuccessfully transmitted')
wbrStpRxSpoofBPDUs = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpRxSpoofBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpRxSpoofBPDUs.setDescription('Total number of BPDUs packets spoofed instead of received')
wbrStpTxSpoofBPDUs = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpTxSpoofBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpTxSpoofBPDUs.setDescription('Total number of BPDUs packets spoofed instead of transmitted')
wbrStpTxSpoofFailed = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpTxSpoofFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpTxSpoofFailed.setDescription('Total number of spoofing protocol packets unsuccessfully transmitted')
wbrStpTxSpoofData = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpTxSpoofData.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpTxSpoofData.setDescription('Total number of packets spoofed instead of transmitted')
wbrStpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10), )
if mibBuilder.loadTexts: wbrStpLinkTable.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTable.setDescription('A table that contains port-specific information for the Spanning Tree Protocol.')
wbrStpLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1), ).setIndexNames((0, "INTEL-WBR-MIB", "wbrStpLinkIfIndex"))
if mibBuilder.loadTexts: wbrStpLinkEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkEntry.setDescription('')
wbrStpLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkIfIndex.setDescription('Link Index')
wbrStpLinkRxProtocolBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkRxProtocolBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkRxProtocolBytes.setDescription('BPDUs bytes received')
wbrStpLinkTxProtocolBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxProtocolBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxProtocolBytes.setDescription('BPDU bytes transmitted')
wbrStpLinkRxBPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkRxBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkRxBPDUs.setDescription('Number of BPDUs packets received')
wbrStpLinkTxBPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxBPDUs.setDescription('Number of BPDUs packets transmitted')
wbrStpLinkTxBPDUsFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxBPDUsFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxBPDUsFailed.setDescription('Number of BPDUs packets unsuccessfully transmitted from the link')
wbrStpLinkRxSpoofBPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkRxSpoofBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkRxSpoofBPDUs.setDescription('Number of BPDUs packets spoofed instead of received on link')
wbrStpLinkTxSpoofBPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxSpoofBPDUs.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxSpoofBPDUs.setDescription('Number of BPDUs packets spoofed instead of transmitted on link')
wbrStpLinkTxSpoofFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxSpoofFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxSpoofFailed.setDescription('Number of spoofing protocol packets unsuccessfully transmitted from the link')
wbrStpLinkTxSpoofData = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTxSpoofData.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTxSpoofData.setDescription('Number of packets spoofed instead of transmitted on link')
wbrStpLinkSPTStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkSPTStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkSPTStatus.setDescription('Status for Spanning Tree Link')
wbrStpLinkConfigBPDUPending = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUPending.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUPending.setDescription("Whether a Configuration BPDU packet is to be forwarded to the Bridges on the Designated ports (via Configuration BPDUs) - 'Yes' or 'No'")
wbrStpLinkTopologyChangeAck = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkTopologyChangeAck.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkTopologyChangeAck.setDescription("Determines if the configuration change is to be forwarded to the Bridges on the Designated Ports (via Configuration BPDUs) - 'Yes' or 'No'")
wbrStpLinkConfigBPDUAgeActive = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUAgeActive.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUAgeActive.setDescription("Whether ConfigBPDUAge is active/valid for monitoring. If not active then ConfigBPDUAge is undefined i.e. 'Not Active'")
wbrStpLinkConfigBPDUAge = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUAge.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkConfigBPDUAge.setDescription('The age of the information within the last Configuration BPDU packet received from the Designated Bridge')
wbrStpLinkBPDUSpoofing = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkBPDUSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkBPDUSpoofing.setDescription("Whether Configuration BPDU packets are spoofed - 'Yes' or 'Not Active'")
wbrStpLinkNonBPDUSpoofing = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkNonBPDUSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkNonBPDUSpoofing.setDescription("Whether Non-BPDU packets are spoofed - 'Yes' or 'Not Active'")
wbrStpLinkSpoofing = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrStpLinkSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: wbrStpLinkSpoofing.setDescription('If Spoofing is enabled in Setup')
wbrTpRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRxPackets.setDescription('Total number of bridged packets (non BPDU packets) received')
wbrTpTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpTxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpTxPackets.setDescription('Total number of bridged packets (non BPDU packets) transmitted')
wbrTpTxFailed = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpTxFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpTxFailed.setDescription('Total number of packets that the router failed to transmit')
wbrTpRxRejUnknown = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRxRejUnknown.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRxRejUnknown.setDescription('Total number of unknown Unicast packets received which were discarded due to exceeding the maximum number of unknown Unicast packets (5 within 5 seconds for the entire Bridge)')
wbrTpRxRejTotal = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRxRejTotal.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRxRejTotal.setDescription('Total number of valid frames received which were rejected (i.e., filtered) by the Forwarding Process')
wbrTpRxInvalid = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRxInvalid.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRxInvalid.setDescription('Total number of erroneous packets received')
wbrTpRejUnicast = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejUnicast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejUnicast.setDescription('Total number of packets received which were rejected by the Unicast Destination Forwarding Table')
wbrTpRejDefaultUnicast = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejDefaultUnicast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejDefaultUnicast.setDescription('Total number of packets received which were rejected by the Default Action of the Unicast Destination Forwarding Table')
wbrTpRejMulticast = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejMulticast.setDescription('Total number of packets received which were rejected by the Multicast Destination Forwarding Table')
wbrTpRejDefaultMulticast = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejDefaultMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejDefaultMulticast.setDescription('Total number of packets received which were rejected by the Default Action of the Multicast Destination Forwarding Table')
wbrTpRejSource = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejSource.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejSource.setDescription('Total number of packets received which were rejected by the Source Forwarding Table')
wbrTpRejDefaultSource = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejDefaultSource.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejDefaultSource.setDescription('Total number of packets received which were rejected by the Default Action of the Source Forwarding Table')
wbrTpRejType = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejType.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejType.setDescription('Total number of packets received which were rejected by the Type Forwarding Table')
wbrTpRejDefaultType = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpRejDefaultType.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpRejDefaultType.setDescription('Total number of packets received which were rejected by the Default Action of the Type Forwarding Table')
wbrTpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15), )
if mibBuilder.loadTexts: wbrTpLinkTable.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkTable.setDescription('A table that contains information about every port that is associated with this transparent bridge.')
wbrTpLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1), ).setIndexNames((0, "INTEL-WBR-MIB", "wbrTpLinkIfIndex"))
if mibBuilder.loadTexts: wbrTpLinkEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkEntry.setDescription('')
wbrTpLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkIfIndex.setDescription('Link Index')
wbrTpLinkRxOtherBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxOtherBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxOtherBytes.setDescription('Non-BPDU bytes received')
wbrTpLinkTxOtherBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkTxOtherBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkTxOtherBytes.setDescription('Non-BPDU bytes transmitted')
wbrTpLinkRxRejectedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejectedBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejectedBytes.setDescription('Number of non-BPDU bytes received on this link which were rejected')
wbrTpLinkTxRejectedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkTxRejectedBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkTxRejectedBytes.setDescription('Number of non-BPDU bytes to be transmitted on this link which were rejected')
wbrTpLinkRxRejUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejUnknown.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejUnknown.setDescription('Number of unknown Unicast packets received on the link which were discarded due to exceeding the maximum number of unknown Unicast packets (5 within 5 seconds for the entire Bridge)')
wbrTpLinkRxInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxInvalid.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxInvalid.setDescription('Number of erroneous packets received')
wbrTpLinkTxFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkTxFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkTxFailed.setDescription('Number of non-BPDU packets unsuccessfully transmitted from the link')
wbrTpLinkRxRejUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejUnicast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejUnicast.setDescription('Number of packets received on this link which were rejected by the Unicast Destination Forwarding Table')
wbrTpLinkRxRejMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejMulticast.setDescription('Number of packets received on this link which were rejected by the Multicast Destination Forwarding Table')
wbrTpLinkRxRejSource = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejSource.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejSource.setDescription('Number of packets received on this link which were rejected by the Source Forwarding Table')
wbrTpLinkRxRejType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejType.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejType.setDescription('Number of packets received on this link which were rejected by the Type Forwarding Table')
wbrTpLinkRxRejDefaultUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultUnicast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultUnicast.setDescription('Number of packets received on this link which were rejected by the Default Action of the Unicast Destination Forwarding Table')
wbrTpLinkRxRejDefaultMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultMulticast.setDescription('Number of packets received on this link which were rejected by the Default Action of the Multicast Destination Forwarding Table')
wbrTpLinkRxRejDefaultSource = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultSource.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultSource.setDescription('Number of packets received on this link which were rejected by the Default Action of the Source Forwarding Table')
wbrTpLinkRxRejDefaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultType.setStatus('mandatory')
if mibBuilder.loadTexts: wbrTpLinkRxRejDefaultType.setDescription('Number of packets received on this link which were rejected by the Default Action of the Type Forwarding Table')
mibBuilder.exportSymbols("INTEL-WBR-MIB", wbrStpLinkTxSpoofFailed=wbrStpLinkTxSpoofFailed, wbrStpTxBPDUs=wbrStpTxBPDUs, wbrStpLinkTxSpoofData=wbrStpLinkTxSpoofData, wbrTpLinkIfIndex=wbrTpLinkIfIndex, wbrTpRejDefaultUnicast=wbrTpRejDefaultUnicast, wbrTpLinkRxRejectedBytes=wbrTpLinkRxRejectedBytes, wbrTpRejDefaultMulticast=wbrTpRejDefaultMulticast, wbrStpTxSpoofFailed=wbrStpTxSpoofFailed, wbrStpLinkEntry=wbrStpLinkEntry, wbrTpRejUnicast=wbrTpRejUnicast, wbrTpLinkRxRejDefaultMulticast=wbrTpLinkRxRejDefaultMulticast, wbrTpRejDefaultType=wbrTpRejDefaultType, wbrTpRxRejUnknown=wbrTpRxRejUnknown, wbrTpTxFailed=wbrTpTxFailed, wbrStpLinkNonBPDUSpoofing=wbrStpLinkNonBPDUSpoofing, wbrTpLinkRxInvalid=wbrTpLinkRxInvalid, wbrStpLinkTxProtocolBytes=wbrStpLinkTxProtocolBytes, wbrBaseBridgingIP=wbrBaseBridgingIP, wbr=wbr, wbrStpBridgeIsRoot=wbrStpBridgeIsRoot, wbrTpLinkRxRejSource=wbrTpLinkRxRejSource, wbrTpLinkTxFailed=wbrTpLinkTxFailed, wbrStpLinkBPDUSpoofing=wbrStpLinkBPDUSpoofing, wbrStp=wbrStp, wbrStpLinkConfigBPDUAgeActive=wbrStpLinkConfigBPDUAgeActive, wbrTpLinkRxRejDefaultType=wbrTpLinkRxRejDefaultType, wbrStpLinkSpoofing=wbrStpLinkSpoofing, wbrTpRejType=wbrTpRejType, wbrTpLinkEntry=wbrTpLinkEntry, wbrTpLinkRxRejDefaultSource=wbrTpLinkRxRejDefaultSource, wbrTpLinkRxRejUnicast=wbrTpLinkRxRejUnicast, wbrTpRejMulticast=wbrTpRejMulticast, wbrStpLinkConfigBPDUAge=wbrStpLinkConfigBPDUAge, wbrTpLinkRxRejType=wbrTpLinkRxRejType, wbrStpLinkSPTStatus=wbrStpLinkSPTStatus, wbrTpLinkTxRejectedBytes=wbrTpLinkTxRejectedBytes, wbrTpRxInvalid=wbrTpRxInvalid, wbrBase=wbrBase, wbrTpLinkRxRejDefaultUnicast=wbrTpLinkRxRejDefaultUnicast, wbrBaseBridging=wbrBaseBridging, wbrStpLinkTopologyChangeAck=wbrStpLinkTopologyChangeAck, wbrBaseLastConfigTime=wbrBaseLastConfigTime, wbrTpRxPackets=wbrTpRxPackets, wbrStpLinkRxSpoofBPDUs=wbrStpLinkRxSpoofBPDUs, wbrStpLinkTable=wbrStpLinkTable, wbrStpTxSpoofBPDUs=wbrStpTxSpoofBPDUs, wbrTpLinkRxRejMulticast=wbrTpLinkRxRejMulticast, wbrTpRxRejTotal=wbrTpRxRejTotal, wbrTpLinkRxOtherBytes=wbrTpLinkRxOtherBytes, wbrStpLinkIfIndex=wbrStpLinkIfIndex, wbrStpRxBPDUs=wbrStpRxBPDUs, wbrTpRejDefaultSource=wbrTpRejDefaultSource, wbrTp=wbrTp, wbrStpLinkTxSpoofBPDUs=wbrStpLinkTxSpoofBPDUs, wbrStpLinkConfigBPDUPending=wbrStpLinkConfigBPDUPending, wbrTpLinkTable=wbrTpLinkTable, wbrTpLinkRxRejUnknown=wbrTpLinkRxRejUnknown, wbrTpLinkTxOtherBytes=wbrTpLinkTxOtherBytes, wbrStpTxBPDUsFailed=wbrStpTxBPDUsFailed, wbrStpLinkRxProtocolBytes=wbrStpLinkRxProtocolBytes, wbrStpLinkRxBPDUs=wbrStpLinkRxBPDUs, wbrStpLinkTxBPDUs=wbrStpLinkTxBPDUs, wbrStpRxSpoofBPDUs=wbrStpRxSpoofBPDUs, wbrTpTxPackets=wbrTpTxPackets, wbrStpLinkTxBPDUsFailed=wbrStpLinkTxBPDUsFailed, wbrBaseBridgingIPX=wbrBaseBridgingIPX, wbrTpRejSource=wbrTpRejSource, wbrStpTxSpoofData=wbrStpTxSpoofData, wbrStpBridgeAgeingTime=wbrStpBridgeAgeingTime)
