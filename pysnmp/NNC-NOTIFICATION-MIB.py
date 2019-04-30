#
# PySNMP MIB module NNC-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNC-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
nncExtensions, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtensions")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter32, Counter64, TimeTicks, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter32", "Counter64", "TimeTicks", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncExtNotif = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 44))
if mibBuilder.loadTexts: nncExtNotif.setLastUpdated('9704220000Z')
if mibBuilder.loadTexts: nncExtNotif.setOrganization('Newbridge Networks Corporation')
nncExtNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 1))
nncExtNotifType = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2))
nncExtNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 3))
nncExtNotifCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 4))
nncExtNotifAlarmType = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1))
nncExtNotifAlarmType_v1Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1, 0)).setLabel("nncExtNotifAlarmType-v1Trap")
nncExtNotifTroubleTicketType = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2))
nncExtNotifTroubleTicketType_v1Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0)).setLabel("nncExtNotifTroubleTicketType-v1Trap")
nncExtNotifHeartBeatType = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3))
nncExtNotifHeartBeatType_v1Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3, 0)).setLabel("nncExtNotifHeartBeatType-v1Trap")
class CpssAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 15)

class StringType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 30)

class ParameterStringType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 40)

class NBNodeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76))
    namedValues = NamedValues(("nd4601", 2), ("nd46020", 3), ("ndTAP", 4), ("nd3600", 5), ("nd3612", 6), ("nd3624", 7), ("nd3630", 8), ("nd5601", 9), ("nd5602", 10), ("nd5610", 11), ("nd4601A", 12), ("nd3645SU", 13), ("nd3645PU", 14), ("ndGeneric", 15), ("ndDEXCS1S", 16), ("nd3645DS3", 17), ("ndA3606V", 19), ("ndA3606D", 20), ("ndConnectExec", 21), ("nd36120", 22), ("nd3645E3", 23), ("nd36150", 24), ("nd3664", 25), ("ndTDAX100", 26), ("ndDACSII", 27), ("ndDEXCS1L", 28), ("ndDACSIIProxyAgent", 29), ("ndGenericDCS", 30), ("nd46020DN", 31), ("nd46020CN", 32), ("nd46020RT", 33), ("nd3620", 34), ("nd36170", 35), ("nd48020", 42), ("ndDCS31", 43), ("ndDCS33", 44), ("ndFRATM", 45), ("nd3620Rtr", 54), ("ndStatsCollector", 55), ("ndMVNMatm", 56), ("nd3600PLUS", 57), ("ndISDNAccess", 58), ("ndEmMgr", 59), ("ndEmGeneric", 60), ("nd2902", 61), ("nd3606IDSU", 62), ("nd36130", 63), ("nd1630SX", 64), ("nd36125", 65), ("nd36160", 66), ("nd36110-8", 67), ("nd36110-20", 68), ("nd36111-24", 69), ("nd36111-80", 70), ("ndIAG", 71), ("ndLAG", 72), ("ndMNSC", 73), ("ndMNSC-DN", 74), ("ndMNSC-CN", 75), ("nd36177", 76))

class SysDescrType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 50)

class AlmPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("diagn", 1), ("minor", 2), ("major", 3), ("critical", 4))

class AlmInfoType(StringType):
    status = 'current'

class TTFaultLocationType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 50)

class TTPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("warning", 1), ("minor", 2), ("major", 3), ("critical", 4))

class TTFaultStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("recovery", 1), ("isolate", 2), ("maintenanc", 3), ("verify", 4), ("cleared", 5), ("user", 6), ("custom", 7), ("tdaxNode", 8), ("dcsNode", 9), ("administrative", 10))

class TThardwareFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("psFailure", 1), ("wrongCdInSlot", 2), ("wrongModOnCd", 3), ("devFailure", 4), ("cdFailure", 5), ("tailEndCircGone", 6), ("cableFailure", 7), ("ringGenFailure", 8), ("modemIsBusted", 9), ("slotIsEmpty", 10), ("nvmIntegrityError", 11), ("ramIntegrityError", 12), ("romIntegrityError", 13), ("activitySwitch", 14), ("nodeProblem", 15), ("reconcileProblem", 16), ("devProblem", 17), ("cableProblem", 18))

class TTsoftwareFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("alarmQOverflow", 1), ("unsupportedCd", 2), ("unsupportedMod", 3), ("notConfigLocally", 4), ("unsupportedStatus", 5), ("alarmProblem", 6), ("busiedOut", 7), ("maximumHops", 8), ("swDownloadProblem", 9))

class TTcommFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("cannotTalkToNode", 1))

class TTuserFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("createdByUser", 1), ("createdBySystem", 2))

class TTcustomNodeFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gfcAlarm", 1), ("customNodeLog", 2))

class TTlanNodeFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("systemTable", 1), ("interfaceRow", 2), ("lanTrap", 3), ("circuitGroup", 4), ("lanPath", 5))

class TTconnectExecFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("mibOutOfSync", 1), ("noReload", 2), ("reloadMIB", 3), ("pathProblem", 4), ("chgsrvQOverflow", 5), ("abnormalShutdown", 6), ("updateStarted", 7), ("reloadAbort", 8))

class TTtDaxNodeFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nodeAlarm", 1), ("shelfAlarm", 2), ("cardAlarm", 3), ("portAlarm", 4))

class TTdcsNodeFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nodeAlarm", 1), ("shelfAlarm", 2), ("cardAlarm", 3), ("portAlarm", 4))

class TTadminFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("passwdViolation", 1), ("licenseViolation", 2), ("invalidLicenseKey", 3))

class TTssdhRingFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("upsrProblem", 1))

class TTextNodeFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("nodeAlarm", 1), ("shelfAlarm", 2), ("cardAlarm", 3), ("deviceAlarm", 4), ("fanAlarm", 5))

class TTcongestionFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("mild", 2), ("severe", 3))

