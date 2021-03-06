#
# PySNMP MIB module ALVARION-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionPriorityQueue, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionPriorityQueue")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, IpAddress, MibIdentifier, Integer32, Unsigned32, Gauge32, NotificationType, ObjectIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "IpAddress", "MibIdentifier", "Integer32", "Unsigned32", "Gauge32", "NotificationType", "ObjectIdentity", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionQOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13))
if mibBuilder.loadTexts: alvarionQOS.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionQOS.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionQOS.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionQOS.setDescription('The MIB module for enterprise specific QoS options.')
alvarionQOSMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1))
coQOSStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1))
coQOSCountersTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1), )
if mibBuilder.loadTexts: coQOSCountersTable.setStatus('current')
if mibBuilder.loadTexts: coQOSCountersTable.setDescription('Group containing attributes that are MAC counters. In tabular form to allow multiple instance on an agent.')
coQOSCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ALVARION-QOS-MIB", "coQOSQueueId"))
if mibBuilder.loadTexts: coQOSCountersEntry.setStatus('current')
if mibBuilder.loadTexts: coQOSCountersEntry.setDescription('An entry in the coQOSCountersEntry Table. ifIndex - Each 802.11 interface is represented by an ifEntry. Interface tables in this MIB module are indexed by ifIndex.')
coQOSQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 1), AlvarionPriorityQueue())
if mibBuilder.loadTexts: coQOSQueueId.setStatus('current')
if mibBuilder.loadTexts: coQOSQueueId.setDescription('Queue identifier used to access the statistics.')
coQOSTransmittedFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSTransmittedFrameCount.setStatus('current')
if mibBuilder.loadTexts: coQOSTransmittedFrameCount.setDescription('This counter increments only when an acknowledged MPDU with an individual address in the address 1 field or MPDU with a multicast address in the address 1 field of type Data or Management.')
coQOSMulticastTransmittedFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSMulticastTransmittedFrameCount.setStatus('current')
if mibBuilder.loadTexts: coQOSMulticastTransmittedFrameCount.setDescription('This counter increments only when the multicast bit is set in the destination MAC address of a successfully transmitted MSDU. When operating as a STA in an ESS, where these frames are directed to the AP, this implies having received an acknowledgment to all associated MPDUs.')
coQOSFailedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSFailedCount.setStatus('current')
if mibBuilder.loadTexts: coQOSFailedCount.setDescription('This counter increments when an MSDU is not transmitted successfully due to the number of transmit attempts exceeding either the coQOSShortRetryLimit or coQOSLongRetryLimit.')
coQOSRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSRetryCount.setStatus('current')
if mibBuilder.loadTexts: coQOSRetryCount.setDescription('This counter increments when an MSDU is successfully transmitted after one or more retransmissions. This is basically a total of single and multiple retry counts.')
coQOSMultipleRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSMultipleRetryCount.setStatus('current')
if mibBuilder.loadTexts: coQOSMultipleRetryCount.setDescription('This counter increments when an MSDU is successfully transmitted after more than one retransmission.')
coQOSFrameDuplicateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSFrameDuplicateCount.setStatus('current')
if mibBuilder.loadTexts: coQOSFrameDuplicateCount.setDescription('This counter increments when a frame is received that the Sequence Control field indicates is a duplicate.')
coQOSReceivedFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSReceivedFrameCount.setStatus('current')
if mibBuilder.loadTexts: coQOSReceivedFrameCount.setDescription('This counter shall be incremented for each successfully received MPDU of type Data or Management. This is basically a total of unicast and multicast received frames.')
coQOSMulticastReceivedFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coQOSMulticastReceivedFrameCount.setStatus('current')
if mibBuilder.loadTexts: coQOSMulticastReceivedFrameCount.setDescription('This counter shall increment when a MPDU is received with the multicast bit set in the destination MAC address.')
coQOSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 2))
coQOSGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 2, 1))
coQOSCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 2, 2))
coQOSCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 2, 2, 1)).setObjects(("ALVARION-QOS-MIB", "coQOSCountersGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coQOSCompliance = coQOSCompliance.setStatus('current')
if mibBuilder.loadTexts: coQOSCompliance.setDescription('The compliance statement for SNMPv2 entities that implement the IEEE 802.11 MIB.')
coQOSCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 13, 1, 2, 1, 1)).setObjects(("ALVARION-QOS-MIB", "coQOSTransmittedFrameCount"), ("ALVARION-QOS-MIB", "coQOSMulticastTransmittedFrameCount"), ("ALVARION-QOS-MIB", "coQOSFailedCount"), ("ALVARION-QOS-MIB", "coQOSRetryCount"), ("ALVARION-QOS-MIB", "coQOSMultipleRetryCount"), ("ALVARION-QOS-MIB", "coQOSFrameDuplicateCount"), ("ALVARION-QOS-MIB", "coQOSReceivedFrameCount"), ("ALVARION-QOS-MIB", "coQOSMulticastReceivedFrameCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coQOSCountersGroup = coQOSCountersGroup.setStatus('current')
if mibBuilder.loadTexts: coQOSCountersGroup.setDescription('Provides the necessary support for QOS counters.')
mibBuilder.exportSymbols("ALVARION-QOS-MIB", coQOSFrameDuplicateCount=coQOSFrameDuplicateCount, coQOSMulticastTransmittedFrameCount=coQOSMulticastTransmittedFrameCount, coQOSMulticastReceivedFrameCount=coQOSMulticastReceivedFrameCount, coQOSRetryCount=coQOSRetryCount, coQOSCountersGroup=coQOSCountersGroup, coQOSCompliance=coQOSCompliance, coQOSTransmittedFrameCount=coQOSTransmittedFrameCount, coQOSQueueId=coQOSQueueId, coQOSCountersTable=coQOSCountersTable, coQOSReceivedFrameCount=coQOSReceivedFrameCount, PYSNMP_MODULE_ID=alvarionQOS, coQOSCompliances=coQOSCompliances, alvarionQOSMIBObjects=alvarionQOSMIBObjects, alvarionQOS=alvarionQOS, coQOSGroups=coQOSGroups, coQOSMultipleRetryCount=coQOSMultipleRetryCount, coQOSStatistics=coQOSStatistics, coQOSCountersEntry=coQOSCountersEntry, coQOSConformance=coQOSConformance, coQOSFailedCount=coQOSFailedCount)
