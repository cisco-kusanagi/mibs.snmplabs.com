#
# PySNMP MIB module CISCO-DOT11-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
CDot11IfVlanIdOrZero, = mibBuilder.importSymbols("CISCO-DOT11-IF-MIB", "CDot11IfVlanIdOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Counter32, ModuleIdentity, NotificationType, Unsigned32, IpAddress, MibIdentifier, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Counter32", "ModuleIdentity", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "TimeTicks", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoDot11QosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 416))
ciscoDot11QosMIB.setRevisions(('2006-05-09 00:00', '2003-11-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11QosMIB.setRevisionsDescriptions(('The DEFVAL clauses have been removed from the definition of the objects cdot11QosCWmin, cdot11QosCWmax, cdot11QosMaxRetry and cdot11QosBackoffOffset, as the default values for these objects depend on the different traffic classes and that there are no common default values across the different traffic classes. ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDot11QosMIB.setLastUpdated('200605090000Z')
if mibBuilder.loadTexts: ciscoDot11QosMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoDot11QosMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11QosMIB.setDescription('This MIB module provides network management support for QoS on wireless LAN devices. The objects defined in this MIB provide equivalent support as the objects in the IEEE 802.11E Standard draft. The original names of the objects in the standard are included in the REFERENCE clauses. GLOSSARY and ACRONYMS Access point (AP) Transmitter/receiver (transceiver) device that commonly connects and transports data between a wireless network and a wired network. AIFS Arbitration Interframe Space. It is one of the five different IFSs defined to provide priority levels for access to the wireless media. It shall be used by QSTAs to transmit data type frames (MPDUs) and management type frames (MMPDUs). BSS IEEE 802.11 Basic Service Set (Radio Cell). The BSS of an AP comprises of the stations directly associating with the AP. CW Contention Window. It is the time period between radio signal collisions caused by simultaneous broadcast from multiple wireless stations. The contention window is used to compute the random backoff of the radio broadcast. The IEEE 802.11b does not specify the unit for the time period. CWP Factor Contention Window Persistence Factor. It indicates the factor used in computing new CW values on every 15 unsuccessful attempt to transmit an MPDU or an MMPDU of a traffic class. It is a scaling factor in units of 1/16ths. IFS Inter-Frame Space is the time interval between frames. A STA shall determine that the medium is idle through the use of the carrier sense function for the interval specified. In other words, the size of the IFS determines the length of the backoff time interval of a device to the medium. In this case, the medium is the radio wave spectrum. The IEEE 802.11b standard does not specify any unit for the time interval. BSS IEEE 802.11 Basic Service Set (Radio Cell). The MAC Medium Access Control. Layer 2 in the network model. MPDU MAC protocol data unit. The unit of data exchanged between two peer MAC entities using the services of the physical layer (PHY). MMPDU Management type MAC protocol data unit. MSDU MAC service data unit. Information that is delivered as a unit between MAC service access points. QBSS Quality of service basic service set. QSTA QoS station. STA (WSTA) A non-AP IEEE 802.11 wireless station.')
ciscoDot11QosMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 0))
ciscoDot11QosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 1))
ciscoDot11QosMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 2))
ciscoDot11QosConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1))
ciscoDot11QosQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2))
ciscoDot11QosStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3))
ciscoDot11QosNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 4))
class Cdot11QosTrafficClass(TextualConvention, Integer32):
    reference = 'IEEE 802.1D-1998, Annex H.2.10 and IEEE 802.11E-2001, section 7.5.1.'
    description = 'This textual convention defines the 802.11E traffic classes: background(0) - background traffic, lowest priority bestEffort(1) - best effort delivery, default priority class for all traffic video(2) - video traffic, 2nd highest priority voice(3) - voice traffic, highest priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("background", 0), ("bestEffort", 1), ("video", 2), ("voice", 3))

