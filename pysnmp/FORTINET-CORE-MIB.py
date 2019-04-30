#
# PySNMP MIB module FORTINET-CORE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-CORE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressPrefixLength")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Unsigned32, NotificationType, ModuleIdentity, Integer32, MibIdentifier, Bits, ObjectIdentity, Counter32, enterprises, iso, TimeTicks, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "enterprises", "iso", "TimeTicks", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fortinet = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356))
fortinet.setRevisions(('2015-01-14 00:00', '2014-12-10 00:00', '2014-04-10 00:00', '2014-03-22 00:00', '2012-05-09 00:00', '2012-04-23 00:00', '2011-12-23 00:00', '2011-04-25 00:00', '2010-05-14 00:00', '2009-05-20 00:00', '2008-11-19 00:00', '2008-10-21 00:00', '2008-06-25 00:00', '2008-06-16 00:00', '2008-04-17 00:00',))
if mibBuilder.loadTexts: fortinet.setLastUpdated('201501140000Z')
if mibBuilder.loadTexts: fortinet.setOrganization('Fortinet Technologies, Inc.')
class FnBoolState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class FnLanguage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("english", 1), ("simplifiedChinese", 2), ("japanese", 3), ("korean", 4), ("spanish", 5), ("traditionalChinese", 6), ("french", 7), ("portuguese", 8), ("undefined", 255))

class FnIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FnSessionProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 41, 46, 47, 50, 51, 89, 103, 108, 255))
    namedValues = NamedValues(("ip", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("ipv6", 41), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("ospf", 89), ("pim", 103), ("comp", 108), ("raw", 255))

fnCoreMib = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100))
fnCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1))
fnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1))
fnSysSerial = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnSysSerial.setStatus('current')
fnMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2))
fnMgmtLanguage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 1), FnLanguage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnMgmtLanguage.setStatus('current')
fnAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100))
fnAdminNumber = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminNumber.setStatus('current')
fnAdminTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2), )
if mibBuilder.loadTexts: fnAdminTable.setStatus('current')
fnAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1), ).setIndexNames((0, "FORTINET-CORE-MIB", "fnAdminIndex"))
if mibBuilder.loadTexts: fnAdminEntry.setStatus('current')
fnAdminIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fnAdminIndex.setStatus('current')
fnAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminName.setStatus('current')
fnAdminAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddrType.setStatus('current')
fnAdminAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddr.setStatus('current')
fnAdminMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminMask.setStatus('current')
fnTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3))
fnTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0))
fnTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1))
fnGenTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fnGenTrapMsg.setStatus('current')
fnTrapCpuThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 101)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapCpuThreshold.setStatus('current')
fnTrapMemThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 102)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapMemThreshold.setStatus('current')
fnTrapLogDiskThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 103)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapLogDiskThreshold.setStatus('current')
fnTrapTempHigh = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 104)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTempHigh.setStatus('current')
fnTrapVoltageOutOfRange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 105)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapVoltageOutOfRange.setStatus('current')
fnTrapPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 106)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapPowerSupplyFailure.setStatus('current')
fnTrapAmcIfBypassMode = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 107)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapAmcIfBypassMode.setStatus('current')
fnTrapFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 108)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapFanFailure.setStatus('current')
fnTrapIpChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 201)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fnTrapIpChange.setStatus('current')
fnTrapTest = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 999)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTest.setStatus('current')
fnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 10))
fnSystemComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 1)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnSystemComplianceGroup = fnSystemComplianceGroup.setStatus('current')
fnMgmtComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 2)).setObjects(("FORTINET-CORE-MIB", "fnMgmtLanguage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMgmtComplianceGroup = fnMgmtComplianceGroup.setStatus('current')
fnAdminComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 3)).setObjects(("FORTINET-CORE-MIB", "fnAdminNumber"), ("FORTINET-CORE-MIB", "fnAdminName"), ("FORTINET-CORE-MIB", "fnAdminAddrType"), ("FORTINET-CORE-MIB", "fnAdminAddr"), ("FORTINET-CORE-MIB", "fnAdminMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnAdminComplianceGroup = fnAdminComplianceGroup.setStatus('current')
fnTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 4)).setObjects(("FORTINET-CORE-MIB", "fnTrapCpuThreshold"), ("FORTINET-CORE-MIB", "fnTrapMemThreshold"), ("FORTINET-CORE-MIB", "fnTrapLogDiskThreshold"), ("FORTINET-CORE-MIB", "fnTrapTempHigh"), ("FORTINET-CORE-MIB", "fnTrapVoltageOutOfRange"), ("FORTINET-CORE-MIB", "fnTrapPowerSupplyFailure"), ("FORTINET-CORE-MIB", "fnTrapAmcIfBypassMode"), ("FORTINET-CORE-MIB", "fnTrapFanFailure"), ("FORTINET-CORE-MIB", "fnTrapIpChange"), ("FORTINET-CORE-MIB", "fnTrapTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnTrapsComplianceGroup = fnTrapsComplianceGroup.setStatus('current')
fnNotifObjectsComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 5)).setObjects(("FORTINET-CORE-MIB", "fnGenTrapMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnNotifObjectsComplianceGroup = fnNotifObjectsComplianceGroup.setStatus('current')
fnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 100, 10, 100)).setObjects(("FORTINET-CORE-MIB", "fnSystemComplianceGroup"), ("FORTINET-CORE-MIB", "fnMgmtComplianceGroup"), ("FORTINET-CORE-MIB", "fnAdminComplianceGroup"), ("FORTINET-CORE-MIB", "fnTrapsComplianceGroup"), ("FORTINET-CORE-MIB", "fnNotifObjectsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMIBCompliance = fnMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FORTINET-CORE-MIB", fnAdmin=fnAdmin, fnNotifObjectsComplianceGroup=fnNotifObjectsComplianceGroup, fnAdminComplianceGroup=fnAdminComplianceGroup, fnTrapsComplianceGroup=fnTrapsComplianceGroup, fnTrapObjects=fnTrapObjects, fnTrapAmcIfBypassMode=fnTrapAmcIfBypassMode, fnMIBConformance=fnMIBConformance, fnTrapMemThreshold=fnTrapMemThreshold, fnAdminNumber=fnAdminNumber, fnTrapIpChange=fnTrapIpChange, FnLanguage=FnLanguage, fortinet=fortinet, fnTrapTempHigh=fnTrapTempHigh, fnSystem=fnSystem, fnAdminAddr=fnAdminAddr, FnIndex=FnIndex, fnAdminName=fnAdminName, PYSNMP_MODULE_ID=fortinet, fnTrapLogDiskThreshold=fnTrapLogDiskThreshold, FnBoolState=FnBoolState, fnAdminEntry=fnAdminEntry, fnSystemComplianceGroup=fnSystemComplianceGroup, fnTrapTest=fnTrapTest, fnAdminAddrType=fnAdminAddrType, fnCommon=fnCommon, fnMgmt=fnMgmt, fnCoreMib=fnCoreMib, fnAdminIndex=fnAdminIndex, fnTrapCpuThreshold=fnTrapCpuThreshold, fnTrapsPrefix=fnTrapsPrefix, fnMIBCompliance=fnMIBCompliance, fnAdminMask=fnAdminMask, fnSysSerial=fnSysSerial, fnTrapFanFailure=fnTrapFanFailure, fnTraps=fnTraps, fnTrapPowerSupplyFailure=fnTrapPowerSupplyFailure, fnTrapVoltageOutOfRange=fnTrapVoltageOutOfRange, fnMgmtComplianceGroup=fnMgmtComplianceGroup, fnMgmtLanguage=fnMgmtLanguage, FnSessionProto=FnSessionProto, fnGenTrapMsg=fnGenTrapMsg, fnAdminTable=fnAdminTable)
