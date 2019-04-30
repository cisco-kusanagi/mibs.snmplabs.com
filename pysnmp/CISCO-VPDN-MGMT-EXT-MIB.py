#
# PySNMP MIB module CISCO-VPDN-MGMT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VPDN-MGMT-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
cvpdnTunnelAttrEntry, cvpdnSessionAttrEntry = mibBuilder.importSymbols("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrEntry", "cvpdnSessionAttrEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Bits, Unsigned32, ObjectIdentity, IpAddress, NotificationType, TimeTicks, Integer32, Counter32, Counter64, MibIdentifier, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "ObjectIdentity", "IpAddress", "NotificationType", "TimeTicks", "Integer32", "Counter32", "Counter64", "MibIdentifier", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoVpdnMgmtExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 51))
ciscoVpdnMgmtExtMIB.setRevisions(('2011-12-01 00:00', '2007-06-04 00:00', '1999-04-14 00:00',))
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setLastUpdated('201112010000Z')
if mibBuilder.loadTexts: ciscoVpdnMgmtExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoVpdnMgmtExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1))
cvpdnTunnelExtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1))
cvpdnSessionExtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2))
cvpdnTunnelExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1), )
if mibBuilder.loadTexts: cvpdnTunnelExtTable.setStatus('current')
cvpdnTunnelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1), )
cvpdnTunnelAttrEntry.registerAugmentions(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtEntry"))
cvpdnTunnelExtEntry.setIndexNames(*cvpdnTunnelAttrEntry.getIndexNames())
if mibBuilder.loadTexts: cvpdnTunnelExtEntry.setStatus('current')
cvpdnTunnelLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelLocalPort.setStatus('current')
cvpdnTunnelRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelRemotePort.setStatus('current')
cvpdnTunnelLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelLastChange.setStatus('current')
cvpdnTunnelPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelPacketsOut.setStatus('current')
cvpdnTunnelBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesOut.setStatus('deprecated')
cvpdnTunnelPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelPacketsIn.setStatus('current')
cvpdnTunnelBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 7), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesIn.setStatus('deprecated')
cvpdnTunnelBytesIn64 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesIn64.setStatus('current')
cvpdnTunnelBytesOut64 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnTunnelBytesOut64.setStatus('current')
cvpdnSessionExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1), )
if mibBuilder.loadTexts: cvpdnSessionExtTable.setStatus('current')
cvpdnSessionExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1), )
cvpdnSessionAttrEntry.registerAugmentions(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtEntry"))
cvpdnSessionExtEntry.setIndexNames(*cvpdnSessionAttrEntry.getIndexNames())
if mibBuilder.loadTexts: cvpdnSessionExtEntry.setStatus('current')
cvpdnSessionRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteId.setStatus('current')
cvpdnSessionInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionInterfaceName.setStatus('current')
cvpdnSessionLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionLastChange.setStatus('current')
cvpdnSessionOutOfOrderPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionOutOfOrderPackets.setStatus('current')
cvpdnSessionSequencing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSequencing.setStatus('current')
cvpdnSessionSendSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSendSequence.setStatus('current')
cvpdnSessionRecvSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvSequence.setStatus('current')
cvpdnSessionRemoteSendSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteSendSequence.setStatus('current')
cvpdnSessionRemoteRecvSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteRecvSequence.setStatus('current')
cvpdnSessionSentZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSentZLB.setStatus('current')
cvpdnSessionRecvZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvZLB.setStatus('current')
cvpdnSessionSentRBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionSentRBits.setStatus('current')
cvpdnSessionRecvRBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRecvRBits.setStatus('current')
cvpdnSessionLocalWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionLocalWindowSize.setStatus('current')
cvpdnSessionRemoteWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRemoteWindowSize.setStatus('current')
cvpdnSessionCurrentWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionCurrentWindowSize.setStatus('current')
cvpdnSessionMinimumWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionMinimumWindowSize.setStatus('current')
cvpdnSessionATOTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionATOTimeouts.setStatus('current')
cvpdnSessionOutGoingQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionOutGoingQueueSize.setStatus('current')
cvpdnSessionCalculationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("adaptive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionCalculationType.setStatus('current')
cvpdnSessionAdaptiveTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionAdaptiveTimeOut.setStatus('current')
cvpdnSessionRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionRoundTripTime.setStatus('current')
cvpdnSessionPktProcessingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionPktProcessingDelay.setStatus('current')
cvpdnSessionZLBTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('msecs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvpdnSessionZLBTime.setStatus('current')
ciscoVpdnMgtExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 2))
ciscoVpdnMgmtExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3))
ciscoVpdnMgmtExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1))
ciscoVpdnMgmtExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2))
ciscoVpdnMgmtExtMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 1)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtGroup"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpdnMgmtExtMIBBasicCompliance = ciscoVpdnMgmtExtMIBBasicCompliance.setStatus('deprecated')
ciscoVpdnMgmtExtMIBBasicComplianceV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 2)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionExtGroup"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelExtGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpdnMgmtExtMIBBasicComplianceV2 = ciscoVpdnMgmtExtMIBBasicComplianceV2.setStatus('current')
cvpdnTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 1)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnTunnelExtGroup = cvpdnTunnelExtGroup.setStatus('deprecated')
cvpdnSessionExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 2)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteId"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionInterfaceName"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSequencing"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSendSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteSendSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteRecvSequence"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutOfOrderPackets"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentZLB"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvZLB"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentRBits"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvRBits"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLocalWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCurrentWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionMinimumWindowSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionATOTimeouts"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutGoingQueueSize"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCalculationType"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionAdaptiveTimeOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRoundTripTime"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionPktProcessingDelay"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionZLBTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnSessionExtGroup = cvpdnSessionExtGroup.setStatus('current')
cvpdnTunnelExtGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 3)).setObjects(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn64"), ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut64"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvpdnTunnelExtGroupV2 = cvpdnTunnelExtGroupV2.setStatus('current')
mibBuilder.exportSymbols("CISCO-VPDN-MGMT-EXT-MIB", cvpdnTunnelExtInfo=cvpdnTunnelExtInfo, cvpdnTunnelExtGroup=cvpdnTunnelExtGroup, cvpdnSessionLocalWindowSize=cvpdnSessionLocalWindowSize, cvpdnSessionMinimumWindowSize=cvpdnSessionMinimumWindowSize, ciscoVpdnMgmtExtMIBBasicCompliance=ciscoVpdnMgmtExtMIBBasicCompliance, ciscoVpdnMgtExtMIBNotificationPrefix=ciscoVpdnMgtExtMIBNotificationPrefix, cvpdnSessionOutGoingQueueSize=cvpdnSessionOutGoingQueueSize, cvpdnSessionZLBTime=cvpdnSessionZLBTime, cvpdnSessionSentRBits=cvpdnSessionSentRBits, cvpdnSessionCurrentWindowSize=cvpdnSessionCurrentWindowSize, cvpdnSessionLastChange=cvpdnSessionLastChange, cvpdnTunnelLocalPort=cvpdnTunnelLocalPort, cvpdnSessionSequencing=cvpdnSessionSequencing, cvpdnSessionOutOfOrderPackets=cvpdnSessionOutOfOrderPackets, ciscoVpdnMgmtExtMIB=ciscoVpdnMgmtExtMIB, cvpdnSessionSendSequence=cvpdnSessionSendSequence, cvpdnSessionRemoteId=cvpdnSessionRemoteId, cvpdnSessionATOTimeouts=cvpdnSessionATOTimeouts, cvpdnTunnelExtGroupV2=cvpdnTunnelExtGroupV2, cvpdnSessionExtEntry=cvpdnSessionExtEntry, cvpdnTunnelBytesOut=cvpdnTunnelBytesOut, cvpdnTunnelPacketsIn=cvpdnTunnelPacketsIn, cvpdnSessionRecvSequence=cvpdnSessionRecvSequence, cvpdnSessionSentZLB=cvpdnSessionSentZLB, ciscoVpdnMgmtExtMIBCompliances=ciscoVpdnMgmtExtMIBCompliances, cvpdnTunnelBytesIn=cvpdnTunnelBytesIn, cvpdnSessionRemoteRecvSequence=cvpdnSessionRemoteRecvSequence, cvpdnSessionExtInfo=cvpdnSessionExtInfo, cvpdnTunnelPacketsOut=cvpdnTunnelPacketsOut, cvpdnSessionExtTable=cvpdnSessionExtTable, cvpdnSessionInterfaceName=cvpdnSessionInterfaceName, ciscoVpdnMgmtExtMIBBasicComplianceV2=ciscoVpdnMgmtExtMIBBasicComplianceV2, cvpdnSessionRecvRBits=cvpdnSessionRecvRBits, cvpdnSessionRemoteWindowSize=cvpdnSessionRemoteWindowSize, cvpdnSessionCalculationType=cvpdnSessionCalculationType, ciscoVpdnMgmtExtMIBGroups=ciscoVpdnMgmtExtMIBGroups, cvpdnSessionRemoteSendSequence=cvpdnSessionRemoteSendSequence, cvpdnSessionAdaptiveTimeOut=cvpdnSessionAdaptiveTimeOut, cvpdnTunnelBytesIn64=cvpdnTunnelBytesIn64, ciscoVpdnMgmtExtMIBConformance=ciscoVpdnMgmtExtMIBConformance, cvpdnTunnelExtTable=cvpdnTunnelExtTable, cvpdnTunnelBytesOut64=cvpdnTunnelBytesOut64, cvpdnSessionRoundTripTime=cvpdnSessionRoundTripTime, cvpdnTunnelRemotePort=cvpdnTunnelRemotePort, cvpdnSessionRecvZLB=cvpdnSessionRecvZLB, cvpdnSessionExtGroup=cvpdnSessionExtGroup, cvpdnTunnelLastChange=cvpdnTunnelLastChange, PYSNMP_MODULE_ID=ciscoVpdnMgmtExtMIB, ciscoVpdnMgmtExtMIBObjects=ciscoVpdnMgmtExtMIBObjects, cvpdnSessionPktProcessingDelay=cvpdnSessionPktProcessingDelay, cvpdnTunnelExtEntry=cvpdnTunnelExtEntry)