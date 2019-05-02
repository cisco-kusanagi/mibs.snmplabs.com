#
# PySNMP MIB module PACKETLOGIC-CHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETLOGIC-CHANNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, MibIdentifier, Unsigned32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, NotificationType, Integer32, ObjectIdentity, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "NotificationType", "Integer32", "ObjectIdentity", "IpAddress", "Bits")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
channelstats = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 2))
channelstats.setRevisions(('2012-09-26 12:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: channelstats.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: channelstats.setLastUpdated('201209261248Z')
if mibBuilder.loadTexts: channelstats.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: channelstats.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: channelstats.setDescription('MIB for PacketLogic2 channels')
channelCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8))
channelInfoTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17), )
if mibBuilder.loadTexts: channelInfoTable.setStatus('current')
if mibBuilder.loadTexts: channelInfoTable.setDescription('Conceptual Table')
channelInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "channelInfoEntryIndex"))
if mibBuilder.loadTexts: channelInfoEntry.setStatus('current')
if mibBuilder.loadTexts: channelInfoEntry.setDescription('Conceptual Table')
channelInfoEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: channelInfoEntryIndex.setStatus('current')
if mibBuilder.loadTexts: channelInfoEntryIndex.setDescription('Unique Row Index for Conceptual Table')
netDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25), )
if mibBuilder.loadTexts: netDeviceTable.setStatus('current')
if mibBuilder.loadTexts: netDeviceTable.setDescription('Conceptual Table')
netDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "netDeviceEntryIndex"))
if mibBuilder.loadTexts: netDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: netDeviceEntry.setDescription('Conceptual Table')
netDeviceEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: netDeviceEntryIndex.setStatus('current')
if mibBuilder.loadTexts: netDeviceEntryIndex.setDescription('Unique Row Index for Conceptual Table')
channelRxPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1))
channelTxPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2))
channelRxBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3))
channelTxBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4))
channelRxErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5))
channelTxErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6))
channelRxDrops = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7))
channelTxDrops = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8))
channelCollisions = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9))
channelMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10))
channelRxLengthErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11))
channelRxCrcErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12))
channelRxFrameErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13))
channelRxFifoErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14))
channelRxMissedErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15))
channelTxAborted = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16))
channelTxWindowErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17))
channelTxCarrierErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18))
channelNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumber.setStatus('current')
if mibBuilder.loadTexts: channelNumber.setDescription('Number of available channels in system')
channelInternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMedia.setStatus('current')
if mibBuilder.loadTexts: channelInternalMedia.setDescription('internal_media')
channelExternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMedia.setStatus('current')
if mibBuilder.loadTexts: channelExternalMedia.setDescription('external_media')
channelInternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMedia.setStatus('current')
if mibBuilder.loadTexts: channelInternalNegotiatedMedia.setDescription('internal_negotiated_media')
channelExternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalNegotiatedMedia.setStatus('current')
if mibBuilder.loadTexts: channelExternalNegotiatedMedia.setDescription('external_negotiated_media')
channelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelActive.setStatus('current')
if mibBuilder.loadTexts: channelActive.setDescription('active')
channelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelName.setStatus('current')
if mibBuilder.loadTexts: channelName.setDescription('active')
channelInternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMediaTime.setStatus('current')
if mibBuilder.loadTexts: channelInternalNegotiatedMediaTime.setDescription('internal_negotiated_media_time')
channelexternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelexternalNegotiatedMediaTime.setStatus('current')
if mibBuilder.loadTexts: channelexternalNegotiatedMediaTime.setDescription('external_negotiated_media_time')
channelInternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxPackets.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxPackets.setDescription('RX packets')
channelExternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxPackets.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxPackets.setDescription('RX packets')
channelInternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxPackets.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxPackets.setDescription('TX packets')
channelExternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxPackets.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxPackets.setDescription('TX packets')
channelInternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxBytes.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxBytes.setDescription('RX speed')
channelExternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxBytes.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxBytes.setDescription('RX speed')
channelInternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxBytes.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxBytes.setDescription('TX speed')
channelExternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxBytes.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxBytes.setDescription('TX speed')
channelInternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxErrors.setDescription('RX errors')
channelExternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxErrors.setDescription('RX errors')
channelInternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxErrors.setDescription('TX errors')
channelExternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxErrors.setDescription('TX errors')
channelInternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxDrops.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxDrops.setDescription('RX drops')
channelExternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxDrops.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxDrops.setDescription('RX drops')
channelInternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxDrops.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxDrops.setDescription('TX drops')
channelExternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxDrops.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxDrops.setDescription('TX drops')
channelInternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalCollisions.setStatus('current')
if mibBuilder.loadTexts: channelInternalCollisions.setDescription('Collisions')
channelExternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalCollisions.setStatus('current')
if mibBuilder.loadTexts: channelExternalCollisions.setDescription('Collisions')
channelInternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMulticast.setStatus('current')
if mibBuilder.loadTexts: channelInternalMulticast.setDescription('Multicast packets')
channelExternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMulticast.setStatus('current')
if mibBuilder.loadTexts: channelExternalMulticast.setDescription('Multicast packets')
channelInternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxLengthErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxLengthErrors.setDescription('RX length errors')
channelExternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxLengthErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxLengthErrors.setDescription('RX length errors')
channelInternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxCrcErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxCrcErrors.setDescription('RX CRC errors')
channelExternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxCrcErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxCrcErrors.setDescription('RX CRC errors')
channelInternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxFrameErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxFrameErrors.setDescription('RX frame errors')
channelExternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFrameErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxFrameErrors.setDescription('RX frame errors')
channelINternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelINternalRxFifoErrors.setStatus('current')
if mibBuilder.loadTexts: channelINternalRxFifoErrors.setDescription('RX fifo errors')
channelExternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFifoErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxFifoErrors.setDescription('RX fifo errors')
channelInternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxMissedErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalRxMissedErrors.setDescription('RX missed errors')
channelExternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxMissedErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalRxMissedErrors.setDescription('RX missed errors')
channelInternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxAborted.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxAborted.setDescription('TX aborted')
channelExternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxAborted.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxAborted.setDescription('TX aborted')
channelInternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxWindowErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxWindowErrors.setDescription('TX window errors')
channelExternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxWindowErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxWindowErrors.setDescription('TX window errors')
channelInternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxCarrierErrors.setStatus('current')
if mibBuilder.loadTexts: channelInternalTxCarrierErrors.setDescription('TX carrier errors')
channelExternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxCarrierErrors.setStatus('current')
if mibBuilder.loadTexts: channelExternalTxCarrierErrors.setDescription('TX carrier errors')
mibBuilder.exportSymbols("PACKETLOGIC-CHANNEL-MIB", netDeviceTable=netDeviceTable, channelInternalRxDrops=channelInternalRxDrops, channelActive=channelActive, channelInternalNegotiatedMedia=channelInternalNegotiatedMedia, channelInfoTable=channelInfoTable, channelExternalTxAborted=channelExternalTxAborted, netDeviceEntry=netDeviceEntry, channelExternalTxCarrierErrors=channelExternalTxCarrierErrors, channelInternalCollisions=channelInternalCollisions, channelInternalRxLengthErrors=channelInternalRxLengthErrors, channelInternalTxCarrierErrors=channelInternalTxCarrierErrors, channelExternalMedia=channelExternalMedia, channelExternalTxBytes=channelExternalTxBytes, channelCollisions=channelCollisions, channelInternalNegotiatedMediaTime=channelInternalNegotiatedMediaTime, channelExternalRxBytes=channelExternalRxBytes, channelExternalRxErrors=channelExternalRxErrors, channelExternalRxCrcErrors=channelExternalRxCrcErrors, channelTxDrops=channelTxDrops, channelInternalRxBytes=channelInternalRxBytes, channelExternalTxErrors=channelExternalTxErrors, channelExternalRxMissedErrors=channelExternalRxMissedErrors, PYSNMP_MODULE_ID=channelstats, channelInternalTxAborted=channelInternalTxAborted, channelexternalNegotiatedMediaTime=channelexternalNegotiatedMediaTime, channelExternalTxPackets=channelExternalTxPackets, channelInternalMedia=channelInternalMedia, channelName=channelName, channelInternalMulticast=channelInternalMulticast, channelRxCrcErrors=channelRxCrcErrors, channelRxFifoErrors=channelRxFifoErrors, channelRxDrops=channelRxDrops, channelRxPackets=channelRxPackets, channelExternalRxDrops=channelExternalRxDrops, channelExternalRxFrameErrors=channelExternalRxFrameErrors, channelInternalTxDrops=channelInternalTxDrops, channelExternalRxFifoErrors=channelExternalRxFifoErrors, channelExternalNegotiatedMedia=channelExternalNegotiatedMedia, channelTxCarrierErrors=channelTxCarrierErrors, channelInternalRxErrors=channelInternalRxErrors, channelInfoEntryIndex=channelInfoEntryIndex, channelTxPackets=channelTxPackets, channelRxBytes=channelRxBytes, channelRxErrors=channelRxErrors, channelTxWindowErrors=channelTxWindowErrors, channelExternalTxWindowErrors=channelExternalTxWindowErrors, channelCfg=channelCfg, channelInternalRxFrameErrors=channelInternalRxFrameErrors, channelRxFrameErrors=channelRxFrameErrors, channelExternalRxLengthErrors=channelExternalRxLengthErrors, channelExternalRxPackets=channelExternalRxPackets, channelExternalMulticast=channelExternalMulticast, channelRxMissedErrors=channelRxMissedErrors, channelExternalTxDrops=channelExternalTxDrops, channelstats=channelstats, channelInternalRxPackets=channelInternalRxPackets, channelTxBytes=channelTxBytes, channelInternalTxWindowErrors=channelInternalTxWindowErrors, netDeviceEntryIndex=netDeviceEntryIndex, channelMulticast=channelMulticast, channelInfoEntry=channelInfoEntry, channelRxLengthErrors=channelRxLengthErrors, channelNumber=channelNumber, channelInternalTxBytes=channelInternalTxBytes, channelInternalTxErrors=channelInternalTxErrors, channelExternalCollisions=channelExternalCollisions, channelInternalRxCrcErrors=channelInternalRxCrcErrors, channelInternalRxMissedErrors=channelInternalRxMissedErrors, channelINternalRxFifoErrors=channelINternalRxFifoErrors, channelInternalTxPackets=channelInternalTxPackets, channelTxErrors=channelTxErrors, channelTxAborted=channelTxAborted)