cdot11QosConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1), )
if mibBuilder.loadTexts: cdot11QosConfigTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosConfigTable.setDescription('This table contains the basic set of attributes to configure QoS queues for radio interfaces of a wireless LAN device. This table has an expansion dependent relationship with the ifTable. Each IEEE 802.11 wireless interface has different outbound queues for different network traffic class. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"))
if mibBuilder.loadTexts: cdot11QosConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosConfigEntry.setDescription('Each entry contains parameters to configure traffic contention window, AIFS, priority and MSDU lifetime for each traffic queue on an IEEE 802.11 interface.')
cdot11TrafficQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdot11TrafficQueue.setStatus('current')
if mibBuilder.loadTexts: cdot11TrafficQueue.setDescription('This is the index to the outbound traffic queue on the radio interface.')
cdot11TrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 2), Cdot11QosTrafficClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11TrafficClass.setStatus('current')
if mibBuilder.loadTexts: cdot11TrafficClass.setDescription('This object specifies the traffic class and priority for the traffic on this queue.')
cdot11QosCWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11QosCWmin.setReference('dot11CWmin, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosCWmin.setStatus('current')
if mibBuilder.loadTexts: cdot11QosCWmin.setDescription('This object defines the minimum contention window value for a traffic class. The minimum contention window is 2 to the power of cdot11QosCWmin minus 1, and that is from 0 to 1023. The cdot11QosCWmin value must be less than or equal to cdot11QosCWmax.')
cdot11QosCWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11QosCWmax.setReference('dot11CWmax, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosCWmax.setStatus('current')
if mibBuilder.loadTexts: cdot11QosCWmax.setDescription('This object defines the maximum contention window value for a traffic class. The maximum contention window is 2 to the power of cdot11QosCWmax minus 1, and that is from 0 to 1023. The cdot11QosCWmax value must be greater than or equal to cdot11QosCWmin.')
cdot11QosBackoffOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11QosBackoffOffset.setStatus('current')
if mibBuilder.loadTexts: cdot11QosBackoffOffset.setDescription('This specifies the offset of the radio backoff from the transmission media for this traffic class. The backoff interval of a radio is calculated from a pseudo random integer drawn from a uniform distribution over the interval determined by the maximum and minimum of the contention window.')
cdot11QosMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11QosMaxRetry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosMaxRetry.setDescription('This specifies the number of times the radio retries for a particular transmission if there is a collision for the media.')
cdot11QosSupportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2), )
if mibBuilder.loadTexts: cdot11QosSupportTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosSupportTable.setDescription('This table contains the attributes indicating QoS support information on the IEEE 802.11 interfaces of this device. This table has a sparse dependent relationship with the ifTable. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosSupportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11QosSupportEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosSupportEntry.setDescription('Each entry contains attributes to indicate if QoS and priority queue are supported for an IEEE 802.11 interface.')
cdot11QosOptionImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosOptionImplemented.setReference('dot11QosOptionImplemented, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosOptionImplemented.setStatus('current')
if mibBuilder.loadTexts: cdot11QosOptionImplemented.setDescription('This object indicates if QoS is implemented on this IEEE 802.11 network interface.')
cdot11QosOptionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosOptionEnabled.setStatus('current')
if mibBuilder.loadTexts: cdot11QosOptionEnabled.setDescription("This object indicates if QoS is enabled on this IEEE 802.11 network interface. If it is 'true', QoS queuing is ON and traffic are prioritized according to their traffic class. If it is 'false', there is no QoS queuing and traffic are not prioritized.")
cdot11QosQueuesAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosQueuesAvailable.setReference('dot11QueuesAvailable, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosQueuesAvailable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueuesAvailable.setDescription('This object shows the number of QoS priority queues are available on this IEEE 802.11 network interface. That is the number of queue per interface in the cdot11QosConfigTable.')
cdot11QosQueueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1), )
if mibBuilder.loadTexts: cdot11QosQueueTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueueTable.setDescription('This table contains the queue weight and size information and statistics for each traffic queue on each the IEEE 802.11 interface. This table has a sparse dependent relationship with the ifTable. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"))
if mibBuilder.loadTexts: cdot11QosQueueEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueueEntry.setDescription('Each entry contains the current queue weight, size, and peak size information for each traffic queue on an IEEE 802.11 interface.')
cdot11QosQueueQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosQueueQuota.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueueQuota.setDescription('This is the current QoS priority queue packet quota for this queue on the overall bandwidth. The total available quota is platform dependent and is shared among all the transmitting queues. The queue with the largest quota value has the largest share of the overall bandwidth of the radio. The quota is allocated by the radio driver dynamically.')
cdot11QosQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosQueueSize.setReference('dot11QueueSizeTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosQueueSize.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueueSize.setDescription('This is the current QoS priority queue size for this queue.')
cdot11QosQueuePeakSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosQueuePeakSize.setReference('dot11QueuePeakSizeTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosQueuePeakSize.setStatus('current')
if mibBuilder.loadTexts: cdot11QosQueuePeakSize.setDescription('This is the peak QoS priority queue size for this queue.')
cdot11QosStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1), )
if mibBuilder.loadTexts: cdot11QosStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosStatisticsTable.setDescription('This table contains the QoS statistics by traffic queue on each the IEEE 802.11 network interface. This table has a expansion dependent relationship with the ifTable. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"))
if mibBuilder.loadTexts: cdot11QosStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosStatisticsEntry.setDescription('Each entry contain QoS statistics for data transmission and receive for each traffic queue on an IEEE 802.11 interface.')
cdot11QosDiscardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosDiscardedFrames.setReference('dot11QosDiscardedFrameCountTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosDiscardedFrames.setStatus('current')
if mibBuilder.loadTexts: cdot11QosDiscardedFrames.setDescription('This is the counter for QoS discarded frames transmitting from this IEEE 802.11 interface for the traffic queue.')
cdot11QosFails = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosFails.setReference('dot11QosFailedCountTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosFails.setStatus('current')
if mibBuilder.loadTexts: cdot11QosFails.setDescription('This is the counter for QoS failures on this IEEE 802.11 interface for the traffic queue.')
cdot11QosRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosRetries.setReference('dot11QosRetryCountTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosRetries.setStatus('current')
if mibBuilder.loadTexts: cdot11QosRetries.setDescription('This is the counter for QoS retries performed on this IEEE 802.11 interface for the traffic queue.')
cdot11QosMutipleRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosMutipleRetries.setReference('dot11QosMutipleRetryCountTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosMutipleRetries.setStatus('current')
if mibBuilder.loadTexts: cdot11QosMutipleRetries.setDescription('This is the counter for QoS multiple retries performed on this IEEE 802.11 interface for the traffic queue.')
cdot11QosTransmittedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosTransmittedFrames.setReference('dot11QosTransmittedFrameCountTC, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosTransmittedFrames.setStatus('current')
if mibBuilder.loadTexts: cdot11QosTransmittedFrames.setDescription('This is the counter for QoS frames transmitted from this IEEE 802.11 interface for the traffic queue.')
cdot11QosIfStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2), )
if mibBuilder.loadTexts: cdot11QosIfStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfStatisticsTable.setDescription('This table contains the attributes indicating QoS statistics on the IEEE 802.11 interfaces of the device. This table has a sparse dependent relationship with the ifTable. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosIfStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11QosIfStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfStatisticsEntry.setDescription('Each entry contains attributes to support QoS statistics on an IEEE 802.11 interface.')
cdot11QosIfDiscardedFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosIfDiscardedFragments.setReference('dot11QosDiscardedFragments, IEEE 802.11E-2001/D1.')
if mibBuilder.loadTexts: cdot11QosIfDiscardedFragments.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfDiscardedFragments.setDescription('This object counts the number of QoS discarded transmitting fragments on this radio interface.')
cdot11QosIfVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3), )
if mibBuilder.loadTexts: cdot11QosIfVlanTable.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfVlanTable.setDescription('This table maps VLANs to different traffic classes and defines their QoS properties. This table has an expansion dependent relationship with the ifTable. For each entry in this table, there exists an entry in the ifTable of ifType ieee80211(71).')
cdot11QosIfVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-QOS-MIB", "cdot11QosIfVlanId"))
if mibBuilder.loadTexts: cdot11QosIfVlanEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfVlanEntry.setDescription('Each entry defines parameters determining the traffic class and QoS configuration of a VLAN.')
cdot11QosIfVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1, 1), CDot11IfVlanIdOrZero().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: cdot11QosIfVlanId.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfVlanId.setDescription('This object identifies the VLAN (1 to 4095) on this radio interface.')
cdot11QosIfVlanTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1, 2), Cdot11QosTrafficClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11QosIfVlanTrafficClass.setStatus('current')
if mibBuilder.loadTexts: cdot11QosIfVlanTrafficClass.setDescription('This is the QoS traffic class for the traffic transmitting on this VLAN. The traffic class determines the priority for the VLAN.')
cdot11QosNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11QosNotifEnabled.setStatus('current')
if mibBuilder.loadTexts: cdot11QosNotifEnabled.setDescription('Indicates whether cdot11QosChangeNotif notification will or will not be sent by the agent when the QoS configuration in the cdot11QosConfigTable is changed.')
cdot11QosChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 416, 0, 1)).setObjects(("CISCO-DOT11-QOS-MIB", "cdot11TrafficClass"))
if mibBuilder.loadTexts: cdot11QosChangeNotif.setStatus('current')
if mibBuilder.loadTexts: cdot11QosChangeNotif.setDescription('This notification will be sent when the QoS configuration in the cdot11QosConfigTable is changed. The object cdot11TrafficClass specifies the traffic class of which a queue is configured. The sending of these notifications can be enabled or disabled via cdot11QosNotifEnabled.')
ciscoDot11QosMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 1))
ciscoDot11QosMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2))
ciscoDot11QosMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 1, 1)).setObjects(("CISCO-DOT11-QOS-MIB", "ciscoDot11QosConfigGroup"), ("CISCO-DOT11-QOS-MIB", "ciscoDot11QosStatsGroup"), ("CISCO-DOT11-QOS-MIB", "ciscoDot11QosNotifControlGroup"), ("CISCO-DOT11-QOS-MIB", "ciscoDot11QosNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11QosMIBCompliance = ciscoDot11QosMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11QosMIBCompliance.setDescription('The compliance statement for the configuration and status groups.')
ciscoDot11QosConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 1)).setObjects(("CISCO-DOT11-QOS-MIB", "cdot11TrafficClass"), ("CISCO-DOT11-QOS-MIB", "cdot11QosCWmin"), ("CISCO-DOT11-QOS-MIB", "cdot11QosCWmax"), ("CISCO-DOT11-QOS-MIB", "cdot11QosBackoffOffset"), ("CISCO-DOT11-QOS-MIB", "cdot11QosMaxRetry"), ("CISCO-DOT11-QOS-MIB", "cdot11QosOptionImplemented"), ("CISCO-DOT11-QOS-MIB", "cdot11QosOptionEnabled"), ("CISCO-DOT11-QOS-MIB", "cdot11QosQueuesAvailable"), ("CISCO-DOT11-QOS-MIB", "cdot11QosQueueQuota"), ("CISCO-DOT11-QOS-MIB", "cdot11QosQueueSize"), ("CISCO-DOT11-QOS-MIB", "cdot11QosQueuePeakSize"), ("CISCO-DOT11-QOS-MIB", "cdot11QosIfVlanTrafficClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11QosConfigGroup = ciscoDot11QosConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11QosConfigGroup.setDescription('Configurations for IEEE 802.11 QoS.')
ciscoDot11QosStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 2)).setObjects(("CISCO-DOT11-QOS-MIB", "cdot11QosIfDiscardedFragments"), ("CISCO-DOT11-QOS-MIB", "cdot11QosDiscardedFrames"), ("CISCO-DOT11-QOS-MIB", "cdot11QosFails"), ("CISCO-DOT11-QOS-MIB", "cdot11QosRetries"), ("CISCO-DOT11-QOS-MIB", "cdot11QosMutipleRetries"), ("CISCO-DOT11-QOS-MIB", "cdot11QosTransmittedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11QosStatsGroup = ciscoDot11QosStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11QosStatsGroup.setDescription('Status and statistics for IEEE 802.11 QoS.')
ciscoDot11QosNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 3)).setObjects(("CISCO-DOT11-QOS-MIB", "cdot11QosNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11QosNotifControlGroup = ciscoDot11QosNotifControlGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11QosNotifControlGroup.setDescription('Notification control configuration for QoS.')
ciscoDot11QosNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 4)).setObjects(("CISCO-DOT11-QOS-MIB", "cdot11QosChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11QosNotificationGroup = ciscoDot11QosNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11QosNotificationGroup.setDescription('Notifications for QoS configuration.')
mibBuilder.exportSymbols("CISCO-DOT11-QOS-MIB", PYSNMP_MODULE_ID=ciscoDot11QosMIB, cdot11QosQueueTable=cdot11QosQueueTable, cdot11QosCWmin=cdot11QosCWmin, ciscoDot11QosMIBObjects=ciscoDot11QosMIBObjects, cdot11QosIfVlanTable=cdot11QosIfVlanTable, cdot11QosIfVlanId=cdot11QosIfVlanId, cdot11QosStatisticsTable=cdot11QosStatisticsTable, ciscoDot11QosQueue=ciscoDot11QosQueue, ciscoDot11QosStatistics=ciscoDot11QosStatistics, cdot11QosRetries=cdot11QosRetries, cdot11QosQueuesAvailable=cdot11QosQueuesAvailable, cdot11QosFails=cdot11QosFails, cdot11QosOptionEnabled=cdot11QosOptionEnabled, cdot11QosStatisticsEntry=cdot11QosStatisticsEntry, cdot11TrafficQueue=cdot11TrafficQueue, ciscoDot11QosMIBCompliance=ciscoDot11QosMIBCompliance, ciscoDot11QosMIBCompliances=ciscoDot11QosMIBCompliances, cdot11QosIfStatisticsTable=cdot11QosIfStatisticsTable, cdot11QosIfDiscardedFragments=cdot11QosIfDiscardedFragments, cdot11QosMaxRetry=cdot11QosMaxRetry, cdot11QosMutipleRetries=cdot11QosMutipleRetries, ciscoDot11QosMIB=ciscoDot11QosMIB, cdot11QosQueueQuota=cdot11QosQueueQuota, ciscoDot11QosMIBConformance=ciscoDot11QosMIBConformance, cdot11QosConfigTable=cdot11QosConfigTable, cdot11QosCWmax=cdot11QosCWmax, cdot11QosConfigEntry=cdot11QosConfigEntry, cdot11QosQueueSize=cdot11QosQueueSize, cdot11QosIfVlanEntry=cdot11QosIfVlanEntry, cdot11TrafficClass=cdot11TrafficClass, ciscoDot11QosStatsGroup=ciscoDot11QosStatsGroup, ciscoDot11QosConfig=ciscoDot11QosConfig, ciscoDot11QosNotifControl=ciscoDot11QosNotifControl, cdot11QosSupportEntry=cdot11QosSupportEntry, cdot11QosSupportTable=cdot11QosSupportTable, ciscoDot11QosMIBGroups=ciscoDot11QosMIBGroups, cdot11QosBackoffOffset=cdot11QosBackoffOffset, ciscoDot11QosConfigGroup=ciscoDot11QosConfigGroup, cdot11QosTransmittedFrames=cdot11QosTransmittedFrames, cdot11QosQueueEntry=cdot11QosQueueEntry, ciscoDot11QosNotifControlGroup=ciscoDot11QosNotifControlGroup, ciscoDot11QosNotificationGroup=ciscoDot11QosNotificationGroup, ciscoDot11QosMIBNotifs=ciscoDot11QosMIBNotifs, cdot11QosIfStatisticsEntry=cdot11QosIfStatisticsEntry, cdot11QosNotifEnabled=cdot11QosNotifEnabled, cdot11QosChangeNotif=cdot11QosChangeNotif, cdot11QosOptionImplemented=cdot11QosOptionImplemented, cdot11QosIfVlanTrafficClass=cdot11QosIfVlanTrafficClass, Cdot11QosTrafficClass=Cdot11QosTrafficClass, cdot11QosQueuePeakSize=cdot11QosQueuePeakSize, cdot11QosDiscardedFrames=cdot11QosDiscardedFrames)
