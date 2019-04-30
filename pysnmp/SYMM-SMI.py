#
# PySNMP MIB module SYMM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SYMM-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:06:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, NotificationType, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, iso, Bits, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "iso", "Bits", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmetricom = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070))
symmetricom.setRevisions(('1910-02-06 12:00',))
if mibBuilder.loadTexts: symmetricom.setLastUpdated('1002061200Z')
if mibBuilder.loadTexts: symmetricom.setOrganization('Symmetricom, Inc.')
symmNetworkManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1))
if mibBuilder.loadTexts: symmNetworkManagement.setStatus('current')
symmCmipManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 1))
if mibBuilder.loadTexts: symmCmipManagement.setStatus('current')
symmSnmpManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2))
if mibBuilder.loadTexts: symmSnmpManagement.setStatus('current')
symmTimePictra = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 1))
if mibBuilder.loadTexts: symmTimePictra.setStatus('current')
symmBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 2))
if mibBuilder.loadTexts: symmBroadband.setStatus('current')
symmTTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3))
if mibBuilder.loadTexts: symmTTM.setStatus('current')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1))
experiment = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 99))
ts2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 1))
nts = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 2))
ts2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 3))
s100 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 4))
syncserver = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5))
xli = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 6))
version = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1))
ntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1))
tyming = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2))
gps = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3))
dialup = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 4))
net = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 5))
etc = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6))
ntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysLeap.setStatus('current')
ntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysStratum.setStatus('current')
ntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPrecision.setStatus('current')
ntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRootDelay.setStatus('current')
ntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRootDispersion.setStatus('current')
ntpSysRefID = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRefID.setStatus('current')
ntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRefTime.setStatus('current')
ntpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPoll.setStatus('current')
ntpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPeer.setStatus('current')
ntpSysPhase = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPhase.setStatus('current')
ntpSysFreq = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysFreq.setStatus('current')
ntpSysError = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysError.setStatus('current')
ntpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysClock.setStatus('current')
ntpSysSystem = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysSystem.setStatus('current')
ntpSysProcessor = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysProcessor.setStatus('current')
ntpSysNotrust = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysNotrust.setStatus('mandatory')
ntpSysPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32768))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPktsReceived.setStatus('mandatory')
ntpSysMode = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symactive", 1), ("sympassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedctl", 6), ("reservedpriv", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysMode.setStatus('mandatory')
ntpSysVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysVersion.setStatus('current')
tymingStatus = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingStatus.setStatus('current')
tymingSource = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingSource.setStatus('current')
tymingTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingTime.setStatus('current')
tymingVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingVersion.setStatus('current')
tymingFlyPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingFlyPeriod.setStatus('current')
gpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsPosition.setStatus('current')
gpsUTCOffset = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsUTCOffset.setStatus('current')
gpsHealth = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsHealth.setStatus('current')
gpsSatlist = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSatlist.setStatus('current')
gpsMode = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsMode.setStatus('current')
etcVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcVersion.setStatus('current')
etcSerialNbr = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcSerialNbr.setStatus('current')
etcModel = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcModel.setStatus('current')
etcUpgrade = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcUpgrade.setStatus('current')
etcUpgradeServer = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcUpgradeServer.setStatus('current')
etcAlarmString = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcAlarmString.setStatus('current')
etcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9070) + (0,0)).setObjects(("SYMM-SMI", "etcAlarmString"))
mibBuilder.exportSymbols("SYMM-SMI", ntpSysProcessor=ntpSysProcessor, etcAlarmString=etcAlarmString, gpsPosition=gpsPosition, gpsSatlist=gpsSatlist, PYSNMP_MODULE_ID=symmetricom, etcSerialNbr=etcSerialNbr, ntpSysMode=ntpSysMode, gpsHealth=gpsHealth, etcVersion=etcVersion, ntpSystem=ntpSystem, version=version, tymingStatus=tymingStatus, ntpSysFreq=ntpSysFreq, dialup=dialup, syncserver=syncserver, ntpSysRootDelay=ntpSysRootDelay, net=net, ntpSysRefID=ntpSysRefID, ntpSysPktsReceived=ntpSysPktsReceived, symmTTM=symmTTM, gpsMode=gpsMode, symmetricom=symmetricom, ntpSysVersion=ntpSysVersion, gpsUTCOffset=gpsUTCOffset, ntpSysLeap=ntpSysLeap, etcUpgradeServer=etcUpgradeServer, etcUpgrade=etcUpgrade, symmSnmpManagement=symmSnmpManagement, tymingVersion=tymingVersion, ntpSysPeer=ntpSysPeer, symmTimePictra=symmTimePictra, s100=s100, ntpSysPrecision=ntpSysPrecision, etcAlarm=etcAlarm, ntpSysError=ntpSysError, symmBroadband=symmBroadband, symmNetworkManagement=symmNetworkManagement, tyming=tyming, gps=gps, etc=etc, ntpSysRefTime=ntpSysRefTime, ntpSysRootDispersion=ntpSysRootDispersion, ntpSysSystem=ntpSysSystem, ts2100=ts2100, ntpSysStratum=ntpSysStratum, experiment=experiment, symmCmipManagement=symmCmipManagement, ntpSysPhase=ntpSysPhase, ntpSysNotrust=ntpSysNotrust, ntpSysClock=ntpSysClock, tymingFlyPeriod=tymingFlyPeriod, nts=nts, tymingSource=tymingSource, ntpSysPoll=ntpSysPoll, xli=xli, etcModel=etcModel, ts2000=ts2000, tymingTime=tymingTime, products=products)