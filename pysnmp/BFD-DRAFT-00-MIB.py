#
# PySNMP MIB module BFD-DRAFT-00-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BFD-DRAFT-00-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
mib_2, Counter32, iso, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, Counter64, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Counter32", "iso", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Integer32")
TruthValue, TextualConvention, StorageType, TimeStamp, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "StorageType", "TimeStamp", "RowStatus", "DisplayString")
bfdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 999))
bfdMIB.setRevisions(('2004-01-22 12:00',))
if mibBuilder.loadTexts: bfdMIB.setLastUpdated('200401221200Z')
if mibBuilder.loadTexts: bfdMIB.setOrganization('IETF')
bfdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 0))
bfdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1))
bfdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 3))
bfdScalarObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1))
class BfdSessIndexTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdInterval(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdDiag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noDiagnostic", 1), ("controlDetectionTimeExpired", 2), ("echoFunctionFailed", 3), ("neighborSignaledSessionDown", 4), ("forwardingPlaneReset", 5), ("pathDown", 6), ("concatenatedPathDown", 7), ("administrativelyDown", 8))

bfdAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 999, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdAdminStatus.setStatus('current')
bfdOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 999, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdOperStatus.setStatus('current')
bfdVersionNumber = MibScalar((1, 3, 6, 1, 2, 1, 999, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdVersionNumber.setStatus('current')
bfdSessTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 2), )
if mibBuilder.loadTexts: bfdSessTable.setStatus('current')
bfdSessEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 2, 1), ).setIndexNames((0, "BFD-DRAFT-00-MIB", "bfdSessIndex"))
if mibBuilder.loadTexts: bfdSessEntry.setStatus('current')
bfdSessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1), BfdSessIndexTC())
if mibBuilder.loadTexts: bfdSessIndex.setStatus('current')
bfdSessApplicationId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessApplicationId.setStatus('current')
bfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDiscriminator.setStatus('current')
bfdSessLocalDiscr = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessLocalDiscr.setStatus('current')
bfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteDiscr.setStatus('current')
bfdSessState = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("up", 2), ("failing", 3), ("down", 4), ("adminDown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessState.setStatus('current')
bfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteHeardFlag.setStatus('current')
bfdSessDiag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 8), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bfdSessDiag.setStatus('current')
bfdSessOperMode = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("asyncModeWEchoFun", 1), ("asynchModeWOEchoFun", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessOperMode.setStatus('current')
bfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDemandModeDesiredFlag.setStatus('current')
bfdSessEchoFuncModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessEchoFuncModeDesiredFlag.setStatus('current')
bfdSessEchoFuncFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessEchoFuncFlag.setStatus('current')
bfdSessAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 13), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAddrType.setStatus('current')
bfdSessAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 14), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAddr.setStatus('current')
bfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 15), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDesiredMinTxInterval.setStatus('current')
bfdSessDesiredMinRxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 16), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDesiredMinRxInterval.setStatus('current')
bfdSessDesiredMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 17), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDesiredMinEchoRxInterval.setStatus('current')
bfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 18), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDetectMult.setStatus('current')
bfdSessStorType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 19), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessStorType.setStatus('current')
bfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessRowStatus.setStatus('current')
bfdSessPerfTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 3), )
if mibBuilder.loadTexts: bfdSessPerfTable.setStatus('current')
bfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 3, 1), )
bfdSessEntry.registerAugmentions(("BFD-DRAFT-00-MIB", "bfdSessPerfEntry"))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: bfdSessPerfEntry.setStatus('current')
bfdSessPerfPktIn = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktIn.setStatus('current')
bfdSessPerfPktOut = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOut.setStatus('current')
bfdSessPerfBadDiscrim = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfBadDiscrim.setStatus('current')
bfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastSessDownTime.setStatus('current')
bfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 5), BfdDiag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastCommLostDiag.setStatus('current')
bfdSessPerfSessDownCount = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfSessDownCount.setStatus('current')
bfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfDiscTime.setStatus('current')
bfdSessPerfPktInHC = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktInHC.setStatus('current')
bfdSessPerfPktOutHC = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOutHC.setStatus('current')
bfdSessPerfBadDiscrimHC = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfBadDiscrimHC.setStatus('current')
bfdSessMapTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 4), )
if mibBuilder.loadTexts: bfdSessMapTable.setStatus('current')
bfdSessMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 4, 1), ).setIndexNames((0, "BFD-DRAFT-00-MIB", "bfdSessApplicationId"), (0, "BFD-DRAFT-00-MIB", "bfdSessDiscriminator"), (0, "BFD-DRAFT-00-MIB", "bfdSessAddrType"), (0, "BFD-DRAFT-00-MIB", "bfdSessAddr"))
if mibBuilder.loadTexts: bfdSessMapEntry.setStatus('current')
bfdSessMapBfdIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1), BfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessMapBfdIndex.setStatus('current')
bfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 2, 1, 999, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessNotificationsEnable.setStatus('current')
bfdSessUp = NotificationType((1, 3, 6, 1, 2, 1, 999, 0, 1)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessDiag"), ("BFD-DRAFT-00-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessUp.setStatus('current')
bfdSessDown = NotificationType((1, 3, 6, 1, 2, 1, 999, 0, 2)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessDiag"), ("BFD-DRAFT-00-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessDown.setStatus('current')
bfdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 3, 1))
bfdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 3, 2))
bfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 999, 3, 2, 1)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessionGroup"), ("BFD-DRAFT-00-MIB", "bfdSessionPerfGroup"), ("BFD-DRAFT-00-MIB", "bfdSessionPerfHCGroup"), ("BFD-DRAFT-00-MIB", "bfdNotificationGroup"), ("BFD-DRAFT-00-MIB", "bfdSessionPerfHCGroup"), ("BFD-DRAFT-00-MIB", "bfdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdModuleFullCompliance = bfdModuleFullCompliance.setStatus('current')
bfdSessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 3, 1, 1)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessNotificationsEnable"), ("BFD-DRAFT-00-MIB", "bfdAdminStatus"), ("BFD-DRAFT-00-MIB", "bfdOperStatus"), ("BFD-DRAFT-00-MIB", "bfdVersionNumber"), ("BFD-DRAFT-00-MIB", "bfdSessApplicationId"), ("BFD-DRAFT-00-MIB", "bfdSessDiscriminator"), ("BFD-DRAFT-00-MIB", "bfdSessAddrType"), ("BFD-DRAFT-00-MIB", "bfdSessAddr"), ("BFD-DRAFT-00-MIB", "bfdSessLocalDiscr"), ("BFD-DRAFT-00-MIB", "bfdSessRemoteDiscr"), ("BFD-DRAFT-00-MIB", "bfdSessState"), ("BFD-DRAFT-00-MIB", "bfdSessRemoteHeardFlag"), ("BFD-DRAFT-00-MIB", "bfdSessDiag"), ("BFD-DRAFT-00-MIB", "bfdSessOperMode"), ("BFD-DRAFT-00-MIB", "bfdSessDemandModeDesiredFlag"), ("BFD-DRAFT-00-MIB", "bfdSessEchoFuncFlag"), ("BFD-DRAFT-00-MIB", "bfdSessEchoFuncModeDesiredFlag"), ("BFD-DRAFT-00-MIB", "bfdSessDesiredMinTxInterval"), ("BFD-DRAFT-00-MIB", "bfdSessDesiredMinRxInterval"), ("BFD-DRAFT-00-MIB", "bfdSessDesiredMinEchoRxInterval"), ("BFD-DRAFT-00-MIB", "bfdSessDetectMult"), ("BFD-DRAFT-00-MIB", "bfdSessStorType"), ("BFD-DRAFT-00-MIB", "bfdSessRowStatus"), ("BFD-DRAFT-00-MIB", "bfdSessMapBfdIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionGroup = bfdSessionGroup.setStatus('current')
bfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 3, 1, 2)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessPerfPktIn"), ("BFD-DRAFT-00-MIB", "bfdSessPerfPktOut"), ("BFD-DRAFT-00-MIB", "bfdSessPerfBadDiscrim"), ("BFD-DRAFT-00-MIB", "bfdSessPerfLastSessDownTime"), ("BFD-DRAFT-00-MIB", "bfdSessPerfLastCommLostDiag"), ("BFD-DRAFT-00-MIB", "bfdSessPerfSessDownCount"), ("BFD-DRAFT-00-MIB", "bfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfGroup = bfdSessionPerfGroup.setStatus('current')
bfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 3, 1, 3)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessPerfPktInHC"), ("BFD-DRAFT-00-MIB", "bfdSessPerfPktOutHC"), ("BFD-DRAFT-00-MIB", "bfdSessPerfBadDiscrimHC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfHCGroup = bfdSessionPerfHCGroup.setStatus('current')
bfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 999, 3, 1, 4)).setObjects(("BFD-DRAFT-00-MIB", "bfdSessUp"), ("BFD-DRAFT-00-MIB", "bfdSessDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdNotificationGroup = bfdNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("BFD-DRAFT-00-MIB", bfdSessionGroup=bfdSessionGroup, bfdVersionNumber=bfdVersionNumber, bfdOperStatus=bfdOperStatus, bfdAdminStatus=bfdAdminStatus, bfdSessOperMode=bfdSessOperMode, BfdInterval=BfdInterval, bfdSessPerfPktIn=bfdSessPerfPktIn, bfdNotificationGroup=bfdNotificationGroup, bfdSessDemandModeDesiredFlag=bfdSessDemandModeDesiredFlag, bfdSessMapEntry=bfdSessMapEntry, BfdDiag=BfdDiag, bfdSessRowStatus=bfdSessRowStatus, bfdSessPerfSessDownCount=bfdSessPerfSessDownCount, bfdNotifications=bfdNotifications, bfdSessDesiredMinTxInterval=bfdSessDesiredMinTxInterval, bfdSessDesiredMinEchoRxInterval=bfdSessDesiredMinEchoRxInterval, bfdSessDown=bfdSessDown, bfdScalarObjects=bfdScalarObjects, bfdMIB=bfdMIB, bfdSessPerfPktOutHC=bfdSessPerfPktOutHC, bfdSessDiag=bfdSessDiag, bfdSessPerfBadDiscrim=bfdSessPerfBadDiscrim, bfdSessMapBfdIndex=bfdSessMapBfdIndex, bfdSessDetectMult=bfdSessDetectMult, bfdGroups=bfdGroups, bfdSessionPerfHCGroup=bfdSessionPerfHCGroup, bfdSessAddr=bfdSessAddr, bfdSessAddrType=bfdSessAddrType, bfdSessStorType=bfdSessStorType, PYSNMP_MODULE_ID=bfdMIB, bfdSessPerfPktOut=bfdSessPerfPktOut, bfdSessPerfPktInHC=bfdSessPerfPktInHC, bfdSessionPerfGroup=bfdSessionPerfGroup, BfdSessIndexTC=BfdSessIndexTC, bfdSessState=bfdSessState, bfdSessPerfLastCommLostDiag=bfdSessPerfLastCommLostDiag, bfdSessUp=bfdSessUp, bfdSessDesiredMinRxInterval=bfdSessDesiredMinRxInterval, bfdSessLocalDiscr=bfdSessLocalDiscr, bfdSessPerfDiscTime=bfdSessPerfDiscTime, bfdSessRemoteDiscr=bfdSessRemoteDiscr, bfdSessEchoFuncModeDesiredFlag=bfdSessEchoFuncModeDesiredFlag, bfdSessMapTable=bfdSessMapTable, bfdSessEchoFuncFlag=bfdSessEchoFuncFlag, bfdCompliances=bfdCompliances, bfdConformance=bfdConformance, bfdSessRemoteHeardFlag=bfdSessRemoteHeardFlag, bfdModuleFullCompliance=bfdModuleFullCompliance, bfdSessEntry=bfdSessEntry, bfdSessPerfBadDiscrimHC=bfdSessPerfBadDiscrimHC, bfdSessPerfEntry=bfdSessPerfEntry, bfdSessPerfTable=bfdSessPerfTable, bfdSessApplicationId=bfdSessApplicationId, bfdSessPerfLastSessDownTime=bfdSessPerfLastSessDownTime, bfdSessNotificationsEnable=bfdSessNotificationsEnable, bfdSessTable=bfdSessTable, bfdSessIndex=bfdSessIndex, bfdObjects=bfdObjects, bfdSessDiscriminator=bfdSessDiscriminator)
