#
# PySNMP MIB module CISCO-METRO-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-METRO-PHY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, Gauge32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter64, NotificationType, Bits, ObjectIdentity, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "Counter32", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoMetroPhyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 69))
ciscoMetroPhyMIB.setRevisions(('2005-09-02 00:00', '2004-11-19 00:00', '2003-08-25 00:00', '2003-01-08 00:00', '2002-05-14 00:00', '2001-08-31 00:00', '2001-04-19 00:00',))
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setLastUpdated('200509020000Z')
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setOrganization('Cisco Systems, Inc.')
class TransmissionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("copper", 2), ("optical", 3))

class ProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("gigabitEthernet", 3), ("tenGigabitEthernet", 4), ("fibreChannel", 5), ("ficon", 6), ("escon", 7), ("sonet", 8), ("sdh", 9), ("sysplexIscCompatibility", 10), ("sysplexIscPeer", 11), ("sysplexTimerEtr", 12), ("sysplexTimerClo", 13), ("fastEthernet", 14), ("fddi", 15), ("e1", 16), ("t1", 17), ("e3", 18), ("t3", 19), ("dvb", 20), ("sdi", 21), ("its", 22))

class TriValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("true", 1), ("false", 2), ("notApplicable", 3))

class CmRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("auto", 2), ("oneGbps", 3), ("twoGbps", 4), ("fourGbps", 5), ("tenGbps", 6))

class CmNegotiatedRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notApplicable", 1), ("negotiating", 2), ("oneGbps", 3), ("twoGbps", 4), ("fourGbps", 5), ("tenGbps", 6))

ciscoMetroPhyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1))
cmPhyIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1))
cmPhyStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2))
cmPhySonetSectionTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3))
cmPhyIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1), )
if mibBuilder.loadTexts: cmPhyIfTable.setStatus('current')
cmPhyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhyIfEntry.setStatus('current')
cmPhyIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode2R", 1), ("mode3R", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfMode.setStatus('current')
cmPhyIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 2), ProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfProtocol.setStatus('current')
cmPhyIfClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10312000))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClockRate.setStatus('current')
cmPhyIfMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfMonitor.setStatus('current')
cmPhyIfLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLoop", 1), ("diagnosticLoop", 2), ("lineLoop", 3), ("otherLoop", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfLoopback.setStatus('current')
cmPhyIfOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfOFC.setStatus('current')
cmPhyIfLaserSafetyControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfLaserSafetyControl.setStatus('deprecated')
cmPhyIfForwardLaserControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfForwardLaserControl.setStatus('deprecated')
cmPhyIfTxBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfTxBufferSize.setStatus('current')
cmPhyIfAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 10), TriValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfAutoNegotiation.setStatus('current')
cmPhyIfTransType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 11), TransmissionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyIfTransType.setStatus('current')
cmPhyIfRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 12), CmRateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfRate.setStatus('current')
cmPhyIfNegotiatedRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 13), CmNegotiatedRateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyIfNegotiatedRate.setStatus('current')
cmPhyIfOverSubscription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 14), TriValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfOverSubscription.setStatus('current')
cmPhyIfClientSubrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4240))).setUnits('mega-bytes-per-second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClientSubrate.setStatus('current')
cmPhyIfClientSubrateLock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClientSubrateLock.setStatus('current')
cmPhyStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1), )
if mibBuilder.loadTexts: cmPhyStatisticsTable.setStatus('current')
cmPhyStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhyStatisticsEntry.setStatus('current')
cmPhyRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4000, 0))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxPower.setStatus('deprecated')
cmPhyRxCVRD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCVRD.setStatus('current')
cmPhyRxCVRDOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCVRDOverflow.setStatus('current')
cmPhyHCRxCVRD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxCVRD.setStatus('current')
cmPhyRxHEC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxHEC.setStatus('deprecated')
cmPhyRxHECOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxHECOverflow.setStatus('deprecated')
cmPhyHCRxHEC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxHEC.setStatus('deprecated')
cmPhyRxCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCRC.setStatus('current')
cmPhyRxCRCOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCRCOverflow.setStatus('current')
cmPhyHCRxCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxCRC.setStatus('current')
cmPhyTxEncapFarEndPktErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrors.setStatus('current')
cmPhyTxEncapFarEndPktErrOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrOverflow.setStatus('current')
cmPhyHCTxEncapFarEndPktErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCTxEncapFarEndPktErrors.setStatus('current')
cmPhySonetSectionTraceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1), )
if mibBuilder.loadTexts: cmPhySonetSectionTraceTable.setStatus('current')
cmPhySonetSectionTraceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhySonetSectionTraceEntry.setStatus('current')
cmPhySonetSectionTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), ValueSizeConstraint(64, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhySonetSectionTraceReceived.setStatus('current')
cmPhySonetSectionTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), ValueSizeConstraint(64, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhySonetSectionTraceExpected.setStatus('current')
ciscoMetroPhyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3))
ciscoMetroPhyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1))
ciscoMetroPhyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2))
cmPhyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 1)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyStatisticsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance = cmPhyMIBCompliance.setStatus('deprecated')
cmPhyMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 2)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance2 = cmPhyMIBCompliance2.setStatus('deprecated')
cmPhyMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 3)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance3 = cmPhyMIBCompliance3.setStatus('deprecated')
cmPhyMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 4)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev4 = cmPhyMIBComplianceRev4.setStatus('deprecated')
cmPhyMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 5)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev5 = cmPhyMIBComplianceRev5.setStatus('deprecated')
cmPhyMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 6)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfGroupSup1"), ("CISCO-METRO-PHY-MIB", "cmPhyIfRateGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientOvsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev6 = cmPhyMIBComplianceRev6.setStatus('current')
cmPhyIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 1)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"), ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"), ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLaserSafetyControl"), ("CISCO-METRO-PHY-MIB", "cmPhyIfForwardLaserControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfGroup = cmPhyIfGroup.setStatus('deprecated')
cmPhyStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 2)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxPower"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxHEC"), ("CISCO-METRO-PHY-MIB", "cmPhyRxHECOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxHEC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyStatisticsGroup = cmPhyStatisticsGroup.setStatus('deprecated')
cmPhySonetSectionTraceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 3)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceReceived"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceExpected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhySonetSectionTraceGroup = cmPhySonetSectionTraceGroup.setStatus('current')
cmPhyIf2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 4)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"), ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"), ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIf2Group = cmPhyIf2Group.setStatus('current')
cmPhyCVRDErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 5)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyCVRDErrorsGroup = cmPhyCVRDErrorsGroup.setStatus('current')
cmPhyCRCErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 6)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxCRC"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCRCOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyCRCErrorsGroup = cmPhyCRCErrorsGroup.setStatus('current')
cmPhyEncapFarEndPktErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 7)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrors"), ("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCTxEncapFarEndPktErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyEncapFarEndPktErrorsGroup = cmPhyEncapFarEndPktErrorsGroup.setStatus('current')
cmPhyIfTxBufferSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 8)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfTxBufferSizeGroup = cmPhyIfTxBufferSizeGroup.setStatus('current')
cmPhyIfAutoNegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 9)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegotiation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfAutoNegGroup = cmPhyIfAutoNegGroup.setStatus('current')
cmPhyIfGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 10)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfTransType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfGroupSup1 = cmPhyIfGroupSup1.setStatus('current')
cmPhyIfRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 11)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfNegotiatedRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfRateGroup = cmPhyIfRateGroup.setStatus('current')
cmPhyIfClientOvsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 12)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfOverSubscription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfClientOvsGroup = cmPhyIfClientOvsGroup.setStatus('current')
cmPhyIfClientSubrateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 13)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrateLock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfClientSubrateGroup = cmPhyIfClientSubrateGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-METRO-PHY-MIB", cmPhyIfEntry=cmPhyIfEntry, cmPhyStatistics=cmPhyStatistics, cmPhyStatisticsGroup=cmPhyStatisticsGroup, cmPhyRxPower=cmPhyRxPower, cmPhyIf=cmPhyIf, TransmissionType=TransmissionType, cmPhyIfClientSubrateLock=cmPhyIfClientSubrateLock, cmPhyMIBComplianceRev5=cmPhyMIBComplianceRev5, cmPhyHCRxHEC=cmPhyHCRxHEC, cmPhyIfGroupSup1=cmPhyIfGroupSup1, cmPhyIfProtocol=cmPhyIfProtocol, ciscoMetroPhyMIB=ciscoMetroPhyMIB, cmPhyMIBCompliance=cmPhyMIBCompliance, cmPhyCVRDErrorsGroup=cmPhyCVRDErrorsGroup, ciscoMetroPhyMIBCompliances=ciscoMetroPhyMIBCompliances, cmPhyIfAutoNegotiation=cmPhyIfAutoNegotiation, cmPhyHCRxCVRD=cmPhyHCRxCVRD, CmNegotiatedRateType=CmNegotiatedRateType, cmPhyHCRxCRC=cmPhyHCRxCRC, cmPhyMIBComplianceRev4=cmPhyMIBComplianceRev4, cmPhyCRCErrorsGroup=cmPhyCRCErrorsGroup, cmPhyIfNegotiatedRate=cmPhyIfNegotiatedRate, cmPhyStatisticsEntry=cmPhyStatisticsEntry, cmPhyIfRateGroup=cmPhyIfRateGroup, cmPhyIfForwardLaserControl=cmPhyIfForwardLaserControl, cmPhyIfTransType=cmPhyIfTransType, cmPhyRxCVRDOverflow=cmPhyRxCVRDOverflow, cmPhyRxCVRD=cmPhyRxCVRD, cmPhyRxHEC=cmPhyRxHEC, cmPhyTxEncapFarEndPktErrors=cmPhyTxEncapFarEndPktErrors, cmPhyTxEncapFarEndPktErrOverflow=cmPhyTxEncapFarEndPktErrOverflow, cmPhyEncapFarEndPktErrorsGroup=cmPhyEncapFarEndPktErrorsGroup, cmPhyIfAutoNegGroup=cmPhyIfAutoNegGroup, cmPhySonetSectionTraceReceived=cmPhySonetSectionTraceReceived, cmPhyIfTable=cmPhyIfTable, cmPhyIfMode=cmPhyIfMode, cmPhyRxHECOverflow=cmPhyRxHECOverflow, cmPhyIfClockRate=cmPhyIfClockRate, cmPhyIf2Group=cmPhyIf2Group, TriValue=TriValue, ciscoMetroPhyMIBObjects=ciscoMetroPhyMIBObjects, cmPhyIfMonitor=cmPhyIfMonitor, cmPhyIfTxBufferSize=cmPhyIfTxBufferSize, cmPhyRxCRCOverflow=cmPhyRxCRCOverflow, ciscoMetroPhyMIBGroups=ciscoMetroPhyMIBGroups, CmRateType=CmRateType, ciscoMetroPhyMIBConformance=ciscoMetroPhyMIBConformance, cmPhyIfTxBufferSizeGroup=cmPhyIfTxBufferSizeGroup, cmPhyIfClientOvsGroup=cmPhyIfClientOvsGroup, cmPhySonetSectionTrace=cmPhySonetSectionTrace, cmPhyIfClientSubrate=cmPhyIfClientSubrate, cmPhyStatisticsTable=cmPhyStatisticsTable, cmPhySonetSectionTraceExpected=cmPhySonetSectionTraceExpected, cmPhyMIBCompliance2=cmPhyMIBCompliance2, cmPhyMIBComplianceRev6=cmPhyMIBComplianceRev6, cmPhyIfClientSubrateGroup=cmPhyIfClientSubrateGroup, cmPhyHCTxEncapFarEndPktErrors=cmPhyHCTxEncapFarEndPktErrors, cmPhyIfLoopback=cmPhyIfLoopback, cmPhySonetSectionTraceEntry=cmPhySonetSectionTraceEntry, PYSNMP_MODULE_ID=ciscoMetroPhyMIB, cmPhyRxCRC=cmPhyRxCRC, cmPhyMIBCompliance3=cmPhyMIBCompliance3, cmPhyIfOFC=cmPhyIfOFC, ProtocolType=ProtocolType, cmPhyIfLaserSafetyControl=cmPhyIfLaserSafetyControl, cmPhySonetSectionTraceTable=cmPhySonetSectionTraceTable, cmPhyIfRate=cmPhyIfRate, cmPhySonetSectionTraceGroup=cmPhySonetSectionTraceGroup, cmPhyIfOverSubscription=cmPhyIfOverSubscription, cmPhyIfGroup=cmPhyIfGroup)