nncNodeInfo = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1), )
if mibBuilder.loadTexts: nncNodeInfo.setStatus('current')
nncNodeIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncNodeIPAddr.setStatus('current')
nncNodeCPSSAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 2), CpssAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncNodeCPSSAddr.setStatus('current')
nncNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 3), NBNodeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncNodeType.setStatus('current')
nncNodeFullName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 4), StringType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncNodeFullName.setStatus('current')
nncAlmInfo = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2), )
if mibBuilder.loadTexts: nncAlmInfo.setStatus('current')
nncAlmDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncAlmDateAndTime.setStatus('current')
nncAlmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 2), AlmPriorityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncAlmPriority.setStatus('current')
nncAlmText = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 3), StringType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncAlmText.setStatus('current')
nncTTInfo = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3), )
if mibBuilder.loadTexts: nncTTInfo.setStatus('current')
nncTTFaultType = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4), )
if mibBuilder.loadTexts: nncTTFaultType.setStatus('current')
nncTTDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTDateAndTime.setStatus('current')
nncTTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 2), TTPriorityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTPriority.setStatus('current')
nncTTFaultLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 3), TTFaultLocationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTFaultLocation.setStatus('current')
nncTTFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 4), TTFaultStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTFaultStatus.setStatus('current')
nncTTOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 5), StringType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTOwner.setStatus('current')
nncExtNotifAlarm = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1, 0, 1)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncAlmInfo"))
if mibBuilder.loadTexts: nncExtNotifAlarm.setStatus('current')
nncExtNotifHardwareTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 2)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTThardwareFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifHardwareTT.setStatus('current')
nncExtNotifSoftwareTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 3)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTsoftwareFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifSoftwareTT.setStatus('current')
nncExtNotifCommTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 4)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTcommFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifCommTT.setStatus('current')
nncExtNotifUserTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 5)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTuserFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifUserTT.setStatus('current')
nncExtNotifCustomNodeTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 6)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTcustomNodeFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifCustomNodeTT.setStatus('current')
nncExtNotifLanNodeTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 7)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTlanNodeFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifLanNodeTT.setStatus('current')
nncExtNotifConnectExecTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 8)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTconnectExecFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifConnectExecTT.setStatus('current')
nncExtNotifTDaxNodeTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 9)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTtDaxNodeFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifTDaxNodeTT.setStatus('current')
nncExtNotifAdminTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 10)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTadminFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifAdminTT.setStatus('current')
nncExtNotifSsdhRingTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 11)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTssdhRingFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifSsdhRingTT.setStatus('current')
nncExtNotifExternalNodeTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 12)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTextNodeFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifExternalNodeTT.setStatus('current')
nncExtNotifCongestionTT = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 13)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncTTcongestionFaultType"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
if mibBuilder.loadTexts: nncExtNotifCongestionTT.setStatus('current')
nncExtNotifHeartBeat = NotificationType((1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3, 0, 1)).setObjects(("NNC-NOTIFICATION-MIB", "nncSysDescr"), ("NNC-NOTIFICATION-MIB", "nncSysUpTime"))
if mibBuilder.loadTexts: nncExtNotifHeartBeat.setStatus('current')
nncHeartBeatInfo = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5), )
if mibBuilder.loadTexts: nncHeartBeatInfo.setStatus('current')
nncSysDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5, 1), SysDescrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncSysDescr.setStatus('current')
nncSysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncSysUpTime.setStatus('current')
nncTThardwareFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 1), TThardwareFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTThardwareFaultType.setStatus('current')
nncTTsoftwareFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 2), TTsoftwareFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTsoftwareFaultType.setStatus('current')
nncTTcommFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 3), TTcommFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTcommFaultType.setStatus('current')
nncTTuserFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 4), TTuserFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTuserFaultType.setStatus('current')
nncTTcustomNodeFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 5), TTcustomNodeFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTcustomNodeFaultType.setStatus('current')
nncTTlanNodeFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 6), TTlanNodeFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTlanNodeFaultType.setStatus('current')
nncTTconnectExecFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 7), TTconnectExecFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTconnectExecFaultType.setStatus('current')
nncTTtDaxNodeFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 8), TTtDaxNodeFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTtDaxNodeFaultType.setStatus('current')
nncTTdcsNodeFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 9), TTdcsNodeFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTdcsNodeFaultType.setStatus('current')
nncTTadminFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 10), TTadminFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTadminFaultType.setStatus('current')
nncTTssdhRingFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 11), TTssdhRingFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTssdhRingFaultType.setStatus('current')
nncTTextNodeFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 12), TTextNodeFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTextNodeFaultType.setStatus('current')
nncTTcongestionFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 13), TTcongestionFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncTTcongestionFaultType.setStatus('current')
nncExtNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 44, 3, 1)).setObjects(("NNC-NOTIFICATION-MIB", "nncNodeInfo"), ("NNC-NOTIFICATION-MIB", "nncAlmInfo"), ("NNC-NOTIFICATION-MIB", "nncTTInfo"), ("NNC-NOTIFICATION-MIB", "nncTTFaultType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtNotifGroup = nncExtNotifGroup.setStatus('current')
nncExtNotifCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 44, 4, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncExtNotifCompliance = nncExtNotifCompliance.setStatus('current')
mibBuilder.exportSymbols("NNC-NOTIFICATION-MIB", nncExtNotifCongestionTT=nncExtNotifCongestionTT, TTdcsNodeFaultType=TTdcsNodeFaultType, nncSysUpTime=nncSysUpTime, nncExtNotifConnectExecTT=nncExtNotifConnectExecTT, nncAlmText=nncAlmText, nncTTssdhRingFaultType=nncTTssdhRingFaultType, nncExtNotifTroubleTicketType=nncExtNotifTroubleTicketType, nncExtNotifObjects=nncExtNotifObjects, nncExtNotifCompliances=nncExtNotifCompliances, nncExtNotifCommTT=nncExtNotifCommTT, nncExtNotifAdminTT=nncExtNotifAdminTT, AlmPriorityType=AlmPriorityType, StringType=StringType, ParameterStringType=ParameterStringType, nncTTdcsNodeFaultType=nncTTdcsNodeFaultType, nncTTconnectExecFaultType=nncTTconnectExecFaultType, nncExtNotifAlarm=nncExtNotifAlarm, nncNodeType=nncNodeType, nncExtNotifAlarmType_v1Trap=nncExtNotifAlarmType_v1Trap, nncTTInfo=nncTTInfo, TTconnectExecFaultType=TTconnectExecFaultType, PYSNMP_MODULE_ID=nncExtNotif, nncExtNotifHeartBeatType_v1Trap=nncExtNotifHeartBeatType_v1Trap, nncNodeIPAddr=nncNodeIPAddr, nncExtNotif=nncExtNotif, nncTTDateAndTime=nncTTDateAndTime, TTlanNodeFaultType=TTlanNodeFaultType, CpssAddress=CpssAddress, nncExtNotifGroups=nncExtNotifGroups, nncExtNotifHeartBeat=nncExtNotifHeartBeat, nncTTOwner=nncTTOwner, nncAlmDateAndTime=nncAlmDateAndTime, nncAlmPriority=nncAlmPriority, nncSysDescr=nncSysDescr, TTuserFaultType=TTuserFaultType, nncExtNotifAlarmType=nncExtNotifAlarmType, nncTTuserFaultType=nncTTuserFaultType, nncExtNotifTroubleTicketType_v1Trap=nncExtNotifTroubleTicketType_v1Trap, TTFaultLocationType=TTFaultLocationType, nncExtNotifGroup=nncExtNotifGroup, nncTTadminFaultType=nncTTadminFaultType, nncExtNotifSsdhRingTT=nncExtNotifSsdhRingTT, nncTTextNodeFaultType=nncTTextNodeFaultType, nncAlmInfo=nncAlmInfo, TTcustomNodeFaultType=TTcustomNodeFaultType, nncTTFaultLocation=nncTTFaultLocation, nncExtNotifUserTT=nncExtNotifUserTT, TTPriorityType=TTPriorityType, nncNodeFullName=nncNodeFullName, nncNodeInfo=nncNodeInfo, TTssdhRingFaultType=TTssdhRingFaultType, nncExtNotifHeartBeatType=nncExtNotifHeartBeatType, nncExtNotifCompliance=nncExtNotifCompliance, nncNodeCPSSAddr=nncNodeCPSSAddr, nncHeartBeatInfo=nncHeartBeatInfo, nncExtNotifType=nncExtNotifType, nncTTPriority=nncTTPriority, TThardwareFaultType=TThardwareFaultType, TTsoftwareFaultType=TTsoftwareFaultType, TTcommFaultType=TTcommFaultType, nncTTFaultStatus=nncTTFaultStatus, nncTTcommFaultType=nncTTcommFaultType, AlmInfoType=AlmInfoType, nncTTlanNodeFaultType=nncTTlanNodeFaultType, nncTThardwareFaultType=nncTThardwareFaultType, nncTTtDaxNodeFaultType=nncTTtDaxNodeFaultType, TTadminFaultType=TTadminFaultType, nncExtNotifLanNodeTT=nncExtNotifLanNodeTT, TTFaultStatusType=TTFaultStatusType, nncTTsoftwareFaultType=nncTTsoftwareFaultType, TTcongestionFaultType=TTcongestionFaultType, NBNodeType=NBNodeType, nncExtNotifSoftwareTT=nncExtNotifSoftwareTT, nncExtNotifCustomNodeTT=nncExtNotifCustomNodeTT, nncExtNotifExternalNodeTT=nncExtNotifExternalNodeTT, nncTTcongestionFaultType=nncTTcongestionFaultType, nncExtNotifTDaxNodeTT=nncExtNotifTDaxNodeTT, nncTTcustomNodeFaultType=nncTTcustomNodeFaultType, TTextNodeFaultType=TTextNodeFaultType, nncTTFaultType=nncTTFaultType, SysDescrType=SysDescrType, nncExtNotifHardwareTT=nncExtNotifHardwareTT, TTtDaxNodeFaultType=TTtDaxNodeFaultType)
