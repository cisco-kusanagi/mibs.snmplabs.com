#
# PySNMP MIB module Dell-SECSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-SECSD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:55:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, ModuleIdentity, Bits, Unsigned32, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "Unsigned32", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "MibIdentifier", "Integer32", "Counter32")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
rlSecSd = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 209))
rlSecSd.setRevisions(('2011-08-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSecSd.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSecSd.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: rlSecSd.setOrganization('Dell')
if mibBuilder.loadTexts: rlSecSd.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlSecSd.setDescription('The private MIB module definition for Security Sensitive Data (SSD), contains the MIB tables and scalars to manage the access through the different management channels as CLI, WEB and others, for sensitive data as user names and passwords in system.')
class RlSecSdRuleUserType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels access users. user-name - the rule is per rlSecSdRuleUserName. default-user - the rule is per the default system user name. all-users - all users which their user level permission is less then 15. level-15-users - users which their user level permission is 15.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("user-name", 1), ("default-user", 2), ("level-15-users", 3), ("all-users", 4))

class RlSecSdChannelType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels: secure - secure channels as console, ssh, scp, https. insecure - insecure channels as telnet, http. secure-xml-snmp - SNMPv3 with privacy or XML over https. insecure-xml-snmp - SNMPv1/v2/v3 without privacy, xml over http.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secure-xml-snmp", 1), ("secure", 2), ("insecure", 3), ("insecure-xml-snmp", 4))

class RlSecSdAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels default read/write access action: exclude - Security Sensitive Data can not retrieved/set. include-encrypted - SSD can retrieved/set as encrypted only. include-decrypted - SSD can retrieved/set as decrypted only.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3))

class RlSecSdPermitAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels access permit read/write action: exclude - Security Sensitive Data can not retrieved/set. include-encrypted - SSD can retrieved/set as encrypted only. include-decrypted - SSD can retrieved/set as decrypted only. include-all - SSD can retrieved/set as encrypted or as decrypted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("include-all", 4))

class RlSecSdSessionAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data (SSD) channels access per session: exclude - Security Sensitive Data can not retrieved. include-encrypted - SSD can retrieved as encrypted only. include-decrypted - SSD can retrieved as decrypted only. default - Set to the default SSD access as defined by the SSD rules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("default", 4))

class RlSecSdRuleOwnerType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data rule owner: default - default rule which is defined by the device. user - rule which is defined by user.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("user", 2))

rlSecSdRulesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 209, 1), )
if mibBuilder.loadTexts: rlSecSdRulesTable.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulesTable.setDescription('The table holding the Security Sensitive Data access rules per: user name / user level and management channel. Allow to add/edit/remove Security Sensitive Data rules.')
rlSecSdRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 209, 1, 1), ).setIndexNames((0, "Dell-SECSD-MIB", "rlSecSdRuleUser"), (0, "Dell-SECSD-MIB", "rlSecSdRuleUserName"), (0, "Dell-SECSD-MIB", "rlSecSdRuleChannel"))
if mibBuilder.loadTexts: rlSecSdRulesEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulesEntry.setDescription('An entry in the rlSecSdRulesTable.')
rlSecSdRuleUser = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 1), RlSecSdRuleUserType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUser.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleUser.setDescription('Contains the Rule user type as described in RlSecSdRuleUserType.')
rlSecSdRuleUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUserName.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleUserName.setDescription('Contains the Rule user name when rlSecSdRuleUser value is user-name, Otherwise it contains an empty string')
rlSecSdRuleChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 3), RlSecSdChannelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleChannel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleChannel.setDescription('Contains the Rule management channel type as described in RlSecSdChannelType. secure-xml-snmp and insecure-xml-snmp management channels have no include-encrypted capability thus their rlSecSdRulePermitRead and rlSecSdRuleRead can have only RlSecSdAccessType values of exclude or include-decrypted.')
rlSecSdRuleRead = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 4), RlSecSdAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleRead.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleRead.setDescription('Contains the Rule default read access level as described in RlSecSdAccessType, must be lower or equal access from rlSecSdRulePermitRead')
rlSecSdRulePermitRead = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 5), RlSecSdPermitAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRulePermitRead.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulePermitRead.setDescription('Contains the Rule maximum permission access level as described in RlSecSdPermitAccessType.')
rlSecSdRuleIsDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdRuleIsDefault.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleIsDefault.setDescription('true - Rule has created by the by the system. false - Rule has created by the user.')
rlSecSdRuleOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 7), RlSecSdRuleOwnerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleOwner.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleOwner.setDescription('Contains the current Rule ownership as defined in RlSecSdRuleOwnerType. when rlSecSdRuleIsDefault is true, rlSecSdRuleOwner allowed to change default rule to user rule and vice versa.')
rlSecSdRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleStatus.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleStatus.setDescription('The status of a table entry. It is used to Add/Edit/Delete an entry from this table.')
rlSecSdMngSessionsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 209, 2), )
if mibBuilder.loadTexts: rlSecSdMngSessionsTable.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionsTable.setDescription('The table holding Security Sensitive Data management sessions. Allowing to get management channel, user name, user level.')
rlSecSdMngSessionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 209, 2, 2), ).setIndexNames((0, "Dell-SECSD-MIB", "rlSecSdMngSessionId"))
if mibBuilder.loadTexts: rlSecSdMngSessionsEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionsEntry.setDescription('An entry in the rlSecSdMngSessionsTable.')
rlSecSdMngSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionId.setDescription('Contains the Security Sensitive Data management session identifier, rlSecSdCurrentSessionId is used to get the current management session identifier')
rlSecSdMngSessionUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionUserLevel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionUserLevel.setDescription('Contains the Security Sensitive Data management session user access level.')
rlSecSdMngSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdMngSessionUserName.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionUserName.setDescription('Contains the Security Sensitive Data management session user name.')
rlSecSdMngSessionChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 209, 2, 2, 4), RlSecSdChannelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionChannel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionChannel.setDescription('Contains the Security Sensitive Data management session channel type as described in RlSecSdChannelType.')
rlSecSdSessionControl = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 3), RlSecSdSessionAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdSessionControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdSessionControl.setDescription('Action scalar which set the default read access of Security Sensitive Data. Affect only on session which from this scalar is configured. Scalar Get value is the default-display/read of the session which from this scalar is retrieved.')
rlSecSdCurrentSessionId = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdCurrentSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSecSdCurrentSessionId.setDescription('Get the current SSD management channel identifier, used to get information from rlSecSdMngSessionsTable.')
rlSecSdPassPhrase = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdPassPhrase.setStatus('current')
if mibBuilder.loadTexts: rlSecSdPassPhrase.setDescription('Set the passphrase for the SSD encryptyption / decryption key. on set, passphrase is in plain text format. on get, passphrase is encrypted.')
rlSecSdFilePassphraseControl = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restricted", 1), ("unrestricted", 2))).clone('unrestricted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFilePassphraseControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFilePassphraseControl.setDescription('File Passphrase control provides an additional level of protection on passphrase and configurations. restricted - a device restricts its passphrase from being inserted into a configuration file. unrestricted - (default) a device will include its passphrase when creating a configuration file.')
rlSecSdFileIntegrityControl = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIntegrityControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFileIntegrityControl.setDescription('File integrity control provides a validation of configuration file. enable - Validate the configuration file digest when downloading the file to startup configuration. disable - Do not validate.')
rlSecSdConfigurationFileSsdDigest = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileSsdDigest.setStatus('current')
if mibBuilder.loadTexts: rlSecSdConfigurationFileSsdDigest.setDescription('SSD block in configuration file integrity digest, auxiliary action scalar for internal system using during configuration download.')
rlSecSdConfigurationFileDigest = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileDigest.setStatus('current')
if mibBuilder.loadTexts: rlSecSdConfigurationFileDigest.setDescription('SSD configuration file integrity digest, auxiliary action scalar for internal system using during configuration download.')
rlSecSdFileIndicator = MibScalar((1, 3, 6, 1, 4, 1, 89, 209, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIndicator.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFileIndicator.setDescription('Retrieve configuration file SSD indicator. set value: configuration file name. get value: Exclude, Encrypted, Plaintext')
mibBuilder.exportSymbols("Dell-SECSD-MIB", rlSecSdRuleUser=rlSecSdRuleUser, RlSecSdRuleOwnerType=RlSecSdRuleOwnerType, rlSecSdMngSessionUserLevel=rlSecSdMngSessionUserLevel, RlSecSdRuleUserType=RlSecSdRuleUserType, rlSecSdRuleChannel=rlSecSdRuleChannel, rlSecSdRuleIsDefault=rlSecSdRuleIsDefault, RlSecSdChannelType=RlSecSdChannelType, PYSNMP_MODULE_ID=rlSecSd, rlSecSdFileIndicator=rlSecSdFileIndicator, RlSecSdSessionAccessType=RlSecSdSessionAccessType, rlSecSdSessionControl=rlSecSdSessionControl, rlSecSdPassPhrase=rlSecSdPassPhrase, rlSecSdCurrentSessionId=rlSecSdCurrentSessionId, rlSecSdRuleOwner=rlSecSdRuleOwner, RlSecSdAccessType=RlSecSdAccessType, rlSecSdFilePassphraseControl=rlSecSdFilePassphraseControl, rlSecSdMngSessionId=rlSecSdMngSessionId, rlSecSdFileIntegrityControl=rlSecSdFileIntegrityControl, rlSecSdConfigurationFileSsdDigest=rlSecSdConfigurationFileSsdDigest, rlSecSd=rlSecSd, rlSecSdMngSessionsEntry=rlSecSdMngSessionsEntry, rlSecSdConfigurationFileDigest=rlSecSdConfigurationFileDigest, RlSecSdPermitAccessType=RlSecSdPermitAccessType, rlSecSdMngSessionUserName=rlSecSdMngSessionUserName, rlSecSdRuleStatus=rlSecSdRuleStatus, rlSecSdRulePermitRead=rlSecSdRulePermitRead, rlSecSdRuleRead=rlSecSdRuleRead, rlSecSdMngSessionsTable=rlSecSdMngSessionsTable, rlSecSdRulesEntry=rlSecSdRulesEntry, rlSecSdRulesTable=rlSecSdRulesTable, rlSecSdRuleUserName=rlSecSdRuleUserName, rlSecSdMngSessionChannel=rlSecSdMngSessionChannel)
