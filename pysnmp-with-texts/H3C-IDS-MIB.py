#
# PySNMP MIB module H3C-IDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-IDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Integer32, Bits, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Integer32", "Bits", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cIDSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1))
if mibBuilder.loadTexts: h3cIDSMib.setLastUpdated('200507141942Z')
if mibBuilder.loadTexts: h3cIDSMib.setOrganization('Huawei-3com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cIDSMib.setContactInfo('R&D Hangzhou, Huawei-3com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cIDSMib.setDescription('This MIB describes IDS private information. IDS(Instruction Detecting System) is used to detect intruder activity. ')
h3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47))
h3cIDSTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1))
h3cIDSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1))
h3cIDSTrapIPFragmentQueueLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPFragmentQueueLen.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapIPFragmentQueueLen.setDescription('The length of IP fragment queue.')
h3cIDSTrapStatSessionTabLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapStatSessionTabLen.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapStatSessionTabLen.setDescription('The length of status session table.')
h3cIDSTrapIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapIPAddressType.setDescription('The type of IP Address.')
h3cIDSTrapIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPAddress.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapIPAddress.setDescription('IP Address.')
h3cIDSTrapUserName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapUserName.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapUserName.setDescription('User name.')
h3cIDSTrapLoginType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("web", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapLoginType.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapLoginType.setDescription('Login type, including telnet, ssh and web.')
h3cIDSTrapUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("programme", 1), ("crb", 2), ("vrb", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapUpgradeType.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapUpgradeType.setDescription('Upgrade type, including programme(system image), crb(custom rule base, one kind of configuration file), vrb(vendor rule base, one kind of configuration file).')
h3cIDSTrapCRLName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCRLName.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCRLName.setDescription('CRL(Certificate Revoke List) name.')
h3cIDSTrapCertName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCertName.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCertName.setDescription('Certificate name.')
h3cIDSTrapDetectRuleID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 10), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleID.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleID.setDescription('The rule ID which is a unique identifier for a specified detect rule.')
h3cIDSTrapEngineID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapEngineID.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapEngineID.setDescription('A unique number used to identify an interface.')
h3cIDSTrapFileName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapFileName.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapFileName.setDescription('The file name.')
h3cIDSTrapCfgLineInFile = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCfgLineInFile.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCfgLineInFile.setDescription('The line number in the configuration file.')
h3cIDSTrapReasonForError = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapReasonForError.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapReasonForError.setDescription('The information of the notification. Although the format and content of this object are device specific, they should be defined uniformly in the device.')
h3cIDSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2))
h3cIDSTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0))
h3cIDSTrapIPFragQueueFull = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 1)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapIPFragmentQueueLen"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapIPFragQueueFull.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapIPFragQueueFull.setDescription('This notification will be generated when the IP fragment queue is full. The h3cIDSTrapIPFragmentQueueLen describes the length of current fragment queue. The h3cIDSTrapReasonForError describes reason for error.')
h3cIDSTrapStatSessTabFull = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 2)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapStatSessionTabLen"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapStatSessTabFull.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapStatSessTabFull.setDescription('This notification will be generated when the status session table is full. The h3cIDSTrapStatSessionTabLen describes the length of current status session table. The h3cIDSTrapReasonForError describes reason for error.')
h3cIDSTrapDetectRuleParseFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 3)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapDetectRuleID"), ("H3C-IDS-MIB", "h3cIDSTrapEngineID"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleParseFail.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleParseFail.setDescription('This notification will be generated when failing to parse the rules for detecting. The h3cIDSTrapDetectRuleID object describes rule ID. The h3cIDSTrapEngineID object identifies an interface the rule applies to. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapDBConnLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 4)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapIPAddressType"), ("H3C-IDS-MIB", "h3cIDSTrapIPAddress"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapDBConnLost.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapDBConnLost.setDescription('This notification will be generated when connecting with database server fails. The h3cIDSTrapIPAddressType object describes the IP address type of database server. The h3cIDSTrapIPAddress object describes the IP address of database server. The h3cIDSTrapReasonForError describes reason of connecting failure.')
h3cIDSTrapCRLNeedUpdate = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 5)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapCRLName"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapCRLNeedUpdate.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCRLNeedUpdate.setDescription('This notification will be generated when IDS device detects that CRL is out of date. The h3cIDSTrapCRLName object describes the CRL(Certificate Revoke List) name. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapCertOverdue = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 6)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapCertName"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapCertOverdue.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCertOverdue.setDescription('This notification will be generated when IDS device detects that certificate is overdue. The h3cIDSTrapCertName object describes the certificate name. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapTooManyLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 7)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapUserName"), ("H3C-IDS-MIB", "h3cIDSTrapIPAddressType"), ("H3C-IDS-MIB", "h3cIDSTrapIPAddress"), ("H3C-IDS-MIB", "h3cIDSTrapLoginType"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapTooManyLoginFail.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapTooManyLoginFail.setDescription('This notification will be generated when the login failure times of a user over a certain number. The h3cIDSTrapUserName object describes the user name when logging in. The h3cIDSTrapIPAddressType object describes the IP address type of client. The h3cIDSTrapIPAddress object describes the IP address of client. The h3cIDSTrapLoginType object describes login type, including: telnet, ssh, web. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 8)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapUpgradeType"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapUpgradeError.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapUpgradeError.setDescription('This notification will be generated when upgrading fails. The h3cIDSTrapUpgradeType object describes upgrade type, including: programme, vrb. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapFileAccessError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 9)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapFileName"), ("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapFileAccessError.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapFileAccessError.setDescription('This notification will be generated when accessing file fails. The h3cIDSTrapFileName object describes the name of file accessed. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapConsArithMemLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 10)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapConsArithMemLow.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapConsArithMemLow.setDescription('This notification will be generated when memory used by constructing the arithmetic to seek content is lacking. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapSSRAMOperFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 11)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapSSRAMOperFail.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapSSRAMOperFail.setDescription('This notification will be generated when reading or writing SSRAM of CIE card fails. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapPacketProcessDisorder = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 12)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapPacketProcessDisorder.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapPacketProcessDisorder.setDescription('This notification will be generated when packets processed is in disorder. The h3cIDSTrapReasonForError object describes reason for error.')
h3cIDSTrapCfgFileFormatError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 47, 1, 1, 2, 0, 13)).setObjects(("H3C-IDS-MIB", "h3cIDSTrapFileName"), ("H3C-IDS-MIB", "h3cIDSTrapCfgLineInFile"))
if mibBuilder.loadTexts: h3cIDSTrapCfgFileFormatError.setStatus('current')
if mibBuilder.loadTexts: h3cIDSTrapCfgFileFormatError.setDescription('When devices startup and load the configuration file, if format error is found, this notification will be generated. The h3cIDSTrapFileName object describes the name of configuration file. The h3cIDSTrapCfgLineInFile object describes the line number in the file.')
mibBuilder.exportSymbols("H3C-IDS-MIB", h3cIDSTrapSSRAMOperFail=h3cIDSTrapSSRAMOperFail, h3cIDSTrapEngineID=h3cIDSTrapEngineID, h3cIDSTrapGroup=h3cIDSTrapGroup, h3cIDSTrapStatSessionTabLen=h3cIDSTrapStatSessionTabLen, h3cIDSTrapUpgradeType=h3cIDSTrapUpgradeType, h3cIDSTrapConsArithMemLow=h3cIDSTrapConsArithMemLow, h3cIDSTrap=h3cIDSTrap, h3cIDSTrapDetectRuleID=h3cIDSTrapDetectRuleID, h3cIDSTrapTooManyLoginFail=h3cIDSTrapTooManyLoginFail, h3cIDSTrapPrefix=h3cIDSTrapPrefix, h3cIDSTrapCfgLineInFile=h3cIDSTrapCfgLineInFile, h3cIDSTrapUserName=h3cIDSTrapUserName, h3cIds=h3cIds, h3cIDSTrapIPAddress=h3cIDSTrapIPAddress, h3cIDSTrapCertOverdue=h3cIDSTrapCertOverdue, h3cIDSTrapCRLNeedUpdate=h3cIDSTrapCRLNeedUpdate, h3cIDSTrapReasonForError=h3cIDSTrapReasonForError, h3cIDSTrapUpgradeError=h3cIDSTrapUpgradeError, h3cIDSTrapIPAddressType=h3cIDSTrapIPAddressType, h3cIDSTrapLoginType=h3cIDSTrapLoginType, h3cIDSTrapStatSessTabFull=h3cIDSTrapStatSessTabFull, h3cIDSTrapDBConnLost=h3cIDSTrapDBConnLost, h3cIDSTrapFileAccessError=h3cIDSTrapFileAccessError, h3cIDSMib=h3cIDSMib, h3cIDSTrapCertName=h3cIDSTrapCertName, h3cIDSTrapFileName=h3cIDSTrapFileName, h3cIDSTrapDetectRuleParseFail=h3cIDSTrapDetectRuleParseFail, h3cIDSTrapPacketProcessDisorder=h3cIDSTrapPacketProcessDisorder, h3cIDSTrapIPFragQueueFull=h3cIDSTrapIPFragQueueFull, h3cIDSTrapCfgFileFormatError=h3cIDSTrapCfgFileFormatError, h3cIDSTrapInfo=h3cIDSTrapInfo, PYSNMP_MODULE_ID=h3cIDSMib, h3cIDSTrapCRLName=h3cIDSTrapCRLName, h3cIDSTrapIPFragmentQueueLen=h3cIDSTrapIPFragmentQueueLen)
