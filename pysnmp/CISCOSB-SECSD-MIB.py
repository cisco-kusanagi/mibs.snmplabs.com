#
# PySNMP MIB module CISCOSB-SECSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SECSD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, ObjectIdentity, MibIdentifier, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, iso, Unsigned32, ModuleIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "ObjectIdentity", "MibIdentifier", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "iso", "Unsigned32", "ModuleIdentity", "NotificationType", "Gauge32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
rlSecSd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209))
rlSecSd.setRevisions(('2011-08-31 00:00',))
if mibBuilder.loadTexts: rlSecSd.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: rlSecSd.setOrganization('Cisco Small Business')
class RlSecSdRuleUserType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("user-name", 1), ("default-user", 2), ("level-15-users", 3), ("all-users", 4))

class RlSecSdChannelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secure-xml-snmp", 1), ("secure", 2), ("insecure", 3), ("insecure-xml-snmp", 4))

class RlSecSdAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3))

class RlSecSdPermitAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("include-all", 4))

class RlSecSdSessionAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("default", 4))

class RlSecSdRuleOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("user", 2))

rlSecSdRulesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1), )
if mibBuilder.loadTexts: rlSecSdRulesTable.setStatus('current')
rlSecSdRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1), ).setIndexNames((0, "CISCOSB-SECSD-MIB", "rlSecSdRuleUser"), (0, "CISCOSB-SECSD-MIB", "rlSecSdRuleUserName"), (0, "CISCOSB-SECSD-MIB", "rlSecSdRuleChannel"))
if mibBuilder.loadTexts: rlSecSdRulesEntry.setStatus('current')
rlSecSdRuleUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 1), RlSecSdRuleUserType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUser.setStatus('current')
rlSecSdRuleUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUserName.setStatus('current')
rlSecSdRuleChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 3), RlSecSdChannelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleChannel.setStatus('current')
rlSecSdRuleRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 4), RlSecSdAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleRead.setStatus('current')
rlSecSdRulePermitRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 5), RlSecSdPermitAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRulePermitRead.setStatus('current')
rlSecSdRuleIsDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdRuleIsDefault.setStatus('current')
rlSecSdRuleOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 7), RlSecSdRuleOwnerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleOwner.setStatus('current')
rlSecSdRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleStatus.setStatus('current')
rlSecSdMngSessionsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2), )
if mibBuilder.loadTexts: rlSecSdMngSessionsTable.setStatus('current')
rlSecSdMngSessionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 2), ).setIndexNames((0, "CISCOSB-SECSD-MIB", "rlSecSdMngSessionId"))
if mibBuilder.loadTexts: rlSecSdMngSessionsEntry.setStatus('current')
rlSecSdMngSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionId.setStatus('current')
rlSecSdMngSessionUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionUserLevel.setStatus('current')
rlSecSdMngSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdMngSessionUserName.setStatus('current')
rlSecSdMngSessionChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 2, 4), RlSecSdChannelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionChannel.setStatus('current')
rlSecSdSessionControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 3), RlSecSdSessionAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdSessionControl.setStatus('current')
rlSecSdCurrentSessionId = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdCurrentSessionId.setStatus('current')
rlSecSdPassPhrase = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdPassPhrase.setStatus('current')
rlSecSdFilePassphraseControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restricted", 1), ("unrestricted", 2))).clone('unrestricted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFilePassphraseControl.setStatus('current')
rlSecSdFileIntegrityControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIntegrityControl.setStatus('current')
rlSecSdConfigurationFileSsdDigest = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileSsdDigest.setStatus('current')
rlSecSdConfigurationFileDigest = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileDigest.setStatus('current')
rlSecSdFileIndicator = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIndicator.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SECSD-MIB", PYSNMP_MODULE_ID=rlSecSd, rlSecSdRuleOwner=rlSecSdRuleOwner, rlSecSdRulesEntry=rlSecSdRulesEntry, rlSecSdMngSessionUserName=rlSecSdMngSessionUserName, rlSecSdCurrentSessionId=rlSecSdCurrentSessionId, RlSecSdSessionAccessType=RlSecSdSessionAccessType, rlSecSdRulesTable=rlSecSdRulesTable, RlSecSdChannelType=RlSecSdChannelType, rlSecSdRuleStatus=rlSecSdRuleStatus, rlSecSdRuleIsDefault=rlSecSdRuleIsDefault, rlSecSdRulePermitRead=rlSecSdRulePermitRead, RlSecSdRuleOwnerType=RlSecSdRuleOwnerType, rlSecSdMngSessionId=rlSecSdMngSessionId, rlSecSdSessionControl=rlSecSdSessionControl, rlSecSdMngSessionsTable=rlSecSdMngSessionsTable, rlSecSdRuleUserName=rlSecSdRuleUserName, RlSecSdAccessType=RlSecSdAccessType, rlSecSdConfigurationFileDigest=rlSecSdConfigurationFileDigest, rlSecSdMngSessionsEntry=rlSecSdMngSessionsEntry, RlSecSdRuleUserType=RlSecSdRuleUserType, rlSecSdMngSessionUserLevel=rlSecSdMngSessionUserLevel, rlSecSdRuleUser=rlSecSdRuleUser, rlSecSdConfigurationFileSsdDigest=rlSecSdConfigurationFileSsdDigest, rlSecSdRuleRead=rlSecSdRuleRead, rlSecSdPassPhrase=rlSecSdPassPhrase, rlSecSdMngSessionChannel=rlSecSdMngSessionChannel, RlSecSdPermitAccessType=RlSecSdPermitAccessType, rlSecSd=rlSecSd, rlSecSdFileIndicator=rlSecSdFileIndicator, rlSecSdFileIntegrityControl=rlSecSdFileIntegrityControl, rlSecSdRuleChannel=rlSecSdRuleChannel, rlSecSdFilePassphraseControl=rlSecSdFilePassphraseControl)
