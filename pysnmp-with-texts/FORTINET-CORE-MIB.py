#
# PySNMP MIB module FORTINET-CORE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-CORE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, IpAddress, MibIdentifier, ModuleIdentity, iso, NotificationType, Counter32, Unsigned32, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "iso", "NotificationType", "Counter32", "Unsigned32", "enterprises", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fortinet = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356))
fortinet.setRevisions(('2015-01-14 00:00', '2014-12-10 00:00', '2014-04-10 00:00', '2014-03-22 00:00', '2012-05-09 00:00', '2012-04-23 00:00', '2011-12-23 00:00', '2011-04-25 00:00', '2010-05-14 00:00', '2009-05-20 00:00', '2008-11-19 00:00', '2008-10-21 00:00', '2008-06-25 00:00', '2008-06-16 00:00', '2008-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fortinet.setRevisionsDescriptions(('Registered and updated FortiAuthenticatorMib/FortiRecorderMib/FortiVoiceMib/FortiBridgeMib/FortiDirectorMib OIDs', 'Registered FortiVoiceMib OID', 'Registered FortiADCMib OID', 'Added fan failure and AMC bypass traps', 'Registered FortiDDoSMib OID', 'Registered FortiDNSMib OID', 'Registered FortiCacheMib OID', 'Supporting portuguese language', 'Registered FortiScanMib OID', 'MIB module for Fortinet network devices.', 'Registered FortiWebMib OID', 'Added SMI comments', 'Adjusted fnAdmin tree to start at .1', 'Spelling corrections.', 'Initial version of fortinet core MIB.',))
if mibBuilder.loadTexts: fortinet.setLastUpdated('201501140000Z')
if mibBuilder.loadTexts: fortinet.setOrganization('Fortinet Technologies, Inc.')
if mibBuilder.loadTexts: fortinet.setContactInfo('Technical Support email: support@fortinet.com http://www.fortinet.com ')
if mibBuilder.loadTexts: fortinet.setDescription('Registered FortiWANMib OIDs')
class FnBoolState(TextualConvention, Integer32):
    description = 'Boolean data type representing enabled/disabled'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class FnLanguage(TextualConvention, Integer32):
    description = 'Enumerated type for user interface languages'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("english", 1), ("simplifiedChinese", 2), ("japanese", 3), ("korean", 4), ("spanish", 5), ("traditionalChinese", 6), ("french", 7), ("portuguese", 8), ("undefined", 255))

class FnIndex(TextualConvention, Integer32):
    description = 'Data type for table index values'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FnSessionProto(TextualConvention, Integer32):
    description = 'Data type for session protocols'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 41, 46, 47, 50, 51, 89, 103, 108, 255))
    namedValues = NamedValues(("ip", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("ipv6", 41), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("ospf", 89), ("pim", 103), ("comp", 108), ("raw", 255))

fnCoreMib = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100))
fnCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1))
fnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1))
fnSysSerial = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnSysSerial.setStatus('current')
if mibBuilder.loadTexts: fnSysSerial.setDescription('Device serial number. This is the same serial number as given in the ENTITY-MIB tables for the base entity.')
fnMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2))
fnMgmtLanguage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 1), FnLanguage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnMgmtLanguage.setStatus('current')
if mibBuilder.loadTexts: fnMgmtLanguage.setDescription('Language used for administration interfaces')
fnAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100))
fnAdminNumber = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminNumber.setStatus('current')
if mibBuilder.loadTexts: fnAdminNumber.setDescription('The number of admin accounts in fnAdminTable')
fnAdminTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2), )
if mibBuilder.loadTexts: fnAdminTable.setStatus('current')
if mibBuilder.loadTexts: fnAdminTable.setDescription('A table of administrator accounts on the device. This table is intended to be extended with platform specific information.')
fnAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1), ).setIndexNames((0, "FORTINET-CORE-MIB", "fnAdminIndex"))
if mibBuilder.loadTexts: fnAdminEntry.setStatus('current')
if mibBuilder.loadTexts: fnAdminEntry.setDescription('An entry containing information applicable to a particular admin account')
fnAdminIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fnAdminIndex.setStatus('current')
if mibBuilder.loadTexts: fnAdminIndex.setDescription('An index uniquely defining an administrator account within the fnAdminTable')
fnAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminName.setStatus('current')
if mibBuilder.loadTexts: fnAdminName.setDescription('The user-name of the specified administrator account')
fnAdminAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddrType.setStatus('current')
if mibBuilder.loadTexts: fnAdminAddrType.setDescription('The type of address stored in fnAdminAddr, in compliance with INET-ADDRESS-MIB')
fnAdminAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddr.setStatus('current')
if mibBuilder.loadTexts: fnAdminAddr.setDescription('The address prefix identifying where the administrator account can be used from, typically an IPv4 address. The address type/format is determined by fnAdminAddrType.')
fnAdminMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminMask.setStatus('current')
if mibBuilder.loadTexts: fnAdminMask.setDescription('The address prefix length (or network mask) applied to the fgAdminAddr to determine the subnet or host the administrator can access the device from')
fnTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3))
fnTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0))
fnTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1))
fnGenTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fnGenTrapMsg.setStatus('current')
if mibBuilder.loadTexts: fnGenTrapMsg.setDescription('Generic message associated with an event. The content will depend on the nature of the trap.')
fnTrapCpuThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 101)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapCpuThreshold.setStatus('current')
if mibBuilder.loadTexts: fnTrapCpuThreshold.setDescription('Indicates that the CPU usage has exceeded the configured threshold.')
fnTrapMemThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 102)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapMemThreshold.setStatus('current')
if mibBuilder.loadTexts: fnTrapMemThreshold.setDescription('Indicates memory usage has exceeded the configured threshold.')
fnTrapLogDiskThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 103)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapLogDiskThreshold.setStatus('current')
if mibBuilder.loadTexts: fnTrapLogDiskThreshold.setDescription('Log disk usage has exceeded the configured threshold. Only available on devices with log disks.')
fnTrapTempHigh = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 104)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTempHigh.setStatus('current')
if mibBuilder.loadTexts: fnTrapTempHigh.setDescription('A temperature sensor on the device has exceeded its threshold. Not all devices have thermal sensors. See manual for specifications.')
fnTrapVoltageOutOfRange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 105)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapVoltageOutOfRange.setStatus('current')
if mibBuilder.loadTexts: fnTrapVoltageOutOfRange.setDescription('Power levels have fluctuated outside of normal levels. Not all devices have voltage monitoring instrumentation. See manual for specifications.')
fnTrapPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 106)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapPowerSupplyFailure.setStatus('current')
if mibBuilder.loadTexts: fnTrapPowerSupplyFailure.setDescription('Power supply failure detected. Not available on all models. Available on some devices which support redundant power supplies. See manual for specifications.')
fnTrapAmcIfBypassMode = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 107)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapAmcIfBypassMode.setStatus('current')
if mibBuilder.loadTexts: fnTrapAmcIfBypassMode.setDescription('An AMC interface entered bypass mode. Available on models with an AMC expansion slot. Used with the ASM-CX4 and ASM-FX2 cards.')
fnTrapFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 108)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapFanFailure.setStatus('current')
if mibBuilder.loadTexts: fnTrapFanFailure.setDescription('A fan failure has been detected. Not all devices have fan sensors. See manual for specifications.')
fnTrapIpChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 201)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fnTrapIpChange.setStatus('current')
if mibBuilder.loadTexts: fnTrapIpChange.setDescription('Indicates that the IP address of the specified interface has been changed.')
fnTrapTest = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 999)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTest.setStatus('current')
if mibBuilder.loadTexts: fnTrapTest.setDescription('Trap sent for diagnostic purposes by an administrator.')
fnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 10))
fnSystemComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 1)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnSystemComplianceGroup = fnSystemComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fnSystemComplianceGroup.setDescription('Objects relating to the physical device.')
fnMgmtComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 2)).setObjects(("FORTINET-CORE-MIB", "fnMgmtLanguage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMgmtComplianceGroup = fnMgmtComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fnMgmtComplianceGroup.setDescription('Objects relating the management of a device.')
fnAdminComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 3)).setObjects(("FORTINET-CORE-MIB", "fnAdminNumber"), ("FORTINET-CORE-MIB", "fnAdminName"), ("FORTINET-CORE-MIB", "fnAdminAddrType"), ("FORTINET-CORE-MIB", "fnAdminAddr"), ("FORTINET-CORE-MIB", "fnAdminMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnAdminComplianceGroup = fnAdminComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fnAdminComplianceGroup.setDescription('Administration access control objects.')
fnTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 4)).setObjects(("FORTINET-CORE-MIB", "fnTrapCpuThreshold"), ("FORTINET-CORE-MIB", "fnTrapMemThreshold"), ("FORTINET-CORE-MIB", "fnTrapLogDiskThreshold"), ("FORTINET-CORE-MIB", "fnTrapTempHigh"), ("FORTINET-CORE-MIB", "fnTrapVoltageOutOfRange"), ("FORTINET-CORE-MIB", "fnTrapPowerSupplyFailure"), ("FORTINET-CORE-MIB", "fnTrapAmcIfBypassMode"), ("FORTINET-CORE-MIB", "fnTrapFanFailure"), ("FORTINET-CORE-MIB", "fnTrapIpChange"), ("FORTINET-CORE-MIB", "fnTrapTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnTrapsComplianceGroup = fnTrapsComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fnTrapsComplianceGroup.setDescription('Event notifications')
fnNotifObjectsComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 5)).setObjects(("FORTINET-CORE-MIB", "fnGenTrapMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnNotifObjectsComplianceGroup = fnNotifObjectsComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fnNotifObjectsComplianceGroup.setDescription('Object identifiers used in notifications')
fnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 100, 10, 100)).setObjects(("FORTINET-CORE-MIB", "fnSystemComplianceGroup"), ("FORTINET-CORE-MIB", "fnMgmtComplianceGroup"), ("FORTINET-CORE-MIB", "fnAdminComplianceGroup"), ("FORTINET-CORE-MIB", "fnTrapsComplianceGroup"), ("FORTINET-CORE-MIB", "fnNotifObjectsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMIBCompliance = fnMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: fnMIBCompliance.setDescription('The compliance statement for the application MIB.')
mibBuilder.exportSymbols("FORTINET-CORE-MIB", fnAdminComplianceGroup=fnAdminComplianceGroup, fnAdminNumber=fnAdminNumber, fnAdminEntry=fnAdminEntry, fnTrapMemThreshold=fnTrapMemThreshold, fnSystemComplianceGroup=fnSystemComplianceGroup, fnAdminName=fnAdminName, fnCommon=fnCommon, fnGenTrapMsg=fnGenTrapMsg, fnMgmt=fnMgmt, FnIndex=FnIndex, FnSessionProto=FnSessionProto, fnTrapObjects=fnTrapObjects, fnTrapCpuThreshold=fnTrapCpuThreshold, fnTraps=fnTraps, fnTrapTest=fnTrapTest, fnTrapLogDiskThreshold=fnTrapLogDiskThreshold, fnTrapTempHigh=fnTrapTempHigh, FnBoolState=FnBoolState, fnMgmtComplianceGroup=fnMgmtComplianceGroup, FnLanguage=FnLanguage, fnTrapsComplianceGroup=fnTrapsComplianceGroup, fnSysSerial=fnSysSerial, fnAdminAddr=fnAdminAddr, fnMIBConformance=fnMIBConformance, fnMgmtLanguage=fnMgmtLanguage, PYSNMP_MODULE_ID=fortinet, fnAdminMask=fnAdminMask, fnCoreMib=fnCoreMib, fnSystem=fnSystem, fnTrapVoltageOutOfRange=fnTrapVoltageOutOfRange, fortinet=fortinet, fnTrapsPrefix=fnTrapsPrefix, fnNotifObjectsComplianceGroup=fnNotifObjectsComplianceGroup, fnAdminAddrType=fnAdminAddrType, fnTrapFanFailure=fnTrapFanFailure, fnMIBCompliance=fnMIBCompliance, fnTrapAmcIfBypassMode=fnTrapAmcIfBypassMode, fnAdminTable=fnAdminTable, fnTrapPowerSupplyFailure=fnTrapPowerSupplyFailure, fnTrapIpChange=fnTrapIpChange, fnAdminIndex=fnAdminIndex, fnAdmin=fnAdmin)
