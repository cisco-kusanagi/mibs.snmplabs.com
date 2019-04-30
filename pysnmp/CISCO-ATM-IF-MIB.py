#
# PySNMP MIB module CISCO-ATM-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
atmInterfaceConfEntry, = mibBuilder.importSymbols("ATM-MIB", "atmInterfaceConfEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Bits, Counter64, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, ModuleIdentity, NotificationType, TimeTicks, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter64", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "NotificationType", "TimeTicks", "MibIdentifier", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoAtmIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 14))
ciscoAtmIfMIB.setRevisions(('2002-02-13 00:00', '2001-08-08 00:00', '2001-05-21 00:00', '2000-04-11 00:00', '1999-03-11 00:00', '1997-11-30 00:00', '1997-09-10 00:00', '1996-11-01 00:00', '1996-10-14 00:00',))
if mibBuilder.loadTexts: ciscoAtmIfMIB.setLastUpdated('200202130000Z')
if mibBuilder.loadTexts: ciscoAtmIfMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 14, 1))
class NsapAtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
class UpcMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("passing", 1), ("tagging", 2), ("dropping", 3))

ciscoAtmIfIlmiAccessGlobalDefaultFilter = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("permitAll", 1), ("permitPrefix", 2), ("permitPrefixAndWellknownGroups", 3), ("permitPrefixAndAllGroups", 4))).clone('permitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiAccessGlobalDefaultFilter.setStatus('current')
ciscoAtmIfNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfNotifsEnabled.setStatus('current')
ciscoAtmIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmIfTable.setStatus('current')
ciscoAtmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1), )
atmInterfaceConfEntry.registerAugmentions(("CISCO-ATM-IF-MIB", "ciscoAtmIfEntry"))
ciscoAtmIfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoAtmIfEntry.setStatus('current')
ciscoAtmIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("uni", 2), ("pnni", 3), ("iisp", 4), ("nniPvcOnly", 5), ("aini", 6))).clone('uni')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfType.setStatus('current')
ciscoAtmIfSide = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("user", 1), ("network", 2), ("notApplicable", 3))).clone('network')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSide.setStatus('current')
ciscoAtmIfUniType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("public", 1), ("private", 2))).clone('private')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfUniType.setStatus('current')
ciscoAtmIfPVPs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfPVPs.setStatus('current')
ciscoAtmIfPVCs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfPVCs.setStatus('current')
ciscoAtmIfActiveSVPs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfActiveSVPs.setStatus('current')
ciscoAtmIfActiveSVCs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfActiveSVCs.setStatus('current')
ciscoAtmIfTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfTotalConnections.setStatus('current')
ciscoAtmIfConfVplIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfConfVplIf.setStatus('current')
ciscoAtmIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("other", 1), ("cpu", 2), ("ethernet", 3), ("oc3Utp", 4), ("oc3SingleModeFiber", 5), ("oc3MultiModeFiber", 6), ("oc12SingleModeFiber", 7), ("ds3", 8), ("e3", 9), ("ds1", 10), ("e1", 11), ("oc3Utp3", 12), ("oc3Utp5", 13), ("oc3SmIr", 14), ("oc3SmIrPlus", 15), ("oc3SmLr", 16), ("oc3Pof", 17), ("oc12MultiModeFiber", 18), ("oc12SmIr", 19), ("oc12SmIrPlus", 20), ("oc12SmLr", 21), ("oc12Pof", 22), ("oc12SmLr2", 23), ("oc12SmLr3", 24), ("atm25", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfPortType.setStatus('current')
ciscoAtmIfXmitLed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("off", 1), ("steadyGreen", 2), ("steadyYellow", 3), ("steadyRed", 4), ("flashGreen", 5), ("flashYellow", 6), ("flashRed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfXmitLed.setStatus('current')
ciscoAtmIfRecvLed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("off", 1), ("steadyGreen", 2), ("steadyYellow", 3), ("steadyRed", 4), ("flashGreen", 5), ("flashYellow", 6), ("flashRed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfRecvLed.setStatus('current')
ciscoAtmIfXmitCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfXmitCells.setStatus('current')
ciscoAtmIfRecvCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfRecvCells.setStatus('current')
ciscoAtmIfSvcMinVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfSvcMinVci.setStatus('deprecated')
ciscoAtmIfIlmiConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiConfiguration.setStatus('current')
ciscoAtmIfIlmiAddressRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiAddressRegistration.setStatus('current')
ciscoAtmIfIlmiAutoConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiAutoConfiguration.setStatus('current')
ciscoAtmIfIlmiKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiKeepAlive.setStatus('current')
ciscoAtmIfSoftVcDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 20), NsapAtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfSoftVcDestAddress.setStatus('current')
ciscoAtmIfUniSignallingVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("atmfUni3Dot0", 2), ("atmfUni3Dot1", 3), ("atmfUni4Dot0", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfUniSignallingVersion.setStatus('current')
ciscoAtmIfSvcUpcIntent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("passing", 1), ("tagging", 2), ("dropping", 3))).clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntent.setStatus('deprecated')
ciscoAtmIfAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nsap", 1), ("esi", 2), ("e164", 3), ("null", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAddressType.setStatus('obsolete')
ciscoAtmIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 24), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAddress.setStatus('obsolete')
ciscoAtmIfWellKnownVcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2), ("manualDeleteUponEntry", 3))).clone('automatic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfWellKnownVcMode.setStatus('current')
ciscoAtmIfSignallingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSignallingAdminStatus.setStatus('current')
ciscoAtmIfCdLed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("steadyGreen", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfCdLed.setStatus('current')
ciscoAtmIfIlmiAccessFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("permitAll", 1), ("permitPrefix", 2), ("permitPrefixAndWellknownGroups", 3), ("permitPrefixAndAllGroups", 4), ("useGlobalDefaultFilter", 5))).clone('useGlobalDefaultFilter')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfIlmiAccessFilter.setStatus('current')
ciscoAtmIfConfigAESA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 35), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(7, 7), ValueSizeConstraint(20, 20), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfConfigAESA.setStatus('current')
ciscoAtmIfDerivedAESA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 36), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfDerivedAESA.setStatus('current')
ciscoAtmIfE164Address = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 37), AtmAddr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfE164Address.setStatus('current')
ciscoAtmIfE164AutoConversionOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 38), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfE164AutoConversionOnly.setStatus('current')
ciscoAtmIfRxCellUpcViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfRxCellUpcViolations.setStatus('current')
ciscoAtmIfRxCellDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfRxCellDiscards.setStatus('current')
ciscoAtmIfIlmiFSMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("down", 1), ("restarting", 2), ("waitDevType", 3), ("deviceAndPortTypeComplete", 4), ("awaitPnniConfig", 5), ("pnniConfigComplete", 6), ("awaitRestartAck", 7), ("upAndNormal", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfIlmiFSMState.setStatus('current')
ciscoAtmIfIlmiUpDownChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfIlmiUpDownChanges.setStatus('current')
ciscoAtmIfSscopFSMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("idle", 1), ("outgoingConnectionPending", 2), ("incomingConnectionPending", 3), ("dataTransferReady", 4), ("outgoingDisconnectionPending", 5), ("outgoingResyncPending", 6), ("incomingResyncPending", 7), ("outgoingRecoveryPending", 8), ("incomingRecoveryPending", 9), ("concurrentResyncPending", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfSscopFSMState.setStatus('current')
ciscoAtmIfSscopUpDownChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoAtmIfSscopUpDownChanges.setStatus('current')
ciscoAtmIfSvcUpcIntentCbr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 45), UpcMethod().clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntentCbr.setStatus('current')
ciscoAtmIfSvcUpcIntentVbrRt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 46), UpcMethod().clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntentVbrRt.setStatus('current')
ciscoAtmIfSvcUpcIntentVbrNrt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 47), UpcMethod().clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntentVbrNrt.setStatus('current')
ciscoAtmIfSvcUpcIntentAbr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 48), UpcMethod().clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntentAbr.setStatus('current')
ciscoAtmIfSvcUpcIntentUbr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 49), UpcMethod().clone('passing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfSvcUpcIntentUbr.setStatus('current')
ciscoAtmIfMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 14, 0))
ciscoAtmIfEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 14, 0, 1)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiFSMState"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopFSMState"))
if mibBuilder.loadTexts: ciscoAtmIfEvent.setStatus('current')
ciscoAtmIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 14, 3))
ciscoAtmIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1))
ciscoAtmIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2))
ciscoAtmIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 1)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance = ciscoAtmIfMIBCompliance.setStatus('obsolete')
ciscoAtmIfMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 2)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance2 = ciscoAtmIfMIBCompliance2.setStatus('obsolete')
ciscoAtmIfMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 3)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup2"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance3 = ciscoAtmIfMIBCompliance3.setStatus('obsolete')
ciscoAtmIfMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 4)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup2"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup3"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance4 = ciscoAtmIfMIBCompliance4.setStatus('obsolete')
ciscoAtmIfMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 5)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup2"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup3"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup4"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance5 = ciscoAtmIfMIBCompliance5.setStatus('obsolete')
ciscoAtmIfMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 6)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup2"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup4"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup5"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup6"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance6 = ciscoAtmIfMIBCompliance6.setStatus('obsolete')
ciscoAtmIfMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 7)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup4"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup5"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup6"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup7"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup8"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance7 = ciscoAtmIfMIBCompliance7.setStatus('deprecated')
ciscoAtmIfMIBCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 8)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup4"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup5"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup6"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup7"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup8"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup9"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfMIBGroup10"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBCompliance8 = ciscoAtmIfMIBCompliance8.setStatus('current')
ciscoAtmIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 1)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSide"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfUniType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVPs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVCs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVPs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVCs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfTotalConnections"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfConfVplIf"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPortType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitLed"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvLed"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitCells"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvCells"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcMinVci"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiConfiguration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAddressRegistration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAutoConfiguration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiKeepAlive"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSoftVcDestAddress"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfCdLed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup = ciscoAtmIfMIBGroup.setStatus('deprecated')
ciscoAtmIfMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 2)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfUniSignallingVersion"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup2 = ciscoAtmIfMIBGroup2.setStatus('deprecated')
ciscoAtmIfMIBGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 3)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfAddressType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfAddress"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfWellKnownVcMode"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSignallingAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup3 = ciscoAtmIfMIBGroup3.setStatus('obsolete')
ciscoAtmIfMIBGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 4)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAccessGlobalDefaultFilter"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAccessFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup4 = ciscoAtmIfMIBGroup4.setStatus('current')
ciscoAtmIfMIBGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 5)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfConfigAESA"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfDerivedAESA"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfE164Address"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfE164AutoConversionOnly"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup5 = ciscoAtmIfMIBGroup5.setStatus('current')
ciscoAtmIfMIBGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 6)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfWellKnownVcMode"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSignallingAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup6 = ciscoAtmIfMIBGroup6.setStatus('current')
ciscoAtmIfMIBGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 7)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfRxCellUpcViolations"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfRxCellDiscards"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiFSMState"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiUpDownChanges"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopFSMState"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopUpDownChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup7 = ciscoAtmIfMIBGroup7.setStatus('current')
ciscoAtmIfMIBGroup8 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 8)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfUniSignallingVersion"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentCbr"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentVbrRt"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentVbrNrt"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentAbr"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentUbr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup8 = ciscoAtmIfMIBGroup8.setStatus('current')
ciscoAtmIfMIBGroup9 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 9)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSide"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfUniType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVPs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVCs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVPs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVCs"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfTotalConnections"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfConfVplIf"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfPortType"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitLed"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvLed"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitCells"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvCells"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiConfiguration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAddressRegistration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAutoConfiguration"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiKeepAlive"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfSoftVcDestAddress"), ("CISCO-ATM-IF-MIB", "ciscoAtmIfCdLed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup9 = ciscoAtmIfMIBGroup9.setStatus('current')
ciscoAtmIfMIBGroup10 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 10)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfMIBGroup10 = ciscoAtmIfMIBGroup10.setStatus('current')
ciscoAtmIfNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 11)).setObjects(("CISCO-ATM-IF-MIB", "ciscoAtmIfEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfNotifyGroup = ciscoAtmIfNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-IF-MIB", ciscoAtmIfMIBGroup10=ciscoAtmIfMIBGroup10, ciscoAtmIfIlmiAccessFilter=ciscoAtmIfIlmiAccessFilter, ciscoAtmIfMIBGroup2=ciscoAtmIfMIBGroup2, ciscoAtmIfType=ciscoAtmIfType, ciscoAtmIfMIBGroup8=ciscoAtmIfMIBGroup8, ciscoAtmIfAddressType=ciscoAtmIfAddressType, ciscoAtmIfXmitLed=ciscoAtmIfXmitLed, ciscoAtmIfMIBConformance=ciscoAtmIfMIBConformance, ciscoAtmIfEvent=ciscoAtmIfEvent, ciscoAtmIfActiveSVPs=ciscoAtmIfActiveSVPs, ciscoAtmIfMIBGroup7=ciscoAtmIfMIBGroup7, ciscoAtmIfSvcUpcIntentAbr=ciscoAtmIfSvcUpcIntentAbr, ciscoAtmIfPortType=ciscoAtmIfPortType, ciscoAtmIfMIBCompliance7=ciscoAtmIfMIBCompliance7, ciscoAtmIfSvcMinVci=ciscoAtmIfSvcMinVci, ciscoAtmIfSvcUpcIntentCbr=ciscoAtmIfSvcUpcIntentCbr, ciscoAtmIfPVCs=ciscoAtmIfPVCs, ciscoAtmIfWellKnownVcMode=ciscoAtmIfWellKnownVcMode, ciscoAtmIfMIBCompliances=ciscoAtmIfMIBCompliances, ciscoAtmIfMIBGroups=ciscoAtmIfMIBGroups, ciscoAtmIfActiveSVCs=ciscoAtmIfActiveSVCs, ciscoAtmIfEntry=ciscoAtmIfEntry, ciscoAtmIfIlmiAccessGlobalDefaultFilter=ciscoAtmIfIlmiAccessGlobalDefaultFilter, ciscoAtmIfRxCellUpcViolations=ciscoAtmIfRxCellUpcViolations, ciscoAtmIfConfigAESA=ciscoAtmIfConfigAESA, ciscoAtmIfSignallingAdminStatus=ciscoAtmIfSignallingAdminStatus, ciscoAtmIfMIBGroup3=ciscoAtmIfMIBGroup3, ciscoAtmIfTable=ciscoAtmIfTable, ciscoAtmIfE164Address=ciscoAtmIfE164Address, ciscoAtmIfMIBGroup4=ciscoAtmIfMIBGroup4, ciscoAtmIfIlmiAutoConfiguration=ciscoAtmIfIlmiAutoConfiguration, ciscoAtmIfMIBGroup9=ciscoAtmIfMIBGroup9, ciscoAtmIfMIBNotifications=ciscoAtmIfMIBNotifications, ciscoAtmIfNotifyGroup=ciscoAtmIfNotifyGroup, ciscoAtmIfMIBCompliance6=ciscoAtmIfMIBCompliance6, ciscoAtmIfRecvCells=ciscoAtmIfRecvCells, ciscoAtmIfRecvLed=ciscoAtmIfRecvLed, NsapAtmAddr=NsapAtmAddr, ciscoAtmIfMIBGroup6=ciscoAtmIfMIBGroup6, ciscoAtmIfSvcUpcIntentVbrRt=ciscoAtmIfSvcUpcIntentVbrRt, ciscoAtmIfUniType=ciscoAtmIfUniType, ciscoAtmIfTotalConnections=ciscoAtmIfTotalConnections, ciscoAtmIfPVPs=ciscoAtmIfPVPs, ciscoAtmIfSvcUpcIntent=ciscoAtmIfSvcUpcIntent, ciscoAtmIfMIBGroup=ciscoAtmIfMIBGroup, ciscoAtmIfSscopUpDownChanges=ciscoAtmIfSscopUpDownChanges, ciscoAtmIfNotifsEnabled=ciscoAtmIfNotifsEnabled, PYSNMP_MODULE_ID=ciscoAtmIfMIB, ciscoAtmIfSide=ciscoAtmIfSide, ciscoAtmIfIlmiUpDownChanges=ciscoAtmIfIlmiUpDownChanges, ciscoAtmIfMIBGroup5=ciscoAtmIfMIBGroup5, ciscoAtmIfIlmiFSMState=ciscoAtmIfIlmiFSMState, ciscoAtmIfMIBCompliance5=ciscoAtmIfMIBCompliance5, ciscoAtmIfConfVplIf=ciscoAtmIfConfVplIf, ciscoAtmIfRxCellDiscards=ciscoAtmIfRxCellDiscards, ciscoAtmIfAddress=ciscoAtmIfAddress, ciscoAtmIfMIBCompliance8=ciscoAtmIfMIBCompliance8, ciscoAtmIfMIB=ciscoAtmIfMIB, ciscoAtmIfIlmiAddressRegistration=ciscoAtmIfIlmiAddressRegistration, ciscoAtmIfMIBCompliance2=ciscoAtmIfMIBCompliance2, ciscoAtmIfCdLed=ciscoAtmIfCdLed, ciscoAtmIfSvcUpcIntentVbrNrt=ciscoAtmIfSvcUpcIntentVbrNrt, ciscoAtmIfMIBCompliance4=ciscoAtmIfMIBCompliance4, ciscoAtmIfDerivedAESA=ciscoAtmIfDerivedAESA, ciscoAtmIfIlmiKeepAlive=ciscoAtmIfIlmiKeepAlive, ciscoAtmIfMIBObjects=ciscoAtmIfMIBObjects, ciscoAtmIfSscopFSMState=ciscoAtmIfSscopFSMState, ciscoAtmIfIlmiConfiguration=ciscoAtmIfIlmiConfiguration, ciscoAtmIfUniSignallingVersion=ciscoAtmIfUniSignallingVersion, ciscoAtmIfMIBCompliance=ciscoAtmIfMIBCompliance, ciscoAtmIfSoftVcDestAddress=ciscoAtmIfSoftVcDestAddress, ciscoAtmIfSvcUpcIntentUbr=ciscoAtmIfSvcUpcIntentUbr, UpcMethod=UpcMethod, AtmAddr=AtmAddr, ciscoAtmIfE164AutoConversionOnly=ciscoAtmIfE164AutoConversionOnly, ciscoAtmIfXmitCells=ciscoAtmIfXmitCells, ciscoAtmIfMIBCompliance3=ciscoAtmIfMIBCompliance3)
