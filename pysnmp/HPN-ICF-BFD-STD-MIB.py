#
# PySNMP MIB module HPN-ICF-BFD-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-BFD-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, TimeTicks, Bits, IpAddress, iso, Unsigned32, Integer32, Counter32, NotificationType, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "IpAddress", "iso", "Unsigned32", "Integer32", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity")
TruthValue, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeStamp", "DisplayString")
hpnicfBfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72))
hpnicfBfdMIB.setRevisions(('2014-01-17 12:00', '2006-05-16 12:00',))
if mibBuilder.loadTexts: hpnicfBfdMIB.setLastUpdated('201401171200Z')
if mibBuilder.loadTexts: hpnicfBfdMIB.setOrganization('')
hpnicfBfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0))
hpnicfBfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1))
hpnicfBfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 2))
hpnicfBfdGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1))
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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 1), ("controlDetectionTimeExpired", 2), ("echoFunctionFailed", 3), ("neighborSignaledSessionDown", 4), ("forwardingPlaneReset", 5), ("pathDown", 6), ("concatenatedPathDown", 7), ("administrativelyDown", 8), ("reverseConcatenatedPathDown", 9))

hpnicfBfdVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 1), Unsigned32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdVersionNumber.setStatus('current')
hpnicfBfdSysInitMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBfdSysInitMode.setStatus('current')
hpnicfBfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBfdSessNotificationsEnable.setStatus('current')
hpnicfBfdSessNumberLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessNumberLimit.setStatus('current')
hpnicfBfdIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2), )
if mibBuilder.loadTexts: hpnicfBfdIfTable.setStatus('current')
hpnicfBfdIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdIfIndex"))
if mibBuilder.loadTexts: hpnicfBfdIfEntry.setStatus('current')
hpnicfBfdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfBfdIfIndex.setStatus('current')
hpnicfBfdIfDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 2), BfdInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBfdIfDesiredMinTxInterval.setStatus('current')
hpnicfBfdIfDesiredMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 3), BfdInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBfdIfDesiredMinRxInterval.setStatus('current')
hpnicfBfdIfDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBfdIfDetectMult.setStatus('current')
hpnicfBfdIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3), ("mmd5", 4), ("sha1", 5), ("msha1", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdIfAuthType.setStatus('current')
hpnicfBfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3), )
if mibBuilder.loadTexts: hpnicfBfdSessTable.setStatus('current')
hpnicfBfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"), (0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"))
if mibBuilder.loadTexts: hpnicfBfdSessEntry.setStatus('current')
hpnicfBfdSessIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfBfdSessIfIndex.setStatus('current')
hpnicfBfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 2), BfdSessIndexTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfBfdSessIndex.setStatus('current')
hpnicfBfdSessAppSupportId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("none", 0), ("ospf", 1), ("isis", 2), ("bgp", 3), ("mpls", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessAppSupportId.setStatus('current')
hpnicfBfdSessLocalDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessLocalDiscr.setStatus('current')
hpnicfBfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessRemoteDiscr.setStatus('current')
hpnicfBfdSessDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 6), InetPortNumber().clone(3784)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessDstPort.setStatus('current')
hpnicfBfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("asynchModeWOEchoFun", 1), ("demandModeWOEchoFunction", 2), ("asyncModeWEchoFun", 3), ("demandModeWEchoFunction", 4))).clone('asynchModeWOEchoFun')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessOperMode.setStatus('current')
hpnicfBfdSessAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessAddrType.setStatus('current')
hpnicfBfdSessLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessLocalAddr.setStatus('current')
hpnicfBfdSessRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessRemoteAddr.setStatus('current')
hpnicfBfdSessLocalDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 11), BfdDiag().clone('noDiagnostic')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessLocalDiag.setStatus('current')
hpnicfBfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("adminDown", 0), ("down", 1), ("init", 2), ("up", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessState.setStatus('current')
hpnicfBfdSessControlPlanIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 13), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessControlPlanIndepFlag.setStatus('current')
hpnicfBfdSessAuthFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 14), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessAuthFlag.setStatus('current')
hpnicfBfdSessDemandModeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessDemandModeFlag.setStatus('current')
hpnicfBfdSessStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4), )
if mibBuilder.loadTexts: hpnicfBfdSessStatTable.setStatus('current')
hpnicfBfdSessStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1), )
hpnicfBfdSessEntry.registerAugmentions(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessStatEntry"))
hpnicfBfdSessStatEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfBfdSessStatEntry.setStatus('current')
hpnicfBfdSessStatPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessStatPktInHC.setStatus('current')
hpnicfBfdSessStatPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessStatPktOutHC.setStatus('current')
hpnicfBfdSessStatDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessStatDownCount.setStatus('current')
hpnicfBfdSessStatPktDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessStatPktDiscard.setStatus('current')
hpnicfBfdSessStatPktLost = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessStatPktLost.setStatus('current')
hpnicfBfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5), )
if mibBuilder.loadTexts: hpnicfBfdSessPerfTable.setStatus('current')
hpnicfBfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1), )
hpnicfBfdSessEntry.registerAugmentions(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessPerfEntry"))
hpnicfBfdSessPerfEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfBfdSessPerfEntry.setStatus('current')
hpnicfBfdSessPerfCreatTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessPerfCreatTime.setStatus('current')
hpnicfBfdSessPerfLastUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessPerfLastUpTime.setStatus('current')
hpnicfBfdSessPerfLastDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBfdSessPerfLastDownTime.setStatus('current')
hpnicfBfdSessStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 1)).setObjects(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
if mibBuilder.loadTexts: hpnicfBfdSessStateChange.setStatus('current')
hpnicfBfdSessAuthFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 2)).setObjects(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdIfIndex"))
if mibBuilder.loadTexts: hpnicfBfdSessAuthFail.setStatus('current')
hpnicfBfdSessStateUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 3)).setObjects(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
if mibBuilder.loadTexts: hpnicfBfdSessStateUp.setStatus('current')
hpnicfBfdSessStateDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 4)).setObjects(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"), ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
if mibBuilder.loadTexts: hpnicfBfdSessStateDown.setStatus('current')
hpnicfBfdSessReachLimit = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 5)).setObjects(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessNumberLimit"))
if mibBuilder.loadTexts: hpnicfBfdSessReachLimit.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-BFD-STD-MIB", hpnicfBfdSessStatPktInHC=hpnicfBfdSessStatPktInHC, BfdSessIndexTC=BfdSessIndexTC, hpnicfBfdSessLocalAddr=hpnicfBfdSessLocalAddr, hpnicfBfdNotifications=hpnicfBfdNotifications, hpnicfBfdSessState=hpnicfBfdSessState, hpnicfBfdSessPerfEntry=hpnicfBfdSessPerfEntry, hpnicfBfdSessAddrType=hpnicfBfdSessAddrType, hpnicfBfdSessReachLimit=hpnicfBfdSessReachLimit, hpnicfBfdSessStateDown=hpnicfBfdSessStateDown, hpnicfBfdSessIndex=hpnicfBfdSessIndex, hpnicfBfdSessAuthFail=hpnicfBfdSessAuthFail, hpnicfBfdIfDetectMult=hpnicfBfdIfDetectMult, hpnicfBfdSessIfIndex=hpnicfBfdSessIfIndex, hpnicfBfdSessPerfTable=hpnicfBfdSessPerfTable, hpnicfBfdGlobalObjects=hpnicfBfdGlobalObjects, hpnicfBfdSessNotificationsEnable=hpnicfBfdSessNotificationsEnable, hpnicfBfdSessTable=hpnicfBfdSessTable, hpnicfBfdSessDstPort=hpnicfBfdSessDstPort, hpnicfBfdSessOperMode=hpnicfBfdSessOperMode, hpnicfBfdSessStatPktOutHC=hpnicfBfdSessStatPktOutHC, hpnicfBfdIfDesiredMinTxInterval=hpnicfBfdIfDesiredMinTxInterval, hpnicfBfdVersionNumber=hpnicfBfdVersionNumber, hpnicfBfdSessStatDownCount=hpnicfBfdSessStatDownCount, BfdInterval=BfdInterval, hpnicfBfdIfIndex=hpnicfBfdIfIndex, PYSNMP_MODULE_ID=hpnicfBfdMIB, hpnicfBfdSessLocalDiag=hpnicfBfdSessLocalDiag, hpnicfBfdSessStatEntry=hpnicfBfdSessStatEntry, hpnicfBfdIfDesiredMinRxInterval=hpnicfBfdIfDesiredMinRxInterval, hpnicfBfdSessStatTable=hpnicfBfdSessStatTable, BfdDiag=BfdDiag, hpnicfBfdSessPerfLastUpTime=hpnicfBfdSessPerfLastUpTime, hpnicfBfdIfTable=hpnicfBfdIfTable, hpnicfBfdIfAuthType=hpnicfBfdIfAuthType, hpnicfBfdSessAuthFlag=hpnicfBfdSessAuthFlag, hpnicfBfdSessStateChange=hpnicfBfdSessStateChange, hpnicfBfdSessRemoteDiscr=hpnicfBfdSessRemoteDiscr, hpnicfBfdSessNumberLimit=hpnicfBfdSessNumberLimit, hpnicfBfdSessControlPlanIndepFlag=hpnicfBfdSessControlPlanIndepFlag, hpnicfBfdSessDemandModeFlag=hpnicfBfdSessDemandModeFlag, hpnicfBfdSessEntry=hpnicfBfdSessEntry, hpnicfBfdSysInitMode=hpnicfBfdSysInitMode, hpnicfBfdMIB=hpnicfBfdMIB, hpnicfBfdIfEntry=hpnicfBfdIfEntry, hpnicfBfdConformance=hpnicfBfdConformance, hpnicfBfdSessPerfCreatTime=hpnicfBfdSessPerfCreatTime, hpnicfBfdSessStatPktDiscard=hpnicfBfdSessStatPktDiscard, hpnicfBfdSessPerfLastDownTime=hpnicfBfdSessPerfLastDownTime, hpnicfBfdSessStateUp=hpnicfBfdSessStateUp, hpnicfBfdSessLocalDiscr=hpnicfBfdSessLocalDiscr, hpnicfBfdSessAppSupportId=hpnicfBfdSessAppSupportId, hpnicfBfdSessStatPktLost=hpnicfBfdSessStatPktLost, hpnicfBfdSessRemoteAddr=hpnicfBfdSessRemoteAddr, hpnicfBfdObjects=hpnicfBfdObjects)
