#
# PySNMP MIB module HH3C-MAC-INFORMATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MAC-INFORMATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, IpAddress, Counter64, Gauge32, MibIdentifier, Integer32, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "IpAddress", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cMACInformation = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 87))
hh3cMACInformation.setRevisions(('2007-12-28 19:12',))
if mibBuilder.loadTexts: hh3cMACInformation.setLastUpdated('200712281912Z')
if mibBuilder.loadTexts: hh3cMACInformation.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
class Hh3cMACInfoWorkMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trap", 1), ("syslog", 2))

hh3cMACInformationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1))
hh3cMACInformationMibGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1))
hh3cMACInformationMIBTableTroop = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2))
hh3cMACInformationMibTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3))
hh3cMACInformationMibTrapExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4))
hh3cMACInformationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACInformationEnabled.setStatus('current')
hh3cMACInformationcSendInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20000)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACInformationcSendInterval.setStatus('current')
hh3cMACInformationLearntMACNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMACInformationLearntMACNum.setStatus('current')
hh3cMACInformationRemovedMACNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMACInformationRemovedMACNum.setStatus('current')
hh3cMACInformationTrapSendNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMACInformationTrapSendNum.setStatus('current')
hh3cMACInformationSyslogSendNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMACInformationSyslogSendNum.setStatus('current')
hh3cMACInformationCacheLen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACInformationCacheLen.setStatus('current')
hh3cMACInfomationWorkMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 8), Hh3cMACInfoWorkMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACInfomationWorkMode.setStatus('current')
hh3cMACInfomationIfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cMACInfomationIfTable.setStatus('current')
hh3cMACInfomationIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cMACInfomationIfEntry.setStatus('current')
hh3cMACLearntEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACLearntEnable.setStatus('current')
hh3cMACRemovedEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMACRemovedEnable.setStatus('current')
hh3cMACInformationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 0))
hh3cMACInformationChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 0, 1)).setObjects(("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapIndex"), ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapCount"), ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapMsg"))
if mibBuilder.loadTexts: hh3cMACInformationChangedTrap.setStatus('current')
hh3cMACInformationTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2))
hh3cMACInfoTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapIndex.setStatus('current')
hh3cMACInfoTrapCount = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapCount.setStatus('current')
hh3cMACInfoTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapMsg.setStatus('current')
hh3cMACInformationTrapsExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 0))
hh3cMACInformationChangedTrapExt = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 0, 1)).setObjects(("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapVerExt"), ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapIndexExt"), ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapCountExt"), ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapMsgExt"))
if mibBuilder.loadTexts: hh3cMACInformationChangedTrapExt.setStatus('current')
hh3cMACInformationTrapObjectsExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2))
hh3cMACInfoTrapVerExt = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapVerExt.setStatus('current')
hh3cMACInfoTrapIndexExt = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapIndexExt.setStatus('current')
hh3cMACInfoTrapCountExt = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapCountExt.setStatus('current')
hh3cMACInfoTrapMsgExt = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cMACInfoTrapMsgExt.setStatus('current')
mibBuilder.exportSymbols("HH3C-MAC-INFORMATION-MIB", hh3cMACInformationMIBTableTroop=hh3cMACInformationMIBTableTroop, hh3cMACRemovedEnable=hh3cMACRemovedEnable, hh3cMACInformationCacheLen=hh3cMACInformationCacheLen, Hh3cMACInfoWorkMode=Hh3cMACInfoWorkMode, hh3cMACInfomationIfTable=hh3cMACInfomationIfTable, hh3cMACInfoTrapMsgExt=hh3cMACInfoTrapMsgExt, hh3cMACInformationTrapSendNum=hh3cMACInformationTrapSendNum, hh3cMACInfomationWorkMode=hh3cMACInfomationWorkMode, hh3cMACInformationEnabled=hh3cMACInformationEnabled, hh3cMACInformationChangedTrap=hh3cMACInformationChangedTrap, hh3cMACInfoTrapVerExt=hh3cMACInfoTrapVerExt, hh3cMACInformationChangedTrapExt=hh3cMACInformationChangedTrapExt, hh3cMACInformation=hh3cMACInformation, hh3cMACLearntEnable=hh3cMACLearntEnable, hh3cMACInfoTrapCountExt=hh3cMACInfoTrapCountExt, hh3cMACInfoTrapCount=hh3cMACInfoTrapCount, hh3cMACInformationObjects=hh3cMACInformationObjects, hh3cMACInformationcSendInterval=hh3cMACInformationcSendInterval, hh3cMACInfoTrapIndexExt=hh3cMACInfoTrapIndexExt, hh3cMACInformationMibTrap=hh3cMACInformationMibTrap, hh3cMACInformationRemovedMACNum=hh3cMACInformationRemovedMACNum, hh3cMACInformationTrapsExt=hh3cMACInformationTrapsExt, hh3cMACInformationMibTrapExt=hh3cMACInformationMibTrapExt, hh3cMACInformationTrapObjects=hh3cMACInformationTrapObjects, hh3cMACInformationLearntMACNum=hh3cMACInformationLearntMACNum, hh3cMACInfomationIfEntry=hh3cMACInfomationIfEntry, hh3cMACInfoTrapIndex=hh3cMACInfoTrapIndex, hh3cMACInformationMibGlobal=hh3cMACInformationMibGlobal, hh3cMACInformationTraps=hh3cMACInformationTraps, PYSNMP_MODULE_ID=hh3cMACInformation, hh3cMACInformationSyslogSendNum=hh3cMACInformationSyslogSendNum, hh3cMACInfoTrapMsg=hh3cMACInfoTrapMsg, hh3cMACInformationTrapObjectsExt=hh3cMACInformationTrapObjectsExt)
